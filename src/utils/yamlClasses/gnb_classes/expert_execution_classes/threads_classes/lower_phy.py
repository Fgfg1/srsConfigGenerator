from config_item import ConfigItem
from common_conf import CommonConfig

class Lower_phy(CommonConfig):
    def __init__(self, name="LowerPhyConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem
        self.execution_profile = ConfigItem(
            key="execution_profile",
            value="quad",
            comment="Execution profile for lower PHY (e.g., 'quad', 'dual', 'single')",
            used=False,
        )

    # Getter and setter for ConfigItem
    @property
    def execution_profile(self):
        return self.execution_profile.value

    @execution_profile.setter
    def execution_profile(self, value):
        self.execution_profile.set_value(value)