from send_sms import send_message
import schedule
import time
MORNING_MESSAGES = [
    "Good morning love!",
    "Hi babe! I hope you have a great day today!",
    "Rise and shine! Love you.",
    "It's a beautiful day to be alive! What are you grateful for today?",
    "Good morning honey! Have the best day!",
    "Good morning."
]

schedule.every().day.at("08:00").do(send_message, MORNING_MESSAGES)

while True:
    schedule.run_pending()
    time.sleep(1)