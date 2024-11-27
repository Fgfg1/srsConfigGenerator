from src.utils.yamlClasses.common_list import CommonList
from cells_data import CellsData

'''
This is the creator of all cells info and everything should relate back to this.
(or at least that is what I believe)
'''

class Cells(CommonList):
    def __init__(self, name="CellsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # provide inital data in items list

        self.add_item(CellsData())

    # Add managment functions to create delete and edit item list.

    # TODO add deffinition to this
    def add_cell(self):
        """Takes CellsData info to add to cells list"""
        pass
   
   # TODO add communication functions between this class and report_configs 
   # and other classes that need to know about the cells information 