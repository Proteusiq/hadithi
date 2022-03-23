# Navigating flukes in ML predictions

Are your classification predictions a fluke or are they real? Maybe both? I will argue that they are mostly like both. A good model is that that minimises the number fluke predictions.

ML diagnostics and metrics evaluation are skills to be developed, a process of constant learning. As Data Scientists, we are forever in a position of apprentice.  Always  learning and improve new ways to develop and evaluate our models. Our model evaluations are only as good as how we define ML problem.

Understanding our model predictions is an art of both improving and evaluating our models. But before we begin, what is it that I mean by fluke predictions?  What I mean by fluke predictions are correct or incorrect classification predictions that lies in the borderline of the decision boundary. That the algorithm predicted correctly or incorrectly is purely by chance (random initial assigned weights).

This is a loaded definition. It rises more questions than answers. For example what do we mean by correctness or decision function? Let us say I am aware of that. But let’s assume for now that we care more about practicality and less on semantics. My goal is for you to take what you find useful, and ignore what you find useless or perhaps wrong.

Let’s code. It easier to show than to explain. As said, code is more worthy than a thousand words.
