import unittest
import json
from app import create_app


class TestPartiesRoute(unittest.TestCase):
    """ Test case for party views """

    def setUp(self):
        """ Init app and test vars """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.party_reg_data = {
            "name": "kenya",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 500
        }

    def test_party_creation_with_valid_data(self):
        """test with valid data - 201 (created) + data"""
        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(self.party_reg_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(
            response.status_code, 201,
            msg="response code SHOULD BE 201 (Created)"
        )

    def test_with_more_fields_than_expected(self):
        """ Test with more fields than expected. """
        test_reg_data = {
            "name": "kenya",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 500,
            "Age": "too old"
        }

        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(test_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 400,
            msg="response code SHOULD BE 400 (bad query) + msg"
        )
        self.assertEqual(
            deserialized_response["error"], "More data fields than expected",
            msg="Response Body Contents- Should be custom message "
        )

    def test_with_fewer_fields_than_expected(self):
        """ Test with fewer fields than expected """
        test_reg_data = {
            "name": "kenya",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg"
        }

        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(test_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 400,
            msg="response code SHOULD BE 400 (bad query) + msg"
        )
        self.assertEqual(
            deserialized_response["error"], "Fewer data fields than expected",
            msg="Response Body Contents- Should be custom message "
        )

    def test_with_an_empty_string_in_field(self):
        """ Test with an empty string in field """
        test_reg_data = {
            "name": "",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 500,
        }

        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(test_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 422,
            msg="response code SHOULD BE 422 (Unprocessable Entity) + msg"
        )
        self.assertEqual(
            deserialized_response["error"], "Empty data field",
            msg="Response Body Contents- Should be custom message "
        )

    def test_with_invalid_value_types(self):
        """test with invalid value types  - 422 (Unprocessable Entity) + msg
        """
        test_reg_data = {
            "name": 12,
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/nairobi.jpeg",
            "Party members": 500
        }

        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(test_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 422,
            msg="response code SHOULD BE 422 (Unprocessable Entity) + msg"
        )
        self.assertEqual(
            deserialized_response["error"], "Invalid value in data field",
            msg="Response Body Contents- Should be custom message "
        )

    def test_with_already_created_party(self):
        """ Test that a party cannot be created twice
        """
        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(self.party_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 201,
            msg="response code SHOULD BE 201 (Created)"
        )
        response = self.client().post(
            "/api/v1/parties",
            data=json.dumps(self.party_reg_data),
            headers={'content-type': 'application/json'}
        )
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_response["error"], "Party already exists",
            msg="Response Body Contents- Should be custom message "
        )

if __name__ == "__main__":
    unittest.main()