from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .tdd_ul_dl_cfg_classes.pattern2 import Pattern2

class Tdd_ul_dl_cfg(CommonConfig):
    def __init__(self, name="tdd_ul_dl_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional INT (10). Sets the TDD pattern periodicity in slots. 
        # The combination of this value and the chosen numerology must lead to a TDD periodicity of 0.5, 0.625, 1, 1.25, 2, 2.5, 3, 4, 5 or 10 milliseconds. Supported: [2 - 80].
        self._dl_ul_tx_period = ConfigItem(
            key="dl_ul_tx_period",
            value=10,
            comment="DL/UL transmission period in milliseconds",
            used=False,
        )

        # Optional INT (6). Number of consecutive full Downlink slots. Supported: [0-80].
        self._nof_dl_slots = ConfigItem(
            key="nof_dl_slots",
            value=6,
            comment="Number of downlink slots in a frame",
            used=False,
        )

        # Optional INT (8). Number of Downlink symbols at the beginning of the slot following full Downlink slots. Supported: [0-13].
        self._nof_dl_symbols = ConfigItem(
            key="nof_dl_symbols",
            value=8,
            comment="Number of downlink symbols in a slot",
            used=False,
        )

        # Optional INT (3). Number of consecutive full Uplink slots. Supported: [0 - 80].
        self._nof_ul_slots = ConfigItem(
            key="nof_ul_slots",
            value=3,
            comment="Number of uplink slots in a frame",
            used=False,
        )

        # Optional INT (0). Number of Uplink symbols at the end of the slot preceding the first full Uplink slot. Supported: [0-13].
        self._nof_ul_symbols = ConfigItem(
            key="nof_ul_symbols",
            value=0,
            comment="Number of uplink symbols in a slot",
            used=False,
        )

        # Sub-configuration
        self._pattern2 = Pattern2()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._dl_ul_tx_period,
            self._nof_dl_slots,
            self._nof_dl_symbols,
            self._nof_ul_slots,
            self._nof_ul_symbols,
            self._pattern2
        ]

    # Getters and setters for ConfigItems
    @property
    def dl_ul_tx_period(self):
        return self._dl_ul_tx_period.value

    @dl_ul_tx_period.setter
    def dl_ul_tx_period(self, value):
        self._dl_ul_tx_period.set_value(value)

    @property
    def nof_dl_slots(self):
        return self._nof_dl_slots.value

    @nof_dl_slots.setter
    def nof_dl_slots(self, value):
        self._nof_dl_slots.set_value(value)

    @property
    def nof_dl_symbols(self):
        return self._nof_dl_symbols.value

    @nof_dl_symbols.setter
    def nof_dl_symbols(self, value):
        self._nof_dl_symbols.set_value(value)

    @property
    def nof_ul_slots(self):
        return self._nof_ul_slots.value

    @nof_ul_slots.setter
    def nof_ul_slots(self, value):
        self._nof_ul_slots.set_value(value)

    @property
    def nof_ul_symbols(self):
        return self._nof_ul_symbols.value

    @nof_ul_symbols.setter
    def nof_ul_symbols(self, value):
        self._nof_ul_symbols.set_value(value)
