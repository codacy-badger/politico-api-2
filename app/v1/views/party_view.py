from flask import Blueprint, jsonify, request
from app.v1.models.party_model import Createparty

app = Blueprint("v1", __name__, url_prefix="/app/v1")

   

@app.route('/parties', methods=['POST', 'GET'])
def parties():
        if request.method == "POST":
             party_reg_data = request.get_json(force=True)
             sample_party = Createparty(party_reg_data)
             if len(party_reg_data) > 4:
                custom_response = jsonify({
                "status": "Bad Query",
                "error": "More data fields than expected"
            }), 400
        elif len(party_reg_data) < 4:
            custom_response = jsonify({
                "status": "Bad Query",
                "error": "Fewer data fields than expected"
            }), 400
        elif sample_party.check_for_expected_value_types() is False:
            custom_response = jsonify({
                "status": "Unprocessable Entity",
                "error": "Invalid value in data field"
            }), 422
        elif sample_party.check_for_any_empty_fields() is False:
            custom_response = jsonify({
                "status": "Unprocessable Entity",
                "error": "Empty data field"
            }), 422
            else:
                custom_response = jsonify(sample_party.create_party()), 201

    elif request.method == "GET":
        custom_response = jsonify(Createparty.get_all_parties())

    else:
        pass


    return custom_response