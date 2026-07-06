China Travel MCP

The most comprehensive MCP server for China inbound travel, powered by Trip.com — the world's #1 travel platform for visiting China. Real-time hotel pricing, flight search, attraction tickets, itinerary planning, and travel tips with one-click booking.

✈️ Official Trip.com Affiliate Partner — All search results include live pricing and direct booking links from Trip.com, supporting Visa/Mastercard/international payment.

Features

🏨 Search Hotels — Find hotels across China with real-time pricing and Trip.com booking links
✈️ Search Flights — Query domestic and international flights to/from China
🎫 Search Attractions — Discover top attractions, ticket prices, and opening hours
📋 Plan Itinerary — Generate complete multi-day travel itineraries
💡 Travel Tips — Get practical advice on visa, transportation, payment, safety, and culture

Quick Start

Installation

bash
1
2
pip install china-travel-mcp



Run as Standalone Server

bash
1
2
china-travel-mcp



Configure in Claude Desktop / Cursor

Add to your MCP client configuration:

json
1
2
3
4
5
6
7
8
9
{
  "mcpServers": {
    "china-travel": {
      "command": "uvx",
      "args": ["china-travel-mcp"]
    }
  }
}



Build from Source

bash
1
2
3
4
git clone https://github.com/mako2026/china-travel-mcp.git
cd china-travel-mcp
pip install -e .



Tools

search_hotels

Search hotels in any Chinese city with pricing and booking links.

Parameters:

city (required) — City name, e.g. "Beijing", "Shanghai", "Xi'an"
check_in — Check-in date (YYYY-MM-DD)
check_out — Check-out date (YYYY-MM-DD)
guests — Number of guests (default: 2)
budget — Budget level, e.g. "budget", "mid-range", "luxury"
preferences — Preferences, e.g. "near city center", "with breakfast"

search_flights

Search flights to, from, or within China.

Parameters:

origin (required) — Departure city, e.g. "Tokyo", "New York"
destination (required) — Arrival city, e.g. "Shanghai", "Beijing"
date (required) — Travel date (YYYY-MM-DD)
trip_type — "one way" or "round trip" (default: "one way")
cabin — "economy", "business", or "first" (default: "economy")

search_attractions

Discover top attractions and things to do in Chinese cities.

Parameters:

city (required) — City name, e.g. "Beijing", "Guilin", "Hangzhou"
days — Number of sightseeing days (default: 1)
interests — Interests, e.g. "history", "nature", "food", "photography"

plan_itinerary

Generate a complete multi-day travel itinerary.

Parameters:

city (required) — City name
days (required) — Number of days
travelers — Number of travelers (default: 2)
interests — Travel interests
budget — Budget level

get_travel_tips

Get practical travel advice for China.

Parameters:

question (required) — Your travel question in natural language

Examples

Ask your AI assistant:

"Find me a hotel in Shanghai near the Bund for 3 nights"
"What flights are available from Tokyo to Beijing next Friday?"
"What are the must-visit attractions in Xi'an?"
"Plan a 5-day trip to Chengdu for a couple interested in food and pandas"
"Do I need a visa to visit China? What about the 144-hour transit visa?"

Supported Languages

The server defaults to English responses. The underlying API also supports: Chinese (zh), Japanese (ja), Korean (ko), Russian (ru), Spanish (es), French (fr), German (de), Arabic (ar), Thai (th), Vietnamese (vi).

Data Source

This MCP server is built by an Official Trip.com Affiliate Partner (Alliance ID: 8405769). All hotel, flight, and attraction data is sourced directly from Trip.com's real-time inventory via the TripGenie API.

Trip.com is the international brand of Trip.com Group (NASDAQ: TCOM / 9961.HK), the world's leading online travel agency. With 1.4M+ hotels, 5,000+ city flight coverage, and 24/7 multilingual support, Trip.com is the most trusted booking platform for travelers visiting China.

All booking links in search results are direct Trip.com links with affiliate tracking, ensuring travelers get the best available prices while supporting the continued development of this MCP server.

License

MIT
