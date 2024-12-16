from subprocess import run

from phi.agent import Agent
from phi.model.groq import Groq
from rich.console import Console
from rich.prompt import Prompt

console = Console(style="bold blue")


def xpython(text: str):
    console.print(f"Input: {text}")
    result = run(
        ["python", "-c", text],
        check=True,
        text=True,
        capture_output=True,
    )
    result_text = result.stdout.strip()

    console.print(result_text)
    return f"The answer is {result_text!r}"

agent = Agent(
    instructions=[
        "Use the tool to answer the questions",
        "Python script should make use of variables",
        "Python script prints the final answer",
        "Use the answer from the tool."
    ],
    model=Groq(id="llama-3.3-70b-versatile",),
    tools=[xpython],
    temperature=0.0,
)


def main():
    console.print("How can I help?")

    while prompt := Prompt.ask("User", console=console):
        agent.print_response(prompt,)


if __name__ == "__main__":
    main()
