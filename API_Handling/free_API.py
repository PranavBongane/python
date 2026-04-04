import requests

def fetch_user_data():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data["success"]:
        users = data["data"]["data"]

        result = []
        for user in users:
            username = user["login"]["username"]
            country = user["location"]["country"]
            result.append((username, country))

        return result
    else:
        raise Exception("failed to fetch user data")
    

def main():
    try:
        users = fetch_user_data()
        for u in users:
            print(f"User: {u[0]} | Country: {u[1]}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()