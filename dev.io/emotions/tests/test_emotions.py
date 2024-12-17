import pytest

from emotions.sentiments import classifier

# noqa: E501
EMOTIONS_EXAMPLES = {
    "nervousness": "I’m nervous about the job interview tomorrow. It’s a big opportunity!",
    "confusion": "His mixed signals have left me feeling utterly confused.",
    "pride": "Seeing my son graduate with honors filled me with pride.",
    "gratitude": "I really appreciate you covering my shift last minute. You're a lifesaver!",
    "sadness": "I’ve felt a lingering sadness since the end of that relationship.",
    "disapproval": "The way he spoke to the customer was completely unacceptable!",
    "optimism": "The future of renewable energy looks bright. We’re heading in the right direction!",
}


@pytest.mark.parametrize(
    "example", EMOTIONS_EXAMPLES.items(), ids=EMOTIONS_EXAMPLES.keys()
)
def test_emotions(example):
    # Arrange
    expected, text = example

    # Act
    prediction = classifier(text).kind

    # Assert
    assert prediction == expected
