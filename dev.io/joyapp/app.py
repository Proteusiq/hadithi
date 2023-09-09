from pathlib import Path
import pickle
from pydantic import BaseModel
from fastapi import FastAPI


MODEL_FILE = "model/naive.pickle"
app = FastAPI(title="😂 Pure Joy")


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


@app.on_event("startup")
def startup_event():
    model_file = Path(MODEL_FILE)
    if not model_file.exists():
        from ml import penguins_model

        app.state.ml = penguins_model()
    else:
        app.state.ml = pickle.loads(model_file.read_bytes())


@app.post("/predict")
def predict(features: Features) -> str:
    X = features.model_dump()
    return app.state.ml.predict_one(X)


@app.post("/learn")
def learn(learn_features: LearnFeatures) -> dict[str, str]:
    X = learn_features.features.model_dump()
    y = learn_features.species

    y_pred = app.state.ml.predict_one(X)
    app.state.ml.learn_one(X, y)

    with Path(MODEL_FILE).open("wb") as f:
        pickle.dump(app.state.ml, f)

    return {"msg": f"we learned {y}. We initially predicted {y_pred}"}
