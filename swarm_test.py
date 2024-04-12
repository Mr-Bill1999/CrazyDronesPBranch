import time

import cflib.crtp
from cflib.crazyflie import HighLevelCommander
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie


def take_off(scf,z):
    print('take off')
    commander:HighLevelCommander = scf.cf.high_level_commander
    commander.takeoff(z, 2.0)
    time.sleep(3)


def final_land(scf):
    print('land')
    commander: HighLevelCommander= scf.cf.high_level_commander

    commander.land(absolute_height_m=0, duration_s=4)
    time.sleep(5)
    commander.stop()


def land(scf):
    print('land')
    commander: HighLevelCommander= scf.cf.high_level_commander

    commander.land(absolute_height_m=0, duration_s=4)
    time.sleep(5)


def hover_sequence(scf, params2, params1, param3, param4):
    x, y, z = params1['x'], params1['y'], params1['z']

    take_off(scf,z)
    time.sleep(3)
    change_position(scf, x, y, z)

    x, y, z = params2['x'], params2['y'], params2['z']
    change_position(scf, x, y, z)
    land(scf)

    x, y, z = param3['x'], param3['y'], param3['z']
    take_off(scf, z)
    change_position(scf, x, y, z)

    x, y, z = param4['x'], param4['y'], param4['z']
    change_position(scf, x, y, z)

    final_land(scf)


def change_position(scf: SyncCrazyflie, x, y, z):
    commander: HighLevelCommander= scf.cf.high_level_commander
    commander.go_to(x,y,z,0,3)
    time.sleep(3)


def rotate(scf):
    print("rotate")
    commander: HighLevelCommander= scf.cf.high_level_commander
    commander.go_to(0, 0, 0, 0, 6, True)


URI1 = "radio://0/80/2M/E7E7E7E7E1"
URI2 = 'radio://0/110/2M/E7E7E7E7E9'
URI3 = 'radio://0/110/2M/E7E7E7E7E3'
URI4 = "radio://0/110/2M/E7E7E7E7E5"

param1 = {'x': 1.64, 'y': 0.23, 'z': 0.5}
param2 = {'x': 1.63, 'y': 1.83, 'z': 1.2}
param3 = {'x': 0.93, 'y': 0.93, 'z': 0.5}
param4 = {'x': 0.93, 'y': 0.93, 'z': 1.2}

uris = {
    URI1,
    URI2
}

params = {
    URI1:[param1,param3, param4, param2],
    URI2:[param2, param4, param3, param1]
}

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        swarm.reset_estimators()
        print('estimators reseted')
        swarm.parallel_safe(hover_sequence, args_dict=params)


