import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")

	elif hour>=12 and hour<18:
		speak("Good Afternoon")

	else:
		speak("Good Evening")

	speak("I am Jarvis Sir. Please tell me how may I help you.")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.energy_threshold = 302
		audio = r.listen(source)

	try:
		print("Recoginizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		#print(e)

		print("Could you say that again please...")
		speak("Could you say that again please")
		return "None"

	return query

if __name__ == '__main__':
	wishMe()
	while True:
		query = takeCommand().lower()
		# Logic for executing tasks based on query

		if 'the time' in query:
			strTime = datetime.datetime.now().strftime('%H:%M:%S')
			speak(f"The time is {strTime}")

		elif 'search' in query:
			speak("Searching Google...")
			query = query.replace("what is","")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Google")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'start music' in query:
			music_dir = 'C:\\Users\\$use\\Music'
			songs = os.listdir(music_dir)
			#print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'play' in query:
			song = query.replace('play','')
			speak('playing' + song)
			pywhatkit.playonyt(song)

	
			
