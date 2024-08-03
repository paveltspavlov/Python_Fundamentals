import math

centuries = int(input())
years = 100 * centuries
days = math.floor((365.2422 * years))
hours = days * 24
minutes = 60 * hours

print(f"{centuries} centuries = {years} years = {days} days = {hours:.0f} hours = {minutes:.0f} minutes")
