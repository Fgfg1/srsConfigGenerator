from config_item import ConfigItem
from common_conf import CommonConfig

class Pusch(CommonConfig):
    def __init__(self, name="PuschConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes as ConfigItem instances
        self.min_ue_mcs = ConfigItem(
            key="min_ue_mcs",
            value=0,
            comment="Minimum UE MCS value",
            used=False
        )
        self.max_ue_mcs = ConfigItem(
            key="max_ue_mcs",
            value=28,
            comment="Maximum UE MCS value",
            used=False
        )
        self.max_consecutive_kos = ConfigItem(
            key="max_consecutive_kos",
            value=100,
            comment="Maximum number of consecutive KOs",
            used=False
        )
        self.mcs_table = ConfigItem(
            key="mcs_table",
            value="qam64",
            comment="Modulation and Coding Scheme table",
            used=False
        )
        self.msg3_delta_preamble = ConfigItem(
            key="msg3_delta_preamble",
            value=6,
            comment="Delta preamble for Msg3",
            used=False
        )
        self.p0_nominal_with_grant = ConfigItem(
            key="p0_nominal_with_grant",
            value=-76,
            comment="Nominal P0 with grant",
            used=False
        )
        self.msg3_delta_power = ConfigItem(
            key="msg3_delta_power",
            value=8,
            comment="Delta power for Msg3",
            used=False
        )
        self.max_puschs_per_slot = ConfigItem(
            key="max_puschs_per_slot",
            value=16,
            comment="Maximum PUSCHs per slot",
            used=False
        )
        self.b_offset_ack_idx_1 = ConfigItem(
            key="b_offset_ack_idx_1",
            value=9,
            comment="Beta offset ACK index 1",
            used=False
        )
        self.b_offset_ack_idx_2 = ConfigItem(
            key="b_offset_ack_idx_2",
            value=9,
            comment="Beta offset ACK index 2",
            used=False
        )
        self.b_offset_ack_idx_3 = ConfigItem(
            key="b_offset_ack_idx_3",
            value=9,
            comment="Beta offset ACK index 3",
            used=False
        )
        self.beta_offset_csi_p1_idx_1 = ConfigItem(
            key="beta_offset_csi_p1_idx_1",
            value=9,
            comment="Beta offset CSI P1 index 1",
            used=False
        )
        self.beta_offset_csi_p1_idx_2 = ConfigItem(
            key="beta_offset_csi_p1_idx_2",
            value=9,
            comment="Beta offset CSI P1 index 2",
            used=False
        )
        self.beta_offset_csi_p2_idx_1 = ConfigItem(
            key="beta_offset_csi_p2_idx_1",
            value=9,
            comment="Beta offset CSI P2 index 1",
            used=False
        )
        self.beta_offset_csi_p2_idx_2 = ConfigItem(
            key="beta_offset_csi_p2_idx_2",
            value=9,
            comment="Beta offset CSI P2 index 2",
            used=False
        )
        self.min_k2 = ConfigItem(
            key="min_k2",
            value=4,
            comment="Minimum K2 value",
            used=False
        )
        self.dc_offset = ConfigItem(
            key="dc_offset",
            value=None,
            comment="DC offset value",
            used=False
        )
        self.olla_snr_inc_step = ConfigItem(
            key="olla_snr_inc_step",
            value=0.001,
            comment="OLLA SNR increment step",
            used=False
        )
        self.olla_target_bler = ConfigItem(
            key="olla_target_bler",
            value=0.01,
            comment="OLLA target BLER",
            used=False
        )
        self.olla_max_snr_offset = ConfigItem(
            key="olla_max_snr_offset",
            value=5,
            comment="OLLA maximum SNR offset",
            used=False
        )
        self.dmrs_additional_position = ConfigItem(
            key="dmrs_additional_position",
            value=2,
            comment="Additional DMRS positions",
            used=False
        )
        self.min_rb_size = ConfigItem(
            key="min_rb_size",
            value=1,
            comment="Minimum RB size",
            used=False
        )
        self.max_rb_size = ConfigItem(
            key="max_rb_size",
            value=275,
            comment="Maximum RB size",
            used=False
        )
        self.start_rb = ConfigItem(
            key="start_rb",
            value=0,
            comment="Start RB",
            used=False
        )
        self.end_rb = ConfigItem(
            key="end_rb",
            value=275,
            comment="End RB",
            used=False
        )
        self.enable_transform_precoding = ConfigItem(
            key="enable_transform_precoding",
            value=False,
            comment="Enable transform precoding",
            used=False
        )
        self.rv_sequence = ConfigItem(
            key="rv_sequence",
            value=[0],
            comment="Sets the redundancy version sequence to use for PUSCH. Supported: any combination of [0, 1, 2, 3].",
            used=False
        )

    @property
    def rv_sequence(self):
        """Optional UINT (0). Sets the redundancy version sequence to use for PUSCH. Supported: any combination of [0, 1, 2, 3]."""
        return self.rv_sequence
    
    @rv_sequence.setter
    def rv_sequence(self, value):
        self._rv_sequence = value

    @property
    def min_ue_mcs(self):
        """Get the minimum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        return self._min_ue_mcs

    @min_ue_mcs.setter
    def min_ue_mcs(self, value):
        """Set the minimum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        self._min_ue_mcs = value

    @property
    def max_ue_mcs(self):
        """Get the maximum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        return self._max_ue_mcs

    @max_ue_mcs.setter
    def max_ue_mcs(self, value):
        """Set the maximum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        self._max_ue_mcs = value

    @property
    def max_consecutive_kos(self):
        """Get the maximum consecutive CRC KOs before reporting an RLF. Supported range: [0 - inf]."""
        return self._max_consecutive_kos

    @max_consecutive_kos.setter
    def max_consecutive_kos(self, value):
        """Set the maximum consecutive CRC KOs before reporting an RLF. Supported range: [0 - inf]."""
        self._max_consecutive_kos = value

    @property
    def mcs_table(self):
        """Get the MCS table for PUSCH. Supported values: [qam64, qam256]."""
        return self._mcs_table

    @mcs_table.setter
    def mcs_table(self, value):
        """Set the MCS table for PUSCH. Supported values: [qam64, qam256]."""
        self._mcs_table = value

    @property
    def msg3_delta_preamble(self):
        """Get the MSG3 DeltaPreamble power offset. Supported range: [-1 - 6]."""
        return self._msg3_delta_preamble

    @msg3_delta_preamble.setter
    def msg3_delta_preamble(self, value):
        """Set the MSG3 DeltaPreamble power offset. Supported range: [-1 - 6]."""
        self._msg3_delta_preamble = value

    @property
    def p0_nominal_with_grant(self):
        """Get the P0 value for PUSCH grant, in dBm. Supported: multiples of 2 within [-202, 24]."""
        return self._p0_nominal_with_grant

    @p0_nominal_with_grant.setter
    def p0_nominal_with_grant(self, value):
        """Set the P0 value for PUSCH grant, in dBm. Supported: multiples of 2 within [-202, 24]."""
        self._p0_nominal_with_grant = value

    @property
    def msg3_delta_power(self):
        """Get the MSG3 Delta power level at the network receiver side, in dBm. Supported: multiples of 2 within [-6, 8]."""
        return self._msg3_delta_power

    @msg3_delta_power.setter
    def msg3_delta_power(self, value):
        """Set the MSG3 Delta power level at the network receiver side, in dBm. Supported: multiples of 2 within [-6, 8]."""
        self._msg3_delta_power = value

    @property
    def max_puschs_per_slot(self):
        """Get the maximum number of PUSCH grants per slot. Supported: [1 - 16]."""
        return self._max_puschs_per_slot

    @max_puschs_per_slot.setter
    def max_puschs_per_slot(self, value):
        """Set the maximum number of PUSCH grants per slot. Supported: [1 - 16]."""
        self._max_puschs_per_slot = value

    @property
    def b_offset_ack_idx_1(self):
        """Get the betaOffsetACK-Index1 for UCI-OnPUSCH. Supported: [0 - 31]."""
        return self._b_offset_ack_idx_1

    @b_offset_ack_idx_1.setter
    def b_offset_ack_idx_1(self, value):
        """Set the betaOffsetACK-Index1 for UCI-OnPUSCH. Supported: [0 - 31]."""
        self._b_offset_ack_idx_1 = value

    @property
    def min_k2(self):
        """Get the minimum value of K2 (difference in slots between PDCCH and PUSCH). Supported: [1 - 4]."""
        return self._min_k2

    @min_k2.setter
    def min_k2(self, value):
        """Set the minimum value of K2 (difference in slots between PDCCH and PUSCH). Supported: [1 - 4]."""
        self._min_k2 = value

    @property
    def dc_offset(self):
        """Get the DC Offset in subcarriers relative to the gNB UL carrier. Supported: [-1650 - 1649] or [outside, undetermined, center]."""
        return self._dc_offset

    @dc_offset.setter
    def dc_offset(self, value):
        """Set the DC Offset in subcarriers relative to the gNB UL carrier. Supported: [-1650 - 1649] or [outside, undetermined, center]."""
        self._dc_offset = value

    @property
    def olla_snr_inc_step(self):
        """Get the OLLA increment value. 0 means OLLA is disabled. Supported: [0 - 1]."""
        return self._olla_snr_inc_step

    @olla_snr_inc_step.setter
    def olla_snr_inc_step(self, value):
        """Set the OLLA increment value. 0 means OLLA is disabled. Supported: [0 - 1]."""
        self._olla_snr_inc_step = value

    @property
    def olla_target_bler(self):
        """Get the target UL BLER for OLLA. Supported: [0 - 0.5]."""
        return self._olla_target_bler

    @olla_target_bler.setter
    def olla_target_bler(self, value):
        """Set the target UL BLER for OLLA. Supported: [0 - 0.5]."""
        self._olla_target_bler = value

    @property
    def olla_max_snr_offset(self):
        """Get the maximum offset for OLLA to estimate UL SNR. Supported: positive float."""
        return self._olla_max_snr_offset

    @olla_max_snr_offset.setter
    def olla_max_snr_offset(self, value):
        """Set the maximum offset for OLLA to estimate UL SNR. Supported: positive float."""
        self._olla_max_snr_offset = value

    @property
    def dmrs_additional_position(self):
        """Get the PUSCH DMRS additional position. Supported: [0 - 3]."""
        return self._dmrs_additional_position

    @dmrs_additional_position.setter
    def dmrs_additional_position(self, value):
        """Set the PUSCH DMRS additional position. Supported: [0 - 3]."""
        self._dmrs_additional_position = value

    @property
    def min_rb_size(self):
        """Get the minimum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        return self._min_rb_size

    @min_rb_size.setter
    def min_rb_size(self, value):
        """Set the minimum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        self._min_rb_size = value

    @property
    def max_rb_size(self):
        """Get the maximum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        return self._max_rb_size

    @max_rb_size.setter
    def max_rb_size(self, value):
        """Set the maximum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        self._max_rb_size = value

    @property
    def start_rb(self):
        """Get the start RB for PUSCH resource allocation. Supported: [0 - 275]."""
        return self._start_rb

    @start_rb.setter
    def start_rb(self, value):
        """Set the start RB for PUSCH resource allocation. Supported: [0 - 275]."""
        self._start_rb = value

    @property
    def end_rb(self):
        """Get the end RB for PUSCH resource allocation. Supported: [0 - 275]."""
        return self._end_rb

    @end_rb.setter
    def end_rb(self, value):
        """Set the end RB for PUSCH resource allocation. Supported: [0 - 275]."""
        self._end_rb = value

    @property
    def enable_transform_precoding(self):
        """Get the status of transform precoding for PUSCH. Supported: [true, false]."""
        return self._enable_transform_precoding

    @enable_transform_precoding.setter
    def enable_transform_precoding(self, value):
        """Enable or disable transform precoding for PUSCH. Supported: [true, false]."""
        self._enable_transform_precoding = value
