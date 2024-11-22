class ConfigItem:
    """
    This class represents an item in the configuration process. It holds a key-value pair, along with 
    a comment and a 'used' flag indicating whether this configuration has been used or not.

    Attributes :
        key (str) : Unique identifier for the configuration value
        value : Actual configurable value
        comment (str) : Explanatory note about the configuration item
        used (bool) : Indicates whether this configuration has been used or not, defaults to False
    """

    def __init__(self, key: str, value, comment: str, used: bool):
        self.key = key
        self.value = value
        self.comment = comment
        self.used = used 
  
    # Getters Methods to access the values
    def get_data(self) -> dict:
        """Returns a dictionary with the configuration data {key : value}"""
        return {self.key : self.value}
   
    def get_comment(self) -> str:
        """Return the explanatory comment for this config item"""
        return self.comment

    def is_used(self) -> bool: 
        """Check if configuration has been used or not """
        return self.used 

    # Setters methods to modify the values
    def set_key(self, key: str):
        """Set a new unique identifier for this config item"""
        self.key = key
  
    def set_value(self, value):
        """Modify current configuration value"""
        self.value = value
   
    def set_comment(self, comment: str):
        """Update explanatory note about this config item"""
        self.comment = comment 

    def set_used(self, used: bool): # Use boolean for a flag
        """Set whether the configuration has been used or not """
        self.used = used 
