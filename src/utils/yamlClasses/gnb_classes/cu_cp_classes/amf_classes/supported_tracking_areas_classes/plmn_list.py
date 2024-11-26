from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .plmn_list_classes.tai_slice_support_list import Tai_slice_support_list

class Plmn_list(CommonConfig):
    def __init__(self, name="PlmnListConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._plmn = ConfigItem(
            key="plmn",
            value="00101",
            comment="Public Land Mobile Network (PLMN) identifier",
            used=False,
        )

        # Sub-configuration
        self._tai_slice_support_list = Tai_slice_support_list()

    # Getter and setter for ConfigItem
    @property
    def plmn(self):
        return self._plmn.value

    @plmn.setter
    def plmn(self, value):
        self._plmn.set_value(value)
