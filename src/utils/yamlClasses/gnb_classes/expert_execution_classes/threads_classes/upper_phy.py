from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Upper_phy(CommonConfig):
    def __init__(self, name="upper_phy", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT (auto). Sets the PDSCH processor type. Supported: [auto, generic, concurrent, lite].
        self._pdsch_processor_type = ConfigItem(
            key="pdsch_processor_type",
            value="auto",
            comment="Type of PDSCH processor (e.g., 'auto', 'manual')",
            used=False,
        )

        # Optional UINT (1). Sets the number of threads used to encode PUSCH.
        self._nof_pusch_decoder_threads = ConfigItem(
            key="nof_pusch_decoder_threads",
            value=1,
            comment="Number of threads for PUSCH decoding",
            used=False,
        )

        # Optional UINT (1). Sets the number of upprt PHY threads to proccess uplink.
        self._nof_ul_threads = ConfigItem(
            key="nof_ul_threads",
            value=1,
            comment="Number of threads for uplink processing",
            used=False,
        )

        # Optional UINT (1). Sets the number of upprt PHY threads to proccess downlink.
        self._nof_dl_threads = ConfigItem(
            key="nof_dl_threads",
            value=4,
            comment="Number of threads for downlink processing",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._pdsch_processor_type,
            self._nof_pusch_decoder_threads,
            self._nof_ul_threads,
            self._nof_dl_threads
        ]

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
