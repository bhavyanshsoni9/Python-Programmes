import os
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def ProcessCommand(c):
    if 'flappy bird' in c.lower():
            os.system('python Games/flappy_bird.py')
    elif 'ludo' in c.lower():
        os.system("python Games/Ludo.py")
    elif 'snake and ladders' in c.lower():
        os.system("python Games/snake_and_ladders.py")
    elif 'rock paper scissors' in c.lower():
        os.system("python Games/rps.py")
    elif 'word guessing game' in c.lower():
        os.system("python Games/word_guess.py")
    elif 'letter guessing game' in c.lower():
        os.system("python Games/letter_guess.py")
    elif 'number guessing game' in c.lower():
        os.system("python Games/number_guess.py")
    elif 'quit' in c.lower():
        

        print("👋 Goodbye! Thanks for playing.")
        
    else:
        print("❌ Invalid choice. Please select a number from the menu.")

if __name__ == '__main__':
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == 'jarvis':
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)
            else:
                print("Please call me with my name 'Jarvis'")
        except Exception as e:
            print("Error: {0}".format(e))
        

    
