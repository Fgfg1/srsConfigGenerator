from config_item import ConfigItem
from common_conf import CommonConfig

class Ofh(CommonConfig):
    def __init__(self, name="OfhConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem
        self.enable_dl_parallelization = ConfigItem(
            key="enable_dl_parallelization",
            value=True,
            comment="Enable or disable downlink parallelization",
            used=False,
        )

    # Getter and setter for ConfigItem
    @property
    def enable_dl_parallelization(self):
        return self.enable_dl_parallelization.value

    @enable_dl_parallelization.setter
    def enable_dl_parallelization(self, value):
        self.enable_dl_parallelization.set_value(value)
