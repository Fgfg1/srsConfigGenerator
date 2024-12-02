from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Ta_sched_cfg(CommonConfig):
    def __init__(self, name="ta_sched_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items for Ta_sched_cfg

        # Optional UINT (80). Sets the measurements periodicity in nof. slots over which the new Timing Advance Command is computed.
        self._ta_measurement_slot_period = ConfigItem(
            key="ta_measurement_slot_period",
            value=80,
            comment="Sets the slot period for TA measurements. Supported: [10, 20, 40, 80, 160].",
            used=False
        )

        # Optional INT (1). Sets the timing Advance Command (T_A) offset threshold above which Timing Advance Command is triggered. If set to less than zero, issuing of TA Command is disabled. Supported: [-1 - 31].
        self._ta_cmd_offset_threshold = ConfigItem(
            key="ta_cmd_offset_threshold",
            value=1,
            comment="Sets the offset threshold for triggering a TA command. Supported: non-negative integer.",
            used=False
        )

        # Optional FLOAT (0). Sets the UL SINR threshold (in dB) above which reported N_TA update measurement is considered valid.
        self._ta_update_measurement_ul_sinr_threshold = ConfigItem(
            key="ta_update_measurement_ul_sinr_threshold",
            value=0,
            comment="Sets the UL SINR threshold for TA update measurements. Supported: non-negative integer.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._ta_measurement_slot_period,
            self._ta_cmd_offset_threshold,
            self._ta_update_measurement_ul_sinr_threshold
        ]

    # Getters and setters for ConfigItem
    @property
    def ta_measurement_slot_period(self):
        """Get or set the slot period for TA measurements."""
        return self._ta_measurement_slot_period.value

    @ta_measurement_slot_period.setter
    def ta_measurement_slot_period(self, value):
        self._ta_measurement_slot_period.value = value

    @property
    def ta_cmd_offset_threshold(self):
        """Get or set the offset threshold for triggering a TA command."""
        return self._ta_cmd_offset_threshold.value

    @ta_cmd_offset_threshold.setter
    def ta_cmd_offset_threshold(self, value):
        self._ta_cmd_offset_threshold.value = value

    @property
    def ta_update_measurement_ul_sinr_threshold(self):
        """Get or set the UL SINR threshold for TA update measurements."""
        return self._ta_update_measurement_ul_sinr_threshold.value

    @ta_update_measurement_ul_sinr_threshold.setter
    def ta_update_measurement_ul_sinr_threshold(self, value):
        self._ta_update_measurement_ul_sinr_threshold.value = value
