import asyncio
from typing import Dict, List, Union

from .helpers import create_url_ending_name
from .webscrapers.strain_scraper import scrape_strain_info


class PotParser():
    """A scraper for cannabis strain information."""
    def get_strain(self, strain_name: str) -> List[List[Dict[str, Union[str, List[str]]]]]:
        """
        Scrape information on a given cannabis strain.

        Args:
            strain_name (str): The name of the strain to scrape information for.

        Returns:
            List[List[Dict[str, Union[str, List[str]]]]]: A nested list of dictionaries, each containing
            information on a different aspect of the strain, such as its effects, flavors, and medicinal uses.
            First Dict contains information from Cannaconnection second Dict contains information from Leafly and Dict List contains information from Wikileaf
        """
        url_name = create_url_ending_name(strain_name)
        result = asyncio.run(scrape_strain_info(url_name))
        return result