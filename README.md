# MULTI-AGENT-FINANCIAL-ANALYST

Multi-agent financial analyst system for processing and analyzing company filings and financial data.

## Overview
Uses multiple specialized agents to extract insights from 10-K documents and other financial reports.

## Quick Start
```bash
uv sync
python main.py
```

**Note:** Full functionality requires LLM API keys. Set `GROQ_API_KEY` and `MISTRAL_AI_API_KEY` (or the exact variable names expected by the agents in this repo) as environment variables before running. Without them the agents will fail at runtime. Prefer a `.env` file loaded via python-dotenv.

## Structure
- `agents.py` – agent definitions
- `pipeline.py` – orchestration
- `prompts.py` – system prompts
- `tools.py` – tools for data access

## Tips
- Run from the repository root so relative paths to sample PDFs resolve correctly.
- Never commit API keys; prefer a `.env` file (add it to `.gitignore`) and load with `python-dotenv`.
- The sample 10-K PDF is included for local testing of document extraction.
- Check agents.py for the precise environment variable names used in this project.

Last updated: 2026-11-26
