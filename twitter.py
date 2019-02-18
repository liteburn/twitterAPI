import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def read_json(acct):
    """
    str -> lst

    Gets info about
    """
    if (len(acct) < 1):
        return 1
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '20'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    for user in range(len(js["users"]) - 1):
        print(js["users"][user]["name"], end=", ")
    print(js["users"][-1]["name"])
    return js


def user_info(info, name):
    for user in info["users"]:
        if user["name"] == name:
            return [user["name"], user["location"], user["followers_count"], user["friends_count"]]


if __name__ == "__main__":
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    acct = input('Enter Twitter Account:')
    info = read_json(acct)
    if len(info) == 0:
        print("None Friends Founded")
        exit()
    name = input("About whom of your friends do you want to know about?(watch names in list above)")
    info = user_info(info, name)
    print("User name is", info[0])
    if info[1] != "":
        print("He is living in", info[1])
    print("He(She) has", info[2], "followers")
    print("He(She) has subscribed to", info[3], "users")
