from src.utils.yamlClasses.common_list import CommonList
from .tai_slice_support_list_data import TaiSliceSupportListData

class Tai_slice_support_list(CommonList):
    def __init__(self, name="tai_slice_support_list", data=None, used=False):
        super().__init__(name, data or {}, used)

        #add inital item to list
        self.add_item(TaiSliceSupportListData())

    # TODO Add managment functions to create delete and edit item list.

    # TODO add deffinition to this
    def add_tracking_area(self):
        """Takes supported_tracking_areas_data info to add to traking area list"""
        pass