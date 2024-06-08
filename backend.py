import requests

API_KEY = "6b2044c73c58ced46b6370ffe93e0ca6"


def get_data(place, forcast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    data = response.json()

    filtered_data_1 = data["list"]

    if not filtered_data_1:  # Check if list is empty

        return None  # Or handle empty list case differently

    nr_values = 8 * (forcast_days - 1)

    filtered_data = filtered_data_1[nr_values: nr_values + 8 * forcast_days]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Chicago", forcast_days=1))
    print(get_data(place="Chicago", forcast_days=2))
    print(get_data(place="Chicago", forcast_days=3))
    print(get_data(place="Chicago", forcast_days=4))
    print(get_data(place="Chicago", forcast_days=5))
