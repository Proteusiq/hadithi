# Navigating flukes in ML predictions 🦊

Are your classification predictions a fluke, or are they real? Maybe both? I will argue that they are likely both. How do we minimise the number of fluke predictions?

ML diagnostics and metrics evaluation are skills to be developed, a constant learning process. As Data Scientists, we are forever in a position of an apprentice.  Always learning and improving new ways to develop and evaluate our models. Our model evaluations are only as good as how we define the ML problems.

Understanding our model predictions is the art of both improving and evaluating our models. But before we begin, what do I mean by fluke predictions?  What I mean by fluke predictions are correct or incorrect classification predictions that lie on the borderline of the decision boundary. That the algorithm predicted correctly or incorrectly is purely by chance (random initial assigned weights).

This is a loaded definition. It raises more questions than answers. For example, what do we mean by correctness or decision function? Let us say I am aware of that. But let’s assume that we care more about practicality and less about semantics. My goal is for you to take what you find helpful, and ignore what you find useless or perhaps wrong.

Let’s code. It easier to show than to explain.


Exploring how far ML interpretability goes and where classical data mining ⛏ {domain experience} comes in.

As said, code is more worthy than a thousand words.

##### Tools:

[cleanlab](https://docs.cleanlab.ai/v2.0.0) - Understanding models with unclean data
