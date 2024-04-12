import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie import syncCrazyflie


def activate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 255)

def deactivate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 0)

def light_check(scf):
    ...

def take_off(scf):
    ...

def land(scf):
    ...


def run_square_sequence(scf):
    ...

uris = ...

# The layout of the positions (1m apart from each other):
#   <------ 1 m ----->
#   0                1
#          ^              ^
#          |Y             |
#          |              |
#          +------> X    1 m
#                         |
#                         |
#   3               2     .


h = 0.0 # remain constant height similar to take off height
x0, y0 = +1.0, +1.0
x1, y1 = -1.0, -1.0

#    x   y   z  time
sequence0 = ...

sequence1 = ...

sequence2 = ...

sequence3 = ...

seq_args = ...

def run_sequence(scf: syncCrazyflie.SyncCrazyflie, sequence):
    ...


if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        swarm.parallel_safe(light_check)

        swarm.reset_estimators()

        swarm.parallel_safe(take_off)
        swarm.parallel_safe(run_square_sequence)
        swarm.parallel_safe(run_sequence, args_dict=seq_args)
        swarm.parallel_safe(land)