from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ofh(CommonConfig):
    def __init__(self, name="ofh", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem

        # Optional BOOLEAN (true). Sets the Open Fronthaul downlink parallelization flag. Supported: [false, true].
        self._enable_dl_parallelization = ConfigItem(
            key="enable_dl_parallelization",
            value=True,
            comment="Enable or disable downlink parallelization",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._enable_dl_parallelization
        ]

    # Getter and setter for ConfigItem
    @property
    def enable_dl_parallelization(self):
        return self._enable_dl_parallelization.value

    @enable_dl_parallelization.setter
    def enable_dl_parallelization(self, value):
        self._enable_dl_parallelization.set_value(value)
