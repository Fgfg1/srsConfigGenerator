from src.utils.yamlClasses.common_list import CommonList
from report_configs_data import Report_configs_data

# Optional TEXT. Sets the list of report configurations to dynamically build a measurement configuration sent to the UEs using the below values.

class Report_configs(CommonList):
    def __init__(self, name="report_configs", data=None, used=False):
        super().__init__(name, data or {}, used)
        
        # TODO for the comment above, This is a per cell thing.


        # Configurable attributes using ConfigItem
        self.add_item(Report_configs_data())

    # Getters and setters for ConfigItems

    # TODO: Implement this function
    def add_report_config(self):
        pass  # Placeholder for implementation logic

    # TODO: Implement this function    
    def del_report_config(self, name:str):
        """delete based on name of report config"""
        pass

    
