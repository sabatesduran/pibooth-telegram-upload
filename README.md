pibooth-telegram-upload
=================

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads)
[![PyPi package](https://badge.fury.io/py/pibooth-telegram-upload.svg)](https://pypi.org/project/pibooth-telegram-upload)
[![PyPi downloads](https://img.shields.io/pypi/dm/pibooth-telegram-upload?color=purple)](https://pypi.org/project/pibooth-telegram-upload)

`pibooth-telegram-upload` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application.

Install
-------

    $ pip3 install pibooth-telegram-upload

Configuration
-------------

Below are the new configuration options available in the [pibooth](https://pypi.org/project/pibooth) configuration. **The keys and their default values are automatically added to your configuration after first** [pibooth](https://pypi.org/project/pibooth) **restart.**

``` {.ini}
[Telegram]

# Telegram bot token
telegram_token =

# Chat/Channel id
telegram_chat_id =

# Message to show when sending the picture
telegram_message =

```

### Note

Edit the configuration by running the command `pibooth --config`.
