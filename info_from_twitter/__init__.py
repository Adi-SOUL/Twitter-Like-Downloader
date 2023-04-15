from typing import Any
import requests


def connect_to_endpoint(url: str, bearer_oauth,  tweet_fields: str | None = None) -> Any:
	if tweet_fields:
		response = requests.request(
			"GET", url, auth=bearer_oauth, params=tweet_fields
		)
	else:
		response = requests.request("GET", url, auth=bearer_oauth)

	if response.status_code != 200:
		raise Exception(
			"Request returned an error: {} {}".format(
				response.status_code, response.text
			)
		)
	return response.json()
