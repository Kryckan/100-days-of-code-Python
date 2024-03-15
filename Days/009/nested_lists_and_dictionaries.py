# Nesting dictionaries in a dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris" "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
# }


travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris" "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

print(travel_log[1])
