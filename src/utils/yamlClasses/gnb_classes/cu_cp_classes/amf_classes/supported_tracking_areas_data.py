from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .supported_tracking_areas_classes.plmn_list import PlmnList

class Supported_tracking_areas_data(CommonConfig):
    def __init__(self, name=None, data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required UINT. Sets the Tracking Area Code.
        self._tac = ConfigItem(
            key="tac",
            value=7,
            comment="Tracking Area Code (TAC) for supported tracking areas",
            used=True,
        )

        # Sub-configuration
        self._plmn_list = PlmnList()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._tac,
            self._plmn_list
        ]

    # Getter and setter for ConfigItem
    @property
    def tac(self):
        return self._tac.value

    @tac.setter
    def tac(self, value):
        self._tac.set_value(value)

    # TODO add methods to update and add PLMN List data
