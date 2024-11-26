from .ntn_classes.epoch_time import Epoch_time
from .ntn_classes.ephemeris_info_ecef import Ephemeris_info_ecef
from .ntn_classes.ephemeris_orbital import Ephemeris_orbital
from config_item import ConfigItem
from common_conf import CommonConfig

class Ntn(CommonConfig):
    def __init__(self, name="NtnConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.cell_specific_koffset = ConfigItem(
            key="cell_specific_koffset",
            value=0,
            comment="Cell-specific offset K for NTN timing advance",
            used=False,
        )
        self.ta_common = ConfigItem(
            key="ta_common",
            value=None,
            comment="Common timing advance parameter for NTN cells",
            used=False,
        )

        # Sub-configurations
        self.epoch_time = Epoch_time()
        self.ephemeris_info_ecef = Ephemeris_info_ecef()
        self.ephemeris_orbital = Ephemeris_orbital()

    # Getters and setters for ConfigItems
    @property
    def cell_specific_koffset(self):
        return self.cell_specific_koffset.value

    @cell_specific_koffset.setter
    def cell_specific_koffset(self, value):
        self.cell_specific_koffset.set_value(value)

    @property
    def ta_common(self):
        return self.ta_common.value

    @ta_common.setter
    def ta_common(self, value):
        self.ta_common.set_value(value)
