from pathlib import Path

from fastapi import FastAPI
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from ml import ml_io
from schemas import Attributes, LearnAttributes, Predictions, Learnings


MODEL_FILE = "model/naive.pickle"
app = FastAPI(title="😂 Pure Joy")


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print(f"path={event.src_path} event={event.event_type}")
        app.state.ml = ml_io(model_file=Path(MODEL_FILE), mode="rb")


handler = FileHandler()
observer = Observer()


@app.on_event("startup")
def startup_event():
    model_file = Path(MODEL_FILE)
    app.state.ml = ml_io(model_file=model_file, mode="rb")

    observer.schedule(handler, path=MODEL_FILE, recursive=False)
    observer.start()


@app.on_event("shutdown")
def shutdown_event():
    observer.stop()
    observer.join()


@app.post("/predict")
def predict(attributes: Attributes) -> Predictions:
    X = attributes.model_dump()
    y_pred = app.state.ml.predict_one(X)
    app.state.ml.meta["predicted"] += 1

    return {
        "species": y_pred,
        **app.state.ml.meta,
    }


@app.post("/learn")
def learn(learn_attributes: LearnAttributes) -> Learnings:
    X = learn_attributes.attributes.model_dump()
    y = learn_attributes.species

    y_pred = app.state.ml.predict_one(X)
    app.state.ml.learn_one(X, y)

    app.state.ml.meta["learned"] += 1

    ml_io(model_file=Path(MODEL_FILE), mode="wb", ml_object=app.state.ml)

    return {
        "status": f"learned {y}. Initially predicted {y_pred}",
        **app.state.ml.meta,
    }
