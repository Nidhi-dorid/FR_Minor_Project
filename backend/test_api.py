import requests
import time
import subprocess
import os
import signal

def test_backend():
    print("Starting backend for testing...")
    # Start the flask app in the background
    backend_proc = subprocess.Popen(
        [os.path.join(os.getcwd(), '.venv', 'Scripts', 'python.exe'), 'app.py'],
        cwd=os.path.join(os.getcwd(), 'backend'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    try:
        # Wait for the server to start
        time.sleep(5)

        base_url = "http://127.0.0.1:5000"

        # 1. Test /api/status
        print("Testing /api/status...")
        resp = requests.get(f"{base_url}/api/status")
        print(f"Status: {resp.status_code}, Response: {resp.json()}")

        # 2. Test /get-weather
        print("Testing /get-weather...")
        resp = requests.post(f"{base_url}/get-weather", json={"zip": "560001"})
        print(f"Status: {resp.status_code}, Response: {resp.json()}")

        # 3. Test /recommend
        print("Testing /recommend...")
        recommend_data = {
            "zip": "560001",
            "Soil_Type": "Sandy",
            "Crop_Type": "Maize",
            "nitrogen": 37,
            "phosphorous": 0,
            "potassium": 0,
            "moisture": 38
        }
        resp = requests.post(f"{base_url}/recommend", json=recommend_data)
        print(f"Status: {resp.status_code}, Response: {resp.json()}")

    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        print("Stopping backend...")
        backend_proc.terminate()
        backend_proc.wait()

if __name__ == "__main__":
    test_backend()
