import os
from . import connect_to_endpoint
from .get_liked import get_new_liked


def bearer_oauth_tw(r):
	r.headers["Authorization"] = f"Bearer {os.environ['BEARER_TOKEN']}"
	r.headers["User-Agent"] = "v2TweetLookupPython"

	return r


def get_links() -> list[tuple[list[str], str, str]]:
	res = []
	liked_tweets = get_new_liked()
	for _id, name in liked_tweets:
		url = f'https://api.twitter.com/2/tweets?ids={_id}&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text'
		tweet_fields = "tweet.fields=id,source"
		json_response = connect_to_endpoint(url=url, tweet_fields=tweet_fields, bearer_oauth=bearer_oauth_tw)

		try:
			media = json_response["includes"]["media"]
			urls = []
			for m in media:
				if m.get("type") != 'photo':
					continue
				else:
					urls.append(m["url"]+'?name=large')
			res.append((urls, name, _id))
		except KeyError:
			continue

	return res
