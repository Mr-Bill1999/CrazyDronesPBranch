from CrazyLogger import  CrazyLogger,create_lg_stab
import cflib.crazyflie.extpos


uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

class escape_landing_problems:

    def escape(uri):
        z_coordinates = []
        lg_stab = LogConfig(name='Stabilizer', period_in_ms=100)
        lg_stab.add_variable('stateEstimate.z', 'float')
        if lg_stab.data_received_cb.add_callback() not in z_coordinates:
