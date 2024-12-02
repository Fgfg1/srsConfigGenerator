from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Sib(CommonConfig):
    def __init__(self, name="sib", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional UINT (160). Sets the length of the SI scheduling window, in slots. It must be always shorter or equal to the period of the SI message. 
        # Supported: [5,10,20,40,80,160,320,640,1280].
        self._si_window_length = ConfigItem(
            key="si_window_length",
            value=160,
            comment="SI window length in milliseconds",
            used=False,
        )

        # Optional TEXT. Configures the scheduling for each of the SI-messages broadcast by the gNB.
        self._si_sched_info = ConfigItem(
            key="si_sched_info",
            value=None,
            comment="Scheduling information for system information (SI)",
            used=False,
        )

        # Optional UINT (1000). Sets the RRC Connection Establishment timer in ms. The timer starts upon transmission of RRCSetupRequest. 
        # Supported: [100,200,300,400,600,1000,1500,2000].
        self._t300 = ConfigItem(
            key="t300",
            value=1000,
            comment="T300 timer duration in milliseconds",
            used=False,
        )

        # Optional UINT (1000). Sets the RRC Connection Re-establishment timer in ms. The timer starts upon transmission of RRCReestablishmentRequest. 
        # Supported: [100,200,300,400,600,1000,1500,2000].
        self._t301 = ConfigItem(
            key="t301",
            value=1000,
            comment="T301 timer duration in milliseconds",
            used=False,
        )

        # Optional UINT (1000). Sets the Out-of-sync timer in ms. The timer starts upon detecting physical layer problems for the SpCell i.e. upon receiving N310 consecutive out-of-sync indications from lower layers. 
        # Supported: [0,50,100,200,500,1000,2000].
        self._t310 = ConfigItem(
            key="t310",
            value=1000,
            comment="T310 timer duration in milliseconds",
            used=False,
        )

        # Optional UINT (1). Sets the Out-of-sync counter. The counter is increased upon reception of "out-of-sync" from lower layer while the timer T310 is stopped. Starts the timer T310, when configured value is reached. 
        # Supported: [1,2,3,4,6,8,10,20].
        self._n310 = ConfigItem(
            key="n310",
            value=1,
            comment="N310 parameter indicating threshold for radio link failure",
            used=False,
        )

        # Optional UINT (3000). Sets the RRC Connection Re-establishment procedure timer in ms. The timer starts upon initiating the RRC connection re-establishment procedure. Supported: [1000,3000,5000,10000,15000,20000,30000].
        self._t311 = ConfigItem(
            key="t311",
            value=3000,
            comment="T311 timer duration in milliseconds",
            used=False,
        )

        # Optional UINT (1). Sets the In-sync counter. The counter is increased upon reception of the "in-sync" from lower layer while the timer T310 is running. Stops the timer T310, when configured value is reached.Supported: [1,2,3,4,5,6,8,10].
        self._n311 = ConfigItem(
            key="n311",
            value=1,
            comment="N311 parameter indicating threshold for cell re-selection",
            used=False,
        )

        # Optional UINT (1000). Sets the RRC Connection Resume timer in ms. The timer starts upon transmission of RRCResumeRequest or RRCResumeRequest1. Supported: [100,200,300,400,600,1000,1500,2000].
        self._t319 = ConfigItem(
            key="t319",
            value=1000,
            comment="T319 timer duration in milliseconds",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._si_window_length,
            self._si_sched_info,
            self._t300,
            self._t301,
            self._t310,
            self._n310,
            self._t311,
            self._n311,
            self._t319
        ]

    # Getters and setters for ConfigItems
    @property
    def si_window_length(self):
        return self._si_window_length.value

    @si_window_length.setter
    def si_window_length(self, value):
        self._si_window_length.set_value(value)

    @property
    def si_sched_info(self):
        return self._si_sched_info.value

    @si_sched_info.setter
    def si_sched_info(self, value):
        self._si_sched_info.set_value(value)

    @property
    def t300(self):
        return self._t300.value

    @t300.setter
    def t300(self, value):
        self._t300.set_value(value)

    @property
    def t301(self):
        return self._t301.value

    @t301.setter
    def t301(self, value):
        self._t301.set_value(value)

    @property
    def t310(self):
        return self._t310.value

    @t310.setter
    def t310(self, value):
        self._t310.set_value(value)

    @property
    def n310(self):
        return self._n310.value

    @n310.setter
    def n310(self, value):
        self._n310.set_value(value)

    @property
    def t311(self):
        return self._t311.value

    @t311.setter
    def t311(self, value):
        self._t311.set_value(value)

    @property
    def n311(self):
        return self._n311.value

    @n311.setter
    def n311(self, value):
        self._n311.set_value(value)

    @property
    def t319(self):
        return self._t319.value

    @t319.setter
    def t319(self, value):
        self._t319.set_value(value)
