import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

SYSTEM_PROMPT = """You summarize meeting transcripts clearly and faithfully.
Return Markdown with exactly these three sections, in this order:
## Summary
## Key Points
## Action Items

Use concise, useful bullets where appropriate. If the transcript does not
contain any action items, write "- None identified." under Action Items."""


def summarize_transcript(transcript: str) -> str:
    """Summarize a transcript with Groq's chat completions API."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript},
        ],
    )
    return response.choices[0].message.content or ""