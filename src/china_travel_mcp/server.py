"""
China Travel MCP Server
Inbound travel assistant for foreign tourists visiting China.
Powered by TripGenie API via SCF proxy, with Trip.com affiliate links.
"""

import requests
from fastmcp import FastMCP


# SCF Proxy configuration
PROXY_URL = "https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com"
PROXY_TOKEN = os.environ.get("PROXY_TOKEN", "tp_8k2mX9vQ4z")


mcp = FastMCP("china-travel-mcp")


def query_tripgenie(query: str, locale: str = "en", command_type: str = "query") -> str:
    """
    Send query to TripGenie API through SCF proxy.

    Args:
        query: Natural language travel query
        locale: Response language (en, zh, ja, ko, ru, etc.)
        command_type: Query type (hotel, flight, attraction, itinerary, query)

    Returns:
        Response text from TripGenie
    """
    headers = {
        "Content-Type": "application/json",
        "X-Proxy-Token": PROXY_TOKEN,
        "User-Agent": "ChinaTravelMCP/1.0",
    }
    payload = {
        "query": query,
        "locale": locale,
        "command_type": command_type,
    }

    try:
        resp = requests.post(PROXY_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()

        if isinstance(result, dict) and "data" in result:
            return str(result["data"])
        elif isinstance(result, str):
            return result
        else:
            return str(result)
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


@mcp.tool()
def search_hotels(city: str, check_in: str = "", check_out: str = "", guests: int = 2, budget: str = "", preferences: str = "") -> str:
    """
    Search hotels in China with real-time pricing and booking links.

    Args:
        city: City name in China, e.g. "Beijing", "Shanghai", "Xi'an", "Chengdu"
        check_in: Check-in date (YYYY-MM-DD format), optional
        check_out: Check-out date (YYYY-MM-DD format), optional
        guests: Number of guests (default: 2)
        budget: Budget level or range, e.g. "budget", "mid-range", "luxury", "$50-100/night"
        preferences: Hotel preferences, e.g. "near city center", "with breakfast", "business hotel"

    Returns:
        Hotel recommendations with names, prices per night, ratings, key features, and booking links
    """
    parts = [f"Find hotels in {city}"]
    if check_in and check_out:
        parts.append(f"from {check_in} to {check_out}")
    parts.append(f"for {guests} guest{'s' if guests > 1 else ''}")
    if budget:
        parts.append(f"budget: {budget}")
    if preferences:
        parts.append(f"preferences: {preferences}")
    parts.append("Include hotel names, prices per night, ratings, key features, and booking links.")

    query = ", ".join(parts)
    return query_tripgenie(query, locale="en", command_type="hotel")


@mcp.tool()
def search_flights(origin: str, destination: str, date: str, trip_type: str = "one way", cabin: str = "economy") -> str:
    """
    Search flights to/from/within China with real-time pricing.

    Args:
        origin: Departure city or airport, e.g. "Tokyo", "New York", "London", "Beijing"
        destination: Arrival city or airport, e.g. "Shanghai", "Beijing", "Guangzhou"
        date: Travel date (YYYY-MM-DD format)
        trip_type: Trip type - "one way" or "round trip" (default: "one way")
        cabin: Cabin class - "economy", "business", "first" (default: "economy")

    Returns:
        Flight options with airline, flight number, departure/arrival times, prices, and booking links
    """
    query = f"Find {cabin} class flights from {origin} to {destination} on {date}, {trip_type}. Include airline names, flight numbers, departure and arrival times, prices, and booking links."
    return query_tripgenie(query, locale="en", command_type="flight")


@mcp.tool()
def search_attractions(city: str, days: int = 1, interests: str = "") -> str:
    """
    Search top attractions and things to do in Chinese cities.

    Args:
        city: City name in China, e.g. "Beijing", "Xi'an", "Guilin", "Hangzhou"
        days: Number of days available for sightseeing (default: 1)
        interests: Specific interests, e.g. "history", "nature", "food", "photography", "family-friendly"

    Returns:
        Attraction recommendations with descriptions, ticket prices, opening hours, and practical tips
    """
    parts = [f"What are the top attractions and things to do in {city}"]
    if days > 1:
        parts.append(f"for {days} days")
    if interests:
        parts.append(f"interested in: {interests}")
    parts.append("Include ticket prices, opening hours, location, and practical tips if available.")

    query = ", ".join(parts)
    return query_tripgenie(query, locale="en", command_type="attraction")


@mcp.tool()
def plan_itinerary(city: str, days: int, travelers: int = 2, interests: str = "", budget: str = "") -> str:
    """
    Plan a complete multi-day itinerary for visiting a Chinese city.

    Args:
        city: City name in China, e.g. "Beijing", "Shanghai", "Chengdu", "Xi'an"
        days: Number of days for the trip
        travelers: Number of travelers (default: 2)
        interests: Travel interests, e.g. "history and culture", "food and nightlife", "nature and hiking"
        budget: Budget level, e.g. "budget", "mid-range", "luxury"

    Returns:
        Complete day-by-day itinerary with hotel recommendations, must-see attractions, dining suggestions, transportation tips, and booking links
    """
    parts = [f"Plan a {days}-day itinerary for {city}"]
    parts.append(f"for {travelers} traveler{'s' if travelers > 1 else ''}")
    if interests:
        parts.append(f"interests: {interests}")
    if budget:
        parts.append(f"budget level: {budget}")
    parts.append("Include hotel recommendations, must-see attractions, dining suggestions, local transportation tips, and practical advice.")

    query = ", ".join(parts)
    return query_tripgenie(query, locale="en", command_type="itinerary")


@mcp.tool()
def get_travel_tips(question: str) -> str:
    """
    Get travel tips and practical information for traveling in China.

    Args:
        question: Travel question in natural language, e.g. "Do I need a visa for China?", "What is the best time to visit the Great Wall?", "How to use Alipay in China?", "Is it safe to travel alone in China?"

    Returns:
        Detailed travel advice covering visa, transportation, payment, safety, cultural tips, and more
    """
    return query_tripgenie(question, locale="en", command_type="query")


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
