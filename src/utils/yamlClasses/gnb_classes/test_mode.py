from .test_mode_classes.test_ue import Test_ue
from config_item import ConfigItem
from common_conf import CommonConfig

class Test_mode(CommonConfig):
    def __init__(self, name="TestModeConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.enable = ConfigItem(
            key="enable", value=False, comment="Enable CU-UP test mode", used=False
        )
        self.integrity_enable = ConfigItem(
            key="integrity_enable", value=False, comment="Enable PDCP integrity testing", used=False
        )
        self.ciphering_enable = ConfigItem(
            key="ciphering_enable", value=False, comment="Enable PDCP ciphering testing", used=False
        )
        self.nea_algo = ConfigItem(
            key="nea_algo", value=2, comment="Sets the NEA algorithm for testing. Supported: [0, 1, 2, 3]", used=False
        )
        self.nia_algo = ConfigItem(
            key="nia_algo", value=2, comment="Sets the NIA algorithm for testing. Supported: [1, 2, 3]", used=False
        )
        self.test_ue = Test_ue()

    # Expose ConfigItem attributes via properties for compatibility
    @property
    def enable(self):
        return self.enable.value

    @enable.setter
    def enable(self, value):
        self.enable.set_value(value)

    @property
    def integrity_enable(self):
        return self.integrity_enable.value

    @integrity_enable.setter
    def integrity_enable(self, value):
        self.integrity_enable.set_value(value)

    @property
    def ciphering_enable(self):
        return self.ciphering_enable.value

    @ciphering_enable.setter
    def ciphering_enable(self, value):
        self.ciphering_enable.set_value(value)

    @property
    def nea_algo(self):
        return self.nea_algo.value

    @nea_algo.setter
    def nea_algo(self, value):
        self.nea_algo.set_value(value)

    @property
    def nia_algo(self):
        return self.nia_algo.value

    @nia_algo.setter
    def nia_algo(self, value):
        self.nia_algo.set_value(value)
