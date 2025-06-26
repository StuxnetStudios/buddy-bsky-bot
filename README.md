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

### Generation 1: Foundation (v1.x.x) - CURRENT
- **v1.0.0** - Initial release: Basic skeleton with core functionality
  - Bluesky authentication via app passwords
  - Mention monitoring and notification parsing
  - Follower verification system
  - Simple reply mechanism
  - Extensible codebase structure

- **v1.1.x** - Enhanced Foundation *(Planned)*
  - Better error handling & logging
  - Configuration file support
  - Rate limiting protection
  - Notification filtering (mentions only)
  - Reply cooldown system

### Generation 2: Intelligence Layer (v2.x.x) - PLANNED
- **v2.0.0** - AI Integration
  - Microsoft Copilot API integration
  - Context-aware responses
  - Personality configuration
  - Custom response templates
  - Sentiment analysis

- **v2.1.x** - Advanced Conversations
  - Thread handling & context memory
  - Multi-turn conversations
  - User preference learning
  - Response quality scoring

### Generation 3: Multi-Platform Era (v3.x.x) - IF COMMERCIAL
- **v3.0.0** - Platform Expansion
  - Twitter/X integration
  - Mastodon support
  - Cross-platform posting
  - Unified follower management

- **v3.1.x** - Analytics & Dashboard
  - Web-based admin panel
  - Interaction analytics
  - Performance metrics
  - User engagement tracking

### Generation 4: Automation & Scale (v4.x.x) - IF SUCCESSFUL
- **v4.0.0** - Advanced Automation
  - Scheduled content posting
  - Keyword-triggered responses
  - Auto-moderation features
  - Bulk follower management

- **v4.1.x** - Enterprise Features
  - Multi-bot management
  - Team collaboration tools
  - Advanced security features
  - API for third-party integrations
