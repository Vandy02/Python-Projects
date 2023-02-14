
import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '+155555555',
        'message' : 'You are doing great! ',
        'key' : 'textbelt'
    })
    print(resp.json())

schedule.every().day.at('08:00').do(send_message)


