from config_item import ConfigItem
from common_conf import CommonConfig

class Amplitude_control(CommonConfig):
    def __init__(self, name="AmplitudeControlConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.tx_gain_backoff = ConfigItem(
            key="tx_gain_backoff",
            value=12.0,
            comment="Transmit gain backoff in dB",
            used=False,
        )
        self.enable_clipping = ConfigItem(
            key="enable_clipping",
            value=False,
            comment="Enable signal clipping",
            used=False,
        )
        self.ceiling = ConfigItem(
            key="ceiling",
            value=-0.1,
            comment="Clipping ceiling level",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def tx_gain_backoff(self):
        return self.tx_gain_backoff.value

    @tx_gain_backoff.setter
    def tx_gain_backoff(self, value):
        self.tx_gain_backoff.set_value(value)

    @property
    def enable_clipping(self):
        return self.enable_clipping.value

    @enable_clipping.setter
    def enable_clipping(self, value):
        self.enable_clipping.set_value(value)

    @property
    def ceiling(self):
        return self.ceiling.value

    @ceiling.setter
    def ceiling(self, value):
        self.ceiling.set_value(value)
