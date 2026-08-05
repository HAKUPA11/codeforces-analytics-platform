import requests


BASE_URL = "https://codeforces.com/api"


def fetch_data(endpoint, params=None):
    """
    Makes a GET request to the Codeforces API.
    Returns the JSON response.
    """

    url = f"{BASE_URL}/{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data["status"] != "OK":
            raise Exception(data["comment"])

        return data["result"]

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

    except Exception as e:
        print(f"API Error: {e}")
        return None


def get_user_info(handle):
    """
    Fetch information about a Codeforces user.
    """

    return fetch_data(
        "user.info",
        {"handles": handle}
    )


def get_contest_list():
    """
    Fetch all contests from Codeforces.
    """

    return fetch_data("contest.list")


def get_problemset():
    """
    Fetch all problems from Codeforces.
    """

    return fetch_data("problemset.problems")