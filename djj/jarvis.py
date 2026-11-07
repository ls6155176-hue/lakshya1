import speech_recognition as sr
import pyttsx3
import pywhatkit

# Jarvis ki awaaz set karna
engine = pyttsx3.init()
engine.say("Namaste Main Aapka Personal Assistant Hoon")
engine.runAndWait()

# Awaaz sunne ka function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bol rahe hain... sun raha hoon...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Samajh raha hoon...")
        command = r.recognize_google(audio, language="hi-IN") # Hindi aur English dono samjhega
        print(f"Aapne kaha: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Samajh nahi aaya, phir se boliye.")
        return ""
    except sr.RequestError:
        print("Internet connection problem hai.")
        return ""

# Jarvis ka loop (Kaam karna)
def run_jarvis():
    while True:
        command = listen()
        
        if "notepad" in command:
            engine.say("Notepad khol raha hoon")
            engine.runAndWait()
            import os
            os.system("notepad") # Notepad kholna
            
        elif "youtube" in command and "song" in command:
            engine.say("YouTube par gaana chal raha hai")
            engine.runAndWait()
            pywhatkit.playonyt(command) # YouTube par search karke play karna
            
        elif "exit" in command or "bye" in command:
            engine.say("Allah Hafiz, milte hain")
            engine.runAndWait()
            break
            
        else:
            print("Main yeh command abhi nahi seekha.")

# Jarvis ko start karo
run_jarvis()