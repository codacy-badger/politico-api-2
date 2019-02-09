rom flask import Blueprint, jsonify, request
from app.v1.models.office_model import Offices

app = Blueprint("v1", __name__, url_prefix="/app/v1")


@app.route("/offices", methods=["POST"])
def offices():
    """
        Create a political office - POST
    """
    custom_response = None
    if request.method == "POST":
        office_reg_data = request.get_json(force=True)
        sample_office = Offices(office_reg_data)
        if len(office_reg_data) > 4:
            custom_response = jsonify({
                "status": "Bad Query",
                "error": "More data fields than expected"
            }), 400
        elif len(office_reg_data) < 4:
            custom_response = jsonify({
                "status": "Bad Query",
                "error": "Fewer data fields than expected"
            }), 400
        elif sample_office.check_for_expected_value_types() is False:
            custom_response = jsonify({
                "status": "Unprocessable Entity",
                "error": "Invalid value in data field"
            }), 422
        elif sample_office.check_for_any_empty_fields() is False:
            custom_response = jsonify({
                "status": "Unprocessable Entity",
                "error": "Empty data field"
            }), 422
            else:
                custom_response = jsonify(sample_office.create_offices()), 201

    elif request.method == "GET":
        custom_response = jsonify(Offices.get_all_offices())

    else:
        pass

    return custom_response

@app.route("/offices/<int:id>", methods=["GET"])
def office(id):
    """
    GET -> Fetch political office by ID
    """
    custom_response = None

    if request.method == "GET":

        if isinstance(pid, int) and pid >= 1:
            if Offices.check_id_exists(id) is True:
                custom_response = jsonify({
                    "status": 200,
                    "data": Offices.fetch_a_party(id)
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