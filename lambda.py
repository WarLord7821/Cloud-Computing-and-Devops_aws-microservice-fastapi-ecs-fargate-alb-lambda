import json
import os
import urllib.request

ALB_URL = os.getenv("ALB_URL")  # e.g., http://my-alb-123.ap-south-1.elb.amazonaws.com

def lambda_handler(event, context):
    name = event.get("name", "there")
    url = f"{ALB_URL}/greet"
    data = json.dumps({"name": name}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = resp.read().decode("utf-8")
            status = resp.getcode()
        return {"statusCode": status, "body": body}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
