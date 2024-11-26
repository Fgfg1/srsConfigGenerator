from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Metrics(CommonConfig):
    def __init__(self, name="metrics", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._addr = ConfigItem(
            key="addr",
            value="127.0.0.1",
            comment="IP address for metrics collection",
            used=False,
        )
        self._port = ConfigItem(
            key="port",
            value=55555,
            comment="Port number for metrics collection",
            used=False,
        )
        self._cu_cp_statistics_report_period = ConfigItem(
            key="cu_cp_statistics_report_period",
            value=1,
            comment="CU-CP statistics report period in seconds",
            used=False,
        )
        self._cu_up_statistics_report_period = ConfigItem(
            key="cu_up_statistics_report_period",
            value=1,
            comment="CU-UP statistics report period in seconds",
            used=False,
        )
        self._pdcp_report_period = ConfigItem(
            key="pdcp_report_period",
            value=0,
            comment="PDCP report period in milliseconds",
            used=False,
        )
        self._rlc_report_period = ConfigItem(
            key="rlc_report_period",
            value=1000,
            comment="RLC report period in milliseconds",
            used=False,
        )
        self._rlc_json_enable = ConfigItem(
            key="rlc_json_enable",
            value=False,
            comment="Enable RLC JSON reporting",
            used=False,
        )
        self._enable_json_metrics = ConfigItem(
            key="enable_json_metrics",
            value=False,
            comment="Enable JSON metrics output",
            used=False,
        )
        self._autostart_stdout_metrics = ConfigItem(
            key="autostart_stdout_metrics",
            value=False,
            comment="Autostart metrics output to stdout",
            used=False,
        )
        self._stdout_metrics_period = ConfigItem(
            key="stdout_metrics_period",
            value=None,
            comment="Period for stdout metrics output in seconds",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def addr(self):
        return self._addr.value

    @addr.setter
    def addr(self, value):
        self._addr.set_value(value)

    @property
    def port(self):
        return self._port.value

    @port.setter
    def port(self, value):
        self._port.set_value(value)

    @property
    def cu_cp_statistics_report_period(self):
        return self._cu_cp_statistics_report_period.value

    @cu_cp_statistics_report_period.setter
    def cu_cp_statistics_report_period(self, value):
        self._cu_cp_statistics_report_period.set_value(value)

    @property
    def cu_up_statistics_report_period(self):
        return self._cu_up_statistics_report_period.value

    @cu_up_statistics_report_period.setter
    def cu_up_statistics_report_period(self, value):
        self._cu_up_statistics_report_period.set_value(value)

    @property
    def pdcp_report_period(self):
        return self._pdcp_report_period.value

    @pdcp_report_period.setter
    def pdcp_report_period(self, value):
        self._pdcp_report_period.set_value(value)

    @property
    def rlc_report_period(self):
        return self._rlc_report_period.value

    @rlc_report_period.setter
    def rlc_report_period(self, value):
        self._rlc_report_period.set_value(value)

    @property
    def rlc_json_enable(self):
        return self._rlc_json_enable.value

    @rlc_json_enable.setter
    def rlc_json_enable(self, value):
        self._rlc_json_enable.set_value(value)

    @property
    def enable_json_metrics(self):
        return self._enable_json_metrics.value

    @enable_json_metrics.setter
    def enable_json_metrics(self, value):
        self._enable_json_metrics.set_value(value)

    @property
    def autostart_stdout_metrics(self):
        return self._autostart_stdout_metrics.value

    @autostart_stdout_metrics.setter
    def autostart_stdout_metrics(self, value):
        self._autostart_stdout_metrics.set_value(value)

    @property
    def stdout_metrics_period(self):
        return self._stdout_metrics_period.value

    @stdout_metrics_period.setter
    def stdout_metrics_period(self, value):
        self._stdout_metrics_period.set_value(value)
