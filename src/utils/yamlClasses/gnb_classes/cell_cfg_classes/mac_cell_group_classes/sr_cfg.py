from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem


# Scheduling Request configuration parameters

class Sr_cfg(CommonConfig):
    def __init__(self, name="sr_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items

        # Optional UINT (64). Sets the maximum number of SR transmissions. Supported: [4, 8, 16, 32, 64].
        self._sr_trans_max = ConfigItem(
            key="sr_trans_max",
            value=64,
            comment="Maximum number of SR transmissions. Supported: [1, 2, 4, 8, 16, 32, 64].",
            used=False
        )

        # Optional TEXT. Sets the timer for SR transmission on PUCCH in ms. Supported: [1, 2, 4, 8, 16, 32, 64, 128].
        self._sr_prohibit_timer = ConfigItem(
            key="sr_prohibit_timer",
            value=None,
            comment="Timer to prohibit SR transmissions after a failed attempt. Supported: non-negative integer or None.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._sr_trans_max,
            self._sr_prohibit_timer
        ]

    # Getters and setters for ConfigItems
    @property
    def sr_trans_max(self):
        """Get or set the maximum number of SR transmissions."""
        return self.__sr_trans_max.value

    @sr_trans_max.setter
    def sr_trans_max(self, value):
        self.__sr_trans_max.value = value

    @property
    def sr_prohibit_timer(self):
        """Get or set the SR prohibit timer."""
        return self.__sr_prohibit_timer.value

    @sr_prohibit_timer.setter
    def sr_prohibit_timer(self, value):
        self.__sr_prohibit_timer.value = value
