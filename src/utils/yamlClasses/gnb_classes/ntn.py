from .ntn_classes.epoch_time import Epoch_time
from .ntn_classes.ephemeris_info_ecef import Ephemeris_info_ecef
from .ntn_classes.ephemeris_orbital import Ephemeris_orbital
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ntn(CommonConfig):
    def __init__(self, name="ntn", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional INT (0). Sets the cell-specific k-offset to be used for NTN. Supported: [0 - 1023].
        self._cell_specific_koffset = ConfigItem(
            key="cell_specific_koffset",
            value=0,
            comment="Cell-specific offset K for NTN timing advance",
            used=False,
        )
        # Optional UINT. Sets the TA common offset.
        self._ta_common = ConfigItem(
            key="ta_common",
            value=None,
            comment="Common timing advance parameter for NTN cells",
            used=False,
        )

        # Sub-configurations
        self._epoch_time = Epoch_time()
        self._ephemeris_info_ecef = Ephemeris_info_ecef()
        self._ephemeris_orbital = Ephemeris_orbital()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._cell_specific_koffset,
            self._ta_common,
            self._epoch_time,
            self._ephemeris_info_ecef,
            self._ephemeris_orbital
        ]

    # Getters and setters for ConfigItems
    @property
    def cell_specific_koffset(self):
        return self._cell_specific_koffset.value

    @cell_specific_koffset.setter
    def cell_specific_koffset(self, value):
        self._cell_specific_koffset.set_value(value)

    @property
    def ta_common(self):
        return self._ta_common.value

    @ta_common.setter
    def ta_common(self, value):
        self._ta_common.set_value(value)
