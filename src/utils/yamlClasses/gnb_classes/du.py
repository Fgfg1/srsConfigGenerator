from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Du(CommonConfig):
    def __init__(self, name="du", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem
        self._warn_on_drop = ConfigItem(
            key="warn_on_drop",
            value=False,
            comment="Issue a warning when packets are dropped",
            used=False,
        )

    # Getter and setter for ConfigItem warn_on_drop
    @property
    def warn_on_drop(self):
        return self._warn_on_drop.value

    @warn_on_drop.setter
    def warn_on_drop(self, value):
        self._warn_on_drop.set_value(value)
