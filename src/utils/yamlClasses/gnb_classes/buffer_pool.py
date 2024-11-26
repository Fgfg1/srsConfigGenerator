from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Buffer_pool(CommonConfig):
    def __init__(self, name="buffer_pool", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._nof_segments = ConfigItem(
            key="nof_segments",
            value=1048576,
            comment="Number of buffer segments",
            used=False,
        )
        self._segment_size = ConfigItem(
            key="segment_size",
            value=2048,
            comment="Size of each buffer segment in bytes",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def nof_segments(self):
        return self._nof_segments.value

    @nof_segments.setter
    def nof_segments(self, value):
        self._nof_segments.set_value(value)

    @property
    def segment_size(self):
        return self._segment_size.value

    @segment_size.setter
    def segment_size(self, value):
        self._segment_size.set_value(value)
