from config_item import ConfigItem
from common_conf import CommonConfig
from .supported_tracking_areas_classes.plmn_list import Plmn_list

class Supported_tracking_areas(CommonConfig):
    def __init__(self, name="SupportedTrackingAreasConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.tac = ConfigItem(
            key="tac",
            value=7,
            comment="Tracking Area Code (TAC) for supported tracking areas",
            used=False,
        )

        # Sub-configuration
        self.plmn_list = Plmn_list()

    # Getter and setter for ConfigItem
    @property
    def tac(self):
        return self.tac.value

    @tac.setter
    def tac(self, value):
        self.tac.set_value(value)