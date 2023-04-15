import os
from . import connect_to_endpoint
from .get_username import username_by_id


def bearer_oauth_liked(r):
	r.headers["Authorization"] = f"Bearer {os.environ['BEARER_TOKEN']}"
	r.headers["User-Agent"] = "v2LikedTweetsPython"

	return r


def get_last_download_liked(file: str) -> list:
	res = []
	with open(file, 'r', encoding='utf-8') as f:
		while True:
			this_line = f.readline()
			if not this_line:
				break
			if this_line[-1] == '\n':
				this_line = this_line[:-1]
			res.append(this_line)
	return res


def write_like(like_list: list[str]) -> None:
	if not like_list:
		return

	with open(r'.\liked_id.txt', 'a', encoding='utf-8') as f:
		for i in like_list:
			f.write(i+'\n')


def get_new_liked() -> list[tuple[str, str]]:
	tweets_id = []
	url = "https://api.twitter.com/2/users/{}/liked_tweets".format(os.environ['TWITTER_ID'])
	tweet_fields = "tweet.fields=lang,author_id,source,withheld"
	json_response = connect_to_endpoint(url=url, tweet_fields=tweet_fields, bearer_oauth=bearer_oauth_liked)

	tweets = json_response["data"]
	last_id = get_last_download_liked(r'.\liked_id.txt')
	for tweet in tweets:
		auth_id = tweet["author_id"]
		user_name = username_by_id(auth_id)
		_id = tweet["id"]
		if _id in last_id:
			break
		else:
			tweets_id.append((_id, user_name))

	return tweets_id
