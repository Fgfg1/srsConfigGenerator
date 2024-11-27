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

from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig


class Gnb(CommonConfig):
    def __init__(self, name=None, data=None, used=True):
        super().__init__(name, data or {}, used)

        # General configuration items
        self._gnb_id = ConfigItem(
            key="gnb_id",
            value=411, 
            comment="Optional UINT (411). Sets the numerical ID associated with the gNB.", 
            used=False
        )
        self._gnb_id_bit_length = ConfigItem(
            key="gnb_id_bit_length", 
            value=22, 
            comment="Optional UNIT (22). Sets the bit length of the gnb_id above. Format: integer between [22 - 32]", used=False
        )
        self._ran_node_name = ConfigItem(
            key="ran_node_name", value="srsgnb01", comment="RAN Node Name", used=False
        )
        self._gnb_du_id = ConfigItem(
            key="gnb_du_id", value=0, comment="GNB DU ID", used=False
        )
        
        # might be a class in the future
        # example can be found https://github.com/srsran/srsRAN_Project/blob/main/configs/qos.yml
        self._qos = ConfigItem(
            key="qos", value=None, comment="Quality of Service configuration", used=False
        )
        
        # might be a class in the future
        # example can be found https://github.com/srsran/srsRAN_Project/blob/main/configs/srb.yml
        self._srbs = ConfigItem(
            key="srbs", value=None, comment="SRB configuration", used=False
        )

        # Sub-modules
        self._cells = Cells()
        self._cu_cp = Cu_cp()
        self._cu_up = Cu_up()
        self._du = Du()
        self._cell_cfg = Cell_cfg()
        self._e2 = E2()
        self._ntn = Ntn()
        self._ru_ofh = Ru_ofh()
        self._ru_sdr = Ru_sdr()
        self._ru_dummy = Ru_dummy()
        self._fapi = Fapi()
        self._hal = Hal()
        self._buffer_pool = Buffer_pool()
        self._expert_phy = Expert_phy()
        self._expert_execution = Expert_execution()
        self._test_mode = Test_mode()
        self._log = Log()
        self._pcap = Pcap()
        self._metrics = Metrics()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._gnb_id,
            self._gnb_id_bit_length,
            self._ran_node_name,
            self._gnb_du_id,
            self._cells,
            self._qos,
            self._srbs,
            self._cu_cp,
            self._cu_up,
            self._du,
            self._cell_cfg,
            self._e2,
            self._ntn,
            self._ru_ofh,
            self._ru_sdr,
            self._ru_dummy,
            self._fapi,
            self._hal,
            self._buffer_pool,
            self._expert_phy,
            self._expert_execution,
            self._test_mode,
            self._log,
            self._pcap,
            self._metrics
        ]

    # Expose ConfigItem attributes via properties for compatibility
    @property
    def gnb_id(self):
        return self._gnb_id.value

    @gnb_id.setter
    def gnb_id(self, value):
        self._gnb_id.set_value(value)

    @property
    def gnb_id_bit_length(self):
        return self._gnb_id_bit_length.value

    @gnb_id_bit_length.setter
    def gnb_id_bit_length(self, value):
        self._gnb_id_bit_length.set_value(value)

    @property
    def ran_node_name(self):
        return self._ran_node_name.value

    @ran_node_name.setter
    def ran_node_name(self, value):
        self._ran_node_name.set_value(value)

    @property
    def gnb_du_id(self):
        return self._gnb_du_id.value

    @gnb_du_id.setter
    def gnb_du_id(self, value):
        self._gnb_du_id.set_value(value)

    @property
    def qos(self):
        return self._qos.value

    @qos.setter
    def qos(self, value):
        self._qos.set_value(value)

    @property
    def srbs(self):
        return self._srbs.value

    @srbs.setter
    def srbs(self, value):
        self._srbs.set_value(value)

    def get_gui_data(self):
        """
        returns a dic of everything in the gnb so that the pyqt6 can interprite it
        Will use the ConfgItem class as the values.
        """
        pass

    def load_data(self, input:dict):
        """Takes dictionary input from pyyaml and inputs all data into gnb"""
        pass
        
