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

parser.add_argument('--usda-api-key', type=str,
                    help='API key for accessing the USDA nutrition API. Available for free at https://api.data.gov/signup/.')

args = parser.parse_args()

client = noms.Client(args.usda_api_key)

if True:

    search_results = client.search_query("orange")

    print(search_results)

milk = {
    'FNDDS': 1097517
}

cereal_musli = {
    'FNDDS': 1101779
}

banana = {
    'FNDDS': 1102653
}

scrambled_egg_no_fat_added = {
    'FNDDS': 1100240
}

tap_water = {
    'FNDDS': 1104492
}

mango = {
    'SRL': 169910,
    'FNDDS': 1102670
}

canned_black_beans_no_added_fat = {
    'FNDDS': 1100378
}

raw_celery = {
    'SRL': 169988,
    'FNDDS': 1103346
}

canned_corn = {
    'FNDDS': 1103505
}

uncle_ben_rice = {
    'SRL': 173263,
}

olive_oil = {
    'FNDDS': 1103861
}

cumin = {
    'SRL': 170923
}

if False:

    # in a week, there are 21 meals
    # 7 of those are breakfast
    # 3.7 L water every day

    cereal_for_breakfast = 5
    eggs_for_breakfast = 1

    meal_0 = noms.Meal(client.get_foods(
        {
            # Water
            tap_water['FNDDS']: 4000 * 7,

            # Breakfast
            cereal_musli['FNDDS']: 150 * cereal_for_breakfast,
            milk['FNDDS']: 200 * cereal_for_breakfast,
            banana['FNDDS']: 25 * cereal_for_breakfast,

            # real weight should be a bit less than 50 after cooking
            scrambled_egg_no_fat_added["FNDDS"]: 3 * (50 - 5) * eggs_for_breakfast,
            orange["todo"]: 100 * eggs_for_breakfast,


            # Monday Lunch
            # pasta
            # Monday Dinner
            cumin['SRL']: 0.1,
            olive_oil['FNDDS']: 10,
            uncle_ben_rice['SRL']: 125,
            canned_corn['FNDDS']: 100,
            raw_celery['FNDDS']: 30,
            canned_black_beans_no_added_fat['FNDDS']: 150,
            mango['FNDDS']: 80,
        }))

    meal_1 = noms.Meal(client.get_foods(
        {
            # Monday Water
            tap_water['FNDDS']: 4000,
            # Monday Breakfast
            cereal_musli['FNDDS']: 150,
            milk['FNDDS']: 200,
            banana['FNDDS']: 25,
            # Monday Lunch
            # pasta
            # Monday Dinner
            cumin['SRL']: 0.1,
            olive_oil['FNDDS']: 10,
            uncle_ben_rice['SRL']: 125,
            canned_corn['FNDDS']: 100,
            raw_celery['FNDDS']: 30,
            canned_black_beans_no_added_fat['FNDDS']: 150,
            mango['FNDDS']: 80,
        }))

    r = noms.report(meal_0)

    for i in r:
        print(i)


# food_list = client.get_foods({'1100240':50})

# print("foods: ", food_list)
# print("foods: ", [noms.report(f) for f in food_list])

# search_results = client.search_query("Raw Broccoli")
# print(search_results)

# food_list = client.get_foods({'1103170':100, '169404':100})

# print("food_list: ", food_list)

# m = noms.Meal(food_list)

# r = noms.report(m)
# for i in r:
#     print(i)
