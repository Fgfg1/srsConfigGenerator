from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .plmn_list_classes.tai_slice_support_list import Tai_slice_support_list

class PlmnListData(CommonConfig):
    def __init__(self, name=None, data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required TEXT. Sets the Public Land Mobile Network code. Format: 7-digit PLMN code containing MCC & MNC.
        self._plmn = ConfigItem(
            key="plmn",
            value="00101",
            comment="Public Land Mobile Network (PLMN) identifier",
            used=True,
        )

        # Sub-configuration
        self._tai_slice_support_list = Tai_slice_support_list()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._plmn,
            self._tai_slice_support_list
        ]

    # Getter and setter for ConfigItem
    @property
    def plmn(self):
        return self._plmn.value

    @plmn.setter
    def plmn(self, value):
        self._plmn.set_value(value)

# TODO add methods to update create and manage tai slice support list