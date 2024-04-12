from threading import Timer

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig


class CrazyLogger(Crazyflie):
    def __init__(self, logConfig=LogConfig(name='Empty', period_in_ms=100000), link=None, ro_cache=None, rw_cache=None):
        super().__init__(link, ro_cache, rw_cache)
        self.logConfig = logConfig
        self.connected.add_callback(self._connected)

    def _connected(self, link_uri):
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""
        print('Connected to %s' % link_uri)

        try:
            self.log.add_config(self.logConfig)
            self.logConfig.start()
        except KeyError as e:
            print('Could not start log configuration,'
                  '{} not found in TOC'.format(str(e)))
        except AttributeError:
            print('Could not add Stabilizer log config, bad configuration.')


def create_lg_stab():
    def _stab_log_error(logconf, msg):
        """Callback from the log API when an error occurs"""
        print('Error when logging %s: %s' % (logconf.name, msg))

    def _stab_log_data( timestamp, data, logconf):
        """Callback from a the log API when data arrives"""
        print(f'[{timestamp}][{logconf.name}]: ', end='')
        for name, value in data.items():
            print(f'{name}: {value:3.3f} ', end='')
        print()

    lg_stab = LogConfig(name='Stabilizer', period_in_ms=100)
    lg_stab.add_variable('stateEstimate.x', 'float')
    lg_stab.add_variable('stateEstimate.y', 'float')
    lg_stab.add_variable('stateEstimate.z', 'float')
    lg_stab.add_variable('stabilizer.roll', 'float')
    lg_stab.add_variable('stabilizer.pitch', 'float')
    lg_stab.add_variable('stabilizer.yaw', 'float')
    # The fetch-as argument can be set to FP16 to save space in the log packet
    lg_stab.add_variable('pm.vbat', 'FP16')
    # This callback will receive the data
    lg_stab.data_received_cb.add_callback(_stab_log_data)
    # This callback will be called on errors
    lg_stab.error_cb.add_callback(_stab_log_error)
    return lg_stab


if __name__ == '__main__':
    create_lg_stab()



