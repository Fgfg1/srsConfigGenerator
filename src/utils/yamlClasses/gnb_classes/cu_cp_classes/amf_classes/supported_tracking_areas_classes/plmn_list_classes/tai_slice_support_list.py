from config_item import ConfigItem
from common_conf import CommonConfig

class Tai_slice_support_list(CommonConfig):
    def __init__(self, name="TaiSliceSupportListConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.sst = ConfigItem(
            key="sst",
            value=1,
            comment="Slice/Service Type (SST) identifier for the slice support",
            used=False,
        )
        self.sd = ConfigItem(
            key="sd",
            value=None,
            comment="Slice Differentiator (SD) identifier for the slice support",
            used=False,
        )

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
