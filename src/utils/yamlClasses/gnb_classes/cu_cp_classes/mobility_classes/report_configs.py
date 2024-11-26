from config_item import ConfigItem
from common_conf import CommonConfig

class Report_configs(CommonConfig):
    def __init__(self, name="ReportConfigs", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.report_cfg_id = ConfigItem(
            key="report_cfg_id",
            value=None,
            comment="ID of the reporting configuration",
            used=False,
        )
        self.report_type = ConfigItem(
            key="report_type",
            value=None,
            comment="Type of reporting (e.g., 'periodic', 'event-based')",
            used=False,
        )
        self.report_interval_ms = ConfigItem(
            key="report_interval_ms",
            value=1024,
            comment="Interval for periodic reporting in milliseconds",
            used=False,
        )
        self.a3_report_type = ConfigItem(
            key="a3_report_type",
            value=None,
            comment="Type of A3 report",
            used=False,
        )
        self.a3_offset_db = ConfigItem(
            key="a3_offset_db",
            value=None,
            comment="Offset for A3 reporting in dB",
            used=False,
        )
        self.a3_hysteresis_db = ConfigItem(
            key="a3_hysteresis_db",
            value=None,
            comment="Hysteresis for A3 reporting in dB",
            used=False,
        )
        self.a3_time_to_trigger_ms = ConfigItem(
            key="a3_time_to_trigger_ms",
            value=None,
            comment="Time to trigger for A3 reports in milliseconds",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def report_cfg_id(self):
        return self.report_cfg_id.value

    @report_cfg_id.setter
    def report_cfg_id(self, value):
        self.report_cfg_id.set_value(value)

    @property
    def report_type(self):
        return self.report_type.value

    @report_type.setter
    def report_type(self, value):
        self.report_type.set_value(value)

    @property
    def report_interval_ms(self):
        return self.report_interval_ms.value

    @report_interval_ms.setter
    def report_interval_ms(self, value):
        self.report_interval_ms.set_value(value)

    @property
    def a3_report_type(self):
        return self.a3_report_type.value

    @a3_report_type.setter
    def a3_report_type(self, value):
        self.a3_report_type.set_value(value)

    @property
    def a3_offset_db(self):
        return self.a3_offset_db.value

    @a3_offset_db.setter
    def a3_offset_db(self, value):
        self.a3_offset_db.set_value(value)

    @property
    def a3_hysteresis_db(self):
        return self.a3_hysteresis_db.value

    @a3_hysteresis_db.setter
    def a3_hysteresis_db(self, value):
        self.a3_hysteresis_db.set_value(value)

    @property
    def a3_time_to_trigger_ms(self):
        return self.a3_time_to_trigger_ms.value

    @a3_time_to_trigger_ms.setter
    def a3_time_to_trigger_ms(self, value):
        self.a3_time_to_trigger_ms.set_value(value)
