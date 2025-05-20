import time
import telebot
from scrape_temuproducts import scrape_temuproduct_links

TOKEN = "7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI"
CHANNEL_USERNAME = "@Similarproducts"
DELAY = 360  # כל 6 דקות

bot = telebot.TeleBot(TOKEN)

def send_links():
    links = scrape_temuproduct_links()
    for link in links:
        try:
            bot.send_message(CHANNEL_USERNAME, link)
            time.sleep(1)
        except Exception as e:
            print(f"Error sending link: {e}")

if __name__ == "__main__":
    while True:
        try:
            send_links()
        except Exception as e:
            print(f"Error in loop: {e}")
        time.sleep(DELAY)
