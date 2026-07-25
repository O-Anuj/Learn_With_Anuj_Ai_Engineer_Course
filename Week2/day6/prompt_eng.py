import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"


def llm_ans(prompt):
    message={
        "role":"user",
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans


prompt = """
# ROLE
You are a customer support ticket classifier for a mobile and laptop company.

# TASK
Read the customer's complaint and classify it into exactly one category.

# CATEGORIES
- BILLING: Issues related to payments, invoices, charges, subscriptions, refunds, or billing errors.
- TECHNICAL: Issues related to device malfunction, software bugs, hardware problems, login issues, or connectivity.
- RETURN: Issues related to returning, replacing, exchanging, or canceling an order.

# RULES
1. Choose only one category.
2. If the complaint does not belong to any of the above categories, return "OTHER".
3. Do not explain your answer.
4. Output must contain only one word.

# OUTPUT
BILLING
TECHNICAL
RETURN
OTHER

# USER COMPLAINT
My laptop is broke and i can`t use it , please help me to fix it. and i  return the product and give me a new one.
"""

print(llm_ans(prompt))