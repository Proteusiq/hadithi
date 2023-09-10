from pydantic import BaseModel


class Attributes(BaseModel):
    island: str
    bill_length_mm: float | None
    bill_depth_mm: float | None
    flipper_length_mm: float | None
    body_mass_g: float | None
    sex: str | None


class LearnAttributes(BaseModel):
    attributes: Attributes
    species: str


class Predictions(BaseModel):
    species: str | None
    predicted: int
    learned: int


class Learnings(BaseModel):
    status: str
    predicted: int
    learned: int
