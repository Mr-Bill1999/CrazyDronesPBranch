from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils.multiranger import Multiranger


class CrazyRanger(Crazyflie):
    def __init__(self, link=None, ro_cache=None, rw_cache=None):
        super().__init__(link, ro_cache, rw_cache)
        self.ranger = Multiranger(self)


class RangerFactory:
    def construct(self, uri):
        cf = CrazyRanger(link=uri)
        return SyncCrazyflie(link_uri=uri, cf=cf)
