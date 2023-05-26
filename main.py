import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

from utils import *
from settings import *


class Game:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT

        self.background = pygame.image.load('assets/background.png')
        self.background = pygame.transform.smoothscale(surface=self.background, size=(self.width, self.height))

        self.loading = pygame.image.load('assets/loading.png')
        self.loading = pygame.transform.smoothscale(surface=self.loading, size=(self.width, self.height))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('ГОВОРЯЩИЙ КОТ')

        self.rec = sr.Recognizer()
        self.mic = sr.Microphone(device_index=1)
        self.speak_engine = pyttsx3.init()

        self.voices = self.speak_engine.getProperty('voices')
        self.speak_engine.setProperty('voice', self.voices[0].id)

        self.answer = 'ANSWER'

        self.log = 'LOG'

    def remove_noise(self):
        with self.mic as source:
            self.reset()

            debug('123',500,450)
            self.rec.adjust_for_ambient_noise(source)
            self.speak("Добрый день, кожанные мешки")
            self.speak("котик слушает")


    def stop_listening(self):
        self.rec.listen_in_background(self.mic,self.callback)

    def reset(self):
        self.screen.blit(self.loading, (0, 0))
        pygame.display.update()

    def speak(self, what):
        print(what)
        self.answer = what
        self.speak_engine.say(what)
        self.speak_engine.runAndWait()
        self.speak_engine.stop()

    def callback(self,recognizer, audio):
        try:
            voice = recognizer.recognize_google(audio, language="ru-RU").lower()
            print("[log] Распознано: " + voice)
            self.log = voice

            if voice.startswith(opts["alias"]):
                # обращаются к коту
                cmd = voice

                for x in opts['alias']:
                    cmd = cmd.replace(x, "").strip()

                for x in opts['tbr']:
                    cmd = cmd.replace(x, "").strip()

                # распознаем и выполняем команду
                cmd = self.recognize_cmd(cmd)
                self.execute_cmd(cmd['cmd'])

        except sr.UnknownValueError:
            print("[log] Голос не распознан!")
            self.log = "Голос не распознан!"

        except sr.RequestError as e:
            print("[log] Неизвестная ошибка, проверьте интернет!")
            self.log = "Неизвестная ошибка, проверьте интернет!"
            self.stop_listening()

    def recognize_cmd(self,cmd):
        RC = {'cmd': '', 'percent': 0}
        for c, v in opts['cmds'].items():

            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > RC['percent']:
                    RC['cmd'] = c
                    RC['percent'] = vrt

        return RC

    def execute_cmd(self,cmd):
        if cmd == 'ctime':
            # сказать текущее время
            now = datetime.datetime.now()
            self.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

        elif cmd == 'ocenka':
            # оценка
            self.speak("только пятерку")


        elif cmd == 'stupid1':
            # староста
            self.speak("Юляша Зарапина конечно что же я думал все это знают")


        else:
            print('Команда не распознана, повторите!')
            self.log = 'Команда не распознана, повторите!'


    def game_cycle(self):
        self.stop_listening()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end = False
                        pygame.quit()
                        quit()
            self.screen.blit(self.background, (0, 0))
            debug(self.answer,500,450)
            debug(self.log, 500, 200)

            clock = pygame.time.Clock()
            pygame.display.update()
            clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.remove_noise()
    game.game_cycle()