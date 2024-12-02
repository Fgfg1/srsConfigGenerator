from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

# Power Headroom report configuration parameters

class Phr_cfg(CommonConfig):
    def __init__(self, name="phr_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items

        # Optional UINT (10). Sets the PHR prohibit timer in nof. subframes. Supported: [0, 10, 20, 50, 100, 200, 500, 1000].
        self._phr_prohibit_timer = ConfigItem(
            key="phr_prohibit_timer",
            value=10,
            comment="Sets the prohibit timer for PHR transmissions. Supported: non-negative integer.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._phr_prohibit_timer
        ]

    # Getters and setters for ConfigItem
    @property
    def phr_prohibit_timer(self):
        """Get or set the prohibit timer for PHR transmissions."""
        return self.__phr_prohibit_timer.value

    @phr_prohibit_timer.setter
    def phr_prohibit_timer(self, value):
        self.__phr_prohibit_timer.value = value
