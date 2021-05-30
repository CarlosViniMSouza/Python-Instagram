#pip install covid

from covid import covid

covid = Covid()

cases = covid.get_status_by_county_name("...")

for x in cases:
    print(x, ":", cases[x])

"""
OUTPUT:

    id : <any int>
    country : <country abbreviation>
    confirmed : <any int>
    active : <any int>
    deaths : <any int>
    recovered : <any int>
"""