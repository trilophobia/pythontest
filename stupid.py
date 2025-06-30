import time
import random

def why_am_i_running():
    thoughts = [
        "Why are you still here?",
        "Is this... entertainment?",
        "I'm just a bunch of loops...",
        "The cake is a lie.",
        "This script does literally nothing.",
        "You're wasting CPU cycles. Congrats."
    ]
    print("Initializing pointless loop...")
    for i in range(5):
        print(f"Thinking{'.' * (i % 4)}")
        time.sleep(0.5)
    print(random.choice(thoughts))

def pointless_calculation():
    print("Calculating the meaning of life...")
    result = 0
    for i in range(1, 100000):
        result += i * 0  # genius
    print(f"Result: {result} (shocking, I know)")

def insult_the_user():
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}. You're using this script. Interesting life choices.")

if __name__ == "__main__":
    insult_the_user()
    why_am_i_running()
    pointless_calculation()
    print("Goodbye. I hope this was as pointless for you as it was for me.")
