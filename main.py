import re
import requests

BOT_TOKEN = "JohnCena"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

def convert_to_cite_x(url):
    match = re.match(r'https?://(?:www\.)?(?:x\.com|twitter\.com)/([^/]+)/status/(\d+)', url)
    if not match:
        return "Invalid Twitter URL. Please provide a valid tweet URL."
    
    username, tweet_id = match.groups()
    cite_x_template = f"{{{{Cite X |user={username} |number={tweet_id} |title=Tweet content |access-date={{{{subst:Date}}}}}}}}"
    return cite_x_template

def send_message(chat_id, text):
    url = f"{API_URL}sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"```\n{text}\n```",
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def get_updates(last_update_id=None):
    url = f"{API_URL}getUpdates"
    params = {"offset": last_update_id + 1} if last_update_id else {}
    response = requests.get(url, params=params).json()
    return response.get("result", [])

def main():
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
                send_message(chat_id, "I am waiting for Twitter/X URL")
            elif text == "/help":
                send_message(chat_id, "Enter any Twitter/X URL like this: https://x.com/anyuser/status/20")
            else:
                cite_x_template = convert_to_cite_x(text)
                send_message(chat_id, cite_x_template)

if __name__ == "__main__":
    main()
