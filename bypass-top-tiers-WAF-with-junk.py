from mitmproxy import http
import json

def request(flow: http.HTTPFlow) -> None:
    # Only process requests with a JSON content-type
    content_type = flow.request.headers.get("Content-Type", "")
    if "application/json" in content_type:
        # Decode the JSON body
        try:
            data = json.loads(flow.request.get_text())
        except json.JSONDecodeError:
            return  # Not valid JSON, skip processing
        
        # Add the "x-secret" parameter
        data["x-secret"] = "123456789"
        
        # Encode the JSON and set it as the new request body
        flow.request.set_text(json.dumps(data))
