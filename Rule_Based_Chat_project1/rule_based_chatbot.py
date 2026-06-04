"""
Rule-Based Chatbot v1.2

The goal : to create a rule-based chatbot that can respond to user inputs based on predefined user input. 
Key Requairements:
1. Handling Greeting and exit command
2. use if-else logic for responses
3. Use a loop to continuously interact with the user until they choose to exit

project specification:
- Input loop : Continuous 'While' cycle
- Sanitization : Handling case & whitespace
- Knowledge base : Predefined responses for specific inputs (Dictionary with 5+ intents)
- Fallback: Default response for unrecognized inputs
- Exit Strategy: Recognize 'exit' command to terminate the conversation (break)

Version 1.2 introduces intent-based matching.

Instead of relying on exact user input,
the chatbot groups related phrases into intents
(e.g., greetings, jokes, help requests) and
matches user messages against predefined patterns.
"""
# Intent-based Knowledge base
responses = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "response": "Hi there! How can I help you today?"
    },

    "how_are_you": {
        "patterns": ["how are you", "how are u", "how r you"],
        "response": "I'm just a chatbot, but I'm doing great! How about you?"
    },

    "name": {
        "patterns": ["what's your name", "your name", "who are you"],
        "response": "I'm a Rule-Based Chatbot. You can call me Chatbot!"
    },

    "abilities": {
        "patterns": ["what can you do", "help", "abilities"],
        "response": "I can respond to simple questions and have a basic conversation with you!"
    },

    "joke": {
    "patterns": ["tell me a joke","make me laugh","say a joke","joke"],
    "response": "Why don't programmers like nature? Because it has too many bugs!"
    },

    "exit": {
        "patterns": ["exit", "bye", "quit"],
        "response": "Goodbye!"
    },

    "thanks": {
    "patterns": ["thanks", "thank you"],
    "response": "You're welcome!"
    },

    "help": {
    "patterns": ["help", "what can you help with"],
    "response": "I can answer greetings, tell jokes, and introduce myself."
    }
    
}


print("Hello! I'm a Rule-Based Chatbot. How can I assist you today? (Type 'exit' to end the conversation) ")
while True:
    user_message = input("You: ")
    user_input = user_message.strip().lower()

    matched = False

    # Loop through intents
    for intent, data in responses.items():
        # Get patterns list
        patterns = data["patterns"]

        # check if any pattern exists in user input
        if any(pattern in user_input for pattern in patterns):
            print("Chatbot:", responses[intent]["response"])
            matched = True

            if intent == "exit":
                break

            # stop checking other intents
            break
    # exit while loop
    if matched and intent == "exit":
        break

    #fallback
    if not matched:
        print("Chatbot: Sorry, I don't understand that. Can you please rephrase?")



