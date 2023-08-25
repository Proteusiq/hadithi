Picture a grand symphony orchestra: woodwinds, brass, strings, and percussion, each section distinct yet harmoniously united. The conductor waves the baton, and every instrument plays its part, contributing to a cohesive, magnificent whole. This musical harmony, the flawless interplay of instruments, is what the SOLID Principles seek to instil in our data science canvas, with the **Single Responsibility Principle (SRP)** as instruments.

Woohoo! You're still here. You're thirsty for more! Not only have you journeyed this far, but you've also conquered ["Building the Bedrock: Employing SOLID Principles in Data Science"](https://dev.to/proteusiq/building-the-bedrock-employing-solid-principles-in-data-science-1loa). I am here. Now, with that fire in our belly, we're all geared up to revolutionize Data Science code using the SRP. Let the explanation and the code snippet examples be the ice in our minds.

### The S in SOLID: The Maestros Behind the Curtain
SRP isn’t just a software design principle. It’s an art form, a meticulous choreography of roles and responsibilities. Beyond the confines of classes, SRP sings a computer science symphony, ensuring every 'instrument' - be it a function, class, or file - resonates with its unique note, yet contributes to the collective melody of the project.

The Single Responsibility Principle (SRP) is pivotal in software design. It is a concept that encourages us to create programs that can be easily pieced together or linked, much like a chain. Doug McIlroy, one of the early pioneers of this concept, imagined a scenario where the output from one segment of software could naturally and efficiently be used as the input for another, even if that next segment hasn't been defined yet.

By adhering to SRP, the ultimate goal is to produce software that is not only robust and reliable but also easy to maintain. When each part of the software focuses on one primary responsibility, it becomes less tangled and, therefore, easier to understand and modify.

## Let's Code: Creating Data Preprocessing Pipeline

```python
# Task Prototype. Each Task has to implement *run* method 
# file: prototypes.py
from abc import ABC, abstractmethod

class Task(ABC):
    @property
    def name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
```

Now, the instruments that do one thing well

```python
# Tasks that can be divided into their own files
# from prototypes import Task

from typing import Literal

import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn import set_config

from srp import config

set_config(transform_output="pandas")


transformer = make_column_transformer(
    (
        FunctionTransformer(np.log),[
            config.COLUMNS_TO_LOG_TRANSFORM
        ],
    ),
    (
        OneHotEncoder(sparse_output=False),[
            config.COLUMNS_TO_ONEHOTENCODE,
        ],
    ),
    verbose_feature_names_out=False,
    remainder="passthrough",
)

class DropZerosTask(Task):
    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        cleaned_data = data[~data.select_dtypes("number").eq(0).any(axis=1)]
        return cleaned_data

class DropColumnsTask(Task):
    def __init__(self, columns: list[str]):
        self.columns = columns

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        cleaned_data = data.drop(columns=self.columns)
        return cleaned_data

# TODO: decorator to save and load transformer
class TransformerTask(Task):
    def __init__(self, stage: Literal["train", "predict"] = "train"):
        self.stage = stage

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        if self.stage == "predict":
            cleaned_data = transformer.transform(data)
        else:
            cleaned_data = transformer.fit_transform(data)

        return cleaned_data

class Floats2IntsTask(Task):
    def __init__(self, columns: list[str]):
        self.columns = columns

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        cleaned_data = data
        cleaned_data[self.columns] = cleaned_data[self.columns].transform(
            pd.to_numeric,
            errors="coerce",
            downcast="integer",
        )
        return cleaned_data
```

This modular approach offers flexibility. As needs and technologies change, it's much simpler to adjust or replace individual parts rather than overhaul the entire system.

Time to _note_ the conductor, responsible for adding and calling instruments:

```python
# DataTasks gather and runner
# file: data/datatasks.py
# from prototypes import Task

from __future__ import annotations
from queue import PriorityQueue
import pandas as pd
from loguru import logger

class DataTasks:
    def __init__(self, tasks: PriorityQueue = None) -> DataTasks:
        if tasks is None:
            self.tasks = PriorityQueue()

    def set_task(self, priority: int, task: Task) -> DataTasks:
        self.tasks.put((priority, task))
        return self

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        while not self.tasks.empty():
            _, task = self.tasks.get()
            logger.debug(f"priority: {_}, task: {task.name}")
            data = task.run(data)
        return data
```

Since `Tasks` need only to implement the `run` method that returns a `DataFrame`, this part of the software does not change with changes in `Tasks`. Thus crafting a piece that is both adaptable to future changes and resilient in its operation.

Finally, a grand symphony. A seamless pipeline that is robust, maintainable, and adaptable to change.

```python
# Implementation
# from data.datatasks import DataTasks
# from data.tasks import ...

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    data_chain = DataTasks()
    (
        data_chain.set_task(priority=2, task=DropZerosTask())
        .set_task(
            priority=1,
            task=DropColumnsTask(
                columns=[
                    "Length2",
                    "Length3",
                ]
            ),
        )
        .set_task(priority=3, task=TransformerTask())
        .set_task(
            priority=4,
            task=Floats2IntsTask(
                columns=[
                    "Species_Bream",
                    "Species_Parkki",
                    "Species_Perch",
                    "Species_Whitefish",
                ]
            ),
        )
        # Add more or remove tasks to the chain as needed
    )

    # Send data through the chain
    return data_chain.run(data)

# in the main
# import process_data

if __name__ == "__main__":
    import pandas as pd

    URI = "https://raw.githubusercontent.com/Ankit152/Fish-Market/main/Fish.csv"
    dataf = pd.read_csv(URI)
    clean_data = process_data(dataf)
```
![Flow Example](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9zjbbhiypu6dcrpq8xg1.png)

### The Guiding Stars: Avoiding the Black Holes
While SRP and design patterns offer a universe of possibilities, beware of the black holes of over-engineering and complexity. Not every problem demands this symphony; sometimes, a simple melody will do. We still need to tailor our approach to the narrative of our project.

The SRP began to transform our data science projects into masterpieces, cohesive yet complex, simple yet sophisticated. Every component, like a perfectly tuned instrument, plays its part, contributing to the entire symphony, and ensuring our projects are maintainable, scalable, and extensible.

The cosmic masterpieces' journey does not end here. It has just started. SOLID guiding stars "O". The Open-Closed Principle (OCP). OCP guides us to build units that are open for extension but closed for modification. A saga for the next article in this series.

`Up Next`: "OCP: Refactoring the Data Science Project"

Until then, keep on coding data science SOLID-ly.


