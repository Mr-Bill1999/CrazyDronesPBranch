import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.high_level_commander import HighLevelCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E1')

def flying(scf):
    commander:HighLevelCommander = scf.cf.high_level_commander
    commander.takeoff(0.8,duration_s=1)
    time.sleep(1)
    commander.go_to(3.5,0,0,yaw=0,relative=True,duration_s=6)
    time.sleep(6)
    commander.go_to(0, 0, 0, yaw=-90, relative=True, duration_s=4)
    time.sleep(4)
    commander.go_to(0.0, -3.5, 0, yaw=0, relative=True, duration_s=6)
    time.sleep(6)
    commander.go_to(0, 0, 0, yaw=-90, relative=True, duration_s=4)
    time.sleep(4)
    commander.go_to(-3.5, 0, 0, yaw=0, relative=True, duration_s=6)
    time.sleep(6)
    commander.go_to(0, 0, 0, yaw=-90, relative=True, duration_s=4)
    time.sleep(4)
    commander.go_to(0.0, 3.5, 0, yaw=0, relative=True, duration_s=6)
    time.sleep(6)


    # commander.go_to(0, 0, 1.5,yaw=0, relative=True,duration_s=2)
    # time.sleep(2)
    # commander.go_to(4.2, 0, 0, yaw=90, relative=True,duration_s=6)
    # time.sleep(6)
    # commander.go_to(4.3, 0, 0, yaw=90, relative=True,duration_s=6)
    # time.sleep(6)
    # commander.go_to(4.2, 0, 0, yaw=90, relative=True,duration_s=6)
    # time.sleep(6)
    # commander.go_to(4.3, 0, 0, yaw=90, relative=True,duration_s=6)
    # time.sleep(6)
    commander.land(0.03, 2)

if __name__ == "__main__":
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        time.sleep(1)
        flying(scf)












