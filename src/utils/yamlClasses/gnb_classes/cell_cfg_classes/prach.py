from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Prach(CommonConfig):
    def __init__(self, name="prach", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes as ConfigItem instances

        # Optional UINT. Sets the PRACH configuration index. If not set, the value is derived, so that the PRACH fits in an UL slot. Supported: [0 - 255].
        self._prach_config_index = ConfigItem(
            key="prach_config_index",
            value=None,
            comment="Sets the PRACH configuration index. Supported: [0 - 255].",
            used=False
        )

        # Optional UINT (1). Sets the PRACH Roost Sequence Index (RSI), which determines the Zadoff-Chu (ZC) sequence used. Supported: [0 - 837]. If the PRACH configuration index is larger than 86, you cannot set a PRACH RSI of more than 137.
        self._prach_root_sequence_index = ConfigItem(
            key="prach_root_sequence_index",
            value=1,
            comment="Sets the PRACH Root Sequence Index (RSI). Supported: [0 - 837].",
            used=False
        )

        # Optional UINT (0). Sets the Zero Correlation Zone, which determines the size of the cyclic shift and the number of preamble sequences which can be generated from each Root Sequence Index. Supported: [0 - 15].
        self._zero_correlation_zone = ConfigItem(
            key="zero_correlation_zone",
            value=0,
            comment="Sets the Zero Correlation Zone. Supported: [0 - 15].",
            used=False
        )

        # Optional UINT (0). Sets a fixed Msg3 MCS. Supported: [0 - 28].
        self._fixed_msg3_mcs = ConfigItem(
            key="fixed_msg3_mcs",
            value=0,
            comment="Sets a fixed Msg3 MCS. Supported: [0 - 28].",
            used=False
        )

        # Optional UINT (4). Sets the maximum number of Msg3 HARQ retransmissions. Supported: [0 - 4].
        self._max_msg3_harq_retx = ConfigItem(
            key="max_msg3_harq_retx",
            value=4,
            comment="Sets the maximum number of Msg3 HARQ retransmissions. Supported: [0 - 4].",
            used=False
        )

        # Optional TEXT. Sets the number of different PRACH preambles. Supported: [1 - 64].
        self._total_nof_ra_preambles = ConfigItem(
            key="total_nof_ra_preambles",
            value=None,
            comment="Sets the total number of RA preambles. Supported: [1 - 64].",
            used=False
        )

        # Optional INT. Set Offset of lowest PRACH transmission occasion in frequency domain respective to PRB 0, in PRBs. Supported: [0 - (MAX_NOF_PRB - 1)].
        self._prach_frequency_start = ConfigItem(
            key="prach_frequency_start",
            value=None,
            comment="Sets the frequency start for PRACH in PRBs. Supported: [0 - (MAX_NOF_PRB - 1)].",
            used=False
        )

        # Optional INT (-100). Sets the Target power level at the network receiver side, in dBm. Supported: multiples of 2 within range [-202, -60].
        self._preamble_rx_target_pw = ConfigItem(
            key="preamble_rx_target_pw",
            value=-100,
            comment="Sets the target power level for PRACH. Supported: multiples of 2 within range [-202, -60].",
            used=False
        )

        # Optional UINT (7). Sets the max number of RA preamble transmissions performed before declaring a failure. Supported: [3, 4, 5, 6, 7, 8, 10, 20, 50, 100, 200].
        self._preamble_trans_max = ConfigItem(
            key="preamble_trans_max",
            value=7,
            comment="Sets the max number of RA preamble transmissions. Supported: [3, 4, 5, 6, 7, 8, 10, 20, 50, 100, 200].",
            used=False
        )

        # Optional UINT (4). Sets the power ramping steps for PRACH. Supported: [0, 2, 4 , 6].
        self._power_ramping_step_db = ConfigItem(
            key="power_ramping_step_db",
            value=4,
            comment="Sets the power ramping steps for PRACH. Supported: [0, 2, 4, 6].",
            used=False
        )

        # Optional UINT. Sets the list of atenna ports. Expected value is a UINT string of antenna port IDs.
        self._ports = ConfigItem(
            key="ports",
            value=None,
            comment="Sets the list of antenna ports. Expected value is a UINT string of port IDs.",
            used=False
        )

        # Optional FLOAT (1). Sets the number of SSBs per RACH occasion. Supported: [1/8, 1/4, 1/2, 1, 2, 4, 8, 16].
        self._nof_ssb_per_ro = ConfigItem(
            key="nof_ssb_per_ro",
            value=1,
            comment="Sets the number of SSBs per RACH occasion. Supported: [1/8, 1/4, 1/2, 1, 2, 4, 8, 16].",
            used=False
        )

        # Optional UINT (4). Sets the number of contention based preambles per SSB. Supported: [1 - 64].
        self._nof_cb_preambles_per_ssb = ConfigItem(
            key="nof_cb_preambles_per_ssb",
            value=4,
            comment="Sets the number of contention-based preambles per SSB. Supported: [1 - 64].",
            used=False
        )

        # Optional UINT. Sets the RA-response window length in number of slots. Supported: {1, 2, 4, 8, 10, 20, 40, 80}.
        self._ra_resp_window = ConfigItem(
            key="ra_resp_window",
            value=None,
            comment="Sets the RA-response window length in slots. Supported: {1, 2, 4, 8, 10, 20, 40, 80}.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._prach_config_index,
            self._prach_root_sequence_index,
            self._zero_correlation_zone,
            self._fixed_msg3_mcs,
            self._max_msg3_harq_retx,
            self._total_nof_ra_preambles,
            self._prach_frequency_start,
            self._preamble_rx_target_pw,
            self._preamble_trans_max,
            self._power_ramping_step_db,
            self._ports,
            self._nof_ssb_per_ro,
            self._nof_cb_preambles_per_ssb,
            self._ra_resp_window
        ]

    @property
    def prach_config_index(self):
        """Get or set the PRACH configuration index."""
        return self._prach_config_index.value

    @prach_config_index.setter
    def prach_config_index(self, value):
        self._prach_config_index.value = value

    @property
    def prach_root_sequence_index(self):
        """Get or set the PRACH Root Sequence Index (RSI)."""
        return self._prach_root_sequence_index.value

    @prach_root_sequence_index.setter
    def prach_root_sequence_index(self, value):
        self._prach_root_sequence_index.value = value

    @property
    def zero_correlation_zone(self):
        """Get or set the Zero Correlation Zone."""
        return self._zero_correlation_zone.value

    @zero_correlation_zone.setter
    def zero_correlation_zone(self, value):
        self._zero_correlation_zone.value = value

    @property
    def fixed_msg3_mcs(self):
        """Get or set the fixed Msg3 MCS."""
        return self._fixed_msg3_mcs.value

    @fixed_msg3_mcs.setter
    def fixed_msg3_mcs(self, value):
        self._fixed_msg3_mcs.value = value

    @property
    def max_msg3_harq_retx(self):
        """Get or set the maximum number of Msg3 HARQ retransmissions."""
        return self._max_msg3_harq_retx.value

    @max_msg3_harq_retx.setter
    def max_msg3_harq_retx(self, value):
        self._max_msg3_harq_retx.value = value

    @property
    def total_nof_ra_preambles(self):
        """Get or set the total number of RA preambles."""
        return self._total_nof_ra_preambles.value

    @total_nof_ra_preambles.setter
    def total_nof_ra_preambles(self, value):
        self._total_nof_ra_preambles.value = value

    @property
    def prach_frequency_start(self):
        """Get or set the frequency start for PRACH in PRBs."""
        return self._prach_frequency_start.value

    @prach_frequency_start.setter
    def prach_frequency_start(self, value):
        self._prach_frequency_start.value = value

    @property
    def preamble_rx_target_pw(self):
        """Get or set the target power level for PRACH preamble reception."""
        return self._preamble_rx_target_pw.value

    @preamble_rx_target_pw.setter
    def preamble_rx_target_pw(self, value):
        self._preamble_rx_target_pw.value = value

    @property
    def preamble_trans_max(self):
        """Get or set the maximum number of RA preamble transmissions."""
        return self._preamble_trans_max.value

    @preamble_trans_max.setter
    def preamble_trans_max(self, value):
        self._preamble_trans_max.value = value

    @property
    def power_ramping_step_db(self):
        """Get or set the power ramping step for PRACH in dB."""
        return self._power_ramping_step_db.value

    @power_ramping_step_db.setter
    def power_ramping_step_db(self, value):
        self._power_ramping_step_db.value = value

    @property
    def ports(self):
        """Get or set the list of antenna ports."""
        return self._ports.value

    @ports.setter
    def ports(self, value):
        self._ports.value = value

    @property
    def nof_ssb_per_ro(self):
        """Get or set the number of SSBs per RACH occasion."""
        return self._nof_ssb_per_ro.value

    @nof_ssb_per_ro.setter
    def nof_ssb_per_ro(self, value):
        self._nof_ssb_per_ro.value = value

    @property
    def nof_cb_preambles_per_ssb(self):
        """Get or set the number of contention-based preambles per SSB."""
        return self._nof_cb_preambles_per_ssb.value

    @nof_cb_preambles_per_ssb.setter
    def nof_cb_preambles_per_ssb(self, value):
        self._nof_cb_preambles_per_ssb.value = value

    @property
    def ra_resp_window(self):
        """Get or set the RA-response window length in slots."""
        return self._ra_resp_window.value

    @ra_resp_window.setter
    def ra_resp_window(self, value):
        self._ra_resp_window.value = value