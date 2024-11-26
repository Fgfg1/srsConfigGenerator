from .cu_cp_classes.amf import Amf
from .cu_cp_classes.mobility import Mobility
from .cu_cp_classes.rrc import Rrc
from .cu_cp_classes.security import Security
from .cu_cp_classes.f1ap import F1ap
from config_item import ConfigItem
from common_conf import CommonConfig

class Cu_cp(CommonConfig):
    def __init__(self, name="CuCpConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.max_nof_dus = ConfigItem(
            key="max_nof_dus",
            value=None,
            comment="Maximum number of DUs",
            used=False,
        )
        self.max_nof_cu_ups = ConfigItem(
            key="max_nof_cu_ups",
            value=None,
            comment="Maximum number of CU-UPs",
            used=False,
        )
        self.max_nof_ues = ConfigItem(
            key="max_nof_ues",
            value=None,
            comment="Maximum number of UEs",
            used=False,
        )
        self.max_nof_drbs_per_ue = ConfigItem(
            key="max_nof_drbs_per_ue",
            value=None,
            comment="Maximum number of DRBs per UE",
            used=False,
        )
        self.inactivity_timer = ConfigItem(
            key="inactivity_timer",
            value=120,
            comment="Inactivity timer in seconds",
            used=False,
        )
        self.pdu_session_setup_timeout = ConfigItem(
            key="pdu_session_setup_timeout",
            value=3,
            comment="PDU session setup timeout in seconds",
            used=False,
        )
        self.load_plugins = ConfigItem(
            key="load_plugins",
            value=False,
            comment="Enable or disable plugin loading",
            used=False,
        )

        # Sub-configurations
        self.amf = Amf()
        self.mobility = Mobility()
        self.rrc = Rrc()
        self.security = Security()
        self.f1ap = F1ap()

    # Getters and setters for ConfigItems
    @property
    def max_nof_dus(self):
        return self.max_nof_dus.value

    @max_nof_dus.setter
    def max_nof_dus(self, value):
        self.max_nof_dus.set_value(value)

    @property
    def max_nof_cu_ups(self):
        return self.max_nof_cu_ups.value

    @max_nof_cu_ups.setter
    def max_nof_cu_ups(self, value):
        self.max_nof_cu_ups.set_value(value)

    @property
    def max_nof_ues(self):
        return self.max_nof_ues.value

    @max_nof_ues.setter
    def max_nof_ues(self, value):
        self.max_nof_ues.set_value(value)

    @property
    def max_nof_drbs_per_ue(self):
        return self.max_nof_drbs_per_ue.value

    @max_nof_drbs_per_ue.setter
    def max_nof_drbs_per_ue(self, value):
        self.max_nof_drbs_per_ue.set_value(value)

    @property
    def inactivity_timer(self):
        return self.inactivity_timer.value

    @inactivity_timer.setter
    def inactivity_timer(self, value):
        self.inactivity_timer.set_value(value)

    @property
    def pdu_session_setup_timeout(self):
        return self.pdu_session_setup_timeout.value

    @pdu_session_setup_timeout.setter
    def pdu_session_setup_timeout(self, value):
        self.pdu_session_setup_timeout.set_value(value)

    @property
    def load_plugins(self):
        return self.load_plugins.value

    @load_plugins.setter
    def load_plugins(self, value):
        self.load_plugins.set_value(value)
