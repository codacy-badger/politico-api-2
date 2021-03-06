import time


class Createparty():
    """This class represents the createparty table."""

   def __init__(self, party_reg_data):
        self.party_reg_data = party_reg_data

    def create_party(self):
        """ Validate, append, return custom message """
        global Createparty
        msg = None
        party_already_present = False
        for each_party in Createparty:
            if each_party["name"] == self.party_reg_data["name"]:
                party_already_present = True
        if party_already_present:
            msg = {
                "status": "Failed",
                "error": "Party already exists"
            }
        else:
            time_stamp = time.localtime(time.time())
           
            self.party_reg_data["registered on"] = time.asctime(time_stamp)
            Createparty.append(self.party_reg_data)
            msg = {
                "Status": "Success",
                "data": [{
                    "id": self.party_reg_data["id"],
                    "name": self.party_reg_data["name"]
                    }]
                }
        return msg

    def check_for_expected_keys(self, list_of_expected_keys):
        """ (dict, list) -> bool
            Checks for dict-key equality
        """
        return list(self.party_reg_data.keys()) == list_of_expected_keys

    def check_for_any_empty_fields(self):
        """ (dict) -> bool
            checks for empty strings
        """
        msg = None
        if "" in self.party_reg_data.values():
            msg = False
        elif (
                  self.party_reg_data["name"].isspace() or
                self.party_reg_data["hqAddress"].isspace() or
                self.party_reg_data["logoUrl"].isspace() or
                self.party_reg_data["Party members"] < 1
        ):
            msg = False
        else:
            msg = True
        return msg

    def check_for_expected_value_types(self):
        """ Check for expected value types"""
        msg = None
        if (
                isinstance(self.party_reg_data["name"], str) and
                isinstance(self.party_reg_data["hqAddress"], str) and
                isinstance(self.party_reg_data["logoUrl"], str) and
                isinstance(self.party_reg_data["Party members"], int)
        ):
            msg = True
        else:
            msg = False
        return msg