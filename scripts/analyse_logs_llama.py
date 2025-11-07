import os
from openai import OpenAI

# Initialize the client for Hugging Face router
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_API_KEY"],
)

# Read Ansible log
with open("ansible_log.txt", "r") as f:
    logs = f.read()

# Define the prompt
prompt = f"""
You are an expert DevOps assistant. 
The following is an Ansible playbook execution log.

Please analyze and explain:
1. What configuration tasks were attempted or completed.
2. Identify any warnings or errors — explain their cause and suggest a possible fix.
3. Give a short summary of the overall result.

Here is the log:
{logs}
"""

# Send log to Llama model
completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct:novita",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=700,
)

# Print the result
print("\n===== LLaMA LOG ANALYSIS =====\n")
print(completion.choices[0].message.content)
print("\n===============================")
