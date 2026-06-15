import argparse
import datetime as _dt
import hashlib
import json
import shutil
import sys
import zipfile
from pathlib import Path


def _fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def _read_json_from_zip(zf: zipfile.ZipFile, member: str) -> dict:
    try:
        with zf.open(member, "r") as f:
            return json.loads(f.read().decode("utf-8"))
    except KeyError:
        _fail(f"Missing required file in zip: {member}")
    except UnicodeDecodeError as e:
        _fail(f"Failed to decode {member} as UTF-8: {e}")
    except json.JSONDecodeError as e:
        _fail(f"Failed to parse {member} as JSON: {e}")


def validate_submission_zip(zip_path: Path) -> dict:
    try:
        zf = zipfile.ZipFile(zip_path, "r")
    except FileNotFoundError:
        _fail(f"File not found: {zip_path}")
    except zipfile.BadZipFile as e:
        _fail(f"Bad zip file: {e}")

    with zf:
        members = set(zf.namelist())
        if "adapter_config.json" not in members:
            _fail("adapter_config.json not found at zip root")

        config = _read_json_from_zip(zf, "adapter_config.json")
        rank = config.get("r")
        if rank is None:
            _fail("adapter_config.json missing key 'r' (LoRA rank)")
        if not isinstance(rank, (int, float)):
            _fail(f"Unsupported rank type for key 'r': {type(rank).__name__} (expected int)")

        rank_val = int(rank)
        if rank_val > 32:
            _fail(f"LoRA rank too large: r={rank_val} (must be <= 32)")

        weight_candidates = [
            "adapter_model.safetensors",
            "adapter_model.bin",
            "pytorch_model.bin",
        ]
        weights_present = [p for p in weight_candidates if p in members]
        if not weights_present:
            _fail(
                "No adapter weights found at zip root. Expected one of: "
                + ", ".join(weight_candidates)
            )

        weight_sizes = {w: int(zf.getinfo(w).file_size) for w in weights_present}

    return {"rank": rank_val, "weights": weights_present, "weight_sizes": weight_sizes}


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Ingest and preserve a Kaggle Nemotron LoRA submission.zip (validate + sha256 + optional copy)."
        )
    )
    parser.add_argument("zip_path", help="Path to submission.zip (from Kaggle kernel outputs)")
    parser.add_argument(
        "--name",
        help="Run name folder under outputs/kaggle/submissions/ (default: timestamp)",
        default=None,
    )
    parser.add_argument(
        "--out-root",
        help="Output root directory (default: outputs/kaggle/submissions)",
        default="outputs/kaggle/submissions",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate + print sha256 only; do not copy/write anything.",
    )
    parser.add_argument(
        "--min-weight-bytes",
        type=int,
        default=1024,
        help=(
            "Minimum uncompressed size (bytes) for adapter weight files inside the zip. "
            "Use 0 to disable. Default: 1024."
        ),
    )
    args = parser.parse_args()

    zip_path = Path(args.zip_path).expanduser().resolve()
    validation = validate_submission_zip(zip_path)
    min_weight_bytes = int(args.min_weight_bytes)
    if min_weight_bytes < 0:
        _fail(f"--min-weight-bytes must be >= 0 (got {min_weight_bytes})")
    if min_weight_bytes > 0:
        too_small = {k: v for k, v in validation["weight_sizes"].items() if v < min_weight_bytes}
        if too_small:
            detail = ", ".join(f"{k}={v}B" for k, v in sorted(too_small.items()))
            _fail(
                "Adapter weight file(s) are suspiciously small; this is likely a smoke/dummy artifact. "
                f"Min required is {min_weight_bytes}B. Found: {detail}"
            )
    sha256 = _sha256(zip_path)

    print("OK")
    print(f"- path: {zip_path}")
    print(f"- sha256: {sha256}")
    print(f"- LoRA rank (r): {validation['rank']}")
    print(f"- weights: {validation['weights']}")
    print(f"- weight_sizes_bytes: {validation['weight_sizes']}")

    if args.dry_run:
        return 0

    ts = _dt.datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    name = args.name or ts
    safe_name = "".join(c if (c.isalnum() or c in "-_.") else "_" for c in name).strip("._")
    if not safe_name:
        safe_name = ts

    out_root = Path(args.out_root)
    dest_dir = out_root / safe_name
    dest_dir.mkdir(parents=True, exist_ok=False)

    dest_zip = dest_dir / "submission.zip"
    shutil.copy2(zip_path, dest_zip)

    manifest = {
        "created_at": _dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_zip_path": str(zip_path),
        "submission_zip": str(dest_zip),
        "sha256": sha256,
        "rank": validation["rank"],
        "weights": validation["weights"],
        "weight_sizes_bytes": validation["weight_sizes"],
        "min_weight_bytes_gate": min_weight_bytes,
    }
    (dest_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"- copied_to: {dest_zip}")
    print(f"- manifest: {dest_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
