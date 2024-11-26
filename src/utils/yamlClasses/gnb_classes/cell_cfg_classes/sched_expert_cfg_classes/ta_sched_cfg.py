from common_conf import CommonConfig
from config_item import ConfigItem

class Ta_sched_cfg(CommonConfig):
    def __init__(self, name="TaSchedConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items for Ta_sched_cfg
        self.ta_measurement_slot_period = ConfigItem(
            key="ta_measurement_slot_period",
            value=80,
            comment="Sets the slot period for TA measurements. Supported: [10, 20, 40, 80, 160].",
            used=False
        )
        self.ta_cmd_offset_threshold = ConfigItem(
            key="ta_cmd_offset_threshold",
            value=1,
            comment="Sets the offset threshold for triggering a TA command. Supported: non-negative integer.",
            used=False
        )
        self.ta_update_measurement_ul_sinr_threshold = ConfigItem(
            key="ta_update_measurement_ul_sinr_threshold",
            value=0,
            comment="Sets the UL SINR threshold for TA update measurements. Supported: non-negative integer.",
            used=False
        )

    # Getters and setters for ConfigItem
    @property
    def ta_measurement_slot_period(self):
        """Get or set the slot period for TA measurements."""
        return self.ta_measurement_slot_period.value

    @ta_measurement_slot_period.setter
    def ta_measurement_slot_period(self, value):
        self.ta_measurement_slot_period.value = value

    @property
    def ta_cmd_offset_threshold(self):
        """Get or set the offset threshold for triggering a TA command."""
        return self.ta_cmd_offset_threshold.value

    @ta_cmd_offset_threshold.setter
    def ta_cmd_offset_threshold(self, value):
        self.ta_cmd_offset_threshold.value = value

    @property
    def ta_update_measurement_ul_sinr_threshold(self):
        """Get or set the UL SINR threshold for TA update measurements."""
        return self.ta_update_measurement_ul_sinr_threshold.value

    @ta_update_measurement_ul_sinr_threshold.setter
    def ta_update_measurement_ul_sinr_threshold(self, value):
        self.ta_update_measurement_ul_sinr_threshold.value = value
