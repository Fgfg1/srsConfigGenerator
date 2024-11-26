from config_item import ConfigItem
from common_conf import CommonConfig

class Ul_common(CommonConfig):
    def __init__(self, name="UlCommonConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.p_max = ConfigItem(
            key="p_max",
            value=None,
            comment="Maximum uplink transmission power in dBm",
            used=False,
        )
        self.max_pucchs_per_slot = ConfigItem(
            key="max_pucchs_per_slot",
            value=31,
            comment="Maximum number of PUCCHs per slot",
            used=False,
        )
        self.max_ul_grants_per_slot = ConfigItem(
            key="max_ul_grants_per_slot",
            value=32,
            comment="Maximum number of UL grants per slot",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def p_max(self):
        return self.p_max.value

    @p_max.setter
    def p_max(self, value):
        self.p_max.set_value(value)

    @property
    def max_pucchs_per_slot(self):
        return self.max_pucchs_per_slot.value

    @max_pucchs_per_slot.setter
    def max_pucchs_per_slot(self, value):
        self.max_pucchs_per_slot.set_value(value)

    @property
    def max_ul_grants_per_slot(self):
        return self.max_ul_grants_per_slot.value

    @max_ul_grants_per_slot.setter
    def max_ul_grants_per_slot(self, value):
        self.max_ul_grants_per_slot.set_value(value)
