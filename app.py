import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by somdev")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            print("goodbye")
            break
        engine.say(x)
        engine.runAndWait()
