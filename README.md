# EchoBot

A minimal Telegram bot written in Python that simply echoes back any text message it receives. 

## Features
- Zero‑configuration start (just add your bot token)
- Single‑file implementation (main.py)
- Ready for auto‑CI pipelines and quick deployment

## Setup
1. **Create a Telegram bot** and obtain the API token via [BotFather](https://t.me/BotFather).
2. Clone this repository:
   ```bash
   git clone https://github.com/yourname/EchoBot.git
   cd EchoBot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```bash
   python main.py YOUR_TELEGRAM_BOT_TOKEN
   ```

The bot will start polling and will echo any text you send to it.

## Why this tiny project?
- **Rapid repo init** – you can spin it up in seconds.
- **Instant scaffolding** – only two files, no boilerplate.
- **Auto‑CI friendly** – works out‑of‑the‑box with GitHub Actions or any CI.
- **Telegram launch alerts** – the bot itself is a Telegram service!

Enjoy!