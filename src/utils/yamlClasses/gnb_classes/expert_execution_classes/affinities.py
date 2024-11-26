from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Affinities(CommonConfig):
    def __init__(self, name="AffinitiesConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._isolated_cpus = ConfigItem(
            key="isolated_cpus",
            value=None,
            comment="List of isolated CPUs for specific tasks",
            used=False,
        )
        self._low_priority_cpus = ConfigItem(
            key="low_priority_cpus",
            value=None,
            comment="List of low-priority CPUs",
            used=False,
        )
        self._low_priority_pinning = ConfigItem(
            key="low_priority_pinning",
            value=None,
            comment="Pinning configuration for low-priority tasks",
            used=False,
        )
        self._ru_timing_cpu = ConfigItem(
            key="ru_timing_cpu",
            value=None,
            comment="CPU dedicated to RU timing tasks",
            used=False,
        )
        self._ofh = ConfigItem(
            key="ofh",
            value=None,
            comment="OFH-specific CPU affinity",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def isolated_cpus(self):
        return self._isolated_cpus.value

    @isolated_cpus.setter
    def isolated_cpus(self, value):
        self._isolated_cpus.set_value(value)

    @property
    def low_priority_cpus(self):
        return self._low_priority_cpus.value

    @low_priority_cpus.setter
    def low_priority_cpus(self, value):
        self._low_priority_cpus.set_value(value)

    @property
    def low_priority_pinning(self):
        return self._low_priority_pinning.value

    @low_priority_pinning.setter
    def low_priority_pinning(self, value):
        self._low_priority_pinning.set_value(value)

    @property
    def ru_timing_cpu(self):
        return self._ru_timing_cpu.value

    @ru_timing_cpu.setter
    def ru_timing_cpu(self, value):
        self._ru_timing_cpu.set_value(value)

    @property
    def ofh(self):
        return self._ofh.value

    @ofh.setter
    def ofh(self, value):
        self._ofh.set_value(value)
