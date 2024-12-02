from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Affinities(CommonConfig):
    def __init__(self, name="affinities", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT. Sets the CPU core(s) isolated for the gNB application. Supported: [1, 2, 3 , ..., N].
        self._isolated_cpus = ConfigItem(
            key="isolated_cpus",
            value=None,
            comment="List of isolated CPUs for specific tasks",
            used=False,
        )

        # Optional TEXT. Sets the CPU core(s) assigned to low priority tasks. Supported: [1, 2, 3 , ..., N].
        self._low_priority_cpus = ConfigItem(
            key="low_priority_cpus",
            value=None,
            comment="List of low-priority CPUs",
            used=False,
        )

        # Optional TEXT. Sets the policy used for assigning CPU cores to low priority tasks.
        self._low_priority_pinning = ConfigItem(
            key="low_priority_pinning",
            value=None,
            comment="Pinning configuration for low-priority tasks",
            used=False,
        )

        # Optional TEXT. Sets the CPU used for timing in the Radio Unity.
        self._ru_timing_cpu = ConfigItem(
            key="ru_timing_cpu",
            value=None,
            comment="CPU dedicated to RU timing tasks",
            used=False,
        )

        # Optional TEXT Sets the CPU affinities configuration for RU cells tx-rx threads. Number of entries specified defines the number of tx-rx threads created. 
        # By default if no entries are specified, the number of tx-rx threads equals the number of RU cells.
        self._ofh = ConfigItem(
            key="ofh",
            value=None,
            comment="OFH-specific CPU affinity",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._isolated_cpus,
            self._low_priority_cpus,
            self._low_priority_pinning,
            self._ru_timing_cpu,
            self._ofh
        ]

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
