from src.utils.yamlClasses.common_list import CommonList
from slicing_data import SlicingData

class Slicing(CommonList):
    def __init__(self, name="slicing", data=None, used=False):
        super().__init__(name, data or {}, used)

        
        # add inital item to slicing data
        # adding default configuration for Slice 1
        self.add_item(SlicingData())

    
    # Add managment functions to create delete and edit item list.

    # TODO add deffinition to this
    def add_slice(self):
        """Takes SlicingData info to add to Slice List"""
        pass
