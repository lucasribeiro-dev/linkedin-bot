# LinkedIn Automation Bot

A Python-based automation bot that helps you grow your LinkedIn network by automatically liking posts and connecting with people. This bot uses Selenium to interact with LinkedIn's interface in a safe and controlled manner.

## Features

- Automatic post liking based on specified keywords
- Automated connection requests
- Configurable settings for personalized automation
- Safe interaction with LinkedIn's interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Chrome browser installed
- LinkedIn account

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
cd linkedin-bot
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the bot, you need to configure your settings in the `config.json` file. Here's what you need to set up:

1. Open `config.json` in your preferred text editor
2. Configure the following settings:
   - LinkedIn credentials (email and password)
   - Search keywords for posts to like
   - Connection request message
   - Daily limits for likes and connections
   - Other bot behavior settings

⚠️ **Important**: Never share your `config.json` file or commit it to version control. Add it to your `.gitignore` file.

## Usage

1. Make sure your virtual environment is activated
2. Configure your `config.json` file
3. Run the bot:
```bash
python main.py
```

The bot will:
- Log in to your LinkedIn account
- Like relevant posts
- Send connection requests to relevant profiles
- Respect the daily limits you've set

## Safety Guidelines

- The bot includes random delays between actions to mimic human behavior
- It's recommended to set conservative daily limits to avoid LinkedIn's rate limiting
- Monitor the bot's activity regularly
- Don't use the bot for spam or aggressive networking

## Troubleshooting

If you encounter any issues:
1. Check your internet connection
2. Verify your LinkedIn credentials in `config.json`
3. Ensure Chrome is installed and up to date
4. Check if you've hit LinkedIn's daily limits

## Disclaimer

This bot is for educational purposes only. Use it responsibly and in accordance with LinkedIn's Terms of Service. The developers are not responsible for any account restrictions or bans that may result from using this bot.

