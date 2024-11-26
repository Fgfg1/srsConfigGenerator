from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Common(CommonConfig):
    def __init__(self, name="CommonConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items
        self._coreset0_index = ConfigItem(
            key="coreset0_index",
            value=None,
            comment="Sets the CORESET 0 index. Supported: [0 - 15].",
            used=False
        )
        self._ss0_index = ConfigItem(
            key="ss0_index",
            value=0,
            comment="Sets the SearchSpace#0 index. Supported: [0 - 15].",
            used=False
        )
        self._max_coreset0_duration = ConfigItem(
            key="max_coreset0_duration",
            value=None,
            comment="Sets the maximum CORESET#0 duration in OFDM symbols. Supported: [1 - 2].",
            used=False
        )
        self._ss1_n_candidates = ConfigItem(
            key="ss1_n_candidates",
            value={0, 0, 1, 0, 0},
            comment="Sets the number of PDCCH candidates per aggregation level for SearchSpace#1. Supported: any 5 value array with values [0 - 8].",
            used=False
        )

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
