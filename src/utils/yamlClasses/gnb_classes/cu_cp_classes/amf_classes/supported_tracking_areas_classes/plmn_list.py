from src.utils.yamlClasses.common_list import CommonList
from plmn_list_data import PlmnListData

class PlmnList(CommonList):
    def __init__(self, name="plmn_list", data=None, used=True):
        super().__init__(name, data or {}, used)

        #add inital item to list
        self.add_item(PlmnListData())

    # TODO Add managment functions to create delete and edit item list.

    # TODO add deffinition to this
    def add_tracking_area(self):
        """Takes supported_tracking_areas_data info to add to traking area list"""
        pass
