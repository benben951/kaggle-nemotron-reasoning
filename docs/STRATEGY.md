# Strategy

## Competition Fit

This is a better Kaggle target than generic tabular playgrounds because it connects to:

- reasoning evaluation
- agent/tool-use workflows
- prompt analysis
- deterministic solver design
- LLM-era hiring narratives

It is not guaranteed prize material. The realistic target is:

1. produce a public, credible repo;
2. submit valid baselines quickly;
3. iterate task-family solvers;
4. use the result as a job-search asset even if prize placement is unlikely.

## First Three Milestones

1. Sanity baseline: create a local answer file from current public test rows and confirm that CSV submission is not the main artifact.
2. Task taxonomy: classify train prompts into families such as bit manipulation, text cipher, arithmetic, grid/logic, and symbolic transformation.
3. Solver track: implement deterministic solvers for the most frequent structured families, then compare against LLM-assisted outputs.
4. LoRA/model track: prepare a small reproducible fine-tuning path if compute becomes available.

## Medal Route

Gold is possible only if we discover a repeatable advantage:

- strong task-family decomposition;
- deterministic solvers for high-volume hidden task types;
- robust prompt/program synthesis for unseen tasks;
- fast error analysis from leaderboard feedback;
- public notebook quality if medal ranking is not reached.

Because the competition expects model-improvement artifacts rather than normal CSV answers, the practical first target is not "submit a quick score." It is to build a credible open notebook/write-up and decide whether we can afford LoRA experiments on the required base model.

## Career Route

The project should be packaged as "agentic reasoning evaluation" rather than "I joined a Kaggle competition." Interview proof should include:

- data schema and prompt taxonomy;
- solver architecture;
- evaluation and failure analysis;
- reproducible scripts;
- competition submission history;
- lessons transferred to risk/AML agent evaluation.
