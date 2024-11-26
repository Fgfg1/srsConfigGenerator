from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Srs(CommonConfig):
    def __init__(self, name="SrsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._srs_period_ms = ConfigItem(
            key="srs_period_ms",
            value=None,
            comment="SRS periodicity in milliseconds",
            used=False,
        )
        self._srs_max_nof_sym_per_slot = ConfigItem(
            key="srs_max_nof_sym_per_slot",
            value=2,
            comment="Maximum number of SRS symbols per slot",
            used=False,
        )
        self._srs_nof_sym_per_resource = ConfigItem(
            key="srs_nof_sym_per_resource",
            value=1,
            comment="Number of symbols per SRS resource",
            used=False,
        )
        self._srs_tx_comb = ConfigItem(
            key="srs_tx_comb",
            value=4,
            comment="Transmission comb for SRS",
            used=False,
        )
        self._srs_cyclic_shift_reuse = ConfigItem(
            key="srs_cyclic_shift_reuse",
            value=1,
            comment="Cyclic shift reuse for SRS",
            used=False,
        )
        self._srs_sequence_id_reuse = ConfigItem(
            key="srs_sequence_id_reuse",
            value=1,
            comment="Sequence ID reuse for SRS",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def srs_period_ms(self):
        return self._srs_period_ms.value

    @srs_period_ms.setter
    def srs_period_ms(self, value):
        self._srs_period_ms.set_value(value)

    @property
    def srs_max_nof_sym_per_slot(self):
        return self._srs_max_nof_sym_per_slot.value

    @srs_max_nof_sym_per_slot.setter
    def srs_max_nof_sym_per_slot(self, value):
        self._srs_max_nof_sym_per_slot.set_value(value)

    @property
    def srs_nof_sym_per_resource(self):
        return self._srs_nof_sym_per_resource.value

    @srs_nof_sym_per_resource.setter
    def srs_nof_sym_per_resource(self, value):
        self._srs_nof_sym_per_resource.set_value(value)

    @property
    def srs_tx_comb(self):
        return self._srs_tx_comb.value

    @srs_tx_comb.setter
    def srs_tx_comb(self, value):
        self._srs_tx_comb.set_value(value)

    @property
    def srs_cyclic_shift_reuse(self):
        return self._srs_cyclic_shift_reuse.value

    @srs_cyclic_shift_reuse.setter
    def srs_cyclic_shift_reuse(self, value):
        self._srs_cyclic_shift_reuse.set_value(value)

    @property
    def srs_sequence_id_reuse(self):
        return self._srs_sequence_id_reuse.value

    @srs_sequence_id_reuse.setter
    def srs_sequence_id_reuse(self, value):
        self._srs_sequence_id_reuse.set_value(value)
