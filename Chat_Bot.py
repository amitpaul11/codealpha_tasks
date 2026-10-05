# Simple Rule-Based Chatbot

def chatbot(user_input):

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("===== SIMPLE CHATBOT =====")
print("Type 'bye' to exit the chatbot.")

while True:

    user_input = input("You: ")

    reply = chatbot(user_input)

    print("Bot:", reply)

    if user_input.lower() == "bye":
        break