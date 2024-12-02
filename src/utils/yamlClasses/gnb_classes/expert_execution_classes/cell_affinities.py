from src.utils.yamlClasses.common_list import CommonList
from .cell_affinities_data import CellAffData

# Optional TEXT. Sets the cell CPU affinities configuration on a per cell basis. Entry order is the same as the order in the defined cell list.

class Cell_affinities(CommonList):
    def __init__(self, name="cell_affinities", data=None, used=False):
        super().__init__(name, data or {}, used)
        
        # TODO for the comment above, This is a per cell thing.
        # Need to implement a way to grab cell data and make sure it syncs
        # Not sure where that data is. (too many diffrent cell configs in thing)

        # I belive this relates to the ru_ofh cells data.

        # Configurable attributes using ConfigItem
        self.add_item(CellAffData())

    # Getters and setters for ConfigItems

    # TODO: Implement this function
    def add_cell_affinity(self, name:str):
        """
        Creates and adds a new cell affinity to the list of cells.

        Steps:
        - uses same name from the cell
        - Instantiates a new CellAffData object with the generated name.
        - Adds the new cell affinity to the list of items.

        Note: Actual implementation to construct and configure the new cell is pending.
        """
        
        pass  # Placeholder for implementation logic

    # TODO: Implement this function    
    def del_cell_affinity(self, name:str):
        """using the name of a cell delete that cell"""
        pass

    
