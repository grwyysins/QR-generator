def respond(message):
    message = message.lower().strip()
    if message in ("hi", "hello", "hey", "yowww"): return "Hello! How can I help?"
    if message in ("name", "what",): return "I'm Botty, a simple chatbot depending on what you ask me to do  :)."
    if "python" in message: return "Python is a programming language."
    if "help" in message: return "You can ask me about my name or Python."
    if "bye" in message: return "Goodbye!"
    return "I'm still learning. Try asking about Python or my name."

def main():
    print("PyBot: Hello! Type 'bye' to leave.")
    while True:
        message = input("You: ")
        answer = respond(message)
        print("PyBot:", answer)
        if message.lower().strip() == "bye": break

if __name__ == "__main__":
    main()
