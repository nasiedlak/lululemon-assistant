import requests
import yagmail
from bs4 import BeautifulSoup
from keys import FROM_EMAIL, TP_KEY, TO_EMAIL

def send_email():
    yag = yagmail.SMTP(FROM_EMAIL, TP_KEY)
    contents = "The espresso Steady State Jogger are now available!"
    yag.send(TO_EMAIL, "lululemon Jogger Update", contents)


def main():
    url = "https://shop.lululemon.com/p/men-joggers/Steady-State-Jogger/_/prod11520164?color=0001"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    swatches = doc.find(class_ = "buttonTileGroupWrapper-3BgOU")
    goal = "espresso"
    for swatch in swatches:
        color = swatch.get("aria-label")
        if(color == goal):
            send_email()

if __name__ == "__main__":
    main()
