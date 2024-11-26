from common_conf import CommonConfig
from config_item import ConfigItem

class Phr_cfg(CommonConfig):
    def __init__(self, name="PhrConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items
        self.phr_prohibit_timer = ConfigItem(
            key="phr_prohibit_timer",
            value=10,
            comment="Sets the prohibit timer for PHR transmissions. Supported: non-negative integer.",
            used=False
        )

    # Getters and setters for ConfigItem
    @property
    def phr_prohibit_timer(self):
        """Get or set the prohibit timer for PHR transmissions."""
        return self._phr_prohibit_timer.value

    @phr_prohibit_timer.setter
    def phr_prohibit_timer(self, value):
        self._phr_prohibit_timer.value = value
