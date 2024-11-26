from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Rrc(CommonConfig):
    def __init__(self, name="RrcConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._force_reestablishment_fallback = ConfigItem(
            key="force_reestablishment_fallback",
            value=False,
            comment="Force RRC reestablishment fallback on failure",
            used=False,
        )
        self._rrc_procedure_timeout_ms = ConfigItem(
            key="rrc_procedure_timeout_ms",
            value=720,
            comment="Timeout for RRC procedures in milliseconds",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def force_reestablishment_fallback(self):
        return self._force_reestablishment_fallback.value

    @force_reestablishment_fallback.setter
    def force_reestablishment_fallback(self, value):
        self._force_reestablishment_fallback.set_value(value)

    @property
    def rrc_procedure_timeout_ms(self):
        return self._rrc_procedure_timeout_ms.value

    @rrc_procedure_timeout_ms.setter
    def rrc_procedure_timeout_ms(self, value):
        self._rrc_procedure_timeout_ms.set_value(value)
