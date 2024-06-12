import requests
import socket
import struct
import random
import time
import threading
import telebot

file = open("ips.txt", "a")
bot = telebot.TeleBot("7199158102:AAGwzvvyUEIZj_ImU36Z8U6dt3lVE54EYb8")
chat_id = 6095330716

bot.send_message(chat_id, f"Бот запущен на {requests.get('https://api.ipify.org').text}")
bot.send_message(1372616596, f"Бот запущен на {requests.get('https://api.ipify.org').text}")

def new():
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, 25565))
        if result != 0:
            print(f"Порт закрыт на {ip}.")
            return

    server_info = requests.get(f"https://api.mcstatus.io/v2/status/java/{ip}:25565").json()
    if server_info["online"]:
        to_write = f"{ip} {server_info["players"]["online"]}/{server_info["players"]["max"]}  -  {server_info["motd"]["clean"]}"
        bot.send_message(chat_id, to_write)
        bot.send_message(1372616596, to_write)
        file.write(to_write + "\n")
        print(to_write)
    else:
        print(f"Сервера {ip} не существует.")

try:
    while True:
        threading.Thread(target=new).start()
        time.sleep(0.1)
except Exception as e:
    bot.send_message(chat_id, f"Бот остановлен на {requests.get('https://api.ipify.org').text}")
    bot.send_message(1372616596, f"Бот остановлен на {requests.get('https://api.ipify.org').text}")
    print(e)
    file.close()
