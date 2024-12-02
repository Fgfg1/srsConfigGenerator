from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Pusch_dec(CommonConfig):
    def __init__(self, name="pusch_dec", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional UINT (0). Sets the number of hardware-accelerated PUSCH decoding functions. Supported: [0 - 64].
        self._nof_hwacc = ConfigItem(
            key="nof_hwacc",
            value=0,
            comment="Number of hardware accelerators",
            used=False,
        )

        # Optional BOOLEAN (true). Select if the soft-buffer is implemented in the accelerator or not. Supported: [false, true].
        self._ext_softbuffer = ConfigItem(
            key="ext_softbuffer",
            value=True,
            comment="Enable external soft buffer usage",
            used=False,
        )

        # Optional UINT. Sets the size of the HARQ context repository.
        self._harq_context_size = ConfigItem(
            key="harq_context_size",
            value=None,
            comment="Size of HARQ context, if applicable",
            used=False,
        )

        # Optional BOOLEAN (true). Selects the hardware queue used for the PUSCH decoder. true = DEDICATED, false = SHARED, Supported: [false, true].
        self._dedicated_queue = ConfigItem(
            key="dedicated_queue",
            value=True,
            comment="Enable dedicated queue for the PUSCH decoder",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._nof_hwacc,
            self._ext_softbuffer,
            self._harq_context_size,
            self._dedicated_queue
        ]

    # Getters and setters for ConfigItems
    @property
    def nof_hwacc(self):
        return self._nof_hwacc.value

    @nof_hwacc.setter
    def nof_hwacc(self, value):
        self._nof_hwacc.set_value(value)

    @property
    def ext_softbuffer(self):
        return self._ext_softbuffer.value

    @ext_softbuffer.setter
    def ext_softbuffer(self, value):
        self._ext_softbuffer.set_value(value)

    @property
    def harq_context_size(self):
        return self._harq_context_size.value

    @harq_context_size.setter
    def harq_context_size(self, value):
        self._harq_context_size.set_value(value)

    @property
    def dedicated_queue(self):
        return self._dedicated_queue.value

    @dedicated_queue.setter
    def dedicated_queue(self, value):
        self._dedicated_queue.set_value(value)
