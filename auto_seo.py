import os
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("TELEGRAM_TOKEN ve TELEGRAM_CHAT_ID tanımlı değil.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Telegram mesajı başarıyla gönderildi.")
        else:
            print(f"Telegram mesajı gönderilemedi: {response.text}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    send_telegram_message("🚀 *bero3t SEO Bot* çalıştı ve sitemap kontrol edildi!")
