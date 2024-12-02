from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Pusch(CommonConfig):
    def __init__(self, name="pusch", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes as ConfigItem instances

        # Optional UINT (0). Sets a minimum PUSCH MCS value to be used for all UEs. Supported: [0 - 28].
        self._min_ue_mcs = ConfigItem(
            key="min_ue_mcs",
            value=0,
            comment="Minimum UE MCS value",
            used=False
        )
        
        # Optional UINT (28). Sets a maximum PUSCH MCS value to be used for all UEs. Supported: [0 - 28].
        self._max_ue_mcs = ConfigItem(
            key="max_ue_mcs",
            value=28,
            comment="Maximum UE MCS value",
            used=False
        )

        # Optional UINT (100). Sets the maximum number of consecutive CRC KOs before an RLF is reported. Supported: [0 - inf].
        self._max_consecutive_kos = ConfigItem(
            key="max_consecutive_kos",
            value=100,
            comment="Maximum number of consecutive KOs",
            used=False
        )

        # Optional UINT (0). Sets the redundancy version sequence to use for PUSCH. Supported: any combination of [0, 1, 2, 3].
        self._rv_sequence = ConfigItem(
            key="rv_sequence",
            value=[0],
            comment="Sets the redundancy version sequence to use for PUSCH. Supported: any combination of [0, 1, 2, 3].",
            used=False
        )

        # Optional TEXT (qam64). Sets the MCS table to use for PUSCH. Supported: [qam64, qam256].
        self._mcs_table = ConfigItem(
            key="mcs_table",
            value="qam64",
            comment="Modulation and Coding Scheme table",
            used=False
        )

        # Optional INT (6). Sets the MSG3 DeltaPreamble power offset between MS3 and RACH preamble transmission. Supported: [-1 - 6].
        self._msg3_delta_preamble = ConfigItem(
            key="msg3_delta_preamble",
            value=6,
            comment="Delta preamble for Msg3",
            used=False
        )

        # Optional INT (-76). Sets the P0 value for PUSCH grant (except MSG3), in dBm. Supported: multiples of 2 within the range [-202, 24].
        self._p0_nominal_with_grant = ConfigItem(
            key="p0_nominal_with_grant",
            value=-76,
            comment="Nominal P0 with grant",
            used=False
        )

        # Optional INT (8). Sets the target power level at the network receiver side, in dBm. Supported: multiples of 2 within the range [-6, 8].
        self._msg3_delta_power = ConfigItem(
            key="msg3_delta_power",
            value=8,
            comment="Delta power for Msg3",
            used=False
        )

        # Optional UINT (16). Sets the maximum number of PUSCH grants per slot. Supprted: [1 - 16].
        self._max_puschs_per_slot = ConfigItem(
            key="max_puschs_per_slot",
            value=16,
            comment="Maximum PUSCHs per slot",
            used=False
        )

        # Optional UINT (9). Sets the betaOffsetACK-Index1 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._b_offset_ack_idx_1 = ConfigItem(
            key="b_offset_ack_idx_1",
            value=9,
            comment="Beta offset ACK index 1",
            used=False
        )

        # Optional UINT (9). Sets the betaOffsetACK-Index2 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._b_offset_ack_idx_2 = ConfigItem(
            key="b_offset_ack_idx_2",
            value=9,
            comment="Beta offset ACK index 2",
            used=False
        )

        # Optional UINT (9). Sets the betaOffsetACK-Index3 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._b_offset_ack_idx_3 = ConfigItem(
            key="b_offset_ack_idx_3",
            value=9,
            comment="Beta offset ACK index 3",
            used=False
        )

        # Optional UINT (9). Sets the b_offset_csi_p1_idx_1 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._beta_offset_csi_p1_idx_1 = ConfigItem(
            key="beta_offset_csi_p1_idx_1",
            value=9,
            comment="Beta offset CSI P1 index 1",
            used=False
        )

        # Optional UINT (9). Sets the b_offset_csi_p1_idx_2 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._beta_offset_csi_p1_idx_2 = ConfigItem(
            key="beta_offset_csi_p1_idx_2",
            value=9,
            comment="Beta offset CSI P1 index 2",
            used=False
        )

        # Optional UINT (9). Sets the b_offset_csi_p2_idx_1 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._beta_offset_csi_p2_idx_1 = ConfigItem(
            key="beta_offset_csi_p2_idx_1",
            value=9,
            comment="Beta offset CSI P2 index 1",
            used=False
        )

        # Optional UINT (9). Sets the b_offset_csi_p2_idx_2 part of UCI-OnPUSCH. Supported: [0 - 31].
        self._beta_offset_csi_p2_idx_2 = ConfigItem(
            key="beta_offset_csi_p2_idx_2",
            value=9,
            comment="Beta offset CSI P2 index 2",
            used=False
        )

        # Optional UINT (4). Sets the minimum value of K2 (difference in slots between PDCCH and PUSCH). Supported: [1 - 4].
        self._min_k2 = ConfigItem(
            key="min_k2",
            value=4,
            comment="Minimum K2 value",
            used=False
        )

        # Optional TEXT. Sets the direct Current (DC) Offset in number of subcarriers, using the common SCS as reference for carrier spacing, and the center of the gNB UL carrier as DC offset value 0. 
        # The user can additionally set "outside" to define that the DC offset falls outside the DL carrier or "undetermined" in the case the DC offset is unknown. 
        # Supported: [-1650 - 1649] OR [outside,undetermined,center].
        self._dc_offset = ConfigItem(
            key="dc_offset",
            value=None,
            comment="DC offset value",
            used=False
        )

        # Optional FLOAT (0.001). Sets the outer-loop link adaptation (OLLA) increment value. The value 0 means that OLLA is disabled. Supported: [0 - 1].
        self._olla_snr_inc_step = ConfigItem(
            key="olla_snr_inc_step",
            value=0.001,
            comment="OLLA SNR increment step",
            used=False
        )

        # Optional FLOAT (0.01). Sets the target UL BLER set in Outer-loop link adaptation (OLLA) algorithm. sUPPORTED: [0 - 0.5].
        self._olla_target_bler = ConfigItem(
            key="olla_target_bler",
            value=0.01,
            comment="OLLA target BLER",
            used=False
        )

        # Optional FLOAT (5). Sets the maximum offset that the Outer-loop link adaptation (OLLA) can apply to estimate the UL SNR. Supported: positive float.
        self._olla_max_snr_offset = ConfigItem(
            key="olla_max_snr_offset",
            value=5,
            comment="OLLA maximum SNR offset",
            used=False
        )

        # Optional UINT (2). Sets the PUSCH DMRS additional position. Supported: [0 - 3].
        self._dmrs_additional_position = ConfigItem(
            key="dmrs_additional_position",
            value=2,
            comment="Additional DMRS positions",
            used=False
        )

        # Optional UINT (1). Sets the minimum RB size for the UE PUSCH resource allocation. Supported: [1 - 275].
        self._min_rb_size = ConfigItem(
            key="min_rb_size",
            value=1,
            comment="Minimum RB size",
            used=False
        )

        # Optional UINT (275). Sets the maximum RB size for the UE PUSCH resource allocation. Supported: [1 - 275].
        self._max_rb_size = ConfigItem(
            key="max_rb_size",
            value=275,
            comment="Maximum RB size",
            used=False
        )

        # Optional UINT (0). Sets the start RB for resource allocation of UE PUSCHs. Supported: [0 - 275].
        self._start_rb = ConfigItem(
            key="start_rb",
            value=0,
            comment="Start RB",
            used=False
        )

        # Optional UINT (275). Sets the end RB for resource allocation of UE PUSCHs. Supported: [0 - 275].
        self._end_rb = ConfigItem(
            key="end_rb",
            value=275,
            comment="End RB",
            used=False
        )

        # Optional BOOLEAN (false). Enables transform precoding for PUSCH. Supported: [false, true]
        self._enable_transform_precoding = ConfigItem(
            key="enable_transform_precoding",
            value=False,
            comment="Enable transform precoding",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._min_ue_mcs,
            self._max_ue_mcs,
            self._max_consecutive_kos,
            self._rv_sequence,
            self._mcs_table,
            self._msg3_delta_preamble,
            self._p0_nominal_with_grant,
            self._msg3_delta_power,
            self._max_puschs_per_slot,
            self._b_offset_ack_idx_1,
            self._b_offset_ack_idx_2,
            self._b_offset_ack_idx_3,
            self._beta_offset_csi_p1_idx_1,
            self._beta_offset_csi_p1_idx_2,
            self._beta_offset_csi_p2_idx_1,
            self._beta_offset_csi_p2_idx_2,
            self._min_k2,
            self._dc_offset,
            self._olla_snr_inc_step,
            self._olla_target_bler,
            self._olla_max_snr_offset,
            self._dmrs_additional_position,
            self._min_rb_size,
            self._max_rb_size,
            self._start_rb,
            self._end_rb,
            self._enable_transform_precoding
        ]

    @property
    def rv_sequence(self):
        """Optional UINT (0). Sets the redundancy version sequence to use for PUSCH. Supported: any combination of [0, 1, 2, 3]."""
        return self._rv_sequence
    
    @rv_sequence.setter
    def rv_sequence(self, value):
        self.__rv_sequence = value

    @property
    def min_ue_mcs(self):
        """Get the minimum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        return self.__min_ue_mcs

    @min_ue_mcs.setter
    def min_ue_mcs(self, value):
        """Set the minimum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        self.__min_ue_mcs = value

    @property
    def max_ue_mcs(self):
        """Get the maximum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        return self.__max_ue_mcs

    @max_ue_mcs.setter
    def max_ue_mcs(self, value):
        """Set the maximum PUSCH MCS value for all UEs. Supported range: [0 - 28]."""
        self.__max_ue_mcs = value

    @property
    def max_consecutive_kos(self):
        """Get the maximum consecutive CRC KOs before reporting an RLF. Supported range: [0 - inf]."""
        return self.__max_consecutive_kos

    @max_consecutive_kos.setter
    def max_consecutive_kos(self, value):
        """Set the maximum consecutive CRC KOs before reporting an RLF. Supported range: [0 - inf]."""
        self.__max_consecutive_kos = value

    @property
    def mcs_table(self):
        """Get the MCS table for PUSCH. Supported values: [qam64, qam256]."""
        return self.__mcs_table

    @mcs_table.setter
    def mcs_table(self, value):
        """Set the MCS table for PUSCH. Supported values: [qam64, qam256]."""
        self.__mcs_table = value

    @property
    def msg3_delta_preamble(self):
        """Get the MSG3 DeltaPreamble power offset. Supported range: [-1 - 6]."""
        return self.__msg3_delta_preamble

    @msg3_delta_preamble.setter
    def msg3_delta_preamble(self, value):
        """Set the MSG3 DeltaPreamble power offset. Supported range: [-1 - 6]."""
        self.__msg3_delta_preamble = value

    @property
    def p0_nominal_with_grant(self):
        """Get the P0 value for PUSCH grant, in dBm. Supported: multiples of 2 within [-202, 24]."""
        return self.__p0_nominal_with_grant

    @p0_nominal_with_grant.setter
    def p0_nominal_with_grant(self, value):
        """Set the P0 value for PUSCH grant, in dBm. Supported: multiples of 2 within [-202, 24]."""
        self.__p0_nominal_with_grant = value

    @property
    def msg3_delta_power(self):
        """Get the MSG3 Delta power level at the network receiver side, in dBm. Supported: multiples of 2 within [-6, 8]."""
        return self.__msg3_delta_power

    @msg3_delta_power.setter
    def msg3_delta_power(self, value):
        """Set the MSG3 Delta power level at the network receiver side, in dBm. Supported: multiples of 2 within [-6, 8]."""
        self.__msg3_delta_power = value

    @property
    def max_puschs_per_slot(self):
        """Get the maximum number of PUSCH grants per slot. Supported: [1 - 16]."""
        return self.__max_puschs_per_slot

    @max_puschs_per_slot.setter
    def max_puschs_per_slot(self, value):
        """Set the maximum number of PUSCH grants per slot. Supported: [1 - 16]."""
        self.__max_puschs_per_slot = value

    @property
    def b_offset_ack_idx_1(self):
        """Get the betaOffsetACK-Index1 for UCI-OnPUSCH. Supported: [0 - 31]."""
        return self.__b_offset_ack_idx_1

    @b_offset_ack_idx_1.setter
    def b_offset_ack_idx_1(self, value):
        """Set the betaOffsetACK-Index1 for UCI-OnPUSCH. Supported: [0 - 31]."""
        self.__b_offset_ack_idx_1 = value

    @property
    def min_k2(self):
        """Get the minimum value of K2 (difference in slots between PDCCH and PUSCH). Supported: [1 - 4]."""
        return self.__min_k2

    @min_k2.setter
    def min_k2(self, value):
        """Set the minimum value of K2 (difference in slots between PDCCH and PUSCH). Supported: [1 - 4]."""
        self.__min_k2 = value

    @property
    def dc_offset(self):
        """Get the DC Offset in subcarriers relative to the gNB UL carrier. Supported: [-1650 - 1649] or [outside, undetermined, center]."""
        return self.__dc_offset

    @dc_offset.setter
    def dc_offset(self, value):
        """Set the DC Offset in subcarriers relative to the gNB UL carrier. Supported: [-1650 - 1649] or [outside, undetermined, center]."""
        self.__dc_offset = value

    @property
    def olla_snr_inc_step(self):
        """Get the OLLA increment value. 0 means OLLA is disabled. Supported: [0 - 1]."""
        return self.__olla_snr_inc_step

    @olla_snr_inc_step.setter
    def olla_snr_inc_step(self, value):
        """Set the OLLA increment value. 0 means OLLA is disabled. Supported: [0 - 1]."""
        self.__olla_snr_inc_step = value

    @property
    def olla_target_bler(self):
        """Get the target UL BLER for OLLA. Supported: [0 - 0.5]."""
        return self.__olla_target_bler

    @olla_target_bler.setter
    def olla_target_bler(self, value):
        """Set the target UL BLER for OLLA. Supported: [0 - 0.5]."""
        self.__olla_target_bler = value

    @property
    def olla_max_snr_offset(self):
        """Get the maximum offset for OLLA to estimate UL SNR. Supported: positive float."""
        return self.__olla_max_snr_offset

    @olla_max_snr_offset.setter
    def olla_max_snr_offset(self, value):
        """Set the maximum offset for OLLA to estimate UL SNR. Supported: positive float."""
        self.__olla_max_snr_offset = value

    @property
    def dmrs_additional_position(self):
        """Get the PUSCH DMRS additional position. Supported: [0 - 3]."""
        return self.__dmrs_additional_position

    @dmrs_additional_position.setter
    def dmrs_additional_position(self, value):
        """Set the PUSCH DMRS additional position. Supported: [0 - 3]."""
        self.__dmrs_additional_position = value

    @property
    def min_rb_size(self):
        """Get the minimum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        return self.__min_rb_size

    @min_rb_size.setter
    def min_rb_size(self, value):
        """Set the minimum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        self.__min_rb_size = value

    @property
    def max_rb_size(self):
        """Get the maximum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        return self.__max_rb_size

    @max_rb_size.setter
    def max_rb_size(self, value):
        """Set the maximum RB size for PUSCH resource allocation. Supported: [1 - 275]."""
        self.__max_rb_size = value

    @property
    def start_rb(self):
        """Get the start RB for PUSCH resource allocation. Supported: [0 - 275]."""
        return self.__start_rb

    @start_rb.setter
    def start_rb(self, value):
        """Set the start RB for PUSCH resource allocation. Supported: [0 - 275]."""
        self.__start_rb = value

    @property
    def end_rb(self):
        """Get the end RB for PUSCH resource allocation. Supported: [0 - 275]."""
        return self.__end_rb

    @end_rb.setter
    def end_rb(self, value):
        """Set the end RB for PUSCH resource allocation. Supported: [0 - 275]."""
        self.__end_rb = value

    @property
    def enable_transform_precoding(self):
        """Get the status of transform precoding for PUSCH. Supported: [true, false]."""
        return self.__enable_transform_precoding

    @enable_transform_precoding.setter
    def enable_transform_precoding(self, value):
        """Enable or disable transform precoding for PUSCH. Supported: [true, false]."""
        self.__enable_transform_precoding = value
