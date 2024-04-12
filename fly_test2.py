import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

DEFAULT_HEIGHT = 1
#   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
#   URI = uri_helper.uri_from_env(default='radio://0/110/2M/E7E7E7E71B')
#   URI = uri_helper.uri_from_env(default='radio://0/110/2M/E7E7E7E7E2')
#   URI = uri_helper.uri_from_env(default='radio://0/80/2M/1')
#   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E1')
URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E8')






def flying(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(3)
        mc.land()



if __name__ == "__main__":
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        time.sleep(1)
        flying(scf)




