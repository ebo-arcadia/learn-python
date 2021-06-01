# refactor
command = ""
started = False
while True:
    command = input(">>").lower()
    if command == "start":
        if started:
            print("Car is already started! ")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
        start ->
        stop ->
        quit ->
        """)
    elif command == "quit":
        break
    else: 
        print("please provide a valid input")
        
# brute force solution
user_input = input("type help for options: ")

while user_input.lower() == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
    user_input = input("type command: ")
    if user_input == "start":
        print("The car is ready to go!")
        break
    elif user_input == "stop":
        print("The car has stopped")
        break
    else:
        print("exit...")
        break
else:
    print("please enter a valid input")
        

    