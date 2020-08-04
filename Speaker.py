# pip install pyttsx3
# pip install win32com.client
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=d5a0bf7dfa8b4323afff588def229eb0')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    try:
        for i in range(0, 11):
            speak(my_json['articles'][i]['title'])
    except IndexError:
        print("news finished...!!!")
    