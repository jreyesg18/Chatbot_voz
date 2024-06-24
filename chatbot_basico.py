import speech_recognition as sr
import openai
from gtts import gTTS
from pygame import mixer
import os
import time as ti
import random

openai.api_key = "Colocar apikey provista en cuenta openai"

def transformar_audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar!")
        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-AR")
            print("you: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return "sigo esperando"

        except sr.RequestError:
            print("Ups, no hay servicio!")
            return "sigo esperando"

        except:
            print("Ups, algo salio mal!")
            return "sigo esperando"

def hablar(mensaje):
    volume = 0.7
    tts = gTTS(mensaje, lang="es", slow=False)
    ran = random.randint(0, 9999)
    filename = 'temp' + format(ran) + '.mp3'
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(volume)
    mixer.music.play()

    while mixer.music.get_busy():
        ti.sleep(0.3)

    mixer.quit()
    os.remove(filename)

def main():
    conversation = ""

    hablar("Hola!, Soy Vicky tu asistente personal, en que puedo ayudar?")

    while True:
        question = transformar_audio_a_texto().lower()

        conversation += "\nYou : " + question + "\n Vicky:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            temperature=0.5,
            max_tokens=100,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        answer = response['choices'][0]['message']['content'].strip()
        conversation += answer
        print("Vicky: " + answer + "\n")
        hablar(answer)

if __name__ == "__main__":
    main()
