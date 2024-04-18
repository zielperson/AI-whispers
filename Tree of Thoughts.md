
The initial "Tree of Thoughts" concept was introduced by Yao in 2023, and you can explore their work [here](https://arxiv.org/abs/2305.10601) and on their [GitHub page](https://github.com/princeton-nlp/tree-of-thought-llm). Long's 2023 paper was basically the same, at the same time.
Their paper is available [here](https://arxiv.org/abs/2305.08291).

I would give the creator title for this technique to both.

Both papers are algorithmic solutions to math problems and produced no direct prompt.

This was dine here by Hulbert in 2023, who successfully condensed the algorithm into a single prompt.
You can view this on the [GitHub page](https://github.com/dave1010/tree-of-thought-prompting).

```
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
The question is {{input}}
```
