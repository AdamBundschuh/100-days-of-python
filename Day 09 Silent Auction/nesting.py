# Nest a list inside a dictionary


# travel_log = {
#     "France": {"cities_visted": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 8,
#     },
# }

# # Nesting a dictionary in a list

# travel_log = [
#     {
#         "country": "France",
#         "cities_visted": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 8,
#     },
# ]


bidder = {
    "name": "Adam",
    "bid": 12
}

bidder2 = {
    "name": "AdamTwo",
    "bid": 122
}

bids = {
    1: bidder,
    2: bidder2
}

print(bids)