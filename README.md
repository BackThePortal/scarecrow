### TTM Ecosystem

- [TheTinMen Posts Database](https://github.com/BackThePortal/thetinmen-db)
- [TheTinMen Posts Classifier](https://github.com/BackThePortal/thetinmen)
- _Scarecrow - Discord Bot_

# Scarecrow

Scarecrow is a Discord bot used in TheTinMen Discord Server to announce new posts published in the Instagram profile. It
also provides easy to use functions to browse the posts database.
It's written in Python and is currently self-hosted in a Raspberry Pi.

## Requirements

- Python 3.11

## Installation

First, you need to clone the repositiory.

```shell
git clone https://github.com/BackThePortal/scarecrow.git
```

### Quick install

If you're on Windows, use [`setup.bat`](setup.bat) to prepare the .env file and run the bot automatically.

During setup, a Notepad window will pop up. Set the Discord API token there.

### Manual install

1. **Create the .env file.**

   Copy the .env.example and set the Discord API token.


2. **Install dependencies**

   Use `pip install -r requirements.txt`


4. Run `main.py.

   Use `python main.py`

## Architecture
This bot is uses the library [discord.py](https://discordpy.readthedocs.io/), but I'm planning on switching to its fork [nextcord](https://docs.nextcord.dev/).

## Things to consider

- Scarecrow automatically generates a file called `channel.txt`, where it stores the ID of the target channel. Do not
  edit nor create this file manually, as it might prevent the bot from functioning properly.
