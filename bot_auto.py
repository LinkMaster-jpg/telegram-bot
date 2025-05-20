import telebot
import time

# הגדרות
TOKEN = '7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI'
CHANNEL_USERNAME = '@Similarproducts'
DELAY = 600  # שליחה כל 10 דקות (600 שניות)

bot = telebot.TeleBot(TOKEN)

def read_links():
    with open("links.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def send_links():
    links = read_links()
    for link in links:
        try:
            bot.send_message(CHANNEL_USERNAME, link)
            print(f"נשלח: {link}")
            time.sleep(DELAY)
        except Exception as e:
            print(f"שגיאה בשליחה: {e}")

if __name__ == "__main__":
    send_links()
