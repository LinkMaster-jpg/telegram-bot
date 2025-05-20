import telebot
import time

TOKEN = "7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI"
CHANNEL_USERNAME = "@Similarproducts"
DELAY = 600  # כל 10 דקות

bot = telebot.TeleBot(TOKEN)

def load_links():
    try:
        with open("links.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def send_links_periodically():
    links = load_links()
    index = 0
    while True:
        if not links:
            print("לא נמצאו קישורים.")
            time.sleep(DELAY)
            continue

        link = links[index % len(links)]
        bot.send_message(CHANNEL_USERNAME, link)
        print(f"נשלח: {link}")
        index += 1
        time.sleep(DELAY)

send_links_periodically()
