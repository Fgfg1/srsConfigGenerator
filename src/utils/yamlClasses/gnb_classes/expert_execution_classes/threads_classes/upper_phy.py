from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Upper_phy(CommonConfig):
    def __init__(self, name="UpperPhyConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._pdsch_processor_type = ConfigItem(
            key="pdsch_processor_type",
            value="auto",
            comment="Type of PDSCH processor (e.g., 'auto', 'manual')",
            used=False,
        )
        self._nof_pusch_decoder_threads = ConfigItem(
            key="nof_pusch_decoder_threads",
            value=1,
            comment="Number of threads for PUSCH decoding",
            used=False,
        )
        self._nof_ul_threads = ConfigItem(
            key="nof_ul_threads",
            value=1,
            comment="Number of threads for uplink processing",
            used=False,
        )
        self._nof_dl_threads = ConfigItem(
            key="nof_dl_threads",
            value=4,
            comment="Number of threads for downlink processing",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def pdsch_processor_type(self):
        return self._pdsch_processor_type.value

    @pdsch_processor_type.setter
    def pdsch_processor_type(self, value):
        self._pdsch_processor_type.set_value(value)

    @property
    def nof_pusch_decoder_threads(self):
        return self._nof_pusch_decoder_threads.value

    @nof_pusch_decoder_threads.setter
    def nof_pusch_decoder_threads(self, value):
        self._nof_pusch_decoder_threads.set_value(value)

    @property
    def nof_ul_threads(self):
        return self._nof_ul_threads.value

    @nof_ul_threads.setter
    def nof_ul_threads(self, value):
        self._nof_ul_threads.set_value(value)

    @property
    def nof_dl_threads(self):
        return self._nof_dl_threads.value

    @nof_dl_threads.setter
    def nof_dl_threads(self, value):
        self._nof_dl_threads.set_value(value)
