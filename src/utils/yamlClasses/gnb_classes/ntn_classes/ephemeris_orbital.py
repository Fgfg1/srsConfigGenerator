from config_item import ConfigItem
from common_conf import CommonConfig

class Ephemeris_orbital(CommonConfig):
    def __init__(self, name="EphemerisOrbitalConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.semi_major_axis = ConfigItem(
            key="semi_major_axis",
            value=0,
            comment="Semi-major axis of the orbit",
            used=False,
        )
        self.eccentricity = ConfigItem(
            key="eccentricity",
            value=0,
            comment="Eccentricity of the orbit",
            used=False,
        )
        self.periapsis = ConfigItem(
            key="periapsis",
            value=0,
            comment="Argument of periapsis of the orbit",
            used=False,
        )
        self.longitude = ConfigItem(
            key="longitude",
            value=0,
            comment="Longitude of ascending node",
            used=False,
        )
        self.inclination = ConfigItem(
            key="inclination",
            value=0,
            comment="Inclination of the orbit in degrees",
            used=False,
        )
        self.mean_anomaly = ConfigItem(
            key="mean_anomaly",
            value=0,
            comment="Mean anomaly of the orbit",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def semi_major_axis(self):
        return self.semi_major_axis.value

    @semi_major_axis.setter
    def semi_major_axis(self, value):
        self.semi_major_axis.set_value(value)

    @property
    def eccentricity(self):
        return self.eccentricity.value

    @eccentricity.setter
    def eccentricity(self, value):
        self.eccentricity.set_value(value)

    @property
    def periapsis(self):
        return self.periapsis.value

    @periapsis.setter
    def periapsis(self, value):
        self.periapsis.set_value(value)

    @property
    def longitude(self):
        return self.longitude.value

    @longitude.setter
    def longitude(self, value):
        self.longitude.set_value(value)

    @property
    def inclination(self):
        return self.inclination.value

    @inclination.setter
    def inclination(self, value):
        self.inclination.set_value(value)

    @property
    def mean_anomaly(self):
        return self.mean_anomaly.value

    @mean_anomaly.setter
    def mean_anomaly(self, value):
        self.mean_anomaly.set_value(value)
