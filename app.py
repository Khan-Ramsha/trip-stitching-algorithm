from flask import Flask, request, jsonify
from mobility_service import MobilityService

app = Flask(__name__)
# referring official documentation of beckn.
# https://developers.becknprotocol.io/docs/developer-documentation/transaction-layer/getting-a-list-of-mobility-service-providers-that-can-transport-a-traveller-from-a-pickup-location-to-a-drop-location-node-js/

# Create instance of the MobilityService
mobility_service = MobilityService()

# Route to search for trips 
@app.route('/mobility/search_by_pickup_drop_location', methods=['POST'])
def search():
    try:
        # Parse and validate input
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON input"}), 400

        pickup = data.get("pickup")
        drop = data.get("drop")
        catalogs = data.get("catalogs", [])
        optimization_parameter = data.get("optimization_parameter", "cost")

        if not pickup or not drop:
            return jsonify({"error": "Pickup and drop locations are required"}), 400

        # Process the search
        search_response = mobility_service.process_search(pickup, drop, catalogs, optimization_parameter)
        return jsonify({"status": "success", "data": search_response}), 200
    except Exception as e:
        app.logger.error(f"Error during search: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to handle the on_search logic (trip stitching)
@app.route('/mobility/on_search', methods=['POST'])
def on_search():
    try:
        # Get search response from the request
        data = request.get_json()
        search_response = data['search_response']  # Raw response from the previous search route
        optimization_parameter = data['optimization_parameter']  # Either cost or distance

        # Use MobilityService to handle the stitching
        stitched_trips = mobility_service.process_on_search(search_response, optimization_parameter)

        # Return the stitched trips
        return jsonify(stitched_trips), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

