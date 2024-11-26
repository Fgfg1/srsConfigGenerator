from .hal_classes.bbdev_hwacc import Bbdev_hwacc
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Hal(CommonConfig):
    def __init__(self, name="hal", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._eal_args = ConfigItem(
            key="eal_args",
            value=None,
            comment="EAL arguments for HAL configuration",
            used=False,
        )

        # Sub-configuration
        self._bbdev_hwacc = Bbdev_hwacc()

    # Getter and setter for ConfigItem eal_args
    @property
    def eal_args(self):
        return self._eal_args.value

    @eal_args.setter
    def eal_args(self, value):
        self._eal_args.set_value(value)
