from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Fapi(CommonConfig):
    def __init__(self, name="fapi", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._l2_nof_slots_ahead = ConfigItem(
            key="l2_nof_slots_ahead",
            value=0,
            comment="Number of slots ahead for L2 processing",
            used=False,
        )

    # Getter and setter for ConfigItem l2_nof_slots_ahead
    @property
    def l2_nof_slots_ahead(self):
        return self._l2_nof_slots_ahead.value

    @l2_nof_slots_ahead.setter
    def l2_nof_slots_ahead(self, value):
        self._l2_nof_slots_ahead.set_value(value)
