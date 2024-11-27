from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Security(CommonConfig):
    def __init__(self, name="SecurityConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT (not_needed). Sets the default integrity protection indication for DRBs.
        self._integrity = ConfigItem(
            key="integrity",
            value="not_needed",
            comment="Integrity protection requirement (e.g., 'required', 'not_needed')",
            used=False,
        )

        # Optional TEXT (required). Sets the default integrity confidentiality indication for DRBs.
        self._confidentiality = ConfigItem(
            key="confidentiality",
            value="required",
            comment="Confidentiality protection requirement (e.g., 'required', 'not_needed')",
            used=False,
        )

        # Optional TEXT (nea0,nea2,nea1). Ordered preference list for the selection of encryption algorithm (NEA). Supported: [nea0,nea2,nea1,nea3].
        self._nea_pref_list = ConfigItem(
            key="nea_pref_list",
            value="nea0,nea2,nea1",
            comment="Preferred NEA algorithm list in order of priority",
            used=False,
        )

        # Optional TEXT (nia2,nia1). Ordered preference list for the selection of encryption algorithm (NIA). Supported: [nia2,nia1,nia3].
        self._nia_pref_list = ConfigItem(
            key="nia_pref_list",
            value="nia2,nia1",
            comment="Preferred NIA algorithm list in order of priority",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._integrity,
            self._confidentiality,
            self._nea_pref_list,
            self._nia_pref_list
        ]

    # Getters and setters for ConfigItems
    @property
    def integrity(self):
        return self._integrity.value

    @integrity.setter
    def integrity(self, value):
        self._integrity.set_value(value)

    @property
    def confidentiality(self):
        return self._confidentiality.value

    @confidentiality.setter
    def confidentiality(self, value):
        self._confidentiality.set_value(value)

    @property
    def nea_pref_list(self):
        return self._nea_pref_list.value

    @nea_pref_list.setter
    def nea_pref_list(self, value):
        self._nea_pref_list.set_value(value)

    @property
    def nia_pref_list(self):
        return self._nia_pref_list.value

    @nia_pref_list.setter
    def nia_pref_list(self, value):
        self._nia_pref_list.set_value(value)
