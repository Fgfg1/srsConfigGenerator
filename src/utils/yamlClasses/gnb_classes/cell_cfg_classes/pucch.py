from common_conf import CommonConfig
from config_item import ConfigItem

class Pucch(CommonConfig):
    def __init__(self, name="PucchConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes as ConfigItem instances
        self.p0_nominal = ConfigItem(
            key="p0_nominal",
            value=-90,
            comment="Power control parameter P0 for PUCCH transmissions in dBm. Supported: [-202, 24] (multiples of 2).",
            used=False
        )
        self.pucch_resource_common = ConfigItem(
            key="pucch_resource_common",
            value=11,
            comment="Index of PUCCH resource set for the common configuration. Supported: [0 - 15].",
            used=False
        )
        self.sr_period_ms = ConfigItem(
            key="sr_period_ms",
            value=20,
            comment="Sets the Scheduling Request (SR) period in milliseconds. Supported: [1, 2, 4, 8, 10, 16, 20, 40, 80, 160, 320].",
            used=False
        )
        self.use_format_0 = ConfigItem(
            key="use_format_0",
            value=False,
            comment="Enables the use of Format 0 for PUCCH resources from resource set 0. Supported: [True, False].",
            used=False
        )
        self.nof_ue_res_harq_per_set = ConfigItem(
            key="nof_ue_res_harq_per_set",
            value=8,
            comment="Number of PUCCH resources available per UE for HARQ in each resource set. Supported: [1 - 8].",
            used=False
        )
        self.f0_or_f1_nof_cell_res_sr = ConfigItem(
            key="f0_or_f1_nof_cell_res_sr",
            value=8,
            comment="Number of PUCCH F0 or F1 resources available per cell for SR. Supported: [1 - 50].",
            used=False
        )
        self.f0_intraslot_freq_hop = ConfigItem(
            key="f0_intraslot_freq_hop",
            value=False,
            comment="Enables intra-slot frequency hopping for PUCCH F0. Supported: [True, False].",
            used=False
        )
        self.f1_enable_occ = ConfigItem(
            key="f1_enable_occ",
            value=True,
            comment="Enables OCC for PUCCH F1. Supported: [True, False].",
            used=False
        )
        self.f1_nof_cyclic_shifts = ConfigItem(
            key="f1_nof_cyclic_shifts",
            value=2,
            comment="Number of possible cyclic shifts for PUCCH F1. Supported: [1, 2, 3, 4, 6, 12].",
            used=False
        )
        self.f1_intraslot_freq_hop = ConfigItem(
            key="f1_intraslot_freq_hop",
            value=False,
            comment="Enables intra-slot frequency hopping for PUCCH F1. Supported: [True, False].",
            used=False
        )
        self.nof_cell_harq_pucch_res_sets = ConfigItem(
            key="nof_cell_harq_pucch_res_sets",
            value=2,
            comment="Number of separate PUCCH resource sets for HARQ-ACK in the cell. Supported: [1 - 10].",
            used=False
        )
        self.f2_nof_cell_res_csi = ConfigItem(
            key="f2_nof_cell_res_csi",
            value=8,
            comment="Number of PUCCH F2 resources available per cell for CSI. Supported: [0 - 50].",
            used=False
        )
        self.f2_max_nof_rbs = ConfigItem(
            key="f2_max_nof_rbs",
            value=1,
            comment="Maximum number of RBs for PUCCH F2 resources. Supported: [1 - 16].",
            used=False
        )
        self.f2_max_payload = ConfigItem(
            key="f2_max_payload",
            value=None,
            comment="Maximum payload bits for PUCCH F2 resources. Supported: [1 - 11].",
            used=False
        )
        self.f2_max_code_rate = ConfigItem(
            key="f2_max_code_rate",
            value="dot35",
            comment="Maximum code rate for PUCCH F2. Supported: [dot08, dot15, dot25, dot35, dot45, dot60, dot80].",
            used=False
        )
        self.f2_intraslot_freq_hop = ConfigItem(
            key="f2_intraslot_freq_hop",
            value=False,
            comment="Enables intra-slot frequency hopping for PUCCH F2. Supported: [True, False].",
            used=False
        )
        self.min_k1 = ConfigItem(
            key="min_k1",
            value=4,
            comment="Minimum value of K1 (difference in slots between PDSCH and HARQ-ACK). Supported: [1 - 4].",
            used=False
        )
        self.max_consecutive_kos = ConfigItem(
            key="max_consecutive_kos",
            value=100,
            comment="Maximum number of consecutive undecoded PUCCH F2 for CSI before an RLF is reported. Supported: [0 - inf].",
            used=False
        )

    # Getters and Setters
    @property
    def p0_nominal(self):
        """Get or set the P0 nominal value for PUCCH transmissions."""
        return self._p0_nominal

    @p0_nominal.setter
    def p0_nominal(self, value):
        self._p0_nominal = value

    @property
    def pucch_resource_common(self):
        """Get or set the PUCCH resource common index."""
        return self._pucch_resource_common

    @pucch_resource_common.setter
    def pucch_resource_common(self, value):
        self._pucch_resource_common = value

    @property
    def sr_period_ms(self):
        """Get or set the Scheduling Request (SR) period in milliseconds."""
        return self._sr_period_ms

    @sr_period_ms.setter
    def sr_period_ms(self, value):
        self._sr_period_ms = value

    @property
    def use_format_0(self):
        """Get or set whether Format 0 is used for PUCCH resources."""
        return self._use_format_0

    @use_format_0.setter
    def use_format_0(self, value):
        self._use_format_0 = value

    @property
    def nof_ue_res_harq_per_set(self):
        """Get or set the number of UE resources per set for HARQ."""
        return self._nof_ue_res_harq_per_set

    @nof_ue_res_harq_per_set.setter
    def nof_ue_res_harq_per_set(self, value):
        self._nof_ue_res_harq_per_set = value

    @property
    def f0_or_f1_nof_cell_res_sr(self):
        """Get or set the number of F0 or F1 cell resources for SR."""
        return self._f0_or_f1_nof_cell_res_sr

    @f0_or_f1_nof_cell_res_sr.setter
    def f0_or_f1_nof_cell_res_sr(self, value):
        self._f0_or_f1_nof_cell_res_sr = value

    @property
    def f0_intraslot_freq_hop(self):
        """Get or set whether intra-slot frequency hopping is enabled for F0."""
        return self._f0_intraslot_freq_hop

    @f0_intraslot_freq_hop.setter
    def f0_intraslot_freq_hop(self, value):
        self._f0_intraslot_freq_hop = value

    @property
    def f1_enable_occ(self):
        """Get or set whether OCC is enabled for F1."""
        return self._f1_enable_occ

    @f1_enable_occ.setter
    def f1_enable_occ(self, value):
        self._f1_enable_occ = value

    @property
    def f1_nof_cyclic_shifts(self):
        """Get or set the number of cyclic shifts for F1."""
        return self._f1_nof_cyclic_shifts

    @f1_nof_cyclic_shifts.setter
    def f1_nof_cyclic_shifts(self, value):
        self._f1_nof_cyclic_shifts = value

    @property
    def f1_intraslot_freq_hop(self):
        """Get or set whether intra-slot frequency hopping is enabled for F1."""
        return self._f1_intraslot_freq_hop

    @f1_intraslot_freq_hop.setter
    def f1_intraslot_freq_hop(self, value):
        self._f1_intraslot_freq_hop = value

    @property
    def nof_cell_harq_pucch_res_sets(self):
        """Get or set the number of HARQ PUCCH resource sets per cell."""
        return self._nof_cell_harq_pucch_res_sets

    @nof_cell_harq_pucch_res_sets.setter
    def nof_cell_harq_pucch_res_sets(self, value):
        self._nof_cell_harq_pucch_res_sets = value

    @property
    def f2_nof_cell_res_csi(self):
        """Get or set the number of F2 cell resources available for CSI."""
        return self._f2_nof_cell_res_csi

    @f2_nof_cell_res_csi.setter
    def f2_nof_cell_res_csi(self, value):
        self._f2_nof_cell_res_csi = value

    @property
    def f2_max_nof_rbs(self):
        """Get or set the maximum number of RBs for F2 resources."""
        return self._f2_max_nof_rbs

    @f2_max_nof_rbs.setter
    def f2_max_nof_rbs(self, value):
        self._f2_max_nof_rbs = value

    @property
    def f2_max_payload(self):
        """Get or set the maximum payload for F2 resources."""
        return self._f2_max_payload

    @f2_max_payload.setter
    def f2_max_payload(self, value):
        self._f2_max_payload = value

    @property
    def f2_max_code_rate(self):
        """Get or set the maximum code rate for F2."""
        return self._f2_max_code_rate

    @f2_max_code_rate.setter
    def f2_max_code_rate(self, value):
        self._f2_max_code_rate = value

    @property
    def f2_intraslot_freq_hop(self):
        """Get or set whether intra-slot frequency hopping is enabled for F2."""
        return self._f2_intraslot_freq_hop

    @f2_intraslot_freq_hop.setter
    def f2_intraslot_freq_hop(self, value):
        self._f2_intraslot_freq_hop = value

    @property
    def min_k1(self):
        """Get or set the minimum value of K1 (difference in slots)."""
        return self._min_k1

    @min_k1.setter
    def min_k1(self, value):
        self._min_k1 = value

    @property
    def max_consecutive_kos(self):
        """Get or set the maximum number of consecutive undecoded packets."""
        return self._max_consecutive_kos

    @max_consecutive_kos.setter
    def max_consecutive_kos(self, value):
        self._max_consecutive_kos = value