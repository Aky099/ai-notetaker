# ai-notetaker

Streamlit app that transcribes uploaded audio and summarizes it with Groq.

## Run & Operate

- `streamlit run app.py --server.port 5000` — run the Streamlit app

## Stack

- Python 3.11+
- Streamlit
- Groq
- python-dotenv

## Where things live

- `app.py` — Streamlit page and processing flow
- `utils/transcribe.py` — Groq audio transcription
- `utils/summarize.py` — Groq transcript summarization
- `requirements.txt` — Python dependencies

## Architecture decisions

_Populate as you build — non-obvious choices a reader couldn't infer from the code (3-5 bullets)._

## Product

_Describe the high-level user-facing capabilities of this app once they exist._

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
