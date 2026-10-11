# Prothombot1
[![Static Badge](https://img.shields.io/badge/Telegram-Bot-0088cc?logo=telegram)](https://telegram.org/blog/bot-revolution)
![GitHub License](https://img.shields.io/github/license/KEmel49/prothombot1)
[![Static Badge](https://img.shields.io/badge/Twitter-API-black?logo=x&logoColor=%23454444&labelColor=white)](https://developer.twitter.com/en/)
<br>
A Telegram bot that converts a Twitter/X post URL into a Wikipedia-compatible `{{Cite tweet}}` template.

## Overview

This bot listens for Telegram messages, checks whether the message is a valid Twitter/X URL, fetches the tweet text, and returns a ready-to-paste citation template for Wikipedia.

It was designed to simplify the workflow of generating citation snippets similar to the behavior of tools like [Citer](https://citer.toolforge.org/).

## Features

- Accepts links in the format:
  - `https://x.com/username/status/1234567890`
  - `https://twitter.com/username/status/1234567890`
- Fetches tweet text via the Twitter/X API
- Produces a Wikipedia-style `{{Cite tweet}}` template
- Sends the generated result back to the Telegram chat

## Requirements

- Python 3
- Telegram Bot API token
- Twitter/X bearer token
- Python packages:
  - `requests`
  - `tweepy`

## Installation

Install the required dependencies:

```bash
pip install requests tweepy
```

## Configuration

Open `main.py` and set your credentials:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bearer_token = "YOUR_TWITTER_BEARER_TOKEN"
```

## Run the bot

```bash
python main.py
```

## Usage

Send a valid Twitter/X URL to the bot.

Example:

```text
https://x.com/anyuser/status/20
```

The bot will return a template similar to:

```wikitext
{{Cite tweet |user=anyuser |number=20 |title=Tweet content |access-date={{subst:Date}}}}
```

## Telegram commands

- `/start` — starts the bot
- `/help` — shows example usage

## Notes and limitations

- The bot depends on the Twitter/X API, which may rate-limit requests.
- Some tweets may fail to load if they are unavailable or restricted.
- Some older tweets may require an additional `|date` field.
- Line breaks in tweet content can break Wikipedia wikitext formatting and may need manual cleanup.
- Always review the generated template before pasting it into Wikipedia.

## Acknowledgements

This project is inspired by the idea of generating Wikipedia-friendly tweet citations using structured templates.
