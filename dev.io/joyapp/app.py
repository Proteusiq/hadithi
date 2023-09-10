from pathlib import Path
import pickle

from pydantic import BaseModel
from fastapi import FastAPI
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


MODEL_FILE = "model/naive.pickle"
app = FastAPI(title="😂 Pure Joy")


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"path={event.src_path} event={event.event_type}")
        app.state.ml = pickle.loads(Path(MODEL_FILE).read_bytes())


class Features(BaseModel):
    island: str
    bill_length_mm: float | None
    bill_depth_mm: float | None
    flipper_length_mm: float | None
    body_mass_g: float | None
    sex: str | None


class LearnFeatures(BaseModel):
    features: Features
    species: str


handler = FileHandler()
observer = Observer()


@app.on_event("startup")
def startup_event():
    model_file = Path(MODEL_FILE)
    if not model_file.exists():
        from ml import penguins_model

        ml = penguins_model()
        ml.meta = {"predictions": 0, "learned": 0,}

        app.state.ml = ml
    else:
        app.state.ml = pickle.loads(model_file.read_bytes())

    observer.schedule(handler, path=MODEL_FILE, recursive=False)
    observer.start()


@app.on_event("shutdown")
def shutdown_event():
    observer.stop()
    observer.join()


@app.post("/predict")
def predict(features: Features) -> dict[str, str | int | None]:
    X = features.model_dump()
    y_pred = app.state.ml.predict_one(X)
    app.state.ml.meta["predictions"] += 1

    return {
        "predicted": y_pred,
        **app.state.ml.meta,
    }


@app.post("/learn")
def learn(learn_features: LearnFeatures) -> dict[str, str | int]:
    X = learn_features.features.model_dump()
    y = learn_features.species

    y_pred = app.state.ml.predict_one(X)
    app.state.ml.learn_one(X, y)

    app.state.ml.meta["learned"] += 1

    Path(MODEL_FILE).write_bytes(pickle.dumps(app.state.ml))

    return {
        "status": f"learned {y}. Initially predicted {y_pred}",
        **app.state.ml.meta,
    }
