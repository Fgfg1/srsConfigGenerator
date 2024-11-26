from .gnb_classes.cells import Cells
from .gnb_classes.cu_cp import Cu_cp
from .gnb_classes.cu_up import Cu_up
from .gnb_classes.du import Du
from .gnb_classes.cell_cfg import Cell_cfg
from .gnb_classes.e2 import E2
from .gnb_classes.ntn import Ntn
from .gnb_classes.ru_ofh import Ru_ofh
from .gnb_classes.ru_sdr import Ru_sdr
from .gnb_classes.ru_dummy import Ru_dummy
from .gnb_classes.fapi import Fapi
from .gnb_classes.hal import Hal
from .gnb_classes.buffer_pool import Buffer_pool
from .gnb_classes.expert_phy import Expert_phy
from .gnb_classes.expert_execution import Expert_execution
from .gnb_classes.test_mode import Test_mode
from .gnb_classes.log import Log
from .gnb_classes.pcap import Pcap
from .gnb_classes.metrics import Metrics

from config_item import ConfigItem
from .common_conf import CommonConfig


class Gnb(CommonConfig):
    def __init__(self, name="GnbConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # General configuration items
        self.gnb_id = ConfigItem(
            key="gnb_id",
            value=411, 
            comment="Optional UINT (411). Sets the numerical ID associated with the gNB.", 
            used=False
        )
        self.gnb_id_bit_length = ConfigItem(
            key="gnb_id_bit_length", 
            value=22, 
            comment="Optional UNIT (22). Sets the bit length of the gnb_id above. Format: integer between [22 - 32]", used=False
        )
        self.ran_node_name = ConfigItem(
            key="ran_node_name", value="srsgnb01", comment="RAN Node Name", used=False
        )
        self.gnb_du_id = ConfigItem(
            key="gnb_du_id", value=0, comment="GNB DU ID", used=False
        )
        self.qos = ConfigItem(
            key="qos", value=None, comment="Quality of Service configuration", used=False
        )
        self.srbs = ConfigItem(
            key="srbs", value=None, comment="SRB configuration", used=False
        )

        # Sub-modules
        self.cells = Cells()
        self.cu_cp = Cu_cp()
        self.cu_up = Cu_up()
        self.du = Du()
        self.cell_cfg = Cell_cfg()
        self.e2 = E2()
        self.ntn = Ntn()
        self.ru_ofh = Ru_ofh()
        self.ru_sdr = Ru_sdr()
        self.ru_dummy = Ru_dummy()
        self.fapi = Fapi()
        self.hal = Hal()
        self.buffer_pool = Buffer_pool()
        self.expert_phy = Expert_phy()
        self.expert_execution = Expert_execution()
        self.test_mode = Test_mode()
        self.log = Log()
        self.pcap = Pcap()
        self.metrics = Metrics()

    # Expose ConfigItem attributes via properties for compatibility
    @property
    def gnb_id(self):
        return self.gnb_id.value

    @gnb_id.setter
    def gnb_id(self, value):
        self.gnb_id.set_value(value)

    @property
    def gnb_id_bit_length(self):
        return self.gnb_id_bit_length.value

    @gnb_id_bit_length.setter
    def gnb_id_bit_length(self, value):
        self.gnb_id_bit_length.set_value(value)

    @property
    def ran_node_name(self):
        return self.ran_node_name.value

    @ran_node_name.setter
    def ran_node_name(self, value):
        self.ran_node_name.set_value(value)

    @property
    def gnb_du_id(self):
        return self.gnb_du_id.value

    @gnb_du_id.setter
    def gnb_du_id(self, value):
        self.gnb_du_id.set_value(value)

    @property
    def qos(self):
        return self.qos.value

    @qos.setter
    def qos(self, value):
        self.qos.set_value(value)

    @property
    def srbs(self):
        return self.srbs.value

    @srbs.setter
    def srbs(self, value):
        self.srbs.set_value(value)

    
