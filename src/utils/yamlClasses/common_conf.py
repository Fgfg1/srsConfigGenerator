"""
    This is my rant:
    
    Used as a parent class and to old most of the reused code.
    Designed specificly so that it could be used to create yaml documents.
    yaml documents are designed in a key value pair where the value might be  a single item
    like a string or another list of key value pairs or possibly an array.

    I am using pyyaml to create the documents and it works really well with a dict.
    All data will be stored in a dictionary.
"""
class CommonConfig:
    def __init__(self, name=None, data:dict = {}, used = False, variables:list = []):  
        '''
        The CommonComfig class is designed to manage configuration parameters. The 'used' flag is set by default to False. 

        Parameters :
            name (str) : Name of the configuration item defaults to None
            data (dict) : Dictionary containing data for configuring some common parameters
            used (bool) : Indicates whether this configuration has been used or not, defaults to False
            variables (list) : List of all variables and sub classes used in 
        '''
        self._name = name # used as they key in the key value pair
        self._data = data  # this will always be set up for printing a yaml file
        self._used = used
        self._variables = variables   
 

    # Getters and setters for each instance variable
    def get_name(self) -> str:
        return self._name
  
    def get_data(self): # return type should be dictionary
        if self._name == None:
            return self._data
        else:
            return {self._name : self._data}

    def is_used(self) -> bool: 
        return self._used   

    def set_name(self, name: str):
        self._name = name
  
    def set_data(self, data): # input type should be a dictionary
        self._data = data
   
    def set_used(self, used: bool): 
        self._used = used 
