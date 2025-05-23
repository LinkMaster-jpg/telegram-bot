import telebot
import time
from temu_scraper import get_product_links

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL = "@YOUR_CHANNEL_USERNAME"
DELAY = 360  # 6 minutes

bot = telebot.TeleBot(TOKEN)

def main():
    while True:
        try:
            links = get_product_links()
            for link in links:
                bot.send_message(CHANNEL, link)
                time.sleep(2)
        except Exception as e:
            print("Error:", e)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
