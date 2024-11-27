from .cu_up_classes.upf import Upf
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Cu_up(CommonConfig):
    def __init__(self, name="cu-up", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional INT (2048). Sets the GTP-U queue size, in PDUs.
        self._gtpu_queue_size = ConfigItem(
            key="gtpu_queue_size",
            value=2048,
            comment="Size of the GTP-U queue",
            used=False,
        )

        # Optional INT (0). Sets the GTP-U RX reordering timer (in milliseconds).
        self._gtpu_reordering_timer = ConfigItem(
            key="gtpu_reordering_timer",
            value=0,
            comment="GTP-U reordering timer in milliseconds",
            used=False,
        )

        # Optional BOOLEAN (false). Enables the option to log a warning for dropped packets in GTP-U and PDCP due to full queues. Supported: [false, true].
        self._warn_on_drop = ConfigItem(
            key="warn_on_drop",
            value=False,
            comment="Issue a warning when packets are dropped",
            used=False,
        )

        # Sub-configuration
        self._upf = Upf()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._gtpu_queue_size,
            self._gtpu_reordering_timer,
            self._warn_on_drop,
            self._upf
        ]

    # Getters and setters for ConfigItems
    @property
    def gtpu_queue_size(self):
        return self._gtpu_queue_size.value

    @gtpu_queue_size.setter
    def gtpu_queue_size(self, value):
        self._gtpu_queue_size.set_value(value)

    @property
    def gtpu_reordering_timer(self):
        return self._gtpu_reordering_timer.value

    @gtpu_reordering_timer.setter
    def gtpu_reordering_timer(self, value):
        self._gtpu_reordering_timer.set_value(value)

    @property
    def warn_on_drop(self):
        return self._warn_on_drop.value

    @warn_on_drop.setter
    def warn_on_drop(self, value):
        self._warn_on_drop.set_value(value)
