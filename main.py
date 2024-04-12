import logging
import time
from typing import Type


import cflib.crtp
from cflib.crazyflie import Crazyflie, Extpos
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander
from cflib.utils import uri_helper

from CrazyLogger import CrazyLogger, create_lg_stab

uri = uri_helper.uri_from_env(default='radio://0/80/2M/1')




def simple_connect(scf):
    print("Yeah, I'm connected! :D")
    motion_controller = MotionCommander(scf)
    motion_controller.take_off()
    motion_controller.up(1)
    motion_controller.forward(0.3)
    motion_controller.turn_right(180)
    motion_controller.forward(0.3)

    time.sleep(1)
    motion_controller.land(0.2)



if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()
    with SyncCrazyflie(uri, cf=CrazyLogger(create_lg_stab(),rw_cache='./cache')) as scf:
        simple_connect(scf)
