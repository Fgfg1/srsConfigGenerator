from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class CellAffData(CommonConfig):
    def __init__(self, name=None, data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT. Sets the CPU core(s) assigned to L1 downlink tasks. Supported: [1, 2, 3 , ..., N]. Where N is the number of total cores available.
        self._l1_dl_cpus = ConfigItem(
            key="l1_dl_cpus",
            value=None,
            comment="List of CPUs assigned for L1 downlink processing",
            used=False,
        )

        # Optional TEXT. Sets the CPU core(s) assigned to L1 uplink tasks. Supported: [1, 2, 3 , ..., N].
        self._l1_ul_cpus = ConfigItem(
            key="l1_ul_cpus",
            value=None,
            comment="List of CPUs assigned for L1 uplink processing",
            used=False,
        )

        # Optional TEXT. Sets the policy used for assigning CPU cores to L1 downlink tasks.
        self._l1_dl_pinning = ConfigItem(
            key="l1_dl_pinning",
            value=None,
            comment="CPU pinning for L1 downlink",
            used=False,
        )

        # Optional TEXT. Sets the policy used for assigning CPU cores to L1 uplink tasks.
        self._l1_ul_pinning = ConfigItem(
            key="l1_ul_pinning",
            value=None,
            comment="CPU pinning for L1 uplink",
            used=False,
        )

        # Optional TEXT. Sets the CPU core(s) assigned to L2 cells tasks. Supported: [1, 2, 3 , ..., N].
        self._l2_cell_cpus = ConfigItem(
            key="l2_cell_cpus",
            value=None,
            comment="List of CPUs assigned for L2 cell processing",
            used=False,
        )

        # Optional TEXT. Sets the policy used for assigning CPU cores to L2 cell tasks.
        self._l2_cell_pinning = ConfigItem(
            key="l2_cell_pinning",
            value=None,
            comment="CPU pinning for L2 cell processing",
            used=False,
        )

        # Optional TEXT. Sets the CPU core(s) used for the Radio Unit tasks. Supported: [1, 2, 3 , ..., N].
        self._ru_cpus = ConfigItem(
            key="ru_cpus",
            value=None,
            comment="List of CPUs assigned for RU processing",
            used=False,
        )

        # Optional TEXT. Sets the policy used for assigning CPU cores to Radio Unity tasks.
        self._ru_pinning = ConfigItem(
            key="ru_pinning",
            value=None,
            comment="CPU pinning for RU processing",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._l1_dl_cpus,
            self._l1_ul_cpus,
            self._l1_dl_pinning,
            self._l1_ul_pinning,
            self._l2_cell_cpus,
            self._l2_cell_pinning,
            self._ru_cpus,
            self._ru_pinning
        ]

    # Getters and setters for ConfigItems
    @property
    def l1_dl_cpus(self):
        return self._l1_dl_cpus.value

    @l1_dl_cpus.setter
    def l1_dl_cpus(self, value):
        self._l1_dl_cpus.set_value(value)

    @property
    def l1_ul_cpus(self):
        return self._l1_ul_cpus.value

    @l1_ul_cpus.setter
    def l1_ul_cpus(self, value):
        self._l1_ul_cpus.set_value(value)

    @property
    def l1_dl_pinning(self):
        return self._l1_dl_pinning.value

    @l1_dl_pinning.setter
    def l1_dl_pinning(self, value):
        self._l1_dl_pinning.set_value(value)

    @property
    def l1_ul_pinning(self):
        return self._l1_ul_pinning.value

    @l1_ul_pinning.setter
    def l1_ul_pinning(self, value):
        self._l1_ul_pinning.set_value(value)

    @property
    def l2_cell_cpus(self):
        return self._l2_cell_cpus.value

    @l2_cell_cpus.setter
    def l2_cell_cpus(self, value):
        self._l2_cell_cpus.set_value(value)

    @property
    def l2_cell_pinning(self):
        return self._l2_cell_pinning.value

    @l2_cell_pinning.setter
    def l2_cell_pinning(self, value):
        self._l2_cell_pinning.set_value(value)

    @property
    def ru_cpus(self):
        return self._ru_cpus.value

    @ru_cpus.setter
    def ru_cpus(self, value):
        self._ru_cpus.set_value(value)

    @property
    def ru_pinning(self):
        return self._ru_pinning.value

    @ru_pinning.setter
    def ru_pinning(self, value):
        self._ru_pinning.set_value(value)
