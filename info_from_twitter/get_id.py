import os
from . import connect_to_endpoint


def bearer_oauth_id(r):
	r.headers["Authorization"] = f"Bearer {os.environ['BEARER_TOKEN']}"
	r.headers["User-Agent"] = "v2UserLookupPython"
	return r


def get_id_through_name(name: str) -> str:
	user_fields = "user.fields=description,created_at"
	url = "https://api.twitter.com/2/users/by?usernames={}&{}".format(name, user_fields)
	json_response = connect_to_endpoint(url=url, bearer_oauth=bearer_oauth_id)
	return json_response['data'][0]['id']
