from src.utils.yamlClasses.common_list import CommonList
from supported_tracking_areas_data import Supported_tracking_areas_data

# Required TEXT. Sets the list of tracking areas supported by this AMF.

class Supported_tracking_areas(CommonList):
    def __init__(self, name="supported_tracking_areas", data=None, used=False):
        super().__init__(name, data or {}, used)

        #add inital item to list
        self.add_item(Supported_tracking_areas_data())

    # TODO Add managment functions to create delete and edit item list.

    # TODO add deffinition to this
    def add_tracking_area(self):
        """Takes supported_tracking_areas_data info to add to traking area list"""
        pass


    