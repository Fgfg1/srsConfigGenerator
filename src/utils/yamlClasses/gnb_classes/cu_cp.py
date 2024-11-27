from .cu_cp_classes.amf import Amf
from .cu_cp_classes.mobility import Mobility
from .cu_cp_classes.rrc import Rrc
from .cu_cp_classes.security import Security
from .cu_cp_classes.f1ap import F1ap
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Cu_cp(CommonConfig):
    def __init__(self, name="cu_cp", data=None, used=True):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional UINT. Maximum number of DU connections that the CU-CP may accept.
        self._max_nof_dus = ConfigItem(
            key="max_nof_dus",
            value=None,
            comment="Maximum number of DUs",
            used=False,
        )

        # Optional UINT. Maximum number of CU-UP connections that the CU-CP may accept.
        self._max_nof_cu_ups = ConfigItem(
            key="max_nof_cu_ups",
            value=None,
            comment="Maximum number of CU-UPs",
            used=False,
        )

        # Optional UINT. Maximum number of UEs that the CU-CP may accept.
        self._max_nof_ues = ConfigItem(
            key="max_nof_ues",
            value=None,
            comment="Maximum number of UEs",
            used=False,
        )

        # Optional UINT. Maximum number of DRBs per UE. Supported: [1 - 29].
        self._max_nof_drbs_per_ue = ConfigItem(
            key="max_nof_drbs_per_ue",
            value=None,
            comment="Maximum number of DRBs per UE",
            used=False,
        )

        # Optional INT (120). Sets the UE/PDU Session/DRB inactivity timer in seconds. Supported: [1 - 7200].
        self._inactivity_timer = ConfigItem(
            key="inactivity_timer",
            value=120,
            comment="Inactivity timer in seconds",
            used=False,
        )

        # Optional INT (3). Timeout for the setup of a PDU session after an InitialUeMessage was sent to the core, in seconds.
        # The timeout must be larger than T310. If the value is reached, the UE will be released
        self._pdu_session_setup_timeout = ConfigItem(
            key="pdu_session_setup_timeout",
            value=3,
            comment="PDU session setup timeout in seconds",
            used=False,
        )

        # Optional BOOLEAN (false). Attempt to load plugin library to enable srsRAN_Enterprise features.
        self._load_plugins = ConfigItem(
            key="load_plugins",
            value=False,
            comment="Enable or disable plugin loading",
            used=False,
        )

        # Sub-configurations
        self._amf = Amf()
        self._mobility = Mobility()
        self._rrc = Rrc()
        self._security = Security()
        self._f1ap = F1ap()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._max_nof_dus,
            self._max_nof_cu_ups,
            self._max_nof_ues,
            self._max_nof_drbs_per_ue,
            self._inactivity_timer,
            self._pdu_session_setup_timeout,
            self._load_plugins,
            self._amf,
            self._mobility,
            self._rrc,
            self._security,
            self._f1ap
        ]

    # Getters and setters for ConfigItems
    @property
    def max_nof_dus(self):
        return self._max_nof_dus.value

    @max_nof_dus.setter
    def max_nof_dus(self, value):
        self._max_nof_dus.set_value(value)

    @property
    def max_nof_cu_ups(self):
        return self._max_nof_cu_ups.value

    @max_nof_cu_ups.setter
    def max_nof_cu_ups(self, value):
        self._max_nof_cu_ups.set_value(value)

    @property
    def max_nof_ues(self):
        return self._max_nof_ues.value

    @max_nof_ues.setter
    def max_nof_ues(self, value):
        self._max_nof_ues.set_value(value)

    @property
    def max_nof_drbs_per_ue(self):
        return self._max_nof_drbs_per_ue.value

    @max_nof_drbs_per_ue.setter
    def max_nof_drbs_per_ue(self, value):
        self._max_nof_drbs_per_ue.set_value(value)

    @property
    def inactivity_timer(self):
        return self._inactivity_timer.value

    @inactivity_timer.setter
    def inactivity_timer(self, value):
        self._inactivity_timer.set_value(value)

    @property
    def pdu_session_setup_timeout(self):
        return self._pdu_session_setup_timeout.value

    @pdu_session_setup_timeout.setter
    def pdu_session_setup_timeout(self, value):
        self._pdu_session_setup_timeout.set_value(value)

    @property
    def load_plugins(self):
        return self._load_plugins.value

    @load_plugins.setter
    def load_plugins(self, value):
        self._load_plugins.set_value(value)
