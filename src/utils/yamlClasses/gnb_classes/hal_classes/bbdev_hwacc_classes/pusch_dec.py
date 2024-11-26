from config_item import ConfigItem
from common_conf import CommonConfig

class Pusch_dec(CommonConfig):
    def __init__(self, name="PuschDecConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.nof_hwacc = ConfigItem(
            key="nof_hwacc",
            value=0,
            comment="Number of hardware accelerators",
            used=False,
        )
        self.ext_softbuffer = ConfigItem(
            key="ext_softbuffer",
            value=True,
            comment="Enable external soft buffer usage",
            used=False,
        )
        self.harq_context_size = ConfigItem(
            key="harq_context_size",
            value=None,
            comment="Size of HARQ context, if applicable",
            used=False,
        )
        self.dedicated_queue = ConfigItem(
            key="dedicated_queue",
            value=True,
            comment="Enable dedicated queue for the PUSCH decoder",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def nof_hwacc(self):
        return self.nof_hwacc.value

    @nof_hwacc.setter
    def nof_hwacc(self, value):
        self.nof_hwacc.set_value(value)

    @property
    def ext_softbuffer(self):
        return self.ext_softbuffer.value

    @ext_softbuffer.setter
    def ext_softbuffer(self, value):
        self.ext_softbuffer.set_value(value)

    @property
    def harq_context_size(self):
        return self.harq_context_size.value

    @harq_context_size.setter
    def harq_context_size(self, value):
        self.harq_context_size.set_value(value)

    @property
    def dedicated_queue(self):
        return self.dedicated_queue.value

    @dedicated_queue.setter
    def dedicated_queue(self, value):
        self.dedicated_queue.set_value(value)
