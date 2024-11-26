from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Epoch_time(CommonConfig):
    def __init__(self, name="EpochTimeConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._sfn = ConfigItem(
            key="sfn",
            value=0,
            comment="System Frame Number (SFN) of the epoch time",
            used=False,
        )
        self._subframe_number = ConfigItem(
            key="subframe_number",
            value=0,
            comment="Subframe number of the epoch time",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def sfn(self):
        return self._sfn.value

    @sfn.setter
    def sfn(self, value):
        self._sfn.set_value(value)

    @property
    def subframe_number(self):
        return self._subframe_number.value

    @subframe_number.setter
    def subframe_number(self, value):
        self._subframe_number.set_value(value)
