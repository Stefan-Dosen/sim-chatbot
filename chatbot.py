def chatbot(name,*topics,**responses):
    def chat():
        print(f"My name is {name}")
        nobye = True
        while nobye:
            msg = input("> ")
            if msg=="bye":
                print("Goodbye")
                nobye = False
            elif msg in responses:
                print(responses[msg])
            elif any(topic in msg for topic in topics):
                print(f"{msg}! Let's talk more about it.")
            else:
                print("Don't understand")
    return chat
                
bot = chatbot("botara",
              "dance","music",
              hi="sup",
              sup="nothing, how about you",
              shower="nahhh")
bot()