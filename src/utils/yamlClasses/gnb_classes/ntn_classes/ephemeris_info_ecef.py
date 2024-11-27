from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ephemeris_info_ecef(CommonConfig):
    def __init__(self, name="EphemerisInfoECEFConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional INT (0). Sets the X position of the satellite. Supported: [-67108864 - 67108863].
        self._pos_x = ConfigItem(
            key="pos_x",
            value=0,
            comment="ECEF position X-coordinate in meters",
            used=False,
        )

        # Optional INT (0). Sets the Y position of the satellite. Supported: [-67108864 - 67108863].
        self._pos_y = ConfigItem(
            key="pos_y",
            value=0,
            comment="ECEF position Y-coordinate in meters",
            used=False,
        )

        # Optional INT (0). Sets the Z position of the satellite. Supported: [-67108864 - 67108863].
        self._pos_z = ConfigItem(
            key="pos_z",
            value=0,
            comment="ECEF position Z-coordinate in meters",
            used=False,
        )

        # Optional INT (0). Sets the X velocity of the satellite. Supported: [-32768 - 32767].
        self._vel_x = ConfigItem(
            key="vel_x",
            value=0,
            comment="ECEF velocity X-component in meters/second",
            used=False,
        )

        # Optional INT (0). Sets the Y velocity of the satellite. Supported: [-32768 - 32767].
        self._vel_y = ConfigItem(
            key="vel_y",
            value=0,
            comment="ECEF velocity Y-component in meters/second",
            used=False,
        )

        # Optional INT (0). Sets the Z velocity of the satellite. Supported: [-32768 - 32767].
        self._vel_z = ConfigItem(
            key="vel_z",
            value=0,
            comment="ECEF velocity Z-component in meters/second",
            used=False,
        )
        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._pos_x,
            self._pos_y,
            self._pos_z,
            self._vel_x,
            self._vel_y,
            self._vel_z
        ]

    # Getters and setters for ConfigItems
    @property
    def pos_x(self):
        return self._pos_x.value

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x.set_value(value)

    @property
    def pos_y(self):
        return self._pos_y.value

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y.set_value(value)

    @property
    def pos_z(self):
        return self._pos_z.value

    @pos_z.setter
    def pos_z(self, value):
        self._pos_z.set_value(value)

    @property
    def vel_x(self):
        return self._vel_x.value

