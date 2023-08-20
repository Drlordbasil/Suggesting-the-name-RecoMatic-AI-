Here is a simple AI chatbot that helps you run the provided program locally on your PC:

```python
import subprocess

# Define the chatbot class
class Chatbot:
    def __init__(self):
        self.user_input = ""
    
    def chat(self):
        # Display welcome message
        print("Welcome to the AI chatbot! How can I assist you today?")
        
        while True:
            # Get user input
            self.user_input = input("User: ")
            
            # Check if user wants to run the program
            if "run program" in self.user_input.lower():
                self.run_program()
            elif "exit" in self.user_input.lower():
                break
            else:
                print("Chatbot: Sorry, I didn't understand. Can you please rephrase?")
    
    def run_program(self):
        try:
            # Run the program using subprocess
            subprocess.run(['python', 'main.py'], check=True)
        except subprocess.CalledProcessError:
            print("Chatbot: An error occurred while running the program.")
        else:
            print("Chatbot: Program executed successfully.")

# Create an instance of the chatbot
chatbot = Chatbot()

# Start the chatbot
chatbot.chat()
```

To use the chatbot, simply run the script and interact with it. When you want to run the program, type "run program" and the chatbot will execute the `main.py` script.