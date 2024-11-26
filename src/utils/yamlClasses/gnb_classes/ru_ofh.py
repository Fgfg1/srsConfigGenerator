from .ru_ofh_classes.cells import Cells
from config_item import ConfigItem
from common_conf import CommonConfig

class Ru_ofh(CommonConfig):
    def __init__(self, name="RuOfhConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.gps_alpha = ConfigItem(
            key="gps_alpha", value=0, comment="GPS alpha. Supported: [0 - 1.2288e+07]", used=False
        )
        self.gps_beta = ConfigItem(
            key="gps_beta", value=0, comment="GPS beta. Supported: [-32768 - +32767]", used=False
        )
        self.ru_bandwidth_MHz = ConfigItem(
            key="ru_bandwidth_MHz",
            value=0,
            comment="Channel bandwidth in MHz. Supported: [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]",
            used=False,
        )
        self.t1a_max_cp_dl = ConfigItem(
            key="t1a_max_cp_dl", value=500, comment="T1a max value for DL control-plane. Supported: [0 - 1960]", used=False
        )
        self.t1a_min_cp_dl = ConfigItem(
            key="t1a_min_cp_dl", value=258, comment="T1a min value for DL control-plane. Supported: [0 - 1960]", used=False
        )
        self.t1a_max_cp_ul = ConfigItem(
            key="t1a_max_cp_ul", value=500, comment="T1a max value for UL control-plane. Supported: [0 - 1960]", used=False
        )
        self.t1a_min_cp_ul = ConfigItem(
            key="t1a_min_cp_ul", value=258, comment="T1a min value for UL control-plane. Supported: [0 - 1960]", used=False
        )
        self.t1a_max_up = ConfigItem(
            key="t1a_max_up", value=300, comment="T1a max value for user-plane. Supported: [0 - 1960]", used=False
        )
        self.t1a_min_up = ConfigItem(
            key="t1a_min_up", value=85, comment="T1a min value for user-plane. Supported: [0 - 1960]", used=False
        )
        self.ta4_max = ConfigItem(
            key="ta4_max", value=300, comment="Ta4 max value for user-plane. Supported: [0 - 1960]", used=False
        )
        self.ta4_min = ConfigItem(
            key="ta4_min", value=85, comment="Ta4 min value for user-plane. Supported: [0 - 1960]", used=False
        )
        self.is_prach_cp_enabled = ConfigItem(
            key="is_prach_cp_enabled", value=True, comment="Enable PRACH control-plane", used=False
        )
        self.is_dl_broadcast_enabled = ConfigItem(
            key="is_dl_broadcast_enabled", value=False, comment="Enable DL broadcast", used=False
        )
        self.ignore_ecpri_seq_id = ConfigItem(
            key="ignore_ecpri_seq_id", value=False, comment="Ignore eCPRI sequence ID", used=False
        )
        self.ignore_ecpri_payload_size = ConfigItem(
            key="ignore_ecpri_payload_size", value=False, comment="Ignore eCPRI payload size", used=False
        )
        self.warn_unreceived_ru_frames = ConfigItem(
            key="warn_unreceived_ru_frames", value=True, comment="Warn on unreceived RU frames", used=False
        )
        self.compr_method_ul = ConfigItem(
            key="compr_method_ul", value="bfp", comment="Uplink compression method", used=False
        )
        self.compr_bitwidth_ul = ConfigItem(
            key="compr_bitwidth_ul", value=9, comment="Uplink compression bit width. Supported: [1 - 16]", used=False
        )
        self.compr_method_dl = ConfigItem(
            key="compr_method_dl", value="bfp", comment="Downlink compression method", used=False
        )
        self.compr_bitwidth_dl = ConfigItem(
            key="compr_bitwidth_dl", value=9, comment="Downlink compression bit width. Supported: [1 - 16]", used=False
        )
        self.compr_method_prach = ConfigItem(
            key="compr_method_prach", value="bfp", comment="PRACH compression method", used=False
        )
        self.compr_bitwidth_prach = ConfigItem(
            key="compr_bitwidth_prach", value=9, comment="PRACH compression bit width. Supported: [1 - 16]", used=False
        )
        self.enable_ul_static_compr_hdr = ConfigItem(
            key="enable_ul_static_compr_hdr", value=True, comment="Enable UL static compression header", used=False
        )
        self.enable_dl_static_compr_hdr = ConfigItem(
            key="enable_dl_static_compr_hdr", value=True, comment="Enable DL static compression header", used=False
        )
        self.iq_scaling = ConfigItem(
            key="iq_scaling", value=0.35, comment="IQ scaling factor. Supported: [0 - 1]", used=False
        )

        # Sub-configuration
        self.cells = Cells()

    # Getters and setters for all ConfigItems
    @property
    def gps_alpha(self):
        return self.gps_alpha.value

    @gps_alpha.setter
    def gps_alpha(self, value):
        self.gps_alpha.set_value(value)

    @property
    def gps_beta(self):
        return self.gps_beta.value

    @gps_beta.setter
    def gps_beta(self, value):
        self.gps_beta.set_value(value)

    @property
    def ru_bandwidth_MHz(self):
        return self.ru_bandwidth_MHz.value

    @ru_bandwidth_MHz.setter
    def ru_bandwidth_MHz(self, value):
        self.ru_bandwidth_MHz.set_value(value)

    @property
    def t1a_max_cp_dl(self):
        return self.t1a_max_cp_dl.value

    @t1a_max_cp_dl.setter
    def t1a_max_cp_dl(self, value):
        self.t1a_max_cp_dl.set_value(value)

    @property
    def t1a_min_cp_dl(self):
        return self.t1a_min_cp_dl.value

    @t1a_min_cp_dl.setter
    def t1a_min_cp_dl(self, value):
        self.t1a_min_cp_dl.set_value(value)

    @property
    def t1a_max_cp_ul(self):
        return self.t1a_max_cp_ul.value

    @t1a_max_cp_ul.setter
    def t1a_max_cp_ul(self, value):
        self.t1a_max_cp_ul.set_value(value)

    @property
    def t1a_min_cp_ul(self):
        return self.t1a_min_cp_ul.value

    @t1a_min_cp_ul.setter
    def t1a_min_cp_ul(self, value):
        self.t1a_min_cp_ul.set_value(value)

    @property
    def t1a_max_up(self):
        return self.t1a_max_up.value

    @t1a_max_up.setter
    def t1a_max_up(self, value):
        self.t1a_max_up.set_value(value)

    @property
    def t1a_min_up(self):
        return self.t1a_min_up.value

    @t1a_min_up.setter
    def t1a_min_up(self, value):
        self.t1a_min_up.set_value(value)

    @property
    def ta4_max(self):
        return self.ta4_max.value

    @ta4_max.setter
    def ta4_max(self, value):
        self.ta4_max.set_value(value)

    @property
    def ta4_min(self):
        return self.ta4_min.value

    @ta4_min.setter
    def ta4_min(self, value):
        self.ta4_min.set_value(value)

    @property
    def is_prach_cp_enabled(self):
        return self.is_prach_cp_enabled.value

    @is_prach_cp_enabled.setter
    def is_prach_cp_enabled(self, value):
        self.is_prach_cp_enabled.set_value(value)

    @property
    def is_dl_broadcast_enabled(self):
        return self.is_dl_broadcast_enabled.value

    @is_dl_broadcast_enabled.setter
    def is_dl_broadcast_enabled(self, value):
        self.is_dl_broadcast_enabled.set_value(value)

    @property
    def ignore_ecpri_seq_id(self):
        return self.ignore_ecpri_seq_id.value

    @ignore_ecpri_seq_id.setter
    def ignore_ecpri_seq_id(self, value):
        self.ignore_ecpri_seq_id.set_value(value)

    @property
    def ignore_ecpri_payload_size(self):
        return self.ignore_ecpri_payload_size.value

    @ignore_ecpri_payload_size.setter
    def ignore_ecpri_payload_size(self, value):
        self.ignore_ecpri_payload_size.set_value(value)

    @property
    def warn_unreceived_ru_frames(self):
        return self.warn_unreceived_ru_frames.value

    @warn_unreceived_ru_frames.setter
    def warn_unreceived_ru_frames(self, value):
        self.warn_unreceived_ru_frames.set_value(value)

    @property
    def compr_method_ul(self):
        return self.compr_method_ul.value

    @compr_method_ul.setter
    def compr_method_ul(self, value):
        self.compr_method_ul.set_value(value)

    @property
    def compr_bitwidth_ul(self):
        return self.compr_bitwidth_ul.value

    @compr_bitwidth_ul.setter
    def compr_bitwidth_ul(self, value):
        self.compr_bitwidth_ul.set_value(value)

    @property
    def compr_method_dl(self):
        return self.compr_method_dl.value

    @compr_method_dl.setter
    def compr_method_dl(self, value):
        self.compr_method_dl.set_value(value)

    @property
    def compr_bitwidth_dl(self):
        return self.compr_bitwidth_dl.value

    @compr_bitwidth_dl.setter
    def compr_bitwidth_dl(self, value):
        self.compr_bitwidth_dl.set_value(value)

    @property
    def compr_method_prach(self):
        return self.compr_method_prach.value

    @compr_method_prach.setter
    def compr_method_prach(self, value):
        self.compr_method_prach.set_value(value)

    @property
    def compr_bitwidth_prach(self):
        return self.compr_bitwidth_prach.value

    @compr_bitwidth_prach.setter
    def compr_bitwidth_prach(self, value):
        self.compr_bitwidth_prach.set_value(value)

    @property
    def enable_ul_static_compr_hdr(self):
        return self.enable_ul_static_compr_hdr.value

    @enable_ul_static_compr_hdr.setter
    def enable_ul_static_compr_hdr(self, value):
        self.enable_ul_static_compr_hdr.set_value(value)

    @property
    def enable_dl_static_compr_hdr(self):
        return self.enable_dl_static_compr_hdr.value

    @enable_dl_static_compr_hdr.setter
    def enable_dl_static_compr_hdr(self, value):
        self.enable_dl_static_compr_hdr.set_value(value)

    @property
    def iq_scaling(self):
        return self.iq_scaling.value

    @iq_scaling.setter
    def iq_scaling(self, value):
        self.iq_scaling.set_value(value)
