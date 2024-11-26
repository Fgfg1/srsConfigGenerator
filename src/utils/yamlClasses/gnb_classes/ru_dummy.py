from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ru_dummy(CommonConfig):
    def __init__(self, name="ru_dummy", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._dl_processing_delay = ConfigItem(
            key="dl_processing_delay",
            value=1,
            comment="DL processing delay in slots. Supported: [1 - 30]",
            used=False,
        )
        self._time_scaling = ConfigItem(
            key="time_scaling",
            value=1,
            comment="Scaling factor for time domain simulation",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def dl_processing_delay(self):
        return self._dl_processing_delay.value

    @dl_processing_delay.setter
    def dl_processing_delay(self, value):
        self._dl_processing_delay.set_value(value)

    @property
    def time_scaling(self):
        return self._time_scaling.value

    @time_scaling.setter
    def time_scaling(self, value):
        self._time_scaling.set_value(value)
