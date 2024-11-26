from .hal_classes.bbdev_hwacc import Bbdev_hwacc
from config_item import ConfigItem
from common_conf import CommonConfig

class Hal(CommonConfig):
    def __init__(self, name="HalConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.eal_args = ConfigItem(
            key="eal_args",
            value=None,
            comment="EAL arguments for HAL configuration",
            used=False,
        )

        # Sub-configuration
        self.bbdev_hwacc = Bbdev_hwacc()

    # Getter and setter for ConfigItem eal_args
    @property
    def eal_args(self):
        return self.eal_args.value

    @eal_args.setter
    def eal_args(self, value):
        self.eal_args.set_value(value)
