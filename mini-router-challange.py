import requests


# -------- CONFIG (fill these from Network tab) --------
ROUTER_IP = "http://192.168.0.1"

LOGIN_URL = "http://192.168.0.1/adminLogin?callback=jQuery111302526878920645955_1769421153553&loginparam=%7B%22username%22%3A%22{username}%22%2C%22password%22%3A%22{password}%22%7D&_=1769421153555"  # full adminLogin URL
DATA_URL = "http://192.168.0.1/jsonp_dashboard?callback=jQuery111305776881634512865_1769610947027&_=1769610947031"  # XHR request where you saw pDashBetteryVol

USERNAME = "admin"  # admin
PASSWORD = "89815951"  # modem passwor

COOKIE_NAME = "mach"  # you already saw this
COOKIE_VALUE = "8N8iMOEAB0QxVg7hOymKSr1r24bB6Qx"  # value from request headers
# -----------------------------------------------------


session = requests.Session()

# 1. login
session.get(LOGIN_URL, params={"username": USERNAME, "password": PASSWORD})

# 2. set session cookie manually
session.cookies.set(COOKIE_NAME, COOKIE_VALUE)

# 3. request battery data
r = session.get(DATA_URL)
text = r.text

with open("response.txt", "w", encoding="utf-8") as file:
    file.write(text)

index = text.find("<batteryPercent>")
# print(index)


print(f"The battery is at {text[71]+text[72]}%")
# already logged in
# session + cookie already set

POWER_OFF_URL = "http://192.168.0.1/jsonp_power_off?callback=jQuery1113009751890353374915_1769895323613&_=1769895323618"  # copy from Network tab
REBOOT_URL = "http://192.168.0.1/jsonp_reset?callback=jQuery111309272888391723422_1770108553524&_=1770108553530"
METHOD = "GET"  # or POST (check Headers)

userinput = input("1.Reboot\n2.Shutdown\n")


def multiselector(response):
    # 1.Reboot
    # 2.TurnOff
    if response == "1":
        session.get(REBOOT_URL)
    if response == "2":
        session.get(POWER_OFF_URL)


multiselector(userinput)
