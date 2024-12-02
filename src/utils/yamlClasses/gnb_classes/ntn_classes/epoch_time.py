from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Epoch_time(CommonConfig):
    def __init__(self, name="epoch_time", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional INT (0). Sets the SFN part. Supported: [0 - 1023].
        self._sfn = ConfigItem(
            key="sfn",
            value=0,
            comment="System Frame Number (SFN) of the epoch time",
            used=False,
        )

        # Optional INT (0). Sets the sub-frame number part. Supported: [0 - 9].
        self._subframe_number = ConfigItem(
            key="subframe_number",
            value=0,
            comment="Subframe number of the epoch time",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._sfn,
            self._subframe_number
        ]

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
