"""
================================================================================
LECTURE 73: Nested Dictionaries & Lists in Dictionaries (#lec69)
LECTURE 74: Coding Exercise #24 - Travel Log Program (#lec70)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Nested Dictionaries:
   - Jab dictionary ki value khud ek Dictionary ya List ho.
   - Example 1: List inside Dictionary: `{"fruits": ["apple", "banana"]}`.
   - Example 2: Dictionary inside Dictionary: `{"student": {"id": 101, "marks": 95}}`.
   - Example 3: Dictionary inside List: `[{"country": "India"}, {"country": "Japan"}]` (JSON APIs me sabse common pattern).

2. Deep Access:
   - Syntax: `data["key1"]["key2"][0]`.

3. Exercise #24 - Travel Log:
   - Ek list of dictionaries maintain karni hai jisme country, number of visits, aur visited cities ki list ho.
   - Ek function banana hai `add_new_country(country, visits, list_of_cities)` jo nayi entry dynamically append kare.
"""

# --- 1. Nested Structures Demo ---
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary:
travel_visited = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print("Cities visited in France:", travel_visited["France"])
print("Second city in France  :", travel_visited["France"][1])

# Nesting Dictionary in a Dictionary:
nested_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}
print("Nested dict visit count for Germany:", nested_travel_log["Germany"]["total_visits"])


# --- 2. LECTURE 74: Exercise #24 - Travel Log (List of Dictionaries) ---
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_entry = {
        "country": country_visited,
        "visits": times_visited,
        "cities": cities_visited
    }
    travel_log.append(new_entry)
    print(f"Successfully added {country_visited} to the travel log!")

# Adding Russia
add_new_country(country_visited="Russia", times_visited=2, cities_visited=["Moscow", "Saint Petersburg"])

print("\n--- Current Travel Log ---")
for entry in travel_log:
    print(f"Country: {entry['country']:8s} | Visits: {entry['visits']} | Cities: {', '.join(entry['cities'])}")
