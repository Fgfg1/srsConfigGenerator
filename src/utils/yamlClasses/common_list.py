from src.utils.yamlClasses.common_conf import CommonConfig

class CommonList(CommonConfig):
    def __init__(self, name=None, data: dict = {}, used=False, variables: list = []):
        super().__init__(name, data, used)
        
        # List to store items of type CommonConfig or its subclasses
        self._items: list[CommonConfig] = []  

    # Getters and setters for each instance variable
    def initialize_data(self):
        """
        Collects the data from each item in _items and aggregates it into a list.
        Then assigns the list to _data as a dictionary with _name as the key.
        """
        data_list = []
        if self._used:
            for item in self._items:
                if isinstance(item, CommonConfig):
                    item.initialize_data()
                # Append the item's data to the list, calling get_data(True)
                data_list.append(item.get_data(True))
        
        self._data = {self._name: data_list}

    def add_item(self, item: CommonConfig):
        """
        Adds an item to the _items list. Ensures it is an instance of CommonConfig.
        """
        if not isinstance(item, CommonConfig):
            raise TypeError(f"Expected an instance of CommonConfig, got {type(item)} instead.")
        self._items.append(item)

    def delete_item(self, name: str):
        """
        Deletes an item from the _items list by matching its name.
        """
        for index, item in enumerate(self._items):
            if item.get_name() == name:
                del self._items[index]
                return True  # Indicate success
        return False  # Indicate failure if no item matched

    def num_items(self) -> int:
        """
        Returns the number of items in the _items list.
        """
        return len(self._items)

    def get_items(self) -> list[CommonConfig]:
        """
        Returns the list of items.
        """
        return self._items
