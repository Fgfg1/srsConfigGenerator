from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Non_rt(CommonConfig):
    def __init__(self, name="NonRtConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem

        # Optional UINT (4). Sets the number of non real time threads for processing of CP and UP data in upper layers.
        self._nof_non_rt_threads = ConfigItem(
            key="nof_non_rt_threads",
            value=4,
            comment="Number of non-real-time threads",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._nof_non_rt_threads
        ]

    # Getter and setter for ConfigItem
    @property
    def nof_non_rt_threads(self):
        return self._nof_non_rt_threads.value

    @nof_non_rt_threads.setter
    def nof_non_rt_threads(self, value):
        self._nof_non_rt_threads.set_value(value)
