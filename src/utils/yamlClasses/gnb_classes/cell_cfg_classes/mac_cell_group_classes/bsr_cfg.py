from common_conf import CommonConfig
from config_item import ConfigItem

class Bsr_cfg(CommonConfig):
    def __init__(self, name="BsrConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items
        self.periodic_bsr_timer = ConfigItem(
            key="periodic_bsr_timer",
            value=10,
            comment="Sets the periodic BSR timer in milliseconds. Supported: [0, 10, 20, 40, 60, 80, 120, 160, 320, 640, 1280, 2560, 5120, 10240].",
            used=False
        )
        self.retx_bsr_timer = ConfigItem(
            key="retx_bsr_timer",
            value=80,
            comment="Sets the retransmission BSR timer in milliseconds. Supported: [0, 10, 20, 40, 60, 80, 120, 160, 320, 640, 1280, 2560, 5120, 10240].",
            used=False
        )
        self.lc_sr_delay_timer = ConfigItem(
            key="lc_sr_delay_timer",
            value=None,
            comment="Sets the LC SR delay timer in milliseconds. Supported: non-negative integer or None.",
            used=False
        )

    # Getters and setters for ConfigItems
    @property
    def periodic_bsr_timer(self):
        """Get or set the periodic BSR timer."""
        return self._periodic_bsr_timer.value

    @periodic_bsr_timer.setter
    def periodic_bsr_timer(self, value):
        self._periodic_bsr_timer.value = value

    @property
    def retx_bsr_timer(self):
        """Get or set the retransmission BSR timer."""
        return self._retx_bsr_timer.value

    @retx_bsr_timer.setter
    def retx_bsr_timer(self, value):
        self._retx_bsr_timer.value = value

    @property
    def lc_sr_delay_timer(self):
        """Get or set the LC SR delay timer."""
        return self._lc_sr_delay_timer.value

    @lc_sr_delay_timer.setter
    def lc_sr_delay_timer(self, value):
        self._lc_sr_delay_timer.value = value
