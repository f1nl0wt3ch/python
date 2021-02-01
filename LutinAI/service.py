# This Python file uses the following encoding: utf-8
import datetime
import traceback
import platform
import speech_recognition as sr
import pyttsx3
import gtts
import locale
import webbrowser
import subprocess
from datetime import date
from datetime import datetime
from playsound import playsound

DEFAULT_ANSWER = "Selvä"
DEFAULT_GREETINGS = "Moikka, saisinko auttaa?"


# open application on mac
def _open_application_on_mac(application):
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/" + application + ".app"]
    )


# close application on mac
def _close_application_on_mac(application):
    subprocess.call(
        ["/usr/bin/osascript", "-e", 'tell application \"' + application + '\" to quit']
    )


# get current date
def _get_current_date():
    locale.setlocale(locale.LC_TIME, "fi_FI")
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    return current_date


# get current time
def _get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# start recording sound
def _speech_to_text(greetings):
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print(greetings)
        # _text_to_speech(greetings)
        _text_to_speech_by_gtts(greetings)
        # recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        _text_to_speech_by_gtts("Minä olen tunnisttamassa sinun ääntä, pieni hetki...")
        # convert speech to text
        question = ""
        try:
            print("Tunnista...")
            try:
                question = recognize.recognize_google(audio, language="fi-FI")
            except Exception as googleException:
                print(googleException)
                try:
                    question = recognize.recognize_sphinx(audio)
                except Exception as sphinxException:
                    print(sphinxException)
                    try:
                        question = recognize.recognize_wit(audio, key="YKJZ3BVLURGKCQFOWH4VHIFMHRJBPD2K")
                    except Exception as witException:
                        print(witException)
                        question = "none"
            if question:
                question = question.lower()
                _text_to_speech_by_gtts("Kysytkö: " + question)
        except Exception as e:
            traceback.print_exc()
    return question


# text to speech using gtts
def _text_to_speech_by_gtts(text):
    tts = gtts.gTTS(text, lang="fi")
    tts.save("audio.mp3")
    playsound("audio.mp3")


# recognize speech using Sphinx
def _text_to_speech_by_pyttsx3(text):
    text = "Sorry, I cannot hear you." if not text else text
    # initialize the engine
    engine = pyttsx3.init()
    try:
        engine.say(text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google could not understand audio")
        engine.say(text)
        engine.runAndWait()
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
        engine.say(text)
        engine.runAndWait()


# how to answer questions
def _answer_question(question):
    if not question:
        answer = "En kuulu mitään."
    elif "google" in question:
        answer = DEFAULT_ANSWER
        webbrowser.get("chrome").open("https://google.com")
    elif "kotisivu" in question:
        selain = _speech_to_text("Minkä selaimen haluat käyttää?")
        answer = DEFAULT_ANSWER
        if any(x in selain for x in ["chrome", "chromella", "chromeella"]):
            webbrowser.get("chrome").open("http://tikkidinh.com")
        else:
            webbrowser.get("safari").open("http://tikkidinh.com")
    elif all(x in question for x in ["sulje", "applikaatio"]):
        closed_app = _speech_to_text("Minkä applikaatio haluut sulkea?")
        answer = DEFAULT_ANSWER
        if "sähköposti" in closed_app:
            _close_application_on_mac("Microsoft Outlook")
        if "safari" in closed_app:
            _close_application_on_mac("safari")
        if "chrome" in closed_app:
            _close_application_on_mac("chrome")
        if all(x in closed_app for x in ["kaikki", "selaimet"]):
            _close_application_on_mac("safari")
            _close_application_on_mac("chrome")
            _close_application_on_mac("firefox")
    elif all(x in question for x in ["avaa", "applikaatio"]):
        opened_app = _speech_to_text("Minkä applikaatio haluut avata?")
        _open_application_on_mac(opened_app)
        answer = DEFAULT_ANSWER
    elif "sähköposti" in question:
        _open_application_on_mac("Microsoft Outlook")
        answer = DEFAULT_ANSWER
    elif all(x in question for x in ["mikä", "päivä", "tänään"]):
        answer = "Tänään on " + _get_current_date()
    elif all(x in question for x in ["mitä", "kello"]):
        answer = _get_current_time()
    elif any(x in question for x in ["käyttöjärjestelmä", "kone"]):
        answer = "Sinulla on " + str(platform.platform()) + " kone"
    elif any(x in question for x in ["vanhaa", "vanha"]):
        answer = "Olen syntynyt vuonna 2020"
    elif "kuuluu" in question:
        answer = "Hyvää kuuluu, kiitos!"
    elif "nimi" in question:
        answer = "Minun nimeni on Lutin"
    elif "moikka" in question:
        answer = "Moikka pomo!"
    elif "kotoisin" in question:
        answer = "Olen kotoisin Suomesta"
    elif "syntynyt" in question:
        answer = "Olen syntynyt Järvenpäässä"
    elif any(x in question for x in ["osaako", "osaatko", "osaaks", "osako"]):
        answer = "Sorry, en osaa. Mutta minun faija varmaan osaa"
    elif any(x in question for x in ["faija", "isä", "isi", "isii"]):
        answer = "Minun faija on Thinh"
    elif not question:
        answer = "En kuulu sinun ääntä. Tarkistathan sinun mikrofoni."
    else:
        answer = "Anteeksi, en taida ymmärtää sun kysymykseen."
    return answer


run = True
while run:
    question = _speech_to_text(DEFAULT_GREETINGS)
    print(question)
    if any(x in question for x in ["lopeta", "lopettaa", "lopetat"]):
        _text_to_speech_by_gtts("On ilo jälleen nähdä ja palvella sinua. Näkemiin!")
        run = False
    else:
        answer = _answer_question(question)
        _text_to_speech_by_gtts(answer)
