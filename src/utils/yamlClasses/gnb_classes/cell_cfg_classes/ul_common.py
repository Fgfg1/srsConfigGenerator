from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ul_common(CommonConfig):
    def __init__(self, name="ul_common", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT. Sets maximum transmit power allowed in this serving cell. Supported: [-30 - +23].
        self._p_max = ConfigItem(
            key="p_max",
            value=None,
            comment="Maximum uplink transmission power in dBm",
            used=False,
        )

        # Optional INT (31). Sets the maximum number of PUCCH grants that can be allocated per slot. Supported: [1 - 64].
        self._max_pucchs_per_slot = ConfigItem(
            key="max_pucchs_per_slot",
            value=31,
            comment="Maximum number of PUCCHs per slot",
            used=False,
        )

        # Optional INT (32). Sets the maximum number of UL grants that can be allocated per slot. Supported: [1 - 80].
        self._max_ul_grants_per_slot = ConfigItem(
            key="max_ul_grants_per_slot",
            value=32,
            comment="Maximum number of UL grants per slot",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._p_max,
            self._max_pucchs_per_slot,
            self._max_ul_grants_per_slot
        ]

    # Getters and setters for ConfigItems
    @property
    def p_max(self):
        return self._p_max.value

    @p_max.setter
    def p_max(self, value):
        self._p_max.set_value(value)

    @property
    def max_pucchs_per_slot(self):
        return self._max_pucchs_per_slot.value

    @max_pucchs_per_slot.setter
    def max_pucchs_per_slot(self, value):
        self._max_pucchs_per_slot.set_value(value)

    @property
    def max_ul_grants_per_slot(self):
        return self._max_ul_grants_per_slot.value

    @max_ul_grants_per_slot.setter
    def max_ul_grants_per_slot(self, value):
        self._max_ul_grants_per_slot.set_value(value)
