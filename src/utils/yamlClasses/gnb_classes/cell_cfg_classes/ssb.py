from config_item import ConfigItem
from common_conf import CommonConfig

class Ssb(CommonConfig):
    def __init__(self, name="SsbConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.ssb_period = ConfigItem(
            key="ssb_period",
            value=10,
            comment="SSB period in milliseconds",
            used=False,
        )
        self.ssb_block_power_dbm = ConfigItem(
            key="ssb_block_power_dbm",
            value=-16,
            comment="SSB block power in dBm",
            used=False,
        )
        self.pss_to_sss_epre_db = ConfigItem(
            key="pss_to_sss_epre_db",
            value=0,
            comment="EPRE difference between PSS and SSS in dB",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def ssb_period(self):
        return self.ssb_period.value

    @ssb_period.setter
    def ssb_period(self, value):
        self.ssb_period.set_value(value)

    @property
    def ssb_block_power_dbm(self):
        return self.ssb_block_power_dbm.value

    @ssb_block_power_dbm.setter
    def ssb_block_power_dbm(self, value):
        self.ssb_block_power_dbm.set_value(value)

    @property
    def pss_to_sss_epre_db(self):
        return self.pss_to_sss_epre_db.value

    @pss_to_sss_epre_db.setter
    def pss_to_sss_epre_db(self, value):
        self.pss_to_sss_epre_db.set_value(value)
