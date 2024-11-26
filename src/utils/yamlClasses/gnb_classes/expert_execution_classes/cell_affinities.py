from config_item import ConfigItem
from common_conf import CommonConfig

class Cell_affinities(CommonConfig):
    def __init__(self, name="CellAffinitiesConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.l1_dl_cpus = ConfigItem(
            key="l1_dl_cpus",
            value=None,
            comment="List of CPUs assigned for L1 downlink processing",
            used=False,
        )
        self.l1_ul_cpus = ConfigItem(
            key="l1_ul_cpus",
            value=None,
            comment="List of CPUs assigned for L1 uplink processing",
            used=False,
        )
        self.l1_dl_pinning = ConfigItem(
            key="l1_dl_pinning",
            value=None,
            comment="CPU pinning for L1 downlink",
            used=False,
        )
        self.l1_ul_pinning = ConfigItem(
            key="l1_ul_pinning",
            value=None,
            comment="CPU pinning for L1 uplink",
            used=False,
        )
        self.l2_cell_cpus = ConfigItem(
            key="l2_cell_cpus",
            value=None,
            comment="List of CPUs assigned for L2 cell processing",
            used=False,
        )
        self.l2_cell_pinning = ConfigItem(
            key="l2_cell_pinning",
            value=None,
            comment="CPU pinning for L2 cell processing",
            used=False,
        )
        self.ru_cpus = ConfigItem(
            key="ru_cpus",
            value=None,
            comment="List of CPUs assigned for RU processing",
            used=False,
        )
        self.ru_pinning = ConfigItem(
            key="ru_pinning",
            value=None,
            comment="CPU pinning for RU processing",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def l1_dl_cpus(self):
        return self.l1_dl_cpus.value

    @l1_dl_cpus.setter
    def l1_dl_cpus(self, value):
        self.l1_dl_cpus.set_value(value)

    @property
    def l1_ul_cpus(self):
        return self.l1_ul_cpus.value

    @l1_ul_cpus.setter
    def l1_ul_cpus(self, value):
        self.l1_ul_cpus.set_value(value)

    @property
    def l1_dl_pinning(self):
        return self.l1_dl_pinning.value

    @l1_dl_pinning.setter
    def l1_dl_pinning(self, value):
        self.l1_dl_pinning.set_value(value)

    @property
    def l1_ul_pinning(self):
        return self.l1_ul_pinning.value

    @l1_ul_pinning.setter
    def l1_ul_pinning(self, value):
        self.l1_ul_pinning.set_value(value)

    @property
    def l2_cell_cpus(self):
        return self.l2_cell_cpus.value

    @l2_cell_cpus.setter
    def l2_cell_cpus(self, value):
        self.l2_cell_cpus.set_value(value)

    @property
    def l2_cell_pinning(self):
        return self.l2_cell_pinning.value

    @l2_cell_pinning.setter
    def l2_cell_pinning(self, value):
        self.l2_cell_pinning.set_value(value)

    @property
    def ru_cpus(self):
        return self.ru_cpus.value

    @ru_cpus.setter
    def ru_cpus(self, value):
        self.ru_cpus.set_value(value)

    @property
    def ru_pinning(self):
        return self.ru_pinning.value

    @ru_pinning.setter
    def ru_pinning(self, value):
        self.ru_pinning.set_value(value)
