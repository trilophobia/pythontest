import time
import random
import sys

class PotatoAI:
    def __init__(self):
        self.knowledge = ["🥔", "I am PotatoGPT", "Predicting nonsense...", "Thinking in starch..."]
    
    def predict_future(self):
        time.sleep(1)
        return random.choice([
            "You will forget why you ran this.",
            "Your computer is judging you.",
            "A potato is more productive than this code.",
            "42 is still the answer.",
            "Stop wasting electricity."
        ])
    
    def display_ascii_potato(self):
        print(r"""
               ___
             /     \
            | () () |
             \  ^  /
              |||||
              |||||
        """)

def loading_bar(text="Processing", duration=3):
    print(f"{text}:", end=" ", flush=True)
    for _ in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" Done.")

def insult_user():
    insults = [
        "You're clearly the genius who ran this.",
        "Nice job wasting a container.",
        "This is peak developer productivity.",
        "Your ancestors are proud (not really)."
    ]
    name = input("What should I call you? ")
    print(f"Hello, {name}. {random.choice(insults)}")

def main():
    insult_user()
    loading_bar("Booting fake AI", 4)

    ai = PotatoAI()
    ai.display_ascii_potato()

    loading_bar("Consulting the potato wisdom", 3)
    print("💡 AI Prediction:", ai.predict_future())

    loading_bar("Now pretending to clean memory", 2)
    print("🧹 Memory cleaned. Nothing was actually done.")

    print("\nGoodbye. The potato believes in you (but shouldn't).")

if __name__ == "__main__":
    main()
