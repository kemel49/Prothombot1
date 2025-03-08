import re
import requests
import tweepy

BOT_TOKEN = "" # Telegram bot token
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

bearer_token = "" # Twitter/X Bearer token


client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweet_text(tweet_id):
 # Get tweet text from original post
    try:
        response = client.get_tweet(tweet_id, tweet_fields=['text'])
        return response.data.text
    except tweepy.TweepyException:
        return None

def convert_to_cite_x(url):
 # Extract username and tweet number from input url
    match = re.match(r'https?://(?:www\.)?(?:x\.com|twitter\.com)/([^/]+)/status/(\d+)', url)
    if not match:
        return "Invalid Twitter URL. Just give me a valid tweet URL."

    username, tweet_id = match.groups()
    tweet_text = fetch_tweet_text(tweet_id)

    if not tweet_text:
        return "Tweet not found or doesn't exist."

    # Generate the {{Cite tweet}} template
    cite_template = f"{{{{Cite tweet |user={username} |number={tweet_id} |title={tweet_text} |access-date={{{{subst:Date}}}}}}}}"
    return cite_template

def send_message(chat_id, text):
 # Bot send message in mono format, it's easy to copy in telegram
    url = f"{API_URL}sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"```\n{text}\n```",
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def get_updates(last_update_id=None):
 # prevent bot from spamming messages afain and again
    url = f"{API_URL}getUpdates"
    params = {"offset": last_update_id + 1} if last_update_id else {}
    response = requests.get(url, params=params).json()
    return response.get("result", [])

def main():
 # Main functionality for telegram bot
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)

        for update in updates:
            last_update_id = update["update_id"]
            message = update.get("message", {})
            text = message.get("text", "")
            chat_id = message.get("chat", {}).get("id")

            if not chat_id:
                continue

            if text == "/start":
                send_message(chat_id, "I am waiting for a Twitter/X URL")
            elif text == "/help":
                send_message(chat_id, "Enter any Twitter/X URL like this: https://x.com/anyuser/status/20")
            else:
                cite_template = convert_to_cite_x(text)
                send_message(chat_id, cite_template)

if __name__ == "__main__":
    main()
