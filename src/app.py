from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/flask/splunk-example", methods=["POST"])
def process_post_request():
    raw_text = request.data.decode("utf-8")

    lines = raw_text.split("\n")

    json_list = []

    for i, line in enumerate(lines):
        json_mock_data_obj = {
            "preview": True,
            "offset": i,
            "result": {
                "_time": "2020-03-18 07:54:55.956 CDT",
                "msg": line,
                "org_name": "Some-NamedOrg",
                "app_name": "smartsearchflaskapi",
                "host": "ss3-b4",
                "FLASKAPI_Route": "/v1/contacts/search",
                "FLASKAPI_MicroService": "Search",
                "FLASKAPI_TransactionID": " 7500001232321_HellyContact_d33as665-4421-4j55-bb6",
                "FLASKAPI_Client": "SNOW",
                "FLASKAPI_ClientIP": "11.122.255.58",
                "FLASKAPI_sc_status": "200",
                "FLASKAPI_time_taken": "42.4242",
            },
        }

        if i == len(lines) - 1:
            json_mock_data_obj["lastrow"] = True

        json_list.append(json_mock_data_obj)

    return jsonify(json_list)


if __name__ == "__main__":
    app.run(debug=True)
