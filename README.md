# SearchBot

This project is an AI-powered information retrieval assistant that helps users answer questions based on provided
context. It supports multiple search bots and languages, allowing for flexible and accurate information retrieval.

[中文说明](README-CN.md)

## Supported Bots

- Baidu
- Bing

## Supported Languages

- Chinese
- English

## Example Usage

```bash
pip install searchbot
```

```python
from searchbot.rag import search

query = "What is the capital of France?"
bot_name = "bing"
lang = "english"
verbose = True

answer = search(query, bot_name=bot_name, lang=lang, verbose=verbose)
print(answer)
```