from config_item import ConfigItem
from common_conf import CommonConfig

class E2(CommonConfig):
    def __init__(self, name="E2Config", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.enable_cu_e2 = ConfigItem(
            key="enable_cu_e2",
            value=False,
            comment="Enable CU E2 agent",
            used=False,
        )
        self.enable_du_e2 = ConfigItem(
            key="enable_du_e2",
            value=False,
            comment="Enable DU E2 agent",
            used=False,
        )
        self.addr = ConfigItem(
            key="addr",
            value="127.0.0.1",
            comment="IP address for E2 connection",
            used=False,
        )
        self.port = ConfigItem(
            key="port",
            value=36421,
            comment="Port number for E2 connection",
            used=False,
        )
        self.bind_addr = ConfigItem(
            key="bind_addr",
            value="127.0.0.1",
            comment="Bind address for E2 connection",
            used=False,
        )
        self.sctp_rto_initial = ConfigItem(
            key="sctp_rto_initial",
            value=120,
            comment="Initial SCTP retransmission timeout in milliseconds",
            used=False,
        )
        self.sctp_rto_min = ConfigItem(
            key="sctp_rto_min",
            value=120,
            comment="Minimum SCTP retransmission timeout in milliseconds",
            used=False,
        )
        self.sctp_rto_max = ConfigItem(
            key="sctp_rto_max",
            value=500,
            comment="Maximum SCTP retransmission timeout in milliseconds",
            used=False,
        )
        self.sctp_initial_max_attempts = ConfigItem(
            key="sctp_initial_max_attempts",
            value=3,
            comment="Maximum attempts for SCTP connection initialization",
            used=False,
        )
        self.sctp_max_init_timeo = ConfigItem(
            key="sctp_max_init_timeo",
            value=500,
            comment="Maximum time for SCTP initialization in milliseconds",
            used=False,
        )
        self.e2sm_kpm_enabled = ConfigItem(
            key="e2sm_kpm_enabled",
            value=False,
            comment="Enable E2SM-KPM reporting",
            used=False,
        )
        self.e2sm_rc_enabled = ConfigItem(
            key="e2sm_rc_enabled",
            value=False,
            comment="Enable E2SM-RC reporting",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def enable_cu_e2(self):
        return self.enable_cu_e2.value

    @enable_cu_e2.setter
    def enable_cu_e2(self, value):
        self.enable_cu_e2.set_value(value)

    @property
    def enable_du_e2(self):
        return self.enable_du_e2.value

    @enable_du_e2.setter
    def enable_du_e2(self, value):
        self.enable_du_e2.set_value(value)

    @property
    def addr(self):
        return self.addr.value

    @addr.setter
    def addr(self, value):
        self.addr.set_value(value)

    @property
    def port(self):
        return self.port.value

    @port.setter
    def port(self, value):
        self.port.set_value(value)

    @property
    def bind_addr(self):
        return self.bind_addr.value

    @bind_addr.setter
    def bind_addr(self, value):
        self.bind_addr.set_value(value)

    @property
    def sctp_rto_initial(self):
        return self.sctp_rto_initial.value

    @sctp_rto_initial.setter
    def sctp_rto_initial(self, value):
        self.sctp_rto_initial.set_value(value)

    @property
    def sctp_rto_min(self):
        return self.sctp_rto_min.value

    @sctp_rto_min.setter
    def sctp_rto_min(self, value):
        self.sctp_rto_min.set_value(value)

    @property
    def sctp_rto_max(self):
        return self.sctp_rto_max.value

    @sctp_rto_max.setter
    def sctp_rto_max(self, value):
        self.sctp_rto_max.set_value(value)

    @property
    def sctp_initial_max_attempts(self):
        return self.sctp_initial_max_attempts.value

    @sctp_initial_max_attempts.setter
    def sctp_initial_max_attempts(self, value):
        self.sctp_initial_max_attempts.set_value(value)

    @property
    def sctp_max_init_timeo(self):
        return self.sctp_max_init_timeo.value

    @sctp_max_init_timeo.setter
    def sctp_max_init_timeo(self, value):
        self.sctp_max_init_timeo.set_value(value)

    @property
    def e2sm_kpm_enabled(self):
        return self.e2sm_kpm_enabled.value

    @e2sm_kpm_enabled.setter
    def e2sm_kpm_enabled(self, value):
        self.e2sm_kpm_enabled.set_value(value)

    @property
    def e2sm_rc_enabled(self):
        return self.e2sm_rc_enabled.value

    @e2sm_rc_enabled.setter
    def e2sm_rc_enabled(self, value):
        self.e2sm_rc_enabled.set_value(value)