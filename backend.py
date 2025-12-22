"""Backend client and configuration"""
import os
import requests

# Simple config
BACKEND_URL = os.getenv("NEATCODE_BACKEND_URL", "http://localhost:3000")
TIMEOUT = 30


class BackendClient:
    """Simple client for NeatCode backend"""
    
    def health_check(self):
        """Check if backend is healthy"""
        try:
            response = requests.get(f"{BACKEND_URL}/health", timeout=TIMEOUT)
            return {
                "healthy": response.status_code == 200,
                "status": response.json() if response.status_code == 200 else None
            }
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def send_webhook(self, event_type, payload):
        """Send webhook to backend"""
        try:
            response = requests.post(
                f"{BACKEND_URL}/webhook",
                json=payload,
                headers={"X-GitHub-Event": event_type},
                timeout=TIMEOUT
            )
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

