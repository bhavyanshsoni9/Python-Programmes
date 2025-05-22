import pyttsx3
import speech_recognition as sr
import re

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("🎤", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"👂 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def calculate(command):
    if "add" in command or "+" in command:
        numbers = list(map(int, re.findall(r'\d+', command)))
        if len(numbers) >= 2:
            result = sum(numbers)
            speak(f"The sum is {result}")
    elif "subtract" in command or "-" in command:
        numbers = list(map(int, re.findall(r'\d+', command)))
        if len(numbers) >= 2:
            result = abs(numbers[0] - numbers[1])
            speak(f"The subtraction result is {result}")
    elif "multiply" in command or "x" in command or "*" in command:
        numbers = list(map(int, re.findall(r'\d+', command)))
        if len(numbers) >= 2:
            result = numbers[0] * numbers[1]
            speak(f"The multiplication result is {result}")
    elif "divide" in command or "/" in command:
        numbers = list(map(int, re.findall(r'\d+', command)))
        if len(numbers) >= 2 and numbers[1] != 0:
            result = numbers[0] / numbers[1]
            speak(f"The division result is {result}")
        else:
            speak("Cannot divide by zero!")
    else:
        speak("Sorry, I can't understand the operation.")

def main():
    speak("Hello! I am your smart voice calculator.")
    while True:
        command = listen()
        if command in ["exit", "quit", "stop", "bye"]:
            speak("Goodbye! 👋")
            break
        elif command:
            calculate(command)

main()
