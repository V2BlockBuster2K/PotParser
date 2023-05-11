import asyncio
from typing import Any, Dict, List, Union

import aiohttp
from lxml import html


def remove_substrings(string: str) -> str:
    """
    Removes words from a string.

    Parameters:
        string (str): The input string.

    Returns:
        str: The modified string with the specified words removed.
    """
    remove_words = {"THC", "CBD", "CBG"}
    return " ".join(word for word in string.split() if word not in remove_words)


async def get_strain_info(session: aiohttp.ClientSession, url: str, xpath_dict: dict[str, str]) -> dict[str, str]:
    """
    Scrapes strain information from a given URL using specified xpaths.

    Parameters:
        session (aiohttp.ClientSession): The aiohttp client session.
        url (str): The URL to scrape strain information from.
        xpath_dict (dict): A dictionary of keys and xpath expressions used to scrape information.

    Returns:
        dict: A dictionary containing the scraped strain information.
    """
    try:
        async with session.get(url) as response:
            if response.status == 404:
                return {'Genetics': 'None', 'THC': 'None', 'CBD': 'None', 'Effects': 'None', 'Other': 'None'}
            html_content = await response.text()  # extract HTML content from response
    except aiohttp.ClientError:
        return {'Genetics': 'None', 'THC': 'None', 'CBD': 'None', 'Effects': 'None', 'Other': 'None'}

        # Parse the HTML content using lxml
    doc = html.fromstring(html_content)
    strain_info = {}

    def get_value(xpath: str) -> Any:
        try:
            value_element: Union[html.HtmlElement, List[html.HtmlElement]] = doc.xpath(xpath)[
                0]
            if isinstance(value_element, list):
                value: List[str] = [remove_substrings(
                    elem.text_content().strip("\n")) for elem in value_element]
            else:
                value: str = remove_substrings(
                    value_element.text_content().strip("\n"))
        except IndexError:
            value = "None"
        return value

    for key, xpath in xpath_dict.items():
        if key in {"CBD", "THC", "Genetics"}:
            strain_info[key] = get_value(xpath)
            if strain_info[key] == "None" and key == "CBD":
                strain_info[key] = get_value(xpath_dict["CBD_alt"])
        elif key == "Effects":
            value_element: List[html.HtmlElement] = doc.xpath(xpath)
            value: List[str] = [elem.replace('\n', '')
                                for elem in value_element]
            strain_info[key] = value
        elif key == "Flavor":
            value_element: List[html.HtmlElement] = doc.xpath(xpath)
            value: List[str] = [elem.replace('\n', '')
                                for elem in value_element]
            strain_info['Other'] = value
        elif key == 'Other':
            strain_info['Other']: Union[str, List[str]] = doc.xpath(xpath)

    return strain_info


async def scrape_strain_info(strain_name: str) -> List[List[Dict[str, Union[str, List[str]]]]]:
    """
    Scrapes strain information from multiple websites using specified xpaths.

    Parameters:
        strain_name (str): The name of the strain to scrape information for.

    Returns:
        dict: A dictionary containing the scraped strain information. The keys are the following:
              - "Genetics": The genetic lineage of the strain.
              - "THC": The THC content of the strain.
              - "CBD": The CBD content of the strain.
              - "Effects": A list of the positive and negative effects of the strain.
              - "Other": Additional information about the strain like flavour, medical aspects & suitable time.
    """
    urls_xpath_dict = {
        "Cannaconnection": {
            "url": f"https://www.cannaconnection.com/strains/{strain_name}",
            "xpath_dict": {
                "Genetics": '//div[@class="feature-title" and text()="Genetics"]/following-sibling::div[@class="feature-value"]',
                "THC": '//div[@class="feature-title" and text()="THC"]/following-sibling::div[@class="feature-value"]',
                "CBD": '//div[@class="feature-title" and text()="CBD"]/following-sibling::div[@class="feature-value"]',
                "Effects": '//div[@class="multifeature-wrapper"]/div[contains(text(), "Effect")]/following-sibling::div/text()',
                "Flavor": '//div[@class="multifeature-wrapper"]/div[contains(text(), "Smell & flavour")]/following-sibling::div/text()',
            }
        },
        "Leafly": {
            "url": f"https://www.leafly.com/strains/{strain_name}",
            "xpath_dict": {
                "Genetics": '//div[@class="flex items-center mb-xs"]/a/span',
                "THC": '//span[@data-testid="THC"]',
                "CBD": '//span[@data-testid="CBD"]',
                "CBD_alt": '//span[@data-testid="CBG"]',
                "Effects": '//div[contains(@class, "items-baseline") and (contains(text(), "Feelings:") or contains(text(), "Negatives:"))]//a/text()',
                "Other": '//div[@id="helps-with-section"]/ul/li/div/a/text()'
            }
        },
        "Wikileaf": {
            "url": f"https://www.wikileaf.com/strain/{strain_name}/",
            "xpath_dict": {
                "Genetics": '//div[contains(@class, "type-time")]/a[1]/div[@class="type"]/div[@class="status"]',
                "THC": '//div[@aria-label="Progress Circle" and text()="THC"]/following-sibling::div//span[@class="compound-percentage"]',
                "CBD": '//div[@aria-label="Progress Circle" and text()="CBD"]/following-sibling::div//span[@class="compound-percentage"]',
                "Effects": '//div[@class="typicalEffectsItem"]//div[@class="effect-label"]/span[@class="underline"]/text()',
                "Other": '//div[contains(@class, "time")]/div[contains(@class, "status")]/text()'
            }
        }
    }

    async with aiohttp.ClientSession() as session:
        tasks = []
        for website, data in urls_xpath_dict.items():
            url = data["url"]
            xpath_dict = data["xpath_dict"]
            tasks.append(asyncio.create_task(
                get_strain_info(session, url, xpath_dict)))

        results = await asyncio.gather(*tasks)
        return results
