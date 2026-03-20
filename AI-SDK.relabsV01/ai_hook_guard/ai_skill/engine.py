# ai_skill/engine.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

from ai_hook_guard.ai_skill.prompts import build_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_ai_skill(code, findings):

    prompt = build_prompt(code, findings)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
