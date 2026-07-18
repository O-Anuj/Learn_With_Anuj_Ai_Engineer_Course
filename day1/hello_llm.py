import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY") or os.getenv("GROQ-API-KEY")

if not my_api_key:
    raise ValueError("Set GROQ_API_KEY in .env before running this script")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="What is java?"
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message]

response=client.chat.completions.create(model=model, messages=messages)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)