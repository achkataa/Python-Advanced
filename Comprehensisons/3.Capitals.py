countries = input().split(", ")
cities = input().split(", ")


pack = zip(countries, cities)

result = {p[0]: p[1] for p in pack}

for key, value in result.items():
    print(f"{key} -> {value}")

