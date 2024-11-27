from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Amplitude_control(CommonConfig):
    def __init__(self, name="AmplitudeControlConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional FLOAT (12.0). Sets baseband gain back-off in dB. This accounts for the signal PAPR and is applied regardless of clipping settings. Format: positive float.
        self._tx_gain_backoff = ConfigItem(
            key="tx_gain_backoff",
            value=12.0,
            comment="Transmit gain backoff in dB",
            used=False,
        )

        # Optional BOOLEAN (false). Sets clipping of the baseband samples on or off. If enabled, samples that exceed the power ceiling are clipped.
        self._enable_clipping = ConfigItem(
            key="enable_clipping",
            value=False,
            comment="Enable signal clipping",
            used=False,
        )

        # Optional FLOAT (-0.1). Sets the power ceiling in dB, relative to the full scale amplitude of the radio. Format: negative float or 0.
        self._ceiling = ConfigItem(
            key="ceiling",
            value=-0.1,
            comment="Clipping ceiling level",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._tx_gain_backoff,
            self._enable_clipping,
            self._ceiling
        ]

    # Getters and setters for ConfigItems
    @property
    def tx_gain_backoff(self):
        return self._tx_gain_backoff.value

    @tx_gain_backoff.setter
    def tx_gain_backoff(self, value):
        self._tx_gain_backoff.set_value(value)

    @property
    def enable_clipping(self):
        return self._enable_clipping.value

    @enable_clipping.setter
    def enable_clipping(self, value):
        self._enable_clipping.set_value(value)

    @property
    def ceiling(self):
        return self._ceiling.value

    @ceiling.setter
    def ceiling(self, value):
        self._ceiling.set_value(value)
