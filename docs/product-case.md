# From a search concept to an evaluation question

## Internship context

During Booz Allen Hamilton's Summer Games program, I worked on an AI-team project for NOAA NESDIS. My contribution included researching comparable solutions and use cases, exploring Ollama and AI queries, participating in benchmarking and testing, refining user stories, and leading the structure of the final presentation.

That experience made evaluation an important part of how I think about product work. A system can return a convincing result without answering the user's actual information need. A useful evaluation therefore begins with a task, an explicit definition of relevance, and a comparison that someone else can inspect.

## Portfolio extension

This repository develops that evaluation idea through a new, small search exercise. The records are invented, and the code was created for the portfolio with AI assistance. It contains no employer source code, client documents, or recovered internship benchmark results.

## Product choices

**Make relevance inspectable.** Each query names its relevant records and explains the judgment. A reviewer can disagree with the label and rerun the analysis instead of accepting a hidden score.

**Return no result when nothing matches.** Filling the page with arbitrary records would obscure a retrieval failure. The empty-result behavior is explicit and tested.

**Separate coverage from ordering.** A method can retrieve a useful record yet place it below irrelevant results. Hit rate, precision, recall, and reciprocal rank answer different parts of the user experience.

**Keep the comparison modest.** The metadata method is intentionally simple. Its purpose is to demonstrate the evaluation workflow and expose assumptions before a more complex approach is justified.

## Outcome of the current exercise

The deliverable is a runnable comparison with documented judgments, computed results, and tests. Its outputs support conclusions about this fixture only. The project does not report a reduction in NOAA query time or describe an employer deployment.

[Evaluation design](evaluation-design.md) · [Results](../results/evaluation.md) · [Return to overview](../README.md)
