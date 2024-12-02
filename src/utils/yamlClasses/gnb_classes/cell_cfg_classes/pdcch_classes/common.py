from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Common(CommonConfig):
    def __init__(self, name="common", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items

        # Optional INT. Sets the CORESET 0 index. Supported: [0 - 15].
        self._coreset0_index = ConfigItem(
            key="coreset0_index",
            value=None,
            comment="Sets the CORESET 0 index. Supported: [0 - 15].",
            used=False
        )

        # Optional UINT ({0, 0, 1, 0, 0}). Sets the number of PDCCH candidates per aggregation level for SearchSpace#1. Supported: any 5 value array containing the following UINT values [0, 1, 2, 3, 4, 5, 6, 7, 8].
        self._ss0_index = ConfigItem(
            key="ss0_index",
            value=0,
            comment="Sets the SearchSpace#0 index. Supported: [0 - 15].",
            used=False
        )

        # Optional UINT (0). Sets the SearchSpace#0 index. Supported: [0 - 15].
        self._max_coreset0_duration = ConfigItem(
            key="max_coreset0_duration",
            value=None,
            comment="Sets the maximum CORESET#0 duration in OFDM symbols. Supported: [1 - 2].",
            used=False
        )

        # Optional INT. Sets the maximum CORESET#0 duration in OFDM symbols to consider when deriving CORESET#0 index. Supported: [1 - 2].
        self._ss1_n_candidates = ConfigItem(
            key="ss1_n_candidates",
            value={0, 0, 1, 0, 0},
            comment="Sets the number of PDCCH candidates per aggregation level for SearchSpace#1. Supported: any 5 value array with values [0 - 8].",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._coreset0_index,
            self._ss1_n_candidates,
            self._ss0_index,
            self._max_coreset0_duration
        ]

    # Getters and setters for ConfigItems
    @property
    def coreset0_index(self):
        return self.__coreset0_index.value

    @coreset0_index.setter
    def coreset0_index(self, value):
        self.__coreset0_index.value = value

    @property
    def ss0_index(self):
        return self.__ss0_index.value

    @ss0_index.setter
    def ss0_index(self, value):
        self.__ss0_index.value = value

    @property
    def max_coreset0_duration(self):
        return self.__max_coreset0_duration.value

    @max_coreset0_duration.setter
    def max_coreset0_duration(self, value):
        self.__max_coreset0_duration.value = value

    @property
    def ss1_n_candidates(self):
        return self.__ss1_n_candidates.value

    @ss1_n_candidates.setter
    def ss1_n_candidates(self, value):
        self.__ss1_n_candidates.value = value
