from config_item import ConfigItem
from common_conf import CommonConfig

class Security(CommonConfig):
    def __init__(self, name="SecurityConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.integrity = ConfigItem(
            key="integrity",
            value="not_needed",
            comment="Integrity protection requirement (e.g., 'required', 'not_needed')",
            used=False,
        )
        self.confidentiality = ConfigItem(
            key="confidentiality",
            value="required",
            comment="Confidentiality protection requirement (e.g., 'required', 'not_needed')",
            used=False,
        )
        self.nea_pref_list = ConfigItem(
            key="nea_pref_list",
            value="nea0,nea2,nea1",
            comment="Preferred NEA algorithm list in order of priority",
            used=False,
        )
        self.nia_pref_list = ConfigItem(
            key="nia_pref_list",
            value="nia2,nia1",
            comment="Preferred NIA algorithm list in order of priority",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def integrity(self):
        return self.integrity.value

    @integrity.setter
    def integrity(self, value):
        self.integrity.set_value(value)

    @property
    def confidentiality(self):
        return self.confidentiality.value

    @confidentiality.setter
    def confidentiality(self, value):
        self.confidentiality.set_value(value)

    @property
    def nea_pref_list(self):
        return self.nea_pref_list.value

    @nea_pref_list.setter
    def nea_pref_list(self, value):
        self.nea_pref_list.set_value(value)

    @property
    def nia_pref_list(self):
        return self.nia_pref_list.value

    @nia_pref_list.setter
    def nia_pref_list(self, value):
        self.nia_pref_list.set_value(value)
