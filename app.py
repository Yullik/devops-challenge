from flask import Flask, jsonify
from datetime import datetime, timezone
import requests

app = Flask(__name__)

METADATA_BASE = "http://169.254.169.254/latest"


def get_imds_token():
    try:
        response = requests.put(
            f"{METADATA_BASE}/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2,
        )
        if response.status_code == 200:
            return response.text
    except Exception:
        return None


def get_metadata(path):
    token = get_imds_token()
    headers = {"X-aws-ec2-metadata-token": token} if token else {}

    try:
        response = requests.get(
            f"{METADATA_BASE}/meta-data/{path}",
            headers=headers,
            timeout=2,
        )
        if response.status_code == 200:
            return response.text
    except Exception:
        pass

    return "unavailable"


@app.route("/info")
def info():
    return jsonify(
        {
            "instance_id": get_metadata("instance-id"),
            "availability_zone": get_metadata("placement/availability-zone"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )


@app.route("/")
def home():
    return jsonify({"message": "Flask app is running. Visit /info"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)