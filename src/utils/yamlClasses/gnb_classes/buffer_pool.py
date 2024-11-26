from config_item import ConfigItem
from common_conf import CommonConfig

class Buffer_pool(CommonConfig):
    def __init__(self, name="BufferPoolConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.nof_segments = ConfigItem(
            key="nof_segments",
            value=1048576,
            comment="Number of buffer segments",
            used=False,
        )
        self.segment_size = ConfigItem(
            key="segment_size",
            value=2048,
            comment="Size of each buffer segment in bytes",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def nof_segments(self):
        return self.nof_segments.value

    @nof_segments.setter
    def nof_segments(self, value):
        self.nof_segments.set_value(value)

    @property
    def segment_size(self):
        return self.segment_size.value

    @segment_size.setter
    def segment_size(self, value):
        self.segment_size.set_value(value)
