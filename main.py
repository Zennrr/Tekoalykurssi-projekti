import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

ASSISTANT_ID = os.getenv("ASSISTANT_ID")
client = OpenAI()

# Create a thread
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "What is the most liveable city in the world?",
        }
    ]
)

# Run the thread
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
print(f"Running thread: {run.id}")

# Wait for the run to complete
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"Run status: {run.status}")
    time.sleep(1)
else:
    print(f"Run completed")

# Retrieve the messages
messages_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = messages_response.data

# Print the response
latest_message = messages[0]
print(f"Response: {latest_message.content[0].text.value}")