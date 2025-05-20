import time
import telebot
from scrape_temuproducts import scrape_temuproduct_links

TOKEN = "7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI"
CHANNEL_USERNAME = "@Similarproducts"
DELAY = 360  # 6 minutes

bot = telebot.TeleBot(TOKEN)

def send_links():
    links = scrape_temuproduct_links()
    for link in links:
        try:
            bot.send_message(CHANNEL_USERNAME, link)
            time.sleep(2)
        except Exception as e:
            print("Error sending link:", e)

if __name__ == "__main__":
    while True:
        try:
            send_links()
            time.sleep(DELAY)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)