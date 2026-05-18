#!/usr/bin/env python3
"""EchoBot – a tiny Telegram bot that echoes incoming text messages.

Run with:
    python main.py <TELEGRAM_BOT_TOKEN>
"""

import sys
import logging
from pathlib import Path

# Attempt to import python-telegram-bot; provide a friendly error if missing.
try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
except ImportError:
    sys.stderr.write(
        "Missing dependency 'python-telegram-bot'. Install via: pip install -r requirements.txt\n"
    )
    sys.exit(1)

# Configure basic logging – ideal for CI pipelines.
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the received message back to the user."""
    if update.message is None:
        return
    text = update.message.text
    user = update.effective_user.username or update.effective_user.id
    logger.info("Echoing message from %s: %s", user, text)
    await update.message.reply_text(text)

def main(token: str) -> None:
    """Start the EchoBot using long polling.

    Args:
        token: Telegram bot token obtained from BotFather.
    """
    app = ApplicationBuilder().token(token).build()
    # Register a handler for normal text messages.
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    logger.info("EchoBot started – listening for messages...")
    # Run the bot until interrupted (Ctrl+C).
    app.run_polling()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python main.py <TELEGRAM_BOT_TOKEN>\n")
        sys.exit(1)
    token_arg = sys.argv[1].strip()
    if not token_arg:
        sys.stderr.write("Error: Bot token cannot be empty.\n")
        sys.exit(1)
    main(token_arg)
