import sys
import time
import speech_recognition
import speech_recognition as sr
import re
from cflib.positioning.motion_commander import MotionCommander
import pyaudio
import cflib
from cflib.crazyflie import Crazyflie
from CrazyLogger import CrazyLogger, create_lg_stab
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper

is_flying = True




def down(motion_controller):
    motion_controller.down(1)
    time.sleep(1)

def forward(motion_controller):
    motion_controller.forward(1)
    time.sleep(1)

def back(motion_controller):
    motion_controller.back(1)
    time.sleep(1)

def up(motion_controller):
    motion_controller.up(1)
    time.sleep(1)

def take_off(motion_controller):
    motion_controller.take_off()
    time.sleep(1)

def land(motion_controller):
    motion_controller.land(0.2)
    time.sleep(1)

def rotate(motion_controller: MotionCommander):
    motion_controller.turn_right(180)
    time.sleep(1)

def end_flying(motion_controller):
    global is_flying
    land(motion_controller)
    is_flying = False

command_map = {
    "взлёт": take_off,
    "посадка": land,
    "вперёд" : forward,
    "назад" : back,
    "вверх" : up,
    "вниз" : down,
    "разворот" : rotate,
    "конец" : end_flying
}

def voice_commander(motion_commander):
    global is_flying
    for command, func in command_map.items():
        if command in transcript.lower():
            func(motion_commander)


if __name__ == '__main__':
    uri = 'radio://0/80/2M/E7E7E7E7E7'
    index = 0
    transcript = ''
    srr = sr.Recognizer()
    mic = sr.Microphone()
    cflib.crtp.init_drivers()




    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        motion_controller = MotionCommander(scf)

        while is_flying:
            with mic as sourse:
                try:
                    srr.energy_threshold = 750
                    srr.adjust_for_ambient_noise(sourse)
                    audio = srr.listen(sourse)
                    transcript = srr.recognize_google(audio, language='ru-RU')
                    print(transcript)
                    voice_commander(motion_controller)

                except speech_recognition.UnknownValueError:
                    pass
