from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

# Buffer status report configuration parameters

class Bsr_cfg(CommonConfig):
    def __init__(self, name="bsr_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration Items

        # Optional UINT (10). Sets the periodic Buffer Status Report Timer value in nof. subframes. Value 0 equates to infinity. Supported: [1, 5, 10, 16, 20, 32, 40, 64, 80, 128, 160, 320, 640, 1280, 2560, 0].
        self._periodic_bsr_timer = ConfigItem(
            key="periodic_bsr_timer",
            value=10,
            comment="Sets the periodic BSR timer in milliseconds. Supported: [0, 10, 20, 40, 60, 80, 120, 160, 320, 640, 1280, 2560, 5120, 10240].",
            used=False
        )

        # Optional UINT (80). sets the retransmission Buffer Status Report Timer value in nof. subframes. Supported: [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240].
        self._retx_bsr_timer = ConfigItem(
            key="retx_bsr_timer",
            value=80,
            comment="Sets the retransmission BSR timer in milliseconds. Supported: [0, 10, 20, 40, 60, 80, 120, 160, 320, 640, 1280, 2560, 5120, 10240].",
            used=False
        )

        # Optional TEXT. Sets the logical Channel SR delay timer in nof. subframes. Supported: [10, 20, 40, 80, 160, 320, 640, 1280, 2560].
        self._lc_sr_delay_timer = ConfigItem(
            key="lc_sr_delay_timer",
            value=None,
            comment="Sets the LC SR delay timer in milliseconds. Supported: non-negative integer or None.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._periodic_bsr_timer,
            self._retx_bsr_timer,
            self._lc_sr_delay_timer
        ]

    # Getters and setters for ConfigItems
    @property
    def periodic_bsr_timer(self):
        """Get or set the periodic BSR timer."""
        return self.__periodic_bsr_timer.value

    @periodic_bsr_timer.setter
    def periodic_bsr_timer(self, value):
        self.__periodic_bsr_timer.value = value

    @property
    def retx_bsr_timer(self):
        """Get or set the retransmission BSR timer."""
        return self.__retx_bsr_timer.value

    @retx_bsr_timer.setter
    def retx_bsr_timer(self, value):
        self.__retx_bsr_timer.value = value

    @property
    def lc_sr_delay_timer(self):
        """Get or set the LC SR delay timer."""
        return self.__lc_sr_delay_timer.value

    @lc_sr_delay_timer.setter
    def lc_sr_delay_timer(self, value):
        self.__lc_sr_delay_timer.value = value
