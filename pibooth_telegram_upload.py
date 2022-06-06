# -*- coding: utf-8 -*-

"""pibooth plugin for uploading pictures to Telegram"""

import os
import telegram

try:
    from telegram.error import TelegramError
except ImportError:
    InstalledAppFlow = None
    pass

import pibooth
from pibooth.utils import LOGGER


__version__ = "1.0.0"

SECTION = "Telegram"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option(SECTION, "telegram_token", "", "Telegram Token")
    cfg.add_option(SECTION, "telegram_chat_id", "", "Telegram chat ID")
    cfg.add_option(
        SECTION,
        "telegram_message",
        "",
        "Message sended on every posted photo",
    )


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Verify Telegram credentials"""
    telegram_token = cfg.get(SECTION, "telegram_token")
    telegram_chat_id = cfg.get(SECTION, "telegram_chat_id")

    if not telegram_token:
        LOGGER.error(
            "Telegram Token not defined in ["
            + SECTION
            + "][telegram_token], uploading deactivated"
        )
    elif not telegram_chat_id:
        LOGGER.error(
            "Telegram Chat ID not defined in ["
            + SECTION
            + "][telegram_chat_id], uploading deactivated"
        )
    else:
        LOGGER.info("Initializing Telegram client")
        app.telegram_client = telegram.Bot(token=telegram_token)


@pibooth.hookimpl
def state_processing_exit(app, cfg):
    """Upload picture to Telegram chat"""
    if hasattr(app, "telegram_client"):
        chat_id = cfg.get(SECTION, "telegram_chat_id").strip('"')
        upload_path = os.path.basename(app.previous_picture_file)
        message = cfg.get(SECTION, "telegram_message")
        try:
            response = app.telegram_client.send_photo(
                chat_id=chat_id,
                caption=message,
                photo=app.previous_picture_file,
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
            LOGGER.info("File uploaded to Telegram chat: " + response)
        except TelegramError as e:
            LOGGER.error(e)
