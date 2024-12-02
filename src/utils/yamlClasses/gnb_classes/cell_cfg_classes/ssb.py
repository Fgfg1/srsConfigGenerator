from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ssb(CommonConfig):
    def __init__(self, name="ssb", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional UINT (10). Sets the period of SSB scheduling in milliseconds. Supported: [5, 10, 20].
        self._ssb_period = ConfigItem(
            key="ssb_period",
            value=10,
            comment="SSB period in milliseconds",
            used=False,
        )

        # Optional INT (-16). Sets the SS PBCH block power in dBm. Supported: [-60 - +50].
        self._ssb_block_power_dbm = ConfigItem(
            key="ssb_block_power_dbm",
            value=-16,
            comment="SSB block power in dBm",
            used=False,
        )

        # Optional UINT (0). Sets the Synchronization Signal Block Primary Synchronization Signal to Secondary Synchronization Signal Energy Per Resource Element ratio in dB. Supported: [0, 3].
        self._pss_to_sss_epre_db = ConfigItem(
            key="pss_to_sss_epre_db",
            value=0,
            comment="EPRE difference between PSS and SSS in dB",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._ssb_period,
            self._ssb_block_power_dbm,
            self._pss_to_sss_epre_db
        ]

    # Getters and setters for ConfigItems
    @property
    def ssb_period(self):
        return self._ssb_period.value

    @ssb_period.setter
    def ssb_period(self, value):
        self._ssb_period.set_value(value)

    @property
    def ssb_block_power_dbm(self):
        return self._ssb_block_power_dbm.value

    @ssb_block_power_dbm.setter
    def ssb_block_power_dbm(self, value):
        self._ssb_block_power_dbm.set_value(value)

    @property
    def pss_to_sss_epre_db(self):
        return self._pss_to_sss_epre_db.value

    @pss_to_sss_epre_db.setter
    def pss_to_sss_epre_db(self, value):
        self._pss_to_sss_epre_db.set_value(value)
