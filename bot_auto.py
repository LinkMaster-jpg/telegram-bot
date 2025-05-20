import telebot
import time

TOKEN = '7764129644:AAGb92YoaceuDuoegh15fpXSZ1WXICOjWZI'
CHANNEL_USERNAME = '@Similarproducts'
DELAY = 600  # 10 דקות

bot = telebot.TeleBot(TOKEN)

def load_links():
    with open("links.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    links = load_links()
    index = 0
    while True:
        if index >= len(links):
            index = 0
        link = links[index]
        try:
            bot.send_message(CHANNEL_USERNAME, link)
            print(f"נשלח: {link}")
        except Exception as e:
            print(f"שגיאה בשליחה: {e}")
        index += 1
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
