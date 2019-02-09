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

@app.route("/parties/<int:id>", methods=["GET"])
def party(id):
    """
    GET -> Fetch political party by ID
    """
    custom_response = None

    if request.method == "GET":

        if isinstance(pid, int) and pid >= 1:
            if Createparty.check_id_exists(id) is True:
                custom_response = jsonify({
                    "status": 200,
                    "data": Createparty.fetch_a_party(id)
                }), 200
            else:
                custom_response = jsonify({
                    "status": 416,
                    "error": "ID not found"
                }), 416
        elif id < 1:
            custom_response = jsonify({
                "status": "Failed",
                "error": "ID can't be less than 1"
            }), 400
    else:
        pass

    return custom_response
@app.route("/parties/<int:id>/name", methods=["PATCH"])
def party_admin(id):
    """ Edit politcal party  by id"""
    custom_response = None
    partylist= request.get_json(force=True)

    if "name" not in partylist or len(partylist) != 1:
        custom_response = jsonify({
            "status": 400,
            "error": "Bad Query - More data fields than expected"
        }), 400
    elif id < 1:
        custom_response = jsonify({
            "status": "Failed",
            "error": "id cannot be zero"
        }), 400
    elif Createparty.check_id_exists(pid) is False:
        custom_response = jsonify({
            "status": 416,
            "error": "id out of range. Requested Range Not Satisfiable"
        }), 416

    elif Createparty.check_for_valid_party_name(partylist["name"]):
        custom_response = jsonify({
            "status": 422,
            "error": "Name cannot be empty/space or 1 letter",
            }), 422

    else:
        custom_response = jsonify({
            "status": 200,
            "data": Createparty.edit_party(partylist, pid)
            }), 200

    return custom_response
    
@app.route("/parties/<int:id>/name", methods=["DELETE"])
def party_admin(id):
    """ delete politcal party  by id"""
    custom_response = None
    partylist= request.get_json(force=True)

    if "name" not in partylist or len(partylist) != 1:
        custom_response = jsonify({
            "status": 400,
            "error": "Bad Query - More data fields than expected"
        }), 400
    elif id < 1:
        custom_response = jsonify({
            "status": "Failed",
            "error": "id cannot be zero"
        }), 400
    elif Createparty.check_id_exists(pid) is False:
        custom_response = jsonify({
            "status": 416,
            "error": "id out of range. Requested Range Not Satisfiable"
        }), 416

    elif Createparty.check_for_valid_party_name(partylist["name"]):
        custom_response = jsonify({
            "status": 422,
            "error": "Name cannot be empty/space or 1 letter",
            }), 422

    else:
        custom_response = jsonify({
            "status": 200,
            "data": Createparty.edit_party(partylist, pid)
            }), 200

    return custom_response
    
   