from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .slicing_classes.sched_cfg import Sched_cfg

class Slicing(CommonConfig):
    def __init__(self, name="SlicingConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._sst = ConfigItem(
            key="sst",
            value=1,
            comment="Slice/Service Type (SST) identifier",
            used=False,
        )
        self._sd = ConfigItem(
            key="sd",
            value=0,
            comment="Slice Differentiator (SD) identifier",
            used=False,
        )

        # Sub-configuration
        self._sched_cfg = Sched_cfg()

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
