# Code Snippets 

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