"""
Note : Cant use Speak(audio) in this package
    Return the string we want to say aloud to demoApp.py then use speak(audio) by importing method.
    Speed Test Intallation = pip install speedtest-cli
        from speedtest import *
        stObj = SpeedTest()
        print(st.download(), st.upload())
    1. Add more songs in Static File and select random songs using random module
    2. use try except block
    3. implement Amazon, Youtube, Search Query
"""

import datetime
from bs4.builder import HTML
from pyttsx3 import *
import speech_recognition as sr
import wikipedia
from bs4 import *
import webbrowser
import wolframalpha
import random
import requests
import json
import os

appId = "ad2706636ddfcf6579b8e07d682d9e68"
clientObj = wolframalpha.Client("QAY9L8-W7G3WGJ875")  # Wolframe API Key
e1 = Engine("sapi5")
e1.setProperty("voice", e1.getProperty("voices")[0].id)


def speak(audio):
    e1.say(audio)
    e1.runAndWait()


def greet(name):
    getTime = datetime.datetime.now().hour
    if getTime >= 0 and getTime < 12:
        return f"Good Morning {name}"

    elif getTime >= 12 and getTime < 18:
        return f"Good Afternoon {name}"

    else:
        return f"Good Evening {name}"


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # default is 0.8
        r.energy_threshold = 200  # default is 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception:   #in any case of On Internet
        # print(e)
        print("Say that again please...")
        return "None"

    return query


def working(query):     #user input will be compare by each task

    if "what is the best time to plant tomatoes" in query:  # Test Status : Working
        return f"The best time to plant tomatoes is in the late spring when the soil has warmed up and all danger of frost has passed"

    elif "How Often Should I Water My Crops" in query:
         return f"The frequency of watering crops depends on a number of factors such as soil type, weather conditions, and the type of crop. Generally, its best to water deeply and infrequently rather than shallowly and frequently"

    elif "how do I control pests and diseases in my crops" in query:
         return f"There are a number of ways to control pests and diseases in crops, including using organic and chemical pesticides, crop rotation, and planting disease-resistant varieties"
    elif "what is the best way to store harvested crops" in query:
        return f"The best way to store harvested crops depends on the type of crop. Generally, crops should be stored in a cool, dry, and dark place. Some crops, such as apples and potatoes, can be stored in a root cellar or cool basement"
    elif "how often should I water my crops" in query:
        return f"The best way to store harvested crops depends on the type of crop. Generally, crops should be stored in a cool, dry, and dark place. Some crops, such as apples and potatoes, can be stored in a root cellar or cool basement"
    elif "How Can I Improve The Quality Of My Soil" in query:
        return f"There are several ways to improve soil quality, including adding organic matter such as compost and manure, rotating crops, and avoiding excessive tillage"
    elif "best crops to grow in this region" in query:
        return f"The best crops to grow in a region depend on factors such as climate, soil type, and rainfall. Some common crops that may thrive in certain regions include corn, wheat, soybeans, cotton, and tobacco. Its always best to consult with local agricultural experts to determine the most suitable crops for your specific area."
    elif "protecting crops from pests and diseases" in query:
        return f"There are several ways to protect crops from pests and diseases, including crop rotation, using pest-resistant crop varieties, applying pesticides or natural insecticides, and practicing good hygiene and sanitation. Its important to identify any pests or diseases early and take action to prevent their spread"
    elif "soil preparation for planting" in query:
        return f"Proper soil preparation is essential for successful crop growth. This includes testing the soil to determine its nutrient content and pH level, adding organic matter such as compost or manure, and tilling the soil to ensure its loose and aerated. Its important to follow soil preparation guidelines specific to the crops youre planting"
    elif "how often should I water my crops" in query:
        return f"Proper soil preparation is essential for successful crop growth. This includes testing the soil to determine its nutrient content and pH level, adding organic matter such as compost or manure, and tilling the soil to ensure its loose and aerated. Its important to follow soil preparation guidelines specific to the crops youre planting"
    elif "best fertilizers for crops" in query:
        return f"The best fertilizers for crops depend on the specific needs of the crops and soil. Organic fertilizers such as manure, compost, and bone meal can provide natural nutrients to the soil, while synthetic fertilizers can deliver specific nutrient ratios. Its important to follow the instructions on the fertilizer package and not overuse them, as this can damage crops and the environment"
    elif "planting and harvesting times" in query:
        return f"Planting and harvesting times can vary depending on the crop and region. Factors such as soil temperature, moisture, and daylight hours can affect when crops are planted and harvested. Its best to consult with local agricultural experts and follow planting and harvesting guidelines specific to the crops youre growing"
    elif "choosing the best livestock for a farm" in query:
        return f"The best livestock for a farm depend on factors such as the size of the farm, available resources, and market demand. Some common livestock options include cattle, sheep, pigs, goats, and poultry. Its important to research the specific requirements and potential challenges of each type of livestock before making a decision."
    elif "grazing and pasture management" in query:
        return f"Grazing and pasture management are important for maintaining healthy livestock and maximizing productivity. This includes managing grazing patterns, providing sufficient water and shade, and monitoring forage quality. Its important to follow recommended grazing and pasture management practices to prevent overgrazing and erosion."
    elif "irrigation systems" in query:
        return f"Irrigation systems can be used to provide crops with the water they need to grow. There are several types of irrigation systems available, including surface, sprinkler, and drip irrigation. The choice of system depends on factors such as crop type, soil type, and available water supply. Its important to properly design, install, and maintain irrigation systems for maximum efficiency and crop yield."
    elif "farm equipment maintenance" in query:
        return f"Proper maintenance of farm equipment is essential for ensuring it operates efficiently and safely. This includes regular inspections, cleaning, and lubrication, as well as timely repairs and replacement of worn parts. Its important to follow manufacturer guidelines and schedule maintenance to minimize downtime and prolong the life of equipment."
    elif "best practices for irrigation" in query:
        return f"Proper irrigation is critical for healthy crop growth. Best practices include monitoring soil moisture levels, using efficient irrigation systems such as drip or sprinkler systems, and irrigating at the right time of day to minimize evaporation. Its also important to follow local water regulations and not overuse water resources."
    elif "managing weeds on the farm" in query:
        return f"Weeds can compete with crops for nutrients and water, and reduce crop yields. Effective weed management techniques include crop rotation, hand weeding, using herbicides, and maintaining healthy soil conditions. Its important to follow safe and legal herbicide usage guidelines."
    elif "managing livestock health" in query:
        return f"Livestock health is essential for optimal productivity and profitability. Best practices include providing proper nutrition and clean water, regular veterinary care and vaccinations, maintaining a clean and safe living environment, and monitoring for signs of illness or injury."
    elif "managing farm finances" in query:
        return f"Managing farm finances is crucial for the success and sustainability of a farm operation. Best practices include creating a budget and tracking expenses, maximizing profits through crop diversification and marketing strategies, and staying up to date on local and national agricultural policies and programs"
    elif "what is the best time to plant cotton" in query:
        return f"The best time to plant cotton is typically in the spring, after the danger of frost has passed and the soil has warmed up."
    elif "what is the best time to plant potatoes" in query:
        return f"general, potatoes are typically planted in early spring, after the last frost date in your area. This allows the soil to warm up to a suitable temperature for planting. However, if you live in a warm climate, you may be able to plant potatoes in the fall for a winter harvest. It's best to consult with a local agricultural extension office or experienced farmers in your area to determine the best planting time for potatoes in your specific location."
    elif "how can I prepare my crops for extreme weather conditions" in query:
        return f"Depending on the type of weather, you can take measures such as installing irrigation systems for drought conditions, using windbreaks to protect against strong winds, and harvesting crops early or covering them to protect against frost."
    elif "what regulations do I need to follow as a farmer" in query:
        return f"Regulations for farmers vary by location, but may include permits for water use, pesticide use, and animal welfare. Check with your local government or agricultural extension office for specific regulations in your area."
    elif "what is the best time to plant wheat" in query:
        return f"Winter wheat is typically planted in the fall, from late September to early November, while spring wheat is planted in the spring, typically from March to April. The exact planting time may vary depending on the specific variety of wheat and the location. It's best to consult with a local agricultural extension office or experienced farmers in your area for guidance on the best planting time for wheat in your location"
    elif "how can I prepare my crops for extreme weather conditions" in query:
        return f"Depending on the type of weather, you can take measures such as installing irrigation systems for drought conditions, using windbreaks to protect against strong winds, and harvesting crops early or covering them to protect against frost."


    # elif "date" in query:
    #     Year = datetime.datetime.now().date().year
    #     Month = datetime.datetime.now().date().month
    #     Date = datetime.datetime.now().date().day
    #     # speak(f"Sir Today's Date is {Date} {Month} {Year}")
    #     return f"Sir Today's Date is {Date} {Month} {Year}"

    elif "how are you" in query:
        # speak("I am Fine, How are you Sir ")
        return "I am Fine, How are you Sir "

    elif "wikipedia" in query:  # Test Status : Working
        try:
            # speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "", 5)
            # lis = BeautifulSoup(HTML, features="html.parser").find_all("li")
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'
    elif "what is" in query:  # Test Status : Working
        try:
            query = query.replace("what is", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "when" in query:  # Test Status : Working
        try:
            query = query.replace("when", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "how to" in query:  # Test Status : Working
        try:
            query = query.replace("how to", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "list" in query:  # Test Status : Working
        try:
            query = query.replace("list", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "give example" in query:  # Test Status : Working
        try:
            query = query.replace("give example", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "describe" in query:  # Test Status : Working
        try:
            query = query.replace("describe", "", 5)
            results = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia. {results}"

        except wikipedia.wikipedia.WikipediaException as e:
            return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    # elif "youtube" in query:       #test =
    #     if "open youtube"in query:
    #         webbrowser.open("www.youtube.in")
    #         return f"Opening youtube please Hold a second"
    #     else:
    #         newQuery = query.replace("youtube", "")
    #         youtubeLink = "https://www.youtube.com/results?search_query="
    #         newUrl = youtubeLink+newQuery.replace(" ", "+").rstrip("+")
    #         webbrowser.open(newUrl)
    #         return f"Opening youtube with search query as {newQuery}"

    # elif "open stack overflow" in query:
    #     webbrowser.open("www.stackoverflow.com")
    #     return f"Opening stack overflow please Hold a second"
    #
    # elif "amazon" in query:     #test = working
    #     if "open amazon"in query:
    #         webbrowser.open("www.amazon.in")
    #         return f"Opening amazon please Hold a second"
    #     else:
    #         newQuery = query.replace("amazon", "")
    #         amazonLink = "https://www.amazon.in/s?k="
    #         newUrl = amazonLink+newQuery.replace(" ", "+").rstrip("+")
    #         webbrowser.open(newUrl)
    #         return f"Opening Amazon with search query as {newQuery}"
    #
    # elif "open spotify" in query:
    #     webbrowser.open("https://www.spotify.com/in-en/")
    #     return f"Opening Spotify please Hold a second"
    #
    # elif (query.split("for ")[0]) == "search " in query:  # query = Search for <keyword / s>
    #     keyWord = query.split("for ")[1]
    #     webbrowser.open("https://www.google.com/search?q=" + keyWord)
    #     return f"This what I found for {keyWord}"
    #
    # elif "play music" in query:
    #     music_dir = "C:\\Users\\pc\\Desktop\\pythonPrathmesh\\Flask-Practical\\static\\Songs"
    #     songs = os.listdir(music_dir)
    #     i = random.randint(0,7)
    #     os.startfile(os.path.join(music_dir, songs[i]))
    #     return f"Playing {songs[i]} Song"

    elif "weather" in query:  # test Status : Null
        baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
        try:
            city = query.replace("weather", "")  # Nandurbar
            res = requests.get(baseUrl+"appid="+appId+"&q="+city)
            data = res.json()
            Celius = data["main"]["temp"] - 273.15
            windSpeed = data["wind"]["speed"]

            # rest = "weather of " + query
            # res = clientObj.query(rest)
            return f"Sir, The Current Temperature is {round(Celius, 2)}°C and Wind Speed is {windSpeed} miles per second"
        except Exception:
            return "Sorry, No Such City"
    #
    # elif "recall the remember task" in query:
    #     readFile = open(
    #         file=r"C:\Users\pc\Desktop\pythonPrathmesh\Flask-Practical\static\memory.txt",
    #         mode="r+",
    #     )
    #     reading = readFile.read()
    #
    #     # check if file has content to read or not
    #     if readFile.tell() == 0:
    #         print("No task To Remember")
    #         return "No task to remember"
    #
    #     else:
    #         readFile.truncate(0)
    #         readFile.close()
    #         return "You said me to remember that" + reading
    #
    # elif "remember" in query:  # That I have my meeting regarding FInal Project on 29th May
    #     save = query.replace("remember", "", 1)
    #     openFile = open(
    #         file=r"C:\Users\pc\Desktop\pythonPrathmesh\Flask-Practical\static\memory.txt",
    #         mode="a",
    #     )
    #     openFile.write(save + "\n")  # to save new text on new line
    #     openFile.close()
    #     return "Ok Sir, I will remember this"

    # elif "calculate" in query:
    #     res = clientObj.query(query)
    #     return f"Your answer is {next(res.results).get('subpod').get('plaintext')}"
    #
    # elif "capstone" in query:
    #     return "Opening Capstne Project as Voice Assistant"

    else:
        return "Sorry I didn't get that \n I'm Still Learning New Stuff"