from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Lower_phy(CommonConfig):
    def __init__(self, name="lower_phy", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem

        # Optional TEXT (quad). Sets the lower physical layer executor profile. Supported: [single, dual, quad].
        self._execution_profile = ConfigItem(
            key="execution_profile",
            value="quad",
            comment="Execution profile for lower PHY (e.g., 'quad', 'dual', 'single')",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._execution_profile
        ]


    # Getter and setter for ConfigItem
    @property
    def execution_profile(self):
        return self._execution_profile.value

    @execution_profile.setter
    def execution_profile(self, value):
        self._execution_profile.set_value(value)
