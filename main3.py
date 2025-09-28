import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
from googletrans import Translator  # Importing Translator for language translation


# Function to process text or speech input and show corresponding ISL gif or images
def process_input(a, isl_gif, arr, translator):
    try:
        # Translate Hindi input to English if it's in Hindi
        if not a.isascii():
            translated_text = translator.translate(a, src='hi', dest='en').text.lower()
            print(f'Translated Text: {translated_text}')
            a = translated_text

        for c in string.punctuation:
            a = a.replace(c, "")

        if a in ['goodbye', 'good bye', 'bye']:
            print("Oops! Time to say goodbye")
            return False

        elif a in isl_gif:
            class ImageLabel(tk.Label):
                """a label that displays images, and plays them if they are gifs"""

                def load(self, im):
                    if isinstance(im, str):
                        im = Image.open(im)
                    self.loc = 0
                    self.frames = []

                    try:
                        for i in count(1):
                            self.frames.append(ImageTk.PhotoImage(im.copy()))
                            im.seek(i)
                    except EOFError:
                        pass

                    try:
                        self.delay = im.info['duration']
                    except:
                        self.delay = 100

                    if len(self.frames) == 1:
                        self.config(image=self.frames[0])
                    else:
                        self.next_frame()

                def unload(self):
                    self.config(image=None)
                    self.frames = None

                def next_frame(self):
                    if self.frames:
                        self.loc += 1
                        self.loc %= len(self.frames)
                        self.config(image=self.frames[self.loc])
                        self.after(self.delay, self.next_frame)

            root = tk.Tk()
            lbl = ImageLabel(root)
            lbl.pack()
            lbl.load(r'ISL_Gifs/{0}.gif'.format(a))
            root.mainloop()

        else:
            for i in range(len(a)):
                if a[i] in arr:
                    ImageAddress = 'letters/' + a[i] + '.jpg'
                    ImageItself = Image.open(ImageAddress)
                    ImageNumpyFormat = np.asarray(ImageItself)
                    plt.imshow(ImageNumpyFormat)
                    plt.draw()
                    plt.pause(0.8)
                else:
                    continue
        plt.close()
        return True

    except Exception as e:
        print("Error: ", str(e))
        return True


# Function to handle voice input
def func():
    r = sr.Recognizer()
    translator = Translator()  # Create a Translator object for translation
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office',
               'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry',
               'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch',
               'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk',
               'i am bore doing nothing',
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything',
               'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur',
               'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage',
               'please wait for sometime', 'shall I help you',
               'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care',
               'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do',
               'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview',
               'when we will go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad',
               'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut',
               'crocodile', 'dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes',
               'gujrat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala',
               'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass',
               'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop',
               'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town',
               'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number',
               'what are you doing', 'are you busy', 'happy', 'keep calm and stay home', 'dear mam thank you so much',
               'happy fathers day', 'how are you', 'wonderful', 'cool', 'export', 'i love you', 'merry christmas',
               'experiment', 'happy easter', 'echo', 'date']

    arr = list(string.ascii_lowercase)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("I am Listening")
            audio = r.listen(source)

            try:
                a = r.recognize_google(audio, language='hi-IN')  # Recognize Hindi and English input
                print('You Said: ' + a)

                if not process_input(a, isl_gif, arr, translator):
                    break

            except Exception as e:
                print("Error: ", str(e))
            plt.close()


# Function to handle text input
def handle_text_input():
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office',
               'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry',
               'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch',
               'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk',
               'i am bore doing nothing',
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything',
               'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur',
               'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage',
               'please wait for sometime', 'shall I help you',
               'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care',
               'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do',
               'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview',
               'when we will go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad',
               'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut',
               'crocodile', 'dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes',
               'gujrat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala',
               'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass',
               'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop',
               'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town',
               'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number',
               'what are you doing', 'are you busy', 'happy', 'keep calm and stay home', 'dear mam thank you so much',
               'happy fathers day', 'how are you', 'wonderful', 'cool', 'export', 'i love you', 'merry christmas',
               'experiment', 'happy easter', 'echo', 'date']
    arr = list(string.ascii_lowercase)
    translator = Translator()  # Create a Translator object for translation

    a = enterbox("Enter your text:")
    if a:
        process_input(a.lower(), isl_gif, arr, translator)


# Main loop with GUI for options
while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "Text Input", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == choices[0]:
        func()
    elif reply == choices[1]:
        handle_text_input()
    elif reply == choices[2]:
        quit()
