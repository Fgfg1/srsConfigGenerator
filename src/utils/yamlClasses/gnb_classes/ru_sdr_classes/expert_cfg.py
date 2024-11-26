from config_item import ConfigItem
from common_conf import CommonConfig

class Expert_cfg(CommonConfig):
    def __init__(self, name="ExpertCfgConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.low_phy_dl_throttling = ConfigItem(
            key="low_phy_dl_throttling",
            value=0,
            comment="Low PHY downlink throttling level",
            used=False,
        )
        self.tx_mode = ConfigItem(
            key="tx_mode",
            value="continuous",
            comment="Transmission mode (e.g., continuous, burst)",
            used=False,
        )
        self.power_ramping_time_us = ConfigItem(
            key="power_ramping_time_us",
            value=0,
            comment="Power ramping time in microseconds",
            used=False,
        )
        self.dl_buffer_size_policy = ConfigItem(
            key="dl_buffer_size_policy",
            value="auto",
            comment="Policy for downlink buffer size management",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def low_phy_dl_throttling(self):
        return self.low_phy_dl_throttling.value

    @low_phy_dl_throttling.setter
    def low_phy_dl_throttling(self, value):
        self.low_phy_dl_throttling.set_value(value)

    @property
    def tx_mode(self):
        return self.tx_mode.value

    @tx_mode.setter
    def tx_mode(self, value):
        self.tx_mode.set_value(value)

    @property
    def power_ramping_time_us(self):
        return self.power_ramping_time_us.value

    @power_ramping_time_us.setter
    def power_ramping_time_us(self, value):
        self.power_ramping_time_us.set_value(value)

    @property
    def dl_buffer_size_policy(self):
        return self.dl_buffer_size_policy.value

    @dl_buffer_size_policy.setter
    def dl_buffer_size_policy(self, value):
        self.dl_buffer_size_policy.set_value(value)
