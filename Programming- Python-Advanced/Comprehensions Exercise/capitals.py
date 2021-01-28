country = (input().split(", "))
city = (input().split(", "))
result = {country[index]: city[index] for index in range(len(city))}
print(*[f"{key} -> {value}"for key, value in result.items()], sep="\n")