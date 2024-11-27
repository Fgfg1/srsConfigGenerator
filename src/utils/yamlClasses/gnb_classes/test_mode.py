from .test_mode_classes.test_ue import Test_ue
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Test_mode(CommonConfig):
    def __init__(self, name="test_mode", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional BOOLEAN (false). Set to true to enable CU-UP test mode. Supported: [true, false].
        self._enable = ConfigItem(
            key="enable", value=False, comment="Enable CU-UP test mode", used=False
        )

        # Optional BOOLEAN (false). Set to true to enable PDCP integrity testing. Supported: [true, false].
        self._integrity_enable = ConfigItem(
            key="integrity_enable", value=False, comment="Enable PDCP integrity testing", used=False
        )

        # Optional BOOLEAN (false). Set to true to enable PDCP ciphering testing. Supported: [true, false].
        self._ciphering_enable = ConfigItem(
            key="ciphering_enable", value=False, comment="Enable PDCP ciphering testing", used=False
        )

        # Optional UINT (2). Sets the NEA algo to use for testing. Supported: [0, 1, 2, 3].
        self._nea_algo = ConfigItem(
            key="nea_algo", value=2, comment="Sets the NEA algorithm for testing. Supported: [0, 1, 2, 3]", used=False
        )

        # Optional UINT (2). Sets the NIA algo to use for testing. Supported: [1, 2, 3].
        self._nia_algo = ConfigItem(
            key="nia_algo", value=2, comment="Sets the NIA algorithm for testing. Supported: [1, 2, 3]", used=False
        )
        
        # Sub-modules
        self._test_ue = Test_ue()

        self._variables = [
            self._enable,
            self._integrity_enable,
            self._ciphering_enable,
            self._nea_algo,
            self._nia_algo,
            self._test_ue
        ]



    # Expose ConfigItem attributes via properties for compatibility
    @property
    def enable(self):
        return self._enable.value

    @enable.setter
    def enable(self, value):
        self._enable.set_value(value)

    @property
    def integrity_enable(self):
        return self._integrity_enable.value

    @integrity_enable.setter
    def integrity_enable(self, value):
        self._integrity_enable.set_value(value)

    @property
    def ciphering_enable(self):
        return self._ciphering_enable.value

    @ciphering_enable.setter
    def ciphering_enable(self, value):
        self._ciphering_enable.set_value(value)

    @property
    def nea_algo(self):
        return self._nea_algo.value

    @nea_algo.setter
    def nea_algo(self, value):
        self._nea_algo.set_value(value)

    @property
    def nia_algo(self):
        return self._nia_algo.value

    @nia_algo.setter
    def nia_algo(self, value):
        self._nia_algo.set_value(value)
