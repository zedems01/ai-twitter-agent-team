import json
from os import getenv
from typing import Optional, List, Dict

from pydantic import BaseModel, Field

from agno.tools import Toolkit, Function
from agno.utils.log import logger


try:
    from firecrawl import FirecrawlApp
except ImportError:
    raise ImportError("The `firecrawl` package is not installed. Please install it via `pip install firecrawl-py`.")




class TrendData(BaseModel):
    """Schema for trend data extraction"""
    trend_subject: str = Field(..., description="Trending topic or hashtag.")
    posts_count: int = Field(..., description="Number of posts related to the trend.")


class TrendsResponse(BaseModel):
    """Schema for multiple trend data response"""
    trends: List[TrendData] = Field(..., description="List of trending topics and their post counts.")
    

class FirecrawlResponse(BaseModel):
    """Schema for Firecrawl API response"""
    success: bool = Field(..., description="Indicates if the API call was successful.")
    data: Dict = Field(..., description="The data returned by the Firecrawl API.")
    status: str = Field(..., description="The status of the Firecrawl API call.")
    expiresAt: str = Field(..., description="The expiration timestamp of the cached Firecrawl API data.")


def format_url(country=None, city=None):
    if country == "worldwide":
        return "https://trends24.in/"
    elif country and city:
        return f"https://trends24.in/{country}/{city}/"
    elif country:
        return f"https://trends24.in/{country}/"
    else:
        return "https://trends24.in/"  # worldwide by default




# TODO: Add a documentation for country and city choices, along with a dynamic way to retrieve them

class FirecrawlExtractTrendsTools(Toolkit):
    """Toolkit for extracting trending topics using Firecrawl."""

    def __init__(
            self,
            api_key: Optional[str] = None
    ):
        super().__init__(name="firecrawl_extract_trends")

        self.register(self.get_trends)
        self.api_key: Optional[str] = api_key or getenv("FIRECRAWL_API_KEY")

        if not self.api_key:
            logger.error("FIRECRAWL_API_KEY not set. Please set the FIRECRAWL_API_KEY environment variable.")

        self.app = FirecrawlApp(api_key=api_key)
        

    def get_trends(
            self,
            country: str = "worldwide",
            city: Optional[str] = None,
            max_trends: int = 2
    ) -> str:
        """
        Use this function to extract the top trending topics on Twitter from a specific location using Firecrawl.

        Args:
            country (str, optional): The country to search for trends. Defaults to "worldwide". 
            city (str, optional): The city to search for trends. Defaults to None. If a city is chosen, then a country must also be set.
            max_trends (int, optional): The maximum number of trends to extract. Defaults to 2.

        Returns:
            str: JSON string containing a list of trending topics and post counts.
        """

        country = country.lower().replace(" ", "-")
        if city:
            city = city.lower().replace(" ", "-")
        logger.debug(f"Extracting trending topics for: country={country}, city={city}, max_trends={max_trends}")


        try:
            url = format_url(country, city)
            urls = [url]
            params = {
                "prompt": f"Extract the top {max_trends} trending topics from few minutes ago, along with their associated post count.",
                # "prompt": f"Extract the most recent top {max_trends} trending topics or hashtags along with their associated post count.",
                "schema": TrendsResponse.model_json_schema(),
            }

            raw_response = self.app.extract(urls=urls, params=params)

            # Handle potential errors and format the response properly
            if raw_response and raw_response.get("success") and raw_response.get("data"):
                # Make a FirecrawlResponse from the result
                parsed_response = FirecrawlResponse(**raw_response)
                trend_data = parsed_response.data

                if trend_data is None:
                    return json.dumps({"trends": []}, indent=2)
                return json.dumps(trend_data, indent=2)

            else:
                logger.error(f"Firecrawl API call failed. The response was : {raw_response}")
                return json.dumps(
                    {"error": "Firecrawl API call failed"}, indent=2
                )  # Return an error object, not just an empty string.

        except Exception as e:
            logger.error(f"Error extracting trends from Firecrawl: {e}")
            return json.dumps({"error": str(e)}, indent=2)