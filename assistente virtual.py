import speech_recognition as sr
import pyttsx3
import pywhatkit
import os


voice_rec = sr.Recognizer()
machine = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as mic:
            voice_rec.adjust_for_ambient_noise(mic)
            print('Ouvindo...')
            machine.say('Ouvindo...')
            voice = voice_rec.listen(mic)
            comando = voice_rec.recognize_google(voice, language='pt-BR')
            comando = comando.lower()
            print(comando)
    except:
        print('Desculpe, não entendi!')

    return comando


def comando_do_usuario():
    while True:
        comando = executa_comando()
        if 'abra no youtube' in comando:
            open_youtube = comando.replace('abra no youtube', '')
            result = pywhatkit.playonyt(open_youtube)
            machine.say('abrindo no youtbe...')
            machine.runAndWait()
        elif 'abrir excel' in comando:
            excel = comando.replace('abrir excel', '')
            os.system('Start Excel.exe')
            machine.say('Abrindo excel')
            machine.runAndWait
        elif 'pesquisar' in comando:
            google_search = comando.replace('pesquisar', '')
            result = pywhatkit.search(google_search)
            machine.say('pesquisando...')
            machine.runAndWait


comando_do_usuario()
