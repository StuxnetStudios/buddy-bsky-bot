# Buddy - Bluesky Bot Starter Kit

**Version:** v1.0.0 (Generation 1: Foundation)

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
   python buddy-bsky-bot.py
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

## Version History

### Generation 1: Foundation (v1.x.x)
- **v1.0.0** - Initial release: Basic skeleton with core functionality
  - Bluesky authentication via app passwords
  - Mention monitoring and notification parsing
  - Follower verification system
  - Simple reply mechanism
  - Extensible codebase structure

### Future Generations
- **Generation 2 (v2.x.x)** - Intelligence Layer *(Planned)*
  - AI-powered response generation
  - Content analysis and sentiment detection
  - Advanced conversation handling

- **Generation 3 (v3.x.x)** - Multi-Platform Era *(Planned)*
  - Cross-platform social media integration
  - Unified dashboard and analytics
  - Advanced automation features
