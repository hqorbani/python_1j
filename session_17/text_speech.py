# to install pyttsx3: python -m pip install pyttsx3
# https://pypi.org/project/pyttsx3/
# https://pyttsx3.readthedocs.io/en/latest/
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()