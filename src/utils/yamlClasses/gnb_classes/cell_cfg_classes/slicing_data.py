from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .slicing_classes.sched_cfg import Sched_cfg

class SlicingData(CommonConfig):
    def __init__(self, name=None, data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional UINT (1). Sets the Slice Service Type. Supported: [0 - 255].
        self._sst = ConfigItem(
            key="sst",
            value=1,
            comment="Slice/Service Type (SST) identifier",
            used=False,
        )

        # Optional UINT (0). Sets the Service Differentiator. Supported: [0-16777215].
        self._sd = ConfigItem(
            key="sd",
            value=0,
            comment="Slice Differentiator (SD) identifier",
            used=False,
        )

        # Sub-module
        # Scheduler configuration for the slice
        self._sched_cfg = Sched_cfg()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._sst,
            self._sd,
            self._sched_cfg
        ]

    # Getters and setters for ConfigItems
    @property
    def sst(self):
        return self._sst.value

    @sst.setter
    def sst(self, value):
        self._sst.set_value(value)

    @property
    def sd(self):
        return self._sd.value

    @sd.setter
    def sd(self, value):
        self._sd.set_value(value)
