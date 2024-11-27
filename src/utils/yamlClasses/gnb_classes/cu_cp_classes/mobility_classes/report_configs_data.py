from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

# Optional TEXT. Sets the list of report configurations to dynamically build a measurement configuration sent to the UEs using the below values.
# Define report configs for each cell

class Report_configs_data(CommonConfig):
    def __init__(self, name="ReportConfigs", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required UINT. The ID of this report configuration.
        self._report_cfg_id = ConfigItem(
            key="report_cfg_id",
            value=None,
            comment="ID of the reporting configuration",
            used=True,
        )

        # Required TEXT. The type of the report. Supported: [event_triggered, periodical]. Note that periodical reports are only supported for serving cells.
        self._report_type = ConfigItem(
            key="report_type",
            value=None,
            comment="Type of reporting (e.g., 'periodic', 'event-based')",
            used=True,
        )

        # Optional UINT (1024). The report interval in ms.
        self._report_interval_ms = ConfigItem(
            key="report_interval_ms",
            value=1024,
            comment="Interval for periodic reporting in milliseconds",
            used=False,
        )

        # Optional TEXT. A3 report type. Supported: [rsrp, rsrq, sinr].
        self._a3_report_type = ConfigItem(
            key="a3_report_type",
            value=None,
            comment="Type of A3 report",
            used=False,
        )

        # Optional UINT. A3 offset in dB used for measurement report trigger.
        self._a3_offset_db = ConfigItem(
            key="a3_offset_db",
            value=None,
            comment="Offset for A3 reporting in dB",
            used=False,
        )

        # Optional UINT. A3 hysteresis in dB used for measurement report trigger.
        self._a3_hysteresis_db = ConfigItem(
            key="a3_hysteresis_db",
            value=None,
            comment="Hysteresis for A3 reporting in dB",
            used=False,
        )

        # Optional UINT. Time in ms during which A3 condition must be met before measurement report trigger.
        self._a3_time_to_trigger_ms = ConfigItem(
            key="a3_time_to_trigger_ms",
            value=None,
            comment="Time to trigger for A3 reports in milliseconds",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._report_cfg_id,
            self._report_type,
            self._report_interval_ms,
            self._a3_report_type,
            self._a3_offset_db,
            self._a3_hysteresis_db,
            self._a3_time_to_trigger_ms
        ]

    # Getters and setters for ConfigItems
    @property
    def report_cfg_id(self):
        return self._report_cfg_id.value

    @report_cfg_id.setter
    def report_cfg_id(self, value):
        self._report_cfg_id.set_value(value)

    @property
    def report_type(self):
        return self._report_type.value

    @report_type.setter
    def report_type(self, value):
        self._report_type.set_value(value)

    @property
    def report_interval_ms(self):
        return self._report_interval_ms.value

    @report_interval_ms.setter
    def report_interval_ms(self, value):
        self._report_interval_ms.set_value(value)

    @property
    def a3_report_type(self):
        return self._a3_report_type.value

    @a3_report_type.setter
    def a3_report_type(self, value):
        self._a3_report_type.set_value(value)

    @property
    def a3_offset_db(self):
        return self._a3_offset_db.value

    @a3_offset_db.setter
    def a3_offset_db(self, value):
        self._a3_offset_db.set_value(value)

    @property
    def a3_hysteresis_db(self):
        return self._a3_hysteresis_db.value

    @a3_hysteresis_db.setter
    def a3_hysteresis_db(self, value):
        self._a3_hysteresis_db.set_value(value)

    @property
    def a3_time_to_trigger_ms(self):
        return self._a3_time_to_trigger_ms.value

    @a3_time_to_trigger_ms.setter
    def a3_time_to_trigger_ms(self, value):
        self._a3_time_to_trigger_ms.set_value(value)
