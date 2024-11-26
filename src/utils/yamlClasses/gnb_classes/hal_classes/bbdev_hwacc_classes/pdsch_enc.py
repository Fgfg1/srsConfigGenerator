from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Pdsch_enc(CommonConfig):
    def __init__(self, name="PdschEncConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._nof_hwacc = ConfigItem(
            key="nof_hwacc",
            value=0,
            comment="Number of hardware accelerators for PDSCH encoding",
            used=False,
        )
        self._cb_mode = ConfigItem(
            key="cb_mode",
            value=False,
            comment="Enable/Disable CB mode for PDSCH encoding",
            used=False,
        )
        self._max_buffer_size = ConfigItem(
            key="max_buffer_size",
            value=None,
            comment="Maximum buffer size for encoding",
            used=False,
        )
        self._dedicated_queue = ConfigItem(
            key="dedicated_queue",
            value=True,
            comment="Enable dedicated queue for PDSCH encoding",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def nof_hwacc(self):
        return self._nof_hwacc.value

    @nof_hwacc.setter
    def nof_hwacc(self, value):
        self._nof_hwacc.set_value(value)

    @property
    def cb_mode(self):
        return self._cb_mode.value

    @cb_mode.setter
    def cb_mode(self, value):
        self._cb_mode.set_value(value)

    @property
    def max_buffer_size(self):
        return self._max_buffer_size.value

    @max_buffer_size.setter
    def max_buffer_size(self, value):
        self._max_buffer_size.set_value(value)

    @property
    def dedicated_queue(self):
        return self._dedicated_queue.value

    @dedicated_queue.setter
    def dedicated_queue(self, value):
        self._dedicated_queue.set_value(value)
