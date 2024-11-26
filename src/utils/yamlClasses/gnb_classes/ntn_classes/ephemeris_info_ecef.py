from config_item import ConfigItem
from common_conf import CommonConfig

class Ephemeris_info_ecef(CommonConfig):
    def __init__(self, name="EphemerisInfoECEFConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.pos_x = ConfigItem(
            key="pos_x",
            value=0,
            comment="ECEF position X-coordinate in meters",
            used=False,
        )
        self.pos_y = ConfigItem(
            key="pos_y",
            value=0,
            comment="ECEF position Y-coordinate in meters",
            used=False,
        )
        self.pos_z = ConfigItem(
            key="pos_z",
            value=0,
            comment="ECEF position Z-coordinate in meters",
            used=False,
        )
        self.vel_x = ConfigItem(
            key="vel_x",
            value=0,
            comment="ECEF velocity X-component in meters/second",
            used=False,
        )
        self.vel_y = ConfigItem(
            key="vel_y",
            value=0,
            comment="ECEF velocity Y-component in meters/second",
            used=False,
        )
        self.vel_z = ConfigItem(
            key="vel_z",
            value=0,
            comment="ECEF velocity Z-component in meters/second",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def pos_x(self):
        return self.pos_x.value

    @pos_x.setter
    def pos_x(self, value):
        self.pos_x.set_value(value)

    @property
    def pos_y(self):
        return self.pos_y.value

    @pos_y.setter
    def pos_y(self, value):
        self.pos_y.set_value(value)

    @property
    def pos_z(self):
        return self.pos_z.value

    @pos_z.setter
    def pos_z(self, value):
        self.pos_z.set_value(value)

    @property
    def vel_x(self):
        return self.vel_x.value
