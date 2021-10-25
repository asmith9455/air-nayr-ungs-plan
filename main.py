# from usda import UsdaClient
# client = UsdaClient('f037JY9qRs866BJTCgcZugFpQmwHbq19VSUQgqXf')

# foods_search = client.search_foods(
#      'coffee, instant, regular, prepared with water', 1)

# coffee = next(foods_search)
# print(coffee)

# report = client.get_food_report(coffee.id)
# for nutrient in report.nutrients:
#      print(nutrient.name, nutrient.value, nutrient.unit)

import noms

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--usda-api-key', type=str, help='API key for accessing the USDA nutrition API. Available for free at https://api.data.gov/signup/.')

args = parser.parse_args()

client = noms.Client(args.usda_api_key)

search_results = client.search_query("Raw Broccoli")
print(search_results)

food_list = client.get_foods({'1103170':100, '169404':100})

print("food_list: ", food_list)

m = noms.Meal(food_list)

r = noms.report(m)
for i in r:
    print(i)