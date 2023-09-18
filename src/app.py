from flask import Flask, request, jsonify

app = Flask(__name__)


# Define a route that listens for POST requests
@app.route("/api/flask/splunk-example", methods=["POST"])
def process_post_request():
    # Get the raw text data from the request body
    raw_text = request.data.decode("utf-8")

    # Split the raw text into lines (assuming each line represents a separate data entry)
    lines = raw_text.split("\n")

    # Create an empty list to store the JSON objects
    json_list = []

    for i, line in enumerate(lines):
        # Create a JSON object from the line (adjust as needed)
        json_obj = {
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

        # Add a "lastrow" key to the last JSON object in the list
        if i == len(lines) - 1:
            json_obj["lastrow"] = True

        json_list.append(json_obj)

    # Return the JSON list as the response
    return jsonify(json_list)


if __name__ == "__main__":
    app.run(debug=True)
