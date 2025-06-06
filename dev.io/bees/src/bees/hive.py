from datetime import datetime
from typing import Literal

from openai import OpenAI
from saa import Clock
from swarm import Agent, Swarm

ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="NotNeeded",
)

client = Swarm(client=ollama_client)


def get_spoken_time(
    language: Literal[
        "en",
        "da",
        "sw",
    ],
) -> str:
    """
    Get spoken time:
       language: iso code for a language
    """
    clock = Clock(language)
    now = datetime.now()
    results = clock(now)
    print(results)
    return results


def transfer_to_ur(message) -> Agent:
    print(f"The Message: {message}")
    _ = message
    return ur


# list of open source model supporting tools https://ollama.com/search?c=tools

preben = Agent(
    name="Preben",
    instructions="You are Preben. Function operator",
    functions=[transfer_to_ur],  # type: ignore
    model="smollm2",
)

ur = Agent(
    name="Ur",
    instructions="Use get_spoken_time to answer what time it is a given language.",
    functions=[get_spoken_time],  # type: ignore
    model="qwen2.5",
)

response = client.run(
    agent=preben,
    messages=[{"role": "user", "content": "Ask what time it is in Danish?"}],
)

print(response.messages[-1]["content"])
