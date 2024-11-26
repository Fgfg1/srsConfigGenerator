from config_item import ConfigItem
from common_conf import CommonConfig

class Sib(CommonConfig):
    def __init__(self, name="SibConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.si_window_length = ConfigItem(
            key="si_window_length",
            value=160,
            comment="SI window length in milliseconds",
            used=False,
        )
        self.si_sched_info = ConfigItem(
            key="si_sched_info",
            value=None,
            comment="Scheduling information for system information (SI)",
            used=False,
        )
        self.t300 = ConfigItem(
            key="t300",
            value=1000,
            comment="T300 timer duration in milliseconds",
            used=False,
        )
        self.t301 = ConfigItem(
            key="t301",
            value=1000,
            comment="T301 timer duration in milliseconds",
            used=False,
        )
        self.t310 = ConfigItem(
            key="t310",
            value=1000,
            comment="T310 timer duration in milliseconds",
            used=False,
        )
        self.n310 = ConfigItem(
            key="n310",
            value=1,
            comment="N310 parameter indicating threshold for radio link failure",
            used=False,
        )
        self.t311 = ConfigItem(
            key="t311",
            value=3000,
            comment="T311 timer duration in milliseconds",
            used=False,
        )
        self.n311 = ConfigItem(
            key="n311",
            value=1,
            comment="N311 parameter indicating threshold for cell re-selection",
            used=False,
        )
        self.t319 = ConfigItem(
            key="t319",
            value=1000,
            comment="T319 timer duration in milliseconds",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def si_window_length(self):
        return self.si_window_length.value

    @si_window_length.setter
    def si_window_length(self, value):
        self.si_window_length.set_value(value)

    @property
    def si_sched_info(self):
        return self.si_sched_info.value

    @si_sched_info.setter
    def si_sched_info(self, value):
        self.si_sched_info.set_value(value)

    @property
    def t300(self):
        return self.t300.value

    @t300.setter
    def t300(self, value):
        self.t300.set_value(value)

    @property
    def t301(self):
        return self.t301.value

    @t301.setter
    def t301(self, value):
        self.t301.set_value(value)

    @property
    def t310(self):
        return self.t310.value

    @t310.setter
    def t310(self, value):
        self.t310.set_value(value)

    @property
    def n310(self):
        return self.n310.value

    @n310.setter
    def n310(self, value):
        self.n310.set_value(value)

    @property
    def t311(self):
        return self.t311.value

    @t311.setter
    def t311(self, value):
        self.t311.set_value(value)

    @property
    def n311(self):
        return self.n311.value

    @n311.setter
    def n311(self, value):
        self.n311.set_value(value)

    @property
    def t319(self):
        return self.t319.value

    @t319.setter
    def t319(self, value):
        self.t319.set_value(value)
