import pandas as pd
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd


class Rumah123BlockSession(Exception):
    def __init__(self, message):
        super().__init__(message)


def convert_price(price_text):
    # Remove 'Rp' and spaces, and handle the commas
    price_text = price_text.replace("Rp", "").replace(" ", "").strip()

    # Regular expression to match 'juta' (million) and 'miliar' (billion)
    if "Miliar" in price_text:
        price_value = float(price_text.replace("Miliar", "").replace(",", ".").strip())
        return price_value * 1000  # Convert to millions (1 miliar = 1000 juta)
    elif "Juta" in price_text:
        price_value = float(price_text.replace("Juta", "").replace(",", ".").strip())
        return price_value
    else:
        # Handle any other cases (e.g., if the price is in plain numbers)
        return float(price_text.replace(",", ".").strip())


def convert_area(area_text):
    # Remove non-numeric characters (e.g., 'm²', spaces, etc.)
    area_value = area_text.replace("LT : ", "").replace("LB : ", "").split(" ")[0]
    return float(area_value)  # Convert to float


async def fetch_page(session: aiohttp.ClientSession, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_page(session: aiohttp.ClientSession, base_url, page):
    url = f"{base_url}&page={page}"
    html = await fetch_page(session, url)
    if "Just a moment" in html:
        pass
        # raise Rumah123BlockSession("Rumah123 block the Session")
    soup = BeautifulSoup(html, "html.parser")
    listings = soup.find_all(class_="ui-organism-intersection__element")

    data = []
    for listing in listings:
        try:
            title = listing.find("h2").text
            price = convert_price(
                listing.find(class_="card-featured__middle-section__price").text
            )
            location = listing.select_one(".card-featured__middle-section > span").text
            attributes_text = listing.select(".attribute-text")
            bedrooms = float(attributes_text[0].text) if len(attributes_text) > 0 else 0
            bathrooms = (
                float(attributes_text[1].text) if len(attributes_text) > 1 else 0
            )
            attributes_info = listing.select(".attribute-info")
            land_area = (
                convert_area(attributes_info[0].text.split(" ")[2])
                if len(attributes_info) > 0
                else "N/A"
            )
            building_area = (
                convert_area(attributes_info[1].text.split(" ")[2])
                if len(attributes_info) > 1
                else "N/A"
            )
            agent_name = listing.select_one(".name").text
            url = "https://rumah123.com/" + listing.find("a")["href"]
            price_per_bedroom = (0.2 * price) / 12 / bedrooms if bedrooms > 0 else 0
            cost_per_bedroom = price / bedrooms if bedrooms > 0 else 0
            area_per_bedroom = building_area / bedrooms if bedrooms > 0 else 0

            data.append(
                {
                    "Title": title,
                    "Price": price,
                    "Location": location,
                    "Bedrooms": bedrooms,
                    "Bathrooms": bathrooms,
                    "Land Area": land_area,
                    "Building Area": building_area,
                    "Agent Name": agent_name,
                    "URL": url,
                    "Price per Bedroom": price_per_bedroom,
                    "Cost per Bedroom": cost_per_bedroom,
                    "Area per Bedroom": area_per_bedroom,
                }
            )
        except Rumah123BlockSession as e:
            print(e)
        except Exception as e:
            print(e)

    return data


async def main(
    session: aiohttp.ClientSession,
    base,
    minPrice,
    minLandArea,
    minBuiltupSize,
    maxLandArea,
    maxBuiltupSize,
    max_page=0,
):
    base_url = f"https://www.rumah123.com/{base}/?maxBuiltupSize={maxBuiltupSize}&maxLandArea={maxLandArea}&minBuiltupSize={minBuiltupSize}&minLandArea={minLandArea}&minPrice={minPrice}&sort=price-asc"

    if max_page == 0:
        html = await fetch_page(session, base_url + "&page=1")
        soup = BeautifulSoup(html, "html.parser")
        max_page = int(
            soup.find("div", id="search-page__content-bottom")
            .find("ul")
            .find_all("li")[5]
            .find("a")
            .text
        )

    tasks = [parse_page(session, base_url, page) for page in range(1, max_page + 1)]
    results = await asyncio.gather(*tasks)

    # Flatten the results and create a DataFrame
    flat_data = [item for sublist in results for item in sublist]
    df = pd.DataFrame(flat_data)
    # Render DataFrame
    if "URL" in df.columns:
        df["URL"] = df["URL"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    else:
        print("URL column not found in the DataFrame.")

    return df
