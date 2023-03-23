import random

def handle_response(message) -> str:
    process_message = message.lower()
    
    if process_message == "hello":
        return "Greetings!"
    
    if process_message == "roll":
        return str(random.randint(1,6))
    
    if process_message == "!help":
        return "What do you need help with?"
