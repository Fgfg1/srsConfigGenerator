from .hal_classes.bbdev_hwacc import Bbdev_hwacc
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Hal(CommonConfig):
    def __init__(self, name="hal", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT. EAL configuration parameters used to initialize DPDK.
        self._eal_args = ConfigItem(
            key="eal_args",
            value=None,
            comment="EAL arguments for HAL configuration",
            used=False,
        )

        # Sub-module
        self._bbdev_hwacc = Bbdev_hwacc()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._eal_args,
            self._bbdev_hwacc
        ]

    # Getter and setter for ConfigItem eal_args
    @property
    def eal_args(self):
        return self._eal_args.value

    @eal_args.setter
    def eal_args(self, value):
        self._eal_args.set_value(value)
