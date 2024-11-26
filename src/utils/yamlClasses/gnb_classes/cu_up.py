from .cu_up_classes.upf import Upf
from config_item import ConfigItem
from common_conf import CommonConfig

class Cu_up(CommonConfig):
    def __init__(self, name="CuUpConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.gtpu_queue_size = ConfigItem(
            key="gtpu_queue_size",
            value=2048,
            comment="Size of the GTP-U queue",
            used=False,
        )
        self.gtpu_reordering_timer = ConfigItem(
            key="gtpu_reordering_timer",
            value=0,
            comment="GTP-U reordering timer in milliseconds",
            used=False,
        )
        self.warn_on_drop = ConfigItem(
            key="warn_on_drop",
            value=False,
            comment="Issue a warning when packets are dropped",
            used=False,
        )

        # Sub-configuration
        self.upf = Upf()

    # Getters and setters for ConfigItems
    @property
    def gtpu_queue_size(self):
        return self.gtpu_queue_size.value

    @gtpu_queue_size.setter
    def gtpu_queue_size(self, value):
        self.gtpu_queue_size.set_value(value)

    @property
    def gtpu_reordering_timer(self):
        return self.gtpu_reordering_timer.value

    @gtpu_reordering_timer.setter
    def gtpu_reordering_timer(self, value):
        self.gtpu_reordering_timer.set_value(value)

    @property
    def warn_on_drop(self):
        return self.warn_on_drop.value

    @warn_on_drop.setter
    def warn_on_drop(self, value):
        self.warn_on_drop.set_value(value)
