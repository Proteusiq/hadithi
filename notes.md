# Code Snippets 

```python
import asyncio
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from litellm import completion, acompletion

# --- App setup ---

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --- Config ---

MODEL = "ollama/llama3"
API_BASE = "http://localhost:11434"
SYSTEM_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, say that you don't know. "
    "Use three sentences maximum and keep the answer concise."
)

# --- Data models ---

class Question(BaseModel):
    question: str


class Stream4(BaseModel):
    stop: int


# --- LLM interaction ---

def ask_llm(question: str) -> str:
    """Blocking call to get answer from LLM."""
    response = completion(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        api_base=API_BASE,
    )
    return response['choices'][0]['message']['content']


async def stream_llm_answer(question: str) -> AsyncGenerator[str, None]:
    """Async generator that streams LLM response."""
    async for chunk in acompletion(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        api_base=API_BASE,
        stream=True,
    ):
        delta = chunk["choices"][0]["delta"]
        content = delta.get("content")
        if content:
            print(content, end="", flush=True)
            yield f"data: {content}\n\n"
        await asyncio.sleep(0.1)  # optional pacing


# --- Routes ---

@app.post("/nostream")
def no_stream_llm(question: Question):
    answer = ask_llm(question.question)
    return {"answer": answer}


@app.get("/stream-with-get")
async def stream_response_get(question: str):
    return StreamingResponse(
        stream_llm_answer(question),
        media_type="text/event-stream"
    )


@app.post("/stream-with-post")
async def stream_response_post(question: Question):
    return StreamingResponse(
        stream_llm_answer(question.question),
        media_type="text/event-stream"
    )
```

old read

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI, AsyncOpenAI


OPEN_AI_API_KEY = 'you_api_key'
async_client = AsyncOpenAI(api_key=OPEN_AI_API_KEY)
client = OpenAI(api_key=OPEN_AI_API_KEY)

app = FastAPI()

async def stream_assistant_response(assistant_id, thread_id):
    stream =  async_client.beta.threads.runs.stream(
        assistant_id=assistant_id,
        thread_id=thread_id
    )

    async with stream as stream:
        async for text in stream.text_deltas:
            yield f"data: {text}\n\n"


@app.get("/message")
async def add_message(assistant_id, thread_id, message):
    # make sure thread exist
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )

    return StreamingResponse(stream_assistant_response(assistant_id, thread_id), media_type="text/event-stream")
    ```