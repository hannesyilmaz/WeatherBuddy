import speech_recognition as sr
import pyttsx3
import requests
from pprint import pprint
import nltk
import random
from time import gmtime, strftime
import datetime
import time
from datetime import timedelta
from datetime import datetime
from requests import get


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ask me about the weather!")
    audio = r.listen(source)
def speech_recog():
    speech_r = []
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        speech_r.append(r.recognize_google(audio))
        return speech_r
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def convertTuple():
    string_r = ' '.join(speech_recog())
    return string_r

print(convertTuple())


#def input_sentence():
    #return [input('ask me about the weather: ')]


def input_word_seg():
    seg_words = nltk.word_tokenize(convertTuple())
    return seg_words

def input_pos_tag():
    input_pos = nltk.pos_tag(input_word_seg())
    return input_pos

use_input = input_pos_tag()
first_indices = [item[0].capitalize() for item in use_input]
first_indices_to = ['Night' if item == 'Tonight' else item for item in first_indices]
second_indices = [item[1] for item in use_input]
print(use_input)
#print(use_input)
#print(first_indices_to)





date_today = datetime.now()
today_fixed = str(date_today.replace(minute=0, second=0, microsecond=0))
tomorrow = date_today + timedelta(days=1)
tomorrow_fixed = str(tomorrow.replace(minute=0, second=0, microsecond=0))
third_day = date_today + timedelta(days=2)
third_day_fixed = str(third_day.replace(minute=0, second=0, microsecond=0))
fourth_day = date_today + timedelta(days=3)
fourth_day_fixed = str(fourth_day.replace(minute=0, second=0, microsecond=0))
fifth_day = date_today + timedelta(days=4)
fifth_day_fixed = str(fifth_day.replace(minute=0, second=0, microsecond=0))

week_day_0000 = date_today.today().strftime("%Y-%m-%d %H:%M:%S In")
week_day_000 = date_today.today().strftime("%Y-%m-%d %H:%M:%S This")
week_day_00 = date_today.today().strftime("%Y-%m-%d %H:%M:%S Today")
week_day_0 = tomorrow.strftime("%Y-%m-%d %H:%M:%S Tomorrow")
week_day_1 = date_today.today().strftime("%Y-%m-%d %H:%M:%S %A")
week_day_2 = tomorrow.strftime("%Y-%m-%d %H:%M:%S %A")
week_day_3 = third_day.strftime("%Y-%m-%d %H:%M:%S %A")
week_day_4 = fourth_day.strftime("%Y-%m-%d %H:%M:%S %A")
week_day_5 = fifth_day.strftime("%Y-%m-%d %H:%M:%S %A")

week_day_numbers = [week_day_0000, week_day_000, week_day_00, week_day_0, week_day_1, week_day_2, week_day_3, week_day_4, week_day_5]

week_day_dictionary = {week_day_0000: today_fixed, week_day_000: today_fixed, week_day_00: today_fixed, week_day_0: tomorrow_fixed, week_day_1: today_fixed, week_day_2: tomorrow_fixed, week_day_3: third_day_fixed, week_day_4: fourth_day_fixed, week_day_5: fifth_day_fixed}

week_days = ['In', 'This', 'Today', 'Tomorrow', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def define_week_day():
    for element in first_indices_to:
        if element in week_days:
            return [item for item in week_day_numbers if element in item]

#print(define_week_day())

def return_week_day():
    for key, value in week_day_dictionary.items():
        if define_week_day() == [key]:
            return value

print(return_week_day())


the_clock = return_week_day()[11:19]
the_clock_replace = the_clock.replace(':', '')
the_clock_integer = int(the_clock_replace)

#print(the_clock_integer)


morning_hours = the_clock_integer >= 0 and the_clock_integer < 90000
noon_hours = the_clock_integer >= 90000 and the_clock_integer < 120000
afternoon_hours = the_clock_integer >= 120000 and the_clock_integer < 180000
evening_hours = the_clock_integer >= 180000 and the_clock_integer < 210000
night_hours = the_clock_integer >= 210000 and the_clock_integer < 235959
day_hours = the_clock_integer >= 0 and the_clock_integer < 235959
today_hours = the_clock_integer >= 0 and the_clock_integer < 235959
tomorrow_hours = the_clock_integer >= 0 and the_clock_integer < 235959

print(afternoon_hours)

hourly_dates = {'Morning': morning_hours, 'Noon': noon_hours, 'Afternoon': afternoon_hours, 'Evening': evening_hours, 'Night': night_hours, 'Today': today_hours, 'Tomorrow': tomorrow_hours, 'Monday': day_hours, 'Tuesday': day_hours, 'Wednesday': day_hours, 'Thursday': day_hours, 'Friday': day_hours, 'Saturday': day_hours, 'Sunday': day_hours}


print(hourly_dates['Afternoon'])


def theDateandHours():
    thedateandhours =[]
    thedateandhours.append(return_week_day()[0:10])
    for key, value in hourly_dates.items():
        if key in first_indices_to:
            if value == True:
                return_week_day_replace = return_week_day()[11:19].replace(':', '')
                return_week_day_integer = int(return_week_day_replace)
                if return_week_day_integer >= 0 and return_week_day_integer < 90000:
                    thedateandhours.append('09:00:00')
                if return_week_day_integer >= 90000 and return_week_day_integer < 120000:
                    thedateandhours.append('12:00:00')
                if return_week_day_integer >= 120000 and return_week_day_integer < 180000:
                    thedateandhours.append('15:00:00')
                if return_week_day_integer >= 180000 and return_week_day_integer < 210000:
                    thedateandhours.append('18:00:00')
                if return_week_day_integer >= 210000 and return_week_day_integer < 235959:
                    thedateandhours.append('21:00:00')
            else:
                if key == 'Morning':
                    thedateandhours.append('09:00:00')
                elif key == 'Noon':
                    thedateandhours.append('12:00:00')
                elif key == 'Afternoon':
                    thedateandhours.append('15:00:00')
                elif key == 'Evening':
                    thedateandhours.append('18:00:00')
                elif key == 'Night':
                    thedateandhours.append('21:00:00')
            return ' '.join(thedateandhours)

print(theDateandHours())

def define_day_time():
    for key in hourly_dates:
        if key in first_indices_to:
            return key
        else:
            pass

#print(define_day_time())

def name_of_city():
    ip_ad = get('https://api.ipify.org').text

    def current_location():
        ip = ip_ad

        url = 'http://ip-api.com/json/' + ip

        req = requests.get(url)

        js = req.json()

        city_name = js['regionName']

        return city_name

    return current_location()

name_city = name_of_city()


def input_city():
    city_is = []
    for item in use_input:
        if item[1] == 'NNP' and item[0] not in week_days:
            city_is.append(item[0])
    return city_is

in_city = input_city()

#print(input_city())

def return_city():
    if not in_city: # check to see if the list is empty or not
        return name_city
    else:
        return ''.join(in_city)

name_of_the_city = return_city()

print(name_of_the_city)

def in_weather():
    if 'What' in first_indices_to:
        if 'Weather' in first_indices_to:
            return True

def in_temp():
    if 'What' in first_indices_to:
        if 'Temperature' in first_indices_to:
            return True

def in_humid():
    if 'What' in first_indices_to:
        if 'Humidity' in first_indices_to:
            return True

def in_wind():
    if 'What' in first_indices_to:
        if 'Wind' in first_indices_to:
            return True



city = name_of_the_city
url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=1d134adf392b45adf4108dbc9949b53d".format(city)
res = requests.get(url)
data = res.json()

#print(data)


def response_today():
    return_today = [item for item in data['list'] if item['dt_txt'] == theDateandHours()]
    return return_today

weather_response = response_today()

forecast_responses = ['The weather forecast predicts', 'There seems to be', 'It seems as if it will be', 'There will be' ]

city_responses = ['in the city of', 'in']

rain_responses = ['so, take you an umberalla with you', 'so, take a pancho with you', 'so, you better dress well', 'so, you should prepare yourself for it',]

clearSky_responses = ['so, do not forget your sun-screen', 'so, don not forget your hat', 'so, you can take a walk today', 'so, enjoy the sun']

cloud_responses = ['so, prepare yourself for anything', 'so, be wary of the weather', 'so, take an umberalla in case it changes', 'so, it might look boring outside']

temperature_low_responses = ['so, you should dress tightly', 'so, be careful in the cold', 'so, you should take precautions', 'so, try to stay indoors']

temperature_mid_responses = ['so, you are good to take a walk', 'so, you dress as you like', 'so, no need for any precaution', 'so, it seems very comfortable outside']

temperature_high_responses = ['so, do not forget your sun screen', 'so, I reccomend you stay indoors', 'so, you should dress lightly', 'so, take your shades with you']

humidity_low_responses = ['so, there is no need for any precautions', 'so, it seems quite comfortable', 'so, it is easy to breathe outside']

humidity_high_responses = ['so, it could be hard to breathe', 'so, you should use a hat for your hair', 'so, take the necessary precautions']

wind_fast_responses = ['so, be careful out there', 'so try not to fly away', 'so, keep in mind fast wind means more danger', 'so, maybe a you fly a kite']

wind_slow_responses = ['so, nothing to worry about', 'so, it looks calm outside', 'so, no flying kites today']





def response_main():

    #weather_main = data['list'][0]['weather'][0]['main']
    weather_spesific = weather_response[0]['weather'][0]['main']
    temp = weather_response[0]['main']['temp']
    humid = weather_response[0]['main']['humidity']
    wind = weather_response[0]['wind']['speed']
    response = []

    if in_weather() == True:
        response.append(define_day_time())
        response.append(random.choice(forecast_responses))
        response.append('{} and {} degrees'.format(weather_spesific, str(temp)))
        response.append(random.choice(city_responses))
        response.append(city)
        return response

    if in_temp() == True:
        if temp < 10:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} degrees'.format(str(temp)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(temperature_low_responses))
        elif temp > 10 and temp < 30:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} degrees '.format(str(temp)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(temperature_mid_responses))
        else:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} degrees'.format(str(temp)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(temperature_high_responses))
        return response

    if in_humid() == True:
        if humid < 50:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} percent humidity'.format(str(humid)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(humidity_low_responses))
        else:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} percent humidity'.format(str(humid)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(humidity_high_responses))
        return response

    if in_wind() == True:
        if wind < 7:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} kilometer per second wind'.format(str(wind)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(wind_slow_responses))
        else:
            response.append(define_day_time())
            response.append(random.choice(forecast_responses))
            response.append('{} kilometer per second wind'.format(str(wind)))
            response.append(random.choice(city_responses))
            response.append(city)
            response.append(random.choice(wind_fast_responses))
        return response



def convertTuple2():
    return_string = ' '.join(response_main())
    return return_string


print(convertTuple2())

engine = pyttsx3.init()


def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

change_voice(engine, "en_US", "VoiceGenderFemale")
engine.say(convertTuple2())

engine.runAndWait()
