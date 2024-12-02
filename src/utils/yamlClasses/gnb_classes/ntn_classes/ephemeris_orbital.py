from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ephemeris_orbital(CommonConfig):
    def __init__(self, name="ephemeris_orbital", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional FLOAT (0). Sets the semi-major axis of the satellite. Supported: [0 - 1000000000].
        self._semi_major_axis = ConfigItem(
            key="semi_major_axis",
            value=0,
            comment="Semi-major axis of the orbit",
            used=False,
        )

        # Optional FLOAT (0). Sets the eccentricity of the satellite.
        self._eccentricity = ConfigItem(
            key="eccentricity",
            value=0,
            comment="Eccentricity of the orbit",
            used=False,
        )

        # Optional FLOAT (0). Sets the periapsis of the satellite.
        self._periapsis = ConfigItem(
            key="periapsis",
            value=0,
            comment="Argument of periapsis of the orbit",
            used=False,
        )

        # Optional FLOAT (0). Sets the longitude of the satellites angle of ascending node.
        self._longitude = ConfigItem(
            key="longitude",
            value=0,
            comment="Longitude of ascending node",
            used=False,
        )

        # Optional FLOAT (0). Sets the inclination of the satellite.
        self._inclination = ConfigItem(
            key="inclination",
            value=0,
            comment="Inclination of the orbit in degrees",
            used=False,
        )

        # Optional FLOAT (0). Sets the mean anomaly of the satellite.
        self._mean_anomaly = ConfigItem(
            key="mean_anomaly",
            value=0,
            comment="Mean anomaly of the orbit",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._semi_major_axis,
            self._eccentricity,
            self._periapsis,
            self._longitude,
            self._inclination,
            self._mean_anomaly
        ]

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
