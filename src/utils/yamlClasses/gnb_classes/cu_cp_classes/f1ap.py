from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class F1ap(CommonConfig):
    def __init__(self, name="f1ap", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem

        # Optional INT (1000). Sets the UE context setup timeout in milliseconds.
        self._procedure_timeout = ConfigItem(
            key="procedure_timeout",
            value=1000,
            comment="Timeout for F1AP procedures in milliseconds",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._procedure_timeout
        ]

    # Getter and setter for ConfigItem
    @property
    def procedure_timeout(self):
        return self._procedure_timeout.value

    @procedure_timeout.setter
    def procedure_timeout(self, value):
        self._procedure_timeout.set_value(value)
