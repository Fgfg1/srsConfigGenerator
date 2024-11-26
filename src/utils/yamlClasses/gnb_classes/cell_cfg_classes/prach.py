from common_conf import CommonConfig
from config_item import ConfigItem

class Prach(CommonConfig):
    def __init__(self, name="PrachConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes as ConfigItem instances
        self.prach_config_index = ConfigItem(
            key="prach_config_index",
            value=None,
            comment="Sets the PRACH configuration index. Supported: [0 - 255].",
            used=False
        )
        self.prach_root_sequence_index = ConfigItem(
            key="prach_root_sequence_index",
            value=1,
            comment="Sets the PRACH Root Sequence Index (RSI). Supported: [0 - 837].",
            used=False
        )
        self.zero_correlation_zone = ConfigItem(
            key="zero_correlation_zone",
            value=0,
            comment="Sets the Zero Correlation Zone. Supported: [0 - 15].",
            used=False
        )
        self.fixed_msg3_mcs = ConfigItem(
            key="fixed_msg3_mcs",
            value=0,
            comment="Sets a fixed Msg3 MCS. Supported: [0 - 28].",
            used=False
        )
        self.max_msg3_harq_retx = ConfigItem(
            key="max_msg3_harq_retx",
            value=4,
            comment="Sets the maximum number of Msg3 HARQ retransmissions. Supported: [0 - 4].",
            used=False
        )
        self.total_nof_ra_preambles = ConfigItem(
            key="total_nof_ra_preambles",
            value=None,
            comment="Sets the total number of RA preambles. Supported: [1 - 64].",
            used=False
        )
        self.prach_frequency_start = ConfigItem(
            key="prach_frequency_start",
            value=None,
            comment="Sets the frequency start for PRACH in PRBs. Supported: [0 - (MAX_NOF_PRB - 1)].",
            used=False
        )
        self.preamble_rx_target_pw = ConfigItem(
            key="preamble_rx_target_pw",
            value=-100,
            comment="Sets the target power level for PRACH. Supported: multiples of 2 within range [-202, -60].",
            used=False
        )
        self.preamble_trans_max = ConfigItem(
            key="preamble_trans_max",
            value=7,
            comment="Sets the max number of RA preamble transmissions. Supported: [3, 4, 5, 6, 7, 8, 10, 20, 50, 100, 200].",
            used=False
        )
        self.power_ramping_step_db = ConfigItem(
            key="power_ramping_step_db",
            value=4,
            comment="Sets the power ramping steps for PRACH. Supported: [0, 2, 4, 6].",
            used=False
        )
        self.ports = ConfigItem(
            key="ports",
            value=None,
            comment="Sets the list of antenna ports. Expected value is a UINT string of port IDs.",
            used=False
        )
        self.nof_ssb_per_ro = ConfigItem(
            key="nof_ssb_per_ro",
            value=1,
            comment="Sets the number of SSBs per RACH occasion. Supported: [1/8, 1/4, 1/2, 1, 2, 4, 8, 16].",
            used=False
        )
        self.nof_cb_preambles_per_ssb = ConfigItem(
            key="nof_cb_preambles_per_ssb",
            value=4,
            comment="Sets the number of contention-based preambles per SSB. Supported: [1 - 64].",
            used=False
        )
        self.ra_resp_window = ConfigItem(
            key="ra_resp_window",
            value=None,
            comment="Sets the RA-response window length in slots. Supported: {1, 2, 4, 8, 10, 20, 40, 80}.",
            used=False
        )

    @property
    def prach_config_index(self):
        """Get or set the PRACH configuration index."""
        return self.prach_config_index.value

    @prach_config_index.setter
    def prach_config_index(self, value):
        self.prach_config_index.value = value

    @property
    def prach_root_sequence_index(self):
        """Get or set the PRACH Root Sequence Index (RSI)."""
        return self.prach_root_sequence_index.value

    @prach_root_sequence_index.setter
    def prach_root_sequence_index(self, value):
        self.prach_root_sequence_index.value = value

    @property
    def zero_correlation_zone(self):
        """Get or set the Zero Correlation Zone."""
        return self.zero_correlation_zone.value

    @zero_correlation_zone.setter
    def zero_correlation_zone(self, value):
        self.zero_correlation_zone.value = value

    @property
    def fixed_msg3_mcs(self):
        """Get or set the fixed Msg3 MCS."""
        return self.fixed_msg3_mcs.value

    @fixed_msg3_mcs.setter
    def fixed_msg3_mcs(self, value):
        self.fixed_msg3_mcs.value = value

    @property
    def max_msg3_harq_retx(self):
        """Get or set the maximum number of Msg3 HARQ retransmissions."""
        return self.max_msg3_harq_retx.value

    @max_msg3_harq_retx.setter
    def max_msg3_harq_retx(self, value):
        self.max_msg3_harq_retx.value = value

    @property
    def total_nof_ra_preambles(self):
        """Get or set the total number of RA preambles."""
        return self.total_nof_ra_preambles.value

    @total_nof_ra_preambles.setter
    def total_nof_ra_preambles(self, value):
        self.total_nof_ra_preambles.value = value

    @property
    def prach_frequency_start(self):
        """Get or set the frequency start for PRACH in PRBs."""
        return self.prach_frequency_start.value

    @prach_frequency_start.setter
    def prach_frequency_start(self, value):
        self.prach_frequency_start.value = value

    @property
    def preamble_rx_target_pw(self):
        """Get or set the target power level for PRACH preamble reception."""
        return self.preamble_rx_target_pw.value

    @preamble_rx_target_pw.setter
    def preamble_rx_target_pw(self, value):
        self.preamble_rx_target_pw.value = value

    @property
    def preamble_trans_max(self):
        """Get or set the maximum number of RA preamble transmissions."""
        return self.preamble_trans_max.value

    @preamble_trans_max.setter
    def preamble_trans_max(self, value):
        self.preamble_trans_max.value = value

    @property
    def power_ramping_step_db(self):
        """Get or set the power ramping step for PRACH in dB."""
        return self.power_ramping_step_db.value

    @power_ramping_step_db.setter
    def power_ramping_step_db(self, value):
        self.power_ramping_step_db.value = value

    @property
    def ports(self):
        """Get or set the list of antenna ports."""
        return self.ports.value

    @ports.setter
    def ports(self, value):
        self.ports.value = value

    @property
    def nof_ssb_per_ro(self):
        """Get or set the number of SSBs per RACH occasion."""
        return self.nof_ssb_per_ro.value

    @nof_ssb_per_ro.setter
    def nof_ssb_per_ro(self, value):
        self.nof_ssb_per_ro.value = value

    @property
    def nof_cb_preambles_per_ssb(self):
        """Get or set the number of contention-based preambles per SSB."""
        return self.nof_cb_preambles_per_ssb.value

    @nof_cb_preambles_per_ssb.setter
    def nof_cb_preambles_per_ssb(self, value):
        self.nof_cb_preambles_per_ssb.value = value

    @property
    def ra_resp_window(self):
        """Get or set the RA-response window length in slots."""
        return self.ra_resp_window.value

    @ra_resp_window.setter
    def ra_resp_window(self, value):
        self.ra_resp_window.value = value