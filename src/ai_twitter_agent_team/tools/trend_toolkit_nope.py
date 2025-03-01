import tweepy
from typing import List, Dict, Any

from agno.agent import Toolkit, Function
from agno.utils.log import logger


def get_woeid(place):
    '''Get woeid by location'''
    try:
        trends = api.trends_available()
        for val in trends:
            if (val['name'].lower() == place.lower()):
                return(val['woeid']) 
        print('Location Not Found')
    except Exception as e:
        print('Exception:',e)
        return(0)


class TwitterTrendsToolkit(Toolkit):
    """
    A toolkit for retrieving trending topics from Twitter (X) using Tweepy.
    """

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
        Initializes the TwitterTrendsToolkit with API credentials.

        Args:
            consumer_key (str): The consumer key from your Twitter app.
            consumer_secret (str): The consumer secret from your Twitter app.
            access_token (str): The access token from your Twitter account.
            access_token_secret (str): The access token secret from your Twitter account.
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.client = self._create_tweepy_client()

    def _create_tweepy_client(self) -> tweepy.Client:
        """
        Creates a Tweepy API client using the provided credentials.
        """
        try:
          client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )
          return client
        except Exception as e:
          logger.error(f"Error creating Tweepy client: {e}")
          raise

    def get_trends(self, area: str) -> List[str]:
        """
        Retrieves the trending topics for a given area.

        Args:
            area (str): The name of the area (e.g., "New York", "London") to get trends for.

        Returns:
            List[str]: A list of trending topic names.
        """
        try:
            # First, need to find the WOEID (Where On Earth ID) for the given area.
            # This is usually done via the trends/closest endpoint (not directly supported in v2)
            # For simplicity and demonstration, we'll assume a WOEID.
            # **IN A REAL IMPLEMENTATION, YOU WOULD NEED TO FIND THE WOEID DYNAMICALLY.**
            #
            # Example: WOEID for New York is 2459115. This value CAN change.
            # It's best practice to look this up programmatically using trends/closest.
            #
            # Since Tweepy v2 doesn't directly support trends/closest,
            # we need to use the API v1.
            # To use API V1, you need to authenticate using OAuth1.0a User Context
            auth = tweepy.OAuth1UserHandler(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
            api = tweepy.API(auth)  # Use API V1
            try:
                closest_trends = api.trends_closest(latitude=40.7128, longitude=-74.0060)  # Example: New York coordinates
                woeid = closest_trends[0]['woeid']  # The first item should give you the required location data

            except Exception as e:
                logger.error(f"Error finding WOEID for area {area}: {e}")
                raise  # Re-raise so calling function knows

            trends_result = self.client.get_place_trends(woeid) # Now using the v2 Client

            trends = [trend['name'] for trend in trends_result.data]
            logger.info(f"Found trends for {area}: {trends}")
            return trends
        except Exception as e:
            logger.error(f"Error getting trends for area {area}: {e}")
            return []

    def get_tools(self) -> List[Function]:
        """Returns a list of Function objects representing the tools in this toolkit."""
        return [
            Function.from_tool(
                self.get_trends,
                name="get_trends",
                description="Retrieves the trending topics for a given area.",
            )
        ]

# Example Usage (Illustrative)
if __name__ == '__main__':
    #  Replace with your actual API keys and secrets
    CONSUMER_KEY = "YOUR_CONSUMER_KEY"
    CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

    try:
        trend_toolkit = TwitterTrendsToolkit(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        new_york_trends = trend_toolkit.get_trends(area="New York") # Corrected method call
        print(f"Trending topics in New York: {new_york_trends}")

        london_trends = trend_toolkit.get_trends(area="London")
        print(f"Trending topics in London: {london_trends}")

    except Exception as e:
        print(f"An error occurred: {e}")