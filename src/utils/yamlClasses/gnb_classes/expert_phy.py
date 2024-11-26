from config_item import ConfigItem
from common_conf import CommonConfig

class Expert_phy(CommonConfig):
    def __init__(self, name="ExpertPhyConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.max_proc_delay = ConfigItem(
            key="max_proc_delay",
            value=5,
            comment="Maximum allowed processing delay in slots",
            used=False,
        )
        self.pusch_dec_max_iterations = ConfigItem(
            key="pusch_dec_max_iterations",
            value=6,
            comment="Maximum number of iterations for PUSCH decoding",
            used=False,
        )
        self.pusch_dec_enable_early_stop = ConfigItem(
            key="pusch_dec_enable_early_stop",
            value=True,
            comment="Enable early stopping for PUSCH decoder",
            used=False,
        )
        self.pusch_sinr_calc_method = ConfigItem(
            key="pusch_sinr_calc_method",
            value="post_equalization",
            comment="Method used for calculating PUSCH SINR",
            used=False,
        )
        self.max_request_headroom_slots = ConfigItem(
            key="max_request_headroom_slots",
            value=0,
            comment="Maximum number of slots for request headroom",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def max_proc_delay(self):
        return self.max_proc_delay.value

    @max_proc_delay.setter
    def max_proc_delay(self, value):
        self.max_proc_delay.set_value(value)

    @property
    def pusch_dec_max_iterations(self):
        return self.pusch_dec_max_iterations.value

    @pusch_dec_max_iterations.setter
    def pusch_dec_max_iterations(self, value):
        self.pusch_dec_max_iterations.set_value(value)

    @property
    def pusch_dec_enable_early_stop(self):
        return self.pusch_dec_enable_early_stop.value

    @pusch_dec_enable_early_stop.setter
    def pusch_dec_enable_early_stop(self, value):
        self.pusch_dec_enable_early_stop.set_value(value)

    @property
    def pusch_sinr_calc_method(self):
        return self.pusch_sinr_calc_method.value

    @pusch_sinr_calc_method.setter
    def pusch_sinr_calc_method(self, value):
        self.pusch_sinr_calc_method.set_value(value)

    @property
    def max_request_headroom_slots(self):
        return self.max_request_headroom_slots.value

    @max_request_headroom_slots.setter
    def max_request_headroom_slots(self, value):
        self.max_request_headroom_slots.set_value(value)
