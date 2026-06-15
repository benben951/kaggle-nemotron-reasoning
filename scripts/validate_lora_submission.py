import argparse
import json
import sys
import zipfile


def _fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)


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


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate Kaggle Nemotron LoRA submission.zip structure "
            "(rank<=32 + required files + non-trivially-sized weights)."
        )
    )
    parser.add_argument("zip_path", help="Path to submission.zip")
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

    zip_path = args.zip_path
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

        # PEFT adapter_config.json typically contains a scalar "r" (rank) or a list/dict per layer.
        rank = config.get("r")
        if rank is None:
            _fail("adapter_config.json missing key 'r' (LoRA rank)")

        if isinstance(rank, (int, float)):
            rank_val = int(rank)
        else:
            _fail(f"Unsupported rank type for key 'r': {type(rank).__name__} (expected int)")

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

        min_weight_bytes = int(args.min_weight_bytes)
        if min_weight_bytes < 0:
            _fail(f"--min-weight-bytes must be >= 0 (got {min_weight_bytes})")

        weight_sizes = {}
        for w in weights_present:
            try:
                weight_sizes[w] = int(zf.getinfo(w).file_size)
            except KeyError:
                # Should not happen due to membership check above, but keep error explicit.
                _fail(f"Weight file missing from zip unexpectedly: {w}")

        if min_weight_bytes > 0:
            too_small = {k: v for k, v in weight_sizes.items() if v < min_weight_bytes}
            if too_small:
                detail = ", ".join(f"{k}={v}B" for k, v in sorted(too_small.items()))
                _fail(
                    "Adapter weight file(s) are suspiciously small; this is likely a smoke/dummy artifact. "
                    f"Min required is {min_weight_bytes}B. Found: {detail}"
                )

        print("OK")
        print(f"- adapter_config.json: present")
        print(f"- LoRA rank (r): {rank_val}")
        print(f"- weights: {weights_present}")
        print(f"- weight_sizes_bytes: {weight_sizes}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
