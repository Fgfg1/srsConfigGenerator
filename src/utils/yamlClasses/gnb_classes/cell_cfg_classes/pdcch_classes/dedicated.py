from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Dedicated(CommonConfig):
    def __init__(self, name="dedicated", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items

        # Optional INT (0). Sets the starting common resource block (CRB) number for CORESET 1, relative to CRB0. Supported: [0 - 275].
        self._coreset1_rb_start = ConfigItem(
            key="coreset1_rb_start",
            value=1,
            comment="Starting common resource block (CRB) number for CORESET 1, relative to CRB0. Supported: [0 - 275].",
            used=False
        )

        # Optional INT (Across entire BW of cell). Sets the length of CORESET 1 in number of CRBs. Supported: [0 - 275].
        self._coreset1_l_crb = ConfigItem(
            key="coreset1_l_crb",
            value=None,
            comment="Length of CORESET 1 in number of CRBs. Supported: [0 - 275].",
            used=False
        )

        # Optional INT (Max(2, Nof. CORESET#0 symbols)). Sets the duration of CORESET 1 in number of OFDM symbols. Supported: [1 - 2].
        self._coreset1_duration = ConfigItem(
            key="coreset1_duration",
            value=None,
            comment="Duration of CORESET 1 in number of OFDM symbols. Supported: [1 - 2].",
            used=False
        )

        # Optional UINT ({0, 0, 0, 0, 0}). Sets the number of PDCCH candidates per aggregation level for SearchSpace#2. Supported: any 5 value array containing the following UINT values [0, 1, 2, 3, 4, 5, 6, 7, 8].
        self._dci_format_0_1_and_1_1 = ConfigItem(
            key="dci_format_0_1_and_1_1",
            value=True,
            comment="Use non-fallback or fallback DCI format in UE SearchSpace#2. Supported: [false, true].",
            used=False
        )

        # Optional BOOLEAN (true). Sets whether to use non-fallback or fallback DCI format in UE SearchSpace#2. Supported: [false, true].
        self._ss2_type = ConfigItem(
            key="ss2_type",
            value="ue_dedicated",
            comment="SearchSpace type for UE dedicated SearchSpace#2. Supported: [common, ue_dedicated].",
            used=False
        )

        # Optional TEXT (ue_dedicated). Sets the SearchSpace type for UE dedicated SearchSpace#2. Supported: [common, ue_dedicated].
        self._ss2_n_candidates = ConfigItem(
            key="ss2_n_candidates",
            value={0, 0, 0, 0, 0},
            comment="Number of PDCCH candidates per aggregation level for SearchSpace#2. Supported: [0, 1, 2, 3, 4, 5, 6, 7, 8].",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._coreset1_rb_start,
            self._coreset1_l_crb,
            self._coreset1_duration,
            self._ss2_n_candidates,
            self._dci_format_0_1_and_1_1,
            self._ss2_type
        ]

    # Property methods for ConfigItem values

    @property
    def coreset1_rb_start(self):
        return self.__coreset1_rb_start.value

    @coreset1_rb_start.setter
    def coreset1_rb_start(self, value):
        self.__coreset1_rb_start.value = value

    @property
    def coreset1_l_crb(self):
        return self.__coreset1_l_crb.value

    @coreset1_l_crb.setter
    def coreset1_l_crb(self, value):
        self.__coreset1_l_crb.value = value

    @property
    def coreset1_duration(self):
        return self.__coreset1_duration.value

    @coreset1_duration.setter
    def coreset1_duration(self, value):
        self.__coreset1_duration.value = value

    @property
    def dci_format_0_1_and_1_1(self):
        return self.__dci_format_0_1_and_1_1.value

    @dci_format_0_1_and_1_1.setter
    def dci_format_0_1_and_1_1(self, value):
        self.__dci_format_0_1_and_1_1.value = value

    @property
    def ss2_type(self):
        return self.__ss2_type.value

    @ss2_type.setter
    def ss2_type(self, value):
        self.__ss2_type.value = value

    @property
    def ss2_n_candidates(self):
        return self.__ss2_n_candidates.value

    @ss2_n_candidates.setter
    def ss2_n_candidates(self, value):
        self.__ss2_n_candidates.value = value
