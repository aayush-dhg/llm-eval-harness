# LLM Eval Harness

A pytest-based harness that tests a grounded LLM question-answering app against a golden dataset.

## Status

Session 1 complete: 10 hand-written evaluation cases, parametrized pytest, and a local `llama3.2:latest` model running through Ollama.

Current local result: 10/10 cases passing.

In progress: larger golden dataset, scoring, LLM-as-judge evaluation, CI, reports, and prompt/model comparison.

## Run it

1. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Make sure Ollama is running and the model is available:

   ```bash
   ollama list
   ```

   This project currently uses:

   ```text
   llama3.2:latest
   ```

   If needed, start the model with:

   ```bash
   ollama run llama3.2:latest
   ```

3. Run the evaluation suite:

   ```bash
   python -m pytest -v
   ```

## What it tests

- Answers contain the required key facts from the provided context
- The model refuses when the context does not support an answer
- Golden dataset cases are executed automatically through parametrized pytest

## First results

10/10 evaluation cases currently pass with `llama3.2:latest`.

During development, one valid answer initially failed because the test expected the exact word `mutable`, while the model correctly answered that the list could be modified after creation.

The test was updated to accept semantically equivalent phrasing, highlighting one of the core challenges of LLM evaluation.
