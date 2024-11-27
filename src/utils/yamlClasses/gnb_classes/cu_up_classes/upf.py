from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Upf(CommonConfig):
    def __init__(self, name="UpfConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT (auto). Sets local IP address to bind for N3 interface. Format: IPV4 or IPV6 IP address.
        self._bind_addr = ConfigItem(
            key="bind_addr",
            value="auto",
            comment="Binding address for UPF (e.g., IP address or 'auto')",
            used=False,
        )

        # Optional TEXT (auto). Sets network device to bind for N3 interface. Format: IPV4 or IPV6 IP address.
        self._bind_interface = ConfigItem(
            key="bind_interface",
            value="auto",
            comment="Binding interface for UPF (e.g., interface name or 'auto')",
            used=False,
        )

        # Optional TEXT (auto). Sets external IP address that is advertised to receive GTP-U packets from UPF via N3 interface. Format: IPV4 or IPV6 IP address.
        self._ext_addr = ConfigItem(
            key="ext_addr",
            value="auto",
            comment="External address for UPF communication",
            used=False,
        )

        # Optional INT (256). Sets the maximum amount of messages RX in a single syscall.
        self._udp_max_rx_msgs = ConfigItem(
            key="udp_max_rx_msgs",
            value=256,
            comment="Maximum number of UDP messages received in the RX queue",
            used=False,
        )

        # Optional FLOAT (0.9). Sets the pool accupancy threshold after which packets are dropped. Supported: [0.0 - 1.0].
        self._pool_threshold = ConfigItem(
            key="pool_threshold",
            value=0.9,
            comment="Threshold for pool utilization (range: 0.0 to 1.0)",
            used=False,
        )

        # Optional BOOLEAN (false). Setting to true allows the gNB to run without a core. Supported: [0, 1].
        self._no_core = ConfigItem(
            key="no_core",
            value=False,
            comment="Flag to disable core allocation for UPF",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._bind_addr,
            self._bind_interface,
            self._ext_addr,
            self._udp_max_rx_msgs,
            self._pool_threshold,
            self._no_core
        ]

    # Getters and setters for ConfigItems
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
    def ext_addr(self):
        return self._ext_addr.value

    @ext_addr.setter
    def ext_addr(self, value):
        self._ext_addr.set_value(value)

    @property
    def udp_max_rx_msgs(self):
        return self._udp_max_rx_msgs.value

    @udp_max_rx_msgs.setter
    def udp_max_rx_msgs(self, value):
        self._udp_max_rx_msgs.set_value(value)

    @property
    def pool_threshold(self):
        return self._pool_threshold.value

    @pool_threshold.setter
    def pool_threshold(self, value):
        self._pool_threshold.set_value(value)

    @property
    def no_core(self):
        return self._no_core.value

    @no_core.setter
    def no_core(self, value):
        self._no_core.set_value(value)
