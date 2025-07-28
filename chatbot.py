import datetime

print("🤖 Hello! I'm your chatbot.")
name = input("Bot: What's your name? ")
print(f"Bot: Nice to meet you, {name}!")

while True:
    user = input(f"{name}: ").lower()

    if "hello" in user:
        print("Bot: Hi there!")
    elif "how are you" in user:
        print("Bot: I'm good, but I'm doing great! 😄")
    elif "time" in user:
        now = datetime.datetime.now()
        print(f"Bot: Current time is {now.strftime('%I:%M %p')}")
    elif "date" in user:
        today = datetime.date.today()
        print(f"Bot: Today's date is {today.strftime('%B %d, %Y')}")
    elif "thank" in user:
        print("Bot: You're always welcome! 😊")
    elif "bye" in user:
        print("Bot: Goodbye! Have a great day!")
        break
    elif "+" in user or "-" in user or "*" in user or "/" in user:
        try:
            result = eval(user)
            print(f"Bot: The answer is {result}")
        except:
            print("Bot: Sorry, I can't calculate that.")
    else:
        print("Bot: Sorry, I didn't understand that.")