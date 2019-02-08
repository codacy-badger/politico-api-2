import time



class Offices:
    """ Methods to model party information """
    def __init__(self, office_reg_data):
        self.office_reg_data = office_reg_data

    def create_offices(self):
        """ Validate, append, return custom message """
        
        msg = None
        party_already_present = False
        for each_party in Offices:
            if each_party["name"] == self.office_reg_data["name"]:
                party_already_present = True
        if party_already_present:
            msg = {
                "status": "Failed",
                "error": "Party already exists"
            }
        else:
            time_stamp = time.localtime(time.time())
            self.office_reg_data["id"] 
            
            self.office_reg_data["registered on"] = time.asctime(time_stamp)
            Offices.append(self.office_reg_data)
            msg = {
                "Status": "Success",
                "data": [{
                    "id": self.office_reg_data["id"],
                    "name": self.office_reg_data["name"]
                    }]
                }
        return msg

    def check_for_expected_keys(self, list_of_expected_keys):
        """ (dict, list) -> bool
            Checks for dict-key equality
        """
        return list(self.office_reg_data.keys()) == list_of_expected_keys

    def check_for_any_empty_fields(self):
        """ (dict) -> bool
            checks for empty strings
        """
        msg = None
        if "" in self.office_reg_data.values():
            msg = False
        elif (
                self.office_reg_data["name"].isspace() or
                self.office_reg_data["hqAddress"].isspace() or
                self.office_reg_data["logoUrl"].isspace() or
                self.office_reg_data["Party members"] < 1
        ):
            msg = False
        else:
            msg = True
        return msg

    def check_for_expected_value_types(self):
        """ Check for expected value types"""
        msg = None
        if (
                isinstance(self.office_reg_data["id"], str) and
                isinstance(self.office_reg_data["type"], str) and
                isinstance(self.office_reg_data["name"], int)
               
        ):
            msg = True
        else:
            msg = False
        return msg

    def get_all_offices():
        """ get all offices """
        global Offices
        msg = None

        if Offices == []:
            msg = {
                "status": "200",
                "data": "The Party list is empty"
            }

        else:
            msg = {
                "status": "200",
                "data": Offices
            }

        return msg