from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'TerminalBot',
    read_only=True,  # Prevents the bot from learning after training
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus data
trainer.train("chatterbot.corpus.english")
