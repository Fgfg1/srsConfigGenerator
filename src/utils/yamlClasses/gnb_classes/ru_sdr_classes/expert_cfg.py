from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Expert_cfg(CommonConfig):
    def __init__(self, name="expert_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional FLOAT (0). Throttles the lower PHY DL baseband generation. Setting to 0 disables throttling. Supported: any value in the range [0 - 1].
        self._low_phy_dl_throttling = ConfigItem(
            key="low_phy_dl_throttling",
            value=0,
            comment="Low PHY downlink throttling level",
            used=False,
        )

        # Optional TEXT (continuous). Selects a radio transmission mode. Discontinuous modes are not supported by all radios. Supported: [continuous, discontinuous, same-port]
        self._tx_mode = ConfigItem(
            key="tx_mode",
            value="continuous",
            comment="Transmission mode (e.g., continuous, burst)",
            used=False,
        )

        # Optional FLOAT (0). Specifies the power ramping time in microseconds, it proactively initiates the transmission and mitigates transient effects. 
        # It is recommended to configure this parameter carefully, taking into account the characteristics of the transmit chain in order to achieve optimal performance
        self._power_ramping_time_us = ConfigItem(
            key="power_ramping_time_us",
            value=0,
            comment="Power ramping time in microseconds",
            used=False,
        )

        # Optional TEXT (auto). Sets the size of the policy of the baseband buffers that pass the DL samples from the lower PHY to the radio.
        self._dl_buffer_size_policy = ConfigItem(
            key="dl_buffer_size_policy",
            value="auto",
            comment="Policy for downlink buffer size management",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._low_phy_dl_throttling,
            self._tx_mode,
            self._power_ramping_time_us,
            self._dl_buffer_size_policy
        ]

    # Getters and setters for ConfigItems
    @property
    def low_phy_dl_throttling(self):
        return self._low_phy_dl_throttling.value

    @low_phy_dl_throttling.setter
    def low_phy_dl_throttling(self, value):
        self._low_phy_dl_throttling.set_value(value)

    @property
    def tx_mode(self):
        return self._tx_mode.value

    @tx_mode.setter
    def tx_mode(self, value):
        self._tx_mode.set_value(value)

    @property
    def power_ramping_time_us(self):
        return self._power_ramping_time_us.value

    @power_ramping_time_us.setter
    def power_ramping_time_us(self, value):
        self._power_ramping_time_us.set_value(value)

    @property
    def dl_buffer_size_policy(self):
        return self._dl_buffer_size_policy.value

    @dl_buffer_size_policy.setter
    def dl_buffer_size_policy(self, value):
        self._dl_buffer_size_policy.set_value(value)
