# import speech_recognition as sr
# import datetime
# import time
# import os
# import sys
# import webbrowser
# import pyttsx3
# import requests
# import json

# from huggingface_hub import InferenceClient

# # Initialize the InferenceClient
# client = InferenceClient(api_key="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")

# # Initialize the speech recognizer
# r = sr.Recognizer()

# # Initialize a list for the to-do list
# todo_list = []

# # Initialize a variable to control the stop functionality
# stop_listening = False

# def voice_Recognizer():
#     recognize_words = ''
#     try:
#         with sr.Microphone() as source:
#             print("Please wait. Calibrating microphone...")
#             r.adjust_for_ambient_noise(source, duration=2)
#             print("Listening...")
#             audio = r.listen(source)
#         recognize_words = r.recognize_google(audio).lower().replace("'", "")
#         print("You said: '" + recognize_words + "'")
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand that. Please try again.")
#     except sr.WaitTimeoutError:
#         print("Listening timed out while waiting for phrase to start.")
#     except sr.RequestError:
#         print('Facing network error!')
#     return recognize_words

# def speak(message):
#     if sys.platform == 'darwin':
#         tts_engine = 'say'
#         return os.system(tts_engine + ' ' + message)
#     elif sys.platform == 'win32':
#         tts_engine = pyttsx3.init('sapi5')
#         voices = tts_engine.getProperty('voices')
#         tts_engine.setProperty('voice', voices[1].id)
#         tts_engine.say(message)
#         tts_engine.runAndWait()
#     elif sys.platform in ['linux', 'linux', 'ubuntu']:
#         tts_engine = 'espeak'
#         print("Assistant: " + message)
#         return os.system(tts_engine + ' "' + message + '"')

# def greeting():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")
#     speak("Hello, I'm Baymax. Nice to meet you, how can I help you?")

# def googleSearch(recognize_words):
#     cleanword = recognize_words.replace("ask google", "").strip()
#     webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))
#     speak("Opening your query in Google search engine.")

# def get_weather(location):
#     api_key = '4e2fbbdcef9845c0827161516240710'  # Replace with your WeatherAPI key
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    
#     response = requests.get(url).json()

#     # Check if there is an error in the response
#     if "error" in response:
#         result = "Sorry, I couldn't find the weather for that location."
#     else:
#         # Extract weather details from the WeatherAPI response
#         weather = response['current']['condition']['text']
#         temp = response['current']['temp_c']
#         result = f"The current weather in {location} is {weather} with a temperature of {temp}°C."
    
#     speak(result)
#     print(result)

# def tell_joke():
#     joke = "Why don't scientists trust atoms? Because they make up everything!"
#     speak(joke)
#     print(joke)

# def add_to_todo_list(item):
#     todo_list.append(item)
#     speak(f"I have added {item} to your to-do list.")
#     print(f"Added to To-Do List: {item}")

# def view_todo_list():
#     if not todo_list:
#         response = "Your to-do list is empty."
#         speak(response)
#         print(response)
#     else:
#         response = "Your to-do list contains: " + ", ".join(todo_list)
#         speak(response)
#         print(response)

# def get_news():
#     url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=49e391e7066c4158937096fb5e55fb5d'  # Replace with your NewsAPI key
#     response = requests.get(url).json()
#     articles = response['articles'][:5]
    
#     news_list = []
#     for article in articles:
#         news_list.append(article['title'])
        
#     result = "Here are the top news headlines: " + ", ".join(news_list)
#     speak(result)
#     print(result)

# def get_trivia():
#     url = "https://opentdb.com/api.php?amount=1&type=multiple"
#     response = requests.get(url).json()
    
#     if response['response_code'] == 0:
#         question = response['results'][0]['question']
#         correct_answer = response['results'][0]['correct_answer']
#         options = response['results'][0]['incorrect_answers']
#         options.append(correct_answer)
#         random.shuffle(options)
        
#         result = f"Trivia Question: {question} Options: {', '.join(options)}"
#     else:
#         result = "Sorry, I couldn't find any trivia questions."
    
#     speak(result)
#     print(result)

# def get_quote():
#     url = "https://api.quotable.io/random"
#     response = requests.get(url).json()
    
#     quote = response['content']
#     author = response['author']
#     result = f"Quote: '{quote}' - {author}"
    
#     speak(result)
#     print(result)

# def conversation_with_bot(user_input):
#     messages = [{"role": "user", "content": user_input}]
    
#     response = ""
#     for message in client.chat_completion(
#         model="microsoft/Phi-3.5-mini-instruct",
#         messages=messages,
#         max_tokens=500,
#         stream=True,
#     ):
#         response += message.choices[0].delta.content
    
#     speak(response)
#     return response

# def save_todo_list():
#     with open('todo_list.json', 'w') as file:
#         json.dump(todo_list, file)

# def load_todo_list():
#     global todo_list
#     if os.path.exists('todo_list.json'):
#         with open('todo_list.json', 'r') as file:
#             todo_list = json.load(file)

# if __name__ == "__main__":
#     load_todo_list()  # Load the todo list at the start
#     time.sleep(2)
#     greeting()
    
#     while True:
#         if stop_listening:
#             # Pausing until the user says "start" again
#             speak("Say 'start' when you're ready to resume.")
#             while True:
#                 command = voice_Recognizer()
#                 if "start" in command:
#                     speak("Resuming...")
#                     stop_listening = False
#                     break

#         recognize_words = voice_Recognizer()

#         if recognize_words:
#             if "who are you" in recognize_words:
#                 response = "I'm your Baymax, a simple virtual assistant."
#                 print(response)
#                 speak(response)
#             elif "goodbye" in recognize_words:
#                 save_todo_list()  # Save the todo list before exiting
#                 response = "See you later, bye!"
#                 print(response)
#                 speak(response)
#                 break
#             elif "ask google" in recognize_words:
#                 googleSearch(recognize_words)
#             elif "weather" in recognize_words:
#                 location = recognize_words.replace("what's the weather in", "").strip()
#                 get_weather(location)
#             elif "tell me a joke" in recognize_words:
#                 tell_joke()
#             elif "add to my to-do list" in recognize_words:
#                 item = recognize_words.replace("add to my to-do list", "").strip()
#                 add_to_todo_list(item)
#             elif "show my to-do list" in recognize_words:
#                 view_todo_list()
#             elif "news" in recognize_words:
#                 get_news()
#             elif "trivia" in recognize_words:
#                 get_trivia()
#             elif "quote" in recognize_words:
#                 get_quote()
#             elif "stop" in recognize_words:
#                 speak("Stopping. Say 'start' to resume.")
#                 stop_listening = True
#             else:
#                 bot_response = conversation_with_bot(recognize_words)
#                 print("Bot:", bot_response)









import os
import json
import datetime
import random
import requests
import webbrowser
import pyttsx3
import speech_recognition as sr
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from huggingface_hub import InferenceClient

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Initialize the InferenceClient with your Hugging Face API key
client = InferenceClient(api_key="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")

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize a list for the to-do list
todo_list = []

# Load existing to-do list from a JSON file
def load_todo_list():
    global todo_list
    if os.path.exists('todo_list.json'):
        with open('todo_list.json', 'r') as file:
            todo_list = json.load(file)

# Save the to-do list to a JSON file
def save_todo_list():
    with open('todo_list.json', 'w') as file:
        json.dump(todo_list, file)

# Function to convert text to speech
def speak(message):
    tts_engine = None
    if os.name == 'nt':  # Windows
        tts_engine = pyttsx3.init('sapi5')
        voices = tts_engine.getProperty('voices')
        tts_engine.setProperty('voice', voices[1].id)
    elif os.name == 'posix':  # macOS or Linux
        if sys.platform == 'darwin':
            tts_engine = 'say'
        else:  # Linux
            tts_engine = 'espeak'
            message = f'"{message}"'  # Quoting for espeak
    else:
        print("Platform not supported for TTS.")
        return

    if tts_engine:
        tts_engine.say(message)
        tts_engine.runAndWait() if os.name == 'nt' else os.system(f"{tts_engine} {message}")

# Greeting function
def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I'm Baymax. Nice to meet you, how can I help you?")

# Function to recognize speech
def voice_recognizer():
    recognize_words = ''
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=2)
            audio = r.listen(source)
            recognize_words = r.recognize_google(audio).lower().replace("'", "")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please try again.")
    except sr.WaitTimeoutError:
        speak("Listening timed out while waiting for phrase to start.")
    except sr.RequestError:
        speak('Facing network error!')
    return recognize_words

# Route for the home page
@app.route('/')
def home():
    load_todo_list()  # Load the todo list at the start
    greeting()  # Initial greeting
    return render_template('index.html')

# Handle user input from the client
@socketio.on('user_input')
def handle_user_input(data):
    user_input = data['message']
    print(f"User: {user_input}")

    if "goodbye" in user_input:
        save_todo_list()  # Save the todo list before exiting
        response = "See you later, bye!"
        socketio.emit('bot_response', {'message': response})
        return

    bot_response = process_user_input(user_input)
    socketio.emit('bot_response', {'message': bot_response})

def process_user_input(user_input):
    # Various commands the bot can handle
    if "who are you" in user_input:
        return "I'm your Baymax, a simple virtual assistant."
    elif "ask google" in user_input:
        google_search(user_input)
        return "Opening your query in Google search engine."
    elif "weather" in user_input:
        location = user_input.replace("what's the weather in", "").strip()
        return get_weather(location)
    elif "tell me a joke" in user_input:
        return tell_joke()
    elif "add to my to-do list" in user_input:
        item = user_input.replace("add to my to-do list", "").strip()
        add_to_todo_list(item)
        return f"I have added {item} to your to-do list."
    elif "show my to-do list" in user_input:
        return view_todo_list()
    elif "news" in user_input:
        return get_news()
    elif "trivia" in user_input:
        return get_trivia()
    elif "quote" in user_input:
        return get_quote()
    elif "stop" in user_input:
        speak("Stopping. Say 'start' to resume.")
        return "Assistant stopped. Say 'start' to resume."
    elif "next" in user_input:  # New feature to move to the next response
        return "Moving to the next response."
    else:
        return conversation_with_bot(user_input)

# Google Search Function
def google_search(user_input):
    cleanword = user_input.replace("ask google", "").strip()
    webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))

# Get Weather Function
def get_weather(location):
    api_key = '4e2fbbdcef9845c0827161516240710'  # Replace with your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    
    response = requests.get(url).json()
    if "error" in response:
        result = "Sorry, I couldn't find the weather for that location."
    else:
        weather = response['current']['condition']['text']
        temp = response['current']['temp_c']
        result = f"The current weather in {location} is {weather} with a temperature of {temp}°C."
    
    speak(result)
    print(result)
    return result

# Tell a Joke Function
def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    speak(joke)
    print(joke)
    return joke

# Add Item to To-Do List
def add_to_todo_list(item):
    todo_list.append(item)
    speak(f"I have added {item} to your to-do list.")
    print(f"Added to To-Do List: {item}")

# View To-Do List
def view_todo_list():
    if not todo_list:
        response = "Your to-do list is empty."
        speak(response)
        print(response)
    else:
        response = "Your to-do list contains: " + ", ".join(todo_list)
        speak(response)
        print(response)
    return response

# Get News Function
def get_news():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=49e391e7066c4158937096fb5e55fb5d'  # Replace with your NewsAPI key
    response = requests.get(url).json()
    articles = response['articles'][:5]
    
    news_list = [article['title'] for article in articles]
    result = "Here are the top news headlines: " + ", ".join(news_list)
    speak(result)
    print(result)
    return result

# Get Trivia Function
def get_trivia():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url).json()
    
    if response['response_code'] == 0:
        question = response['results'][0]['question']
        correct_answer = response['results'][0]['correct_answer']
        options = response['results'][0]['incorrect_answers'] + [correct_answer]
        random.shuffle(options)
        
        result = f"Trivia Question: {question} Options: {', '.join(options)}"
    else:
        result = "Sorry, I couldn't find any trivia questions."
    
    speak(result)
    print(result)
    return result

# Get Quote Function
def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url).json()
    
    quote = response['content']
    author = response['author']
    result = f"Quote: '{quote}' - {author}"
    
    speak(result)
    print(result)
    return result

# Conversation with Bot
def conversation_with_bot(user_input):
    messages = [{"role": "user", "content": user_input}]
    
    response = ""
    for message in client.chat_completion(
        model="microsoft/Phi-3.5-mini-instruct",
        messages=messages,
        max_tokens=500,
        stream=True,
    ):
        response += message.choices[0].delta.content
    
    speak(response)
    return response

# Start the Flask app
if __name__ == "__main__":
    load_todo_list()  # Load the todo list at the start
    socketio.run(app, debug=True)
