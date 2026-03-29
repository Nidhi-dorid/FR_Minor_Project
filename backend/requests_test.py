import requests

def test_backend():
    base_url = "http://127.0.0.1:5000"

    # 1. Test /api/status
    print("Testing /api/status...")
    try:
        resp = requests.get(f"{base_url}/api/status")
        print(f"Status: {resp.status_code}, Response: {resp.json()}")
    except Exception as e:
        print(f"/api/status failed: {e}")

    # 2. Test /get-weather
    print("Testing /get-weather...")
    try:
        resp = requests.post(f"{base_url}/get-weather", json={"zip": "560001"})
        print(f"Status: {resp.status_code}, Response: {resp.json()}")
    except Exception as e:
        print(f"/get-weather failed: {e}")

    # 3. Test /recommend
    print("Testing /recommend...")
    try:
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
        print(f"/recommend failed: {e}")

if __name__ == "__main__":
    test_backend()
