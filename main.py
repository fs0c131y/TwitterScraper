import argparse

from snscrape.modules.twitter import TwitterProfileScraper


def get_args():
    parser = argparse.ArgumentParser(description='Get tweets of a Twitter profile')
    parser.add_argument('--username', '-u', type=str, required=True, help='Username of the Twitter profile')
    parser.add_argument('--limit', '-l', type=int, default=10, help='Number of tweet to dump')
    return parser.parse_args()


def main():
    args = get_args()

    tweets = []

    for count, tweet in enumerate(TwitterProfileScraper(args.username).get_items()):
        if count > args.limit:
            break

        tweet_json = {
            "date": tweet.date,
            "tweet_id": tweet.id,
            "raw_content": tweet.rawContent,
            "username": tweet.user.username
        }
        print(tweet_json)
        tweets.append(tweet_json)


if __name__ == '__main__':
    main()
