import os
from . import connect_to_endpoint


def bearer_oauth_user(r):
	r.headers["Authorization"] = f"Bearer {os.environ['BEARER_TOKEN']}"
	r.headers["User-Agent"] = "v2UserLookupPython"
	return r


def username_by_id(id_: str) -> str:
	url = "https://api.twitter.com/2/users/{}".format(id_)
	json_response = connect_to_endpoint(url=url, tweet_fields=None, bearer_oauth=bearer_oauth_user)

	username = json_response["data"]["username"]

	return username
