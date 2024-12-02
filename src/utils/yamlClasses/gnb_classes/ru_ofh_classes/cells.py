from src.utils.yamlClasses.common_list import CommonList
from .cells_data import CellsData

class Cells(CommonList):
    """
    A specialized class that extends CommonList to manage a collection of CellsData objects.
    Provides additional functionality specific to managing cell-related configurations.
    """
    def __init__(self, name="cells", data=None, used=False):
        """
        Initializes the Cells object that holds a lits of cells.

        Args:
            name (str): The name of the cell group. Default is "cells".
            data (dict): The initial data dictionary for the cell group.
            used (bool): Indicates if the cell group is active or in use.
        """

        # Initialize the base CommonList class with the provided arguments
        super().__init__(name, data or {}, used)
        
        # Automatically add a default cell with the name "Cell 1"
        self.add_item(CellsData("Cell 1"))

    # Add management functions specific to cells below

    # TODO: Implement this function
    def add_cell(self):
        """
        Creates and adds a new cell to the list of cells.

        Steps:
        - Constructs a name for the new cell using the current count of items.
        - Instantiates a new CellsData object with the generated name.
        - Adds the new cell to the list of items.

        Note: Actual implementation to construct and configure the new cell is pending.
        """
        cell_name = f"Cell {self.num_items() + 1}"
        pass  # Placeholder for implementation logic
