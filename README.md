# Buddy - Bluesky Bot Starter Kit

A simple Bluesky bot that monitors mentions and only replies to followers.

## Features

- Authenticates with Bluesky using app passwords
- Monitors notifications for mentions
- Only replies to users who are followers
- Simple and extensible codebase

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install atproto python-dotenv
   ```

3. Create a `.env` file in the project directory with your Bluesky credentials:
   ```
   BSKY_HANDLE=your_handle.bsky.social
   BSKY_APP_PASSWORD=your_app_password
   ```

   **Note**: Use your app password, not your account password. Generate one at https://bsky.app/settings/app-passwords

4. Run the bot:
   ```bash
   python buddy.py
   ```

## Configuration

- The bot will only reply to mentions from users who follow the account
- Default reply message: "I only interact with my followers."
- Modify the `reply_text` variable in `parse_notifications()` to customize the response

## Requirements

- Python 3.7+
- atproto library
- python-dotenv library

## License

Copyleft - Stuxnet Studios 2025

## Security

- Never commit your `.env` file to version control
- Keep your app password secure
- Regularly rotate your app passwords
