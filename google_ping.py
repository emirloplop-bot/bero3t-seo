import requests

def ping_google():
    """Google'a site gönder"""
    sites = [
        "https://guns.lol/bero3t",
        "https://linktr.ee/bero3t",
        "https://instagram.com/f1formula_",
        "https://tiktok.com/@berouser",
        "https://youtube.com/@bero3t"
    ]

    for site in sites:
        url = f"https://www.google.com/ping?sitemap={site}"
        try:
            response = requests.get(url)
            print(f"✅ Ping gönderildi: {site}")
        except:
            print(f"❌ Hata: {site}")

if __name__ == "__main__":
    ping_google()
