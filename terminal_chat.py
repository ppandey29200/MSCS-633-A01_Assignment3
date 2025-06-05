from chatbot import chatbot

def chat():
    print("Welcome to TerminalBot! Type 'exit' to quit.\n")
    while True:
        try:
            user_input = input("user: ")
            if user_input.lower() == 'exit':
                print("bot: Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print(f"bot: {response}\n")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("\nbot: Goodbye!")
            break

if __name__ == "__main__":
    chat()
