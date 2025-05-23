import time
import telebot
from temu_scraper import scrape_temuproduct_links

TOKEN = "7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI"
CHANNEL_USERNAME = "@Similarproducts"
DELAY = 360  # 6 minutes

bot = telebot.TeleBot(TOKEN)

def send_links():
    links = scrape_temuproduct_links()
    for link in links:
        try:
            bot.send_message(CHANNEL_USERNAME, link)
            print(f"נשלח: {link}")
            time.sleep(2)
        except Exception as e:
            print(f"שגיאה בשליחה: {e}")

while True:
    try:
        send_links()
    except Exception as e:
        print(f"שגיאה כללית: {e}")
    time.sleep(DELAY)
