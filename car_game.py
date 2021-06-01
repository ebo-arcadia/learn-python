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
        