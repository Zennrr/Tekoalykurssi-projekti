import time
from openai import OpenAI

ASSISTANT_ID = "asst_GmFrg9ffMtMxMBd9xoDhN845"
client = OpenAI()

thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "What is the most liveable city in the world?",
        }
    ]
)

run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
print(f"Running thread: {run.id}")

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"Run status: {run.status}")
    time.sleep(1)
else:
    print(f"Run completed")

messages_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = messages_response.data

latest_message = messages[0]
print(f"Response: {latest_message.content[0].text.value}")