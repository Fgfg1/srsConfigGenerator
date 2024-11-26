from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Pdsch(CommonConfig):
    def __init__(self, name="PdschConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._min_ue_mcs = ConfigItem(
            key="min_ue_mcs",
            value=0,
            comment="Sets a minimum PDSCH MCS value to be used for all UEs. Supported: [0 - 28].",
            used=False
        )
        self._max_ue_mcs = ConfigItem(
            key="max_ue_mcs",
            value=28,
            comment="Sets a maximum PDSCH MCS value to be used for all UEs. Supported: [0 - 28].",
            used=False
        )
        self._fixed_rar_mcs = ConfigItem(
            key="fixed_rar_mcs",
            value=0,
            comment="Sets a fixed RAR MCS value for all UEs. Supported: [0 - 28].",
            used=False
        )
        self._fixed_sib1_mcs = ConfigItem(
            key="fixed_sib1_mcs",
            value=5,
            comment="Sets a fixed SIB1 MCS for all UEs. Supported: [0 - 28].",
            used=False
        )
        self._nof_harqs = ConfigItem(
            key="nof_harqs",
            value=16,
            comment="Sets the number of Downlink HARQ processes. Supported: [2, 4, 6, 8, 10, 12, 16].",
            used=False
        )
        self._max_nof_harq_retxs = ConfigItem(
            key="max_nof_harq_retxs",
            value=4,
            comment="Sets the maximum number of DL HARQ retransmissions. Supported: [0 - 4].",
            used=False
        )
        self._max_consecutive_kos = ConfigItem(
            key="max_consecutive_kos",
            value=100,
            comment="Sets the maximum number of consecutive HARQ-ACK KOs before reporting an RLF. Supported: [0 - inf].",
            used=False
        )
        self._mcs_table = ConfigItem(
            key="mcs_table",
            value="qam64",
            comment="Sets the MCS table to use for PDSCH. Supported: [qam64, qam256].",
            used=False
        )
        self._min_rb_size = ConfigItem(
            key="min_rb_size",
            value=1,
            comment="Sets the minimum RB size for PDSCH resource allocation. Supported: [1 - 275].",
            used=False
        )
        self._max_rb_size = ConfigItem(
            key="max_rb_size",
            value=275,
            comment="Sets the maximum RB size for PDSCH resource allocation. Supported: [1 - 275].",
            used=False
        )
        self._start_rb = ConfigItem(
            key="start_rb",
            value=0,
            comment="Sets the start RB for resource allocation of UE PDSCHs. Supported: [0 - 275].",
            used=False
        )
        self._end_rb = ConfigItem(
            key="end_rb",
            value=275,
            comment="Sets the end RB for resource allocation of UE PDSCHs. Supported: [0 - 275].",
            used=False
        )
        self._max_pdschs_per_slot = ConfigItem(
            key="max_pdschs_per_slot",
            value=35,
            comment="Sets the maximum number of PDSCH grants per slot, including SIB, RAR, Paging, and UE data grants. Supported: [1 - 35].",
            used=False
        )
        self._max_alloc_attempts = ConfigItem(
            key="max_alloc_attempts",
            value=35,
            comment="Sets the maximum number of DL or UL PDCCH grant allocation attempts per slot before the scheduler skips the slot. Supported: [1 - 35].",
            used=False
        )
        self._olla_cqi_inc_step = ConfigItem(
            key="olla_cqi_inc_step",
            value=0.001,
            comment="Sets the OLLA increment value. Value 0 disables OLLA. Supported: [0 - 1].",
            used=False
        )
        self._olla_target_bler = ConfigItem(
            key="olla_target_bler",
            value=0.01,
            comment="Sets the target DL BLER for the OLLA algorithm. Supported: [0 - 0.5].",
            used=False
        )
        self._olla_max_cqi_offset = ConfigItem(
            key="olla_max_cqi_offset",
            value=4,
            comment="Sets the maximum CQI offset for OLLA. Supported: positive float.",
            used=False
        )
        self._dc_offset = ConfigItem(
            key="dc_offset",
            value=None,
            comment="Sets the DC offset for PDSCH in number of subcarriers.",
            used=False
        )
        self._harq_la_cqi_drop_threshold = ConfigItem(
            key="harq_la_cqi_drop_threshold",
            value=3,
            comment="Sets the HARQ Link Adaptation CQI drop threshold. Supported: [0 - 15].",
            used=False
        )
        self._harq_la_ri_drop_threshold = ConfigItem(
            key="harq_la_ri_drop_threshold",
            value=1,
            comment="Sets the HARQ Link Adaptation RI drop threshold. Supported: [0 - 4].",
            used=False
        )
        self._dmrs_additional_position = ConfigItem(
            key="dmrs_additional_position",
            value=2,
            comment="Sets the additional DMRS positions for PDSCH. Supported: [0 - 3].",
            used=False
        )
        self._rv_sequence = ConfigItem(
            key="rv_sequence",
            value=[0,2,3,1],
            comment="Sets the redundancy version sequence to use for PDSCH. Supported: any combination of [0, 1, 2, 3].",
            used=False
        )

    @property
    def min_ue_mcs(self):
        """Get or set the minimum PDSCH MCS value for UEs."""
        return self._min_ue_mcs.value

    @min_ue_mcs.setter
    def min_ue_mcs(self, value):
        self._min_ue_mcs.value = value

    @property
    def max_ue_mcs(self):
        """Get or set the maximum PDSCH MCS value for UEs."""
        return self._max_ue_mcs.value

    @max_ue_mcs.setter
    def max_ue_mcs(self, value):
        self._max_ue_mcs.value = value

    @property
    def fixed_rar_mcs(self):
        """Get or set the fixed RAR MCS value."""
        return self._fixed_rar_mcs.value

    @fixed_rar_mcs.setter
    def fixed_rar_mcs(self, value):
        self._fixed_rar_mcs.value = value

    @property
    def fixed_sib1_mcs(self):
        """Get or set the fixed SIB1 MCS value."""
        return self._fixed_sib1_mcs.value

    @fixed_sib1_mcs.setter
    def fixed_sib1_mcs(self, value):
        self._fixed_sib1_mcs.value = value

    @property
    def nof_harqs(self):
        """Get or set the number of Downlink HARQ processes."""
        return self._nof_harqs.value

    @nof_harqs.setter
    def nof_harqs(self, value):
        self._nof_harqs.value = value

    @property
    def max_nof_harq_retxs(self):
        """Get or set the maximum number of HARQ retransmissions."""
        return self._max_nof_harq_retxs.value

    @max_nof_harq_retxs.setter
    def max_nof_harq_retxs(self, value):
        self._max_nof_harq_retxs.value = value

    @property
    def max_consecutive_kos(self):
        """Get or set the maximum number of consecutive HARQ-ACK KOs before reporting an RLF."""
        return self._max_consecutive_kos.value

    @max_consecutive_kos.setter
    def max_consecutive_kos(self, value):
        self._max_consecutive_kos.value = value

    @property
    def mcs_table(self):
        """Get or set the MCS table used for PDSCH."""
        return self._mcs_table.value

    @mcs_table.setter
    def mcs_table(self, value):
        self._mcs_table.value = value

    @property
    def min_rb_size(self):
        """Get or set the minimum RB size for PDSCH resource allocation."""
        return self._min_rb_size.value

    @min_rb_size.setter
    def min_rb_size(self, value):
        self._min_rb_size.value = value

    @property
    def max_rb_size(self):
        """Get or set the maximum RB size for PDSCH resource allocation."""
        return self._max_rb_size.value

    @max_rb_size.setter
    def max_rb_size(self, value):
        self._max_rb_size.value = value

    @property
    def start_rb(self):
        """Get or set the start RB for PDSCH resource allocation."""
        return self._start_rb.value

    @start_rb.setter
    def start_rb(self, value):
        self._start_rb.value = value

    @property
    def end_rb(self):
        """Get or set the end RB for PDSCH resource allocation."""
        return self._end_rb.value

    @end_rb.setter
    def end_rb(self, value):
        self._end_rb.value = value

    @property
    def max_pdschs_per_slot(self):
        """Get or set the maximum number of PDSCH grants per slot."""
        return self._max_pdschs_per_slot.value

    @max_pdschs_per_slot.setter
    def max_pdschs_per_slot(self, value):
        self._max_pdschs_per_slot.value = value

    @property
    def max_alloc_attempts(self):
        """Get or set the maximum number of allocation attempts per slot."""
        return self._max_alloc_attempts.value

    @max_alloc_attempts.setter
    def max_alloc_attempts(self, value):
        self._max_alloc_attempts.value = value

    @property
    def olla_cqi_inc_step(self):
        """Get or set the OLLA CQI increment step."""
        return self._olla_cqi_inc_step.value

    @olla_cqi_inc_step.setter
    def olla_cqi_inc_step(self, value):
        self._olla_cqi_inc_step.value = value

    @property
    def olla_target_bler(self):
        """Get or set the OLLA target BLER."""
        return self._olla_target_bler.value

    @olla_target_bler.setter
    def olla_target_bler(self, value):
        self._olla_target_bler.value = value

    @property
    def olla_max_cqi_offset(self):
        """Get or set the maximum CQI offset for OLLA."""
        return self._olla_max_cqi_offset.value

    @olla_max_cqi_offset.setter
    def olla_max_cqi_offset(self, value):
        self._olla_max_cqi_offset.value = value

    @property
    def dc_offset(self):
        """Get or set the DC offset for PDSCH in subcarriers."""
        return self._dc_offset.value

    @dc_offset.setter
    def dc_offset(self, value):
        self._dc_offset.value = value

    @property
    def harq_la_cqi_drop_threshold(self):
        """Get or set the HARQ Link Adaptation CQI drop threshold."""
        return self._harq_la_cqi_drop_threshold.value

    @harq_la_cqi_drop_threshold.setter
    def harq_la_cqi_drop_threshold(self, value):
        self._harq_la_cqi_drop_threshold.value = value

    @property
    def harq_la_ri_drop_threshold(self):
        """Get or set the HARQ Link Adaptation RI drop threshold."""
        return self._harq_la_ri_drop_threshold.value

    @harq_la_ri_drop_threshold.setter
    def harq_la_ri_drop_threshold(self, value):
        self._harq_la_ri_drop_threshold.value = value

    @property
    def dmrs_additional_position(self):
        """Get or set the additional DMRS positions for PDSCH."""
        return self._dmrs_additional_position.value

    @dmrs_additional_position.setter
    def dmrs_additional_position(self, value):
        self._dmrs_additional_position.value = value