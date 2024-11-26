from config_item import ConfigItem
from common_conf import CommonConfig

class Upf(CommonConfig):
    def __init__(self, name="UpfConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.bind_addr = ConfigItem(
            key="bind_addr",
            value="auto",
            comment="Binding address for UPF (e.g., IP address or 'auto')",
            used=False,
        )
        self.bind_interface = ConfigItem(
            key="bind_interface",
            value="auto",
            comment="Binding interface for UPF (e.g., interface name or 'auto')",
            used=False,
        )
        self.ext_addr = ConfigItem(
            key="ext_addr",
            value="auto",
            comment="External address for UPF communication",
            used=False,
        )
        self.udp_max_rx_msgs = ConfigItem(
            key="udp_max_rx_msgs",
            value=256,
            comment="Maximum number of UDP messages received in the RX queue",
            used=False,
        )
        self.pool_threshold = ConfigItem(
            key="pool_threshold",
            value=0.9,
            comment="Threshold for pool utilization (range: 0.0 to 1.0)",
            used=False,
        )
        self.no_core = ConfigItem(
            key="no_core",
            value=False,
            comment="Flag to disable core allocation for UPF",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def bind_addr(self):
        return self.bind_addr.value

    @bind_addr.setter
    def bind_addr(self, value):
        self.bind_addr.set_value(value)

    @property
    def bind_interface(self):
        return self.bind_interface.value

    @bind_interface.setter
    def bind_interface(self, value):
        self.bind_interface.set_value(value)

    @property
    def ext_addr(self):
        return self.ext_addr.value

    @ext_addr.setter
    def ext_addr(self, value):
        self.ext_addr.set_value(value)

    @property
    def udp_max_rx_msgs(self):
        return self.udp_max_rx_msgs.value

    @udp_max_rx_msgs.setter
    def udp_max_rx_msgs(self, value):
        self.udp_max_rx_msgs.set_value(value)

    @property
    def pool_threshold(self):
        return self.pool_threshold.value

    @pool_threshold.setter
    def pool_threshold(self, value):
        self.pool_threshold.set_value(value)

    @property
    def no_core(self):
        return self.no_core.value

    @no_core.setter
    def no_core(self, value):
        self.no_core.set_value(value)
