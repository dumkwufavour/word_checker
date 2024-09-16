# Discord Bot for Banned Word Detection

This Discord bot prevents users from sending messages that contain banned words in any channel of a server. The list of banned words is stored in a JSON file. When a user tries to send a message with a banned word, the bot deletes the message and notifies the channel that the user attempted to use a banned word.

## Version

Current version: `0.1.3`

For a full history of changes, refer to the [Changelog](CHANGELOG.md).

## Features

- **Banned Word Detection**: Automatically detects and blocks messages containing words from a predefined list.
- **Message Deletion**: Deletes messages that contain banned words.
- **User Notification**: Notifies the channel when a user attempts to use a banned word.
- **Environment Variables**: Securely manages bot tokens using a `.env` file.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **discord.py** library
- **dotenv** library for environment variable management

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/discord-bot.git
   cd discord-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install discord.py python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory:
   ```bash
   BOT_TOKEN=your-discord-bot-token
   ```

4. **Create the `banned_words.json` file**:
   Create a `banned_words.json` file in the root directory:
   ```json
   {
     "banned_words": ["fuck", "shit", "damn"]
   }
   ```

### Running the Bot

To start the bot, run the following command:

```bash
python bot.py
```

### Enabling Message Content Intent

Make sure to enable the **Message Content Intent** in the [Discord Developer Portal](https://discord.com/developers/applications) for your bot to detect message content.

## Full Documentation

For detailed instructions on how to set up and customize the bot, check out the full documentation on GitBook:

[Full Documentation on GitBook](https://sydicated.gitbook.io/word-checker/)