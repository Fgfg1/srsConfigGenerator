from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ephemeris_orbital(CommonConfig):
    def __init__(self, name="EphemerisOrbitalConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._semi_major_axis = ConfigItem(
            key="semi_major_axis",
            value=0,
            comment="Semi-major axis of the orbit",
            used=False,
        )
        self._eccentricity = ConfigItem(
            key="eccentricity",
            value=0,
            comment="Eccentricity of the orbit",
            used=False,
        )
        self._periapsis = ConfigItem(
            key="periapsis",
            value=0,
            comment="Argument of periapsis of the orbit",
            used=False,
        )
        self._longitude = ConfigItem(
            key="longitude",
            value=0,
            comment="Longitude of ascending node",
            used=False,
        )
        self._inclination = ConfigItem(
            key="inclination",
            value=0,
            comment="Inclination of the orbit in degrees",
            used=False,
        )
        self._mean_anomaly = ConfigItem(
            key="mean_anomaly",
            value=0,
            comment="Mean anomaly of the orbit",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def semi_major_axis(self):
        return self._semi_major_axis.value

    @semi_major_axis.setter
    def semi_major_axis(self, value):
        self._semi_major_axis.set_value(value)

    @property
    def eccentricity(self):
        return self._eccentricity.value

    @eccentricity.setter
    def eccentricity(self, value):
        self._eccentricity.set_value(value)

    @property
    def periapsis(self):
        return self._periapsis.value

    @periapsis.setter
    def periapsis(self, value):
        self._periapsis.set_value(value)

    @property
    def longitude(self):
        return self._longitude.value

    @longitude.setter
    def longitude(self, value):
        self._longitude.set_value(value)

    @property
    def inclination(self):
        return self._inclination.value

    @inclination.setter
    def inclination(self, value):
        self._inclination.set_value(value)

    @property
    def mean_anomaly(self):
        return self._mean_anomaly.value

    @mean_anomaly.setter
    def mean_anomaly(self, value):
        self._mean_anomaly.set_value(value)
