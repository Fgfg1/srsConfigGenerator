from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .amf_classes.supported_tracking_areas import Supported_tracking_areas

class Amf(CommonConfig):
    def __init__(self, name="AmfConfig", data=None, used=True):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required TEXT. Sets the IP address or hostname of the AMF. Format: IPV4 or IPV6 IP address.
        self._addr = ConfigItem(
            key="addr",
            value=None,
            comment="Address of the AMF",
            used=True,
        )

        # Optional UINT. Sets the AMF port. Format: integer between [20000 - 40000].
        self._port = ConfigItem(
            key="port",
            value=38412,
            comment="Port for the AMF communication",
            used=True,
        )

        # Optional TEXT. Sets local IP address to bind for N2 interface. Format: IPV4 or IPV6 IP address.
        self._bind_addr = ConfigItem(
            key="bind_addr",
            value="127.0.0.1",
            comment="Address to bind for AMF",
            used=True,
        )

        # Optional TEXT. Sets network device to bind for N2 interface. Format: IPV4 or IPV6 IP address.
        self._bind_interface = ConfigItem(
            key="bind_interface",
            value="auto",
            comment="Network interface to bind for AMF",
            used=False,
        )

        # Optional INT. Sets the initial retransmission timeout when creating the SCTP connection.
        self._sctp_rto_initial = ConfigItem(
            key="sctp_rto_initial",
            value=120,
            comment="Initial SCTP RTO in milliseconds",
            used=False,
        )

        # Optional INT. Sets the minimum retransmission timeout for the SCTP connection.
        self._sctp_rto_min = ConfigItem(
            key="sctp_rto_min",
            value=120,
            comment="Minimum SCTP RTO in milliseconds",
            used=False,
        )

        # Optional INT. Sets the maximum retransmission timeout for the SCTP connection.
        self._sctp_rto_max = ConfigItem(
            key="sctp_rto_max",
            value=500,
            comment="Maximum SCTP RTO in milliseconds",
            used=False,
        )

        # Optional INT. Sets the maximum retransmission attempts for the initial SCTP connection.
        self._sctp_initial_max_attempts = ConfigItem(
            key="sctp_initial_max_attempts",
            value=3,
            comment="Maximum SCTP initialization attempts",
            used=False,
        )

        # Optional INT. Sets the maximum retransmission timeout for the initial SCTP connection.
        self._sctp_max_init_timeo = ConfigItem(
            key="sctp_max_init_timeo",
            value=500,
            comment="Maximum SCTP initialization timeout in milliseconds",
            used=False,
        )

        # Optional BOOLEAN. Setting to true allows the gNB to send SCTP messages as soon as possible without any Nagle-like algorithm. Supported: [false, true].
        self._sctp_nodelay = ConfigItem(
            key="sctp_nodelay",
            value=False,
            comment="Enable or disable SCTP_NODELAY option",
            used=False,
        )

        # Optional BOOLEAN. Setting to true allows the gNB to run without a core. Supported: [0, 1].
        self._no_core = ConfigItem(
            key="no_core",
            value=False,
            comment="Flag to disable core functionality",
            used=False,
        )

        # Sub-configurations
        self._supported_tracking_areas = Supported_tracking_areas()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._addr,
            self._port,
            self._bind_addr,
            self._bind_interface,
            self._sctp_rto_initial,
            self._sctp_rto_min,
            self._sctp_rto_max,
            self._sctp_initial_max_attempts,
            self._sctp_max_init_timeo,
            self._sctp_nodelay,
            self._no_core,
            self._supported_tracking_areas
        ]

    # Getters and setters for ConfigItems
    @property
    def addr(self):
        return self._addr.value

    @addr.setter
    def addr(self, value):
        self._addr.set_value(value)

    @property
    def port(self):
        return self._port.value

    @port.setter
    def port(self, value):
        self._port.set_value(value)

    @property
    def bind_addr(self):
        return self._bind_addr.value

    @bind_addr.setter
    def bind_addr(self, value):
        self._bind_addr.set_value(value)

    @property
    def bind_interface(self):
        return self._bind_interface.value

    @bind_interface.setter
    def bind_interface(self, value):
        self._bind_interface.set_value(value)

    @property
    def sctp_rto_initial(self):
        return self._sctp_rto_initial.value

    @sctp_rto_initial.setter
    def sctp_rto_initial(self, value):
        self._sctp_rto_initial.set_value(value)

    @property
    def sctp_rto_min(self):
        return self._sctp_rto_min.value

    @sctp_rto_min.setter
    def sctp_rto_min(self, value):
        self._sctp_rto_min.set_value(value)

    @property
    def sctp_rto_max(self):
        return self._sctp_rto_max.value

    @sctp_rto_max.setter
    def sctp_rto_max(self, value):
        self._sctp_rto_max.set_value(value)

    @property
    def sctp_initial_max_attempts(self):
        return self._sctp_initial_max_attempts.value

    @sctp_initial_max_attempts.setter
    def sctp_initial_max_attempts(self, value):
        self._sctp_initial_max_attempts.set_value(value)

    @property
    def sctp_max_init_timeo(self):
        return self._sctp_max_init_timeo.value

    @sctp_max_init_timeo.setter
    def sctp_max_init_timeo(self, value):
        self._sctp_max_init_timeo.set_value(value)

    @property
    def sctp_nodelay(self):
        return self._sctp_nodelay.value

    @sctp_nodelay.setter
    def sctp_nodelay(self, value):
        self._sctp_nodelay.set_value(value)

    @property
    def no_core(self):
        return self._no_core.value

    @no_core.setter
    def no_core(self, value):
        self._no_core.set_value(value)
