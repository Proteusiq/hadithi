from typing import Literal, Final
from openai import OpenAI
from pydantic import BaseModel, Field
import polars as pl
import instructor

MODEL: Final = "gemma2"

VALID_EMOTIONS: tuple[str, ...] = tuple(
    {
        "admiration",
        "approval",
        "gratitude",
        "optimism",
        "joy",
        "neutral",
        "disapproval",
        "disappointment",
        "love",
        "relief",
        "excitement",
        "desire",
        "caring",
        "pride",
        "realization",
        "disgust",
        "annoyance",
        "remorse",
        "amusement",
        "anger",
        "grief",
        "curiosity",
        "fear",
        "surprise",
        "sadness",
        "embarrassment",
        "confusion",
        "nervousness",
    }
)


class Emotion(BaseModel):
    kind: Literal[VALID_EMOTIONS]  # type: ignore # literal does not like dynamic values
    reason: str = Field(
        ..., description="A short third person reason for selected the emotion"
    )


client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
    ),
    mode=instructor.Mode.JSON,
)


def classifier(text: str, model: str = MODEL) -> Emotion:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"You are a brilliant emotion pyschologist. What is the text emotion: Text: {text}",
            }
        ],
        response_model=Emotion,
        temperature=0.0,
    )

    return response


if __name__ == "__main__":
    pl.Config.set_fmt_str_lengths(100).set_tbl_rows(
        -1
    )  # show more text. default is 25, show all rowss

    print(f"Pyschologist: - model={MODEL}")
    dataf = pl.read_json("data/examples.json").explode(["emotion", "text"])
    dataf = (
        dataf.sample(8)
        .with_columns(
            pl.col("text")
            .map_elements(classifier, return_dtype=pl.Object)
            .alias("prediction")
        )
        .with_columns(
            pl.col("prediction")
            .map_elements(lambda p: p.kind, return_dtype=pl.String)
            .alias("prediction"),
            pl.col("prediction")
            .map_elements(lambda p: p.reason, return_dtype=pl.String)
            .alias("reason"),
        )
    )

    # import json
    # from pathlib import Path

    # Path("data/tests.json").write_text(json.dumps(dataf.to_dicts()))
    print(dataf)
