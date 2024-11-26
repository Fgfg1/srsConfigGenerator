from config_item import ConfigItem
from common_conf import CommonConfig
from .slicing_classes.sched_cfg import Sched_cfg

class Slicing(CommonConfig):
    def __init__(self, name="SlicingConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.sst = ConfigItem(
            key="sst",
            value=1,
            comment="Slice/Service Type (SST) identifier",
            used=False,
        )
        self.sd = ConfigItem(
            key="sd",
            value=0,
            comment="Slice Differentiator (SD) identifier",
            used=False,
        )

        # Sub-configuration
        self.sched_cfg = Sched_cfg()

    # Getters and setters for ConfigItems
    @property
    def sst(self):
        return self.sst.value

    @sst.setter
    def sst(self, value):
        self.sst.set_value(value)

    @property
    def sd(self):
        return self.sd.value

    @sd.setter
    def sd(self, value):
        self.sd.set_value(value)
