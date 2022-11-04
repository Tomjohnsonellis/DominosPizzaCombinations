import itertools
import random

sizes = ["Personal", "Small", "Medium", "Large"]
crusts = ["Classic", "Italian", "Thin & Crispy", "Stuffed Crust"]


def setup_sauces_and_cheeses():
    sauces = {
        "NO SAUCE": 0,
        "BBQ": 1,
        "Extra BBQ": 2,
        "Tomato": 1,
        "Extra Tomato": 2,
    }
    cheeses = {
        "NO CHEESE": 0,
        "Reduced Fat": 1,
        "Extra Reduced Fat": 2,
        "Mozzarella": 1,
        "Extra Mozzarella": 2,
        "Vegan Cheese": 1,
        "Extra Vegan Cheese": 2,
    }
    return sauces, cheeses


def setup_toppings_dict() -> dict:
    toppings = {
        # "NO TOPPINGS": 0,
        "Pepperoni": 1,
        "Extra Pepperoni": 2,
        "Chicken Breast Strips": 1,
        "Extra Chicken Breast Strips": 2,
        "Sweetcorn": 1,
        "Extra Sweetcorn": 2,
        "Ham": 1,
        "Extra Ham": 2,
        "Mushrooms": 1,
        "Extra Mushrooms": 2,
        "Onions": 1,
        "Extra Onions": 2,
        "Pineapple": 1,
        "Extra Pineapple": 2,
        "Smoked Bacon Rashers": 1,
        "Extra Smoked Bacon Rashers": 2,
        "Green and Red Peppers": 1,
        "Extra Green and Red Peppers": 2,
        "Jalapeno Peppers": 1,
        "Extra Jalapeno Peppers": 2,
        "Tandoori Chicken": 1,
        "Extra Tandoori Chicken": 2,
        "Pork Meatballs": 1,
        "Extra Pork Meatballs": 2,
        "Olives": 1,
        "Extra Olives": 2,
        "Ground Beef": 1,
        "Extra Ground Beef": 2,
        "Sausage": 1,
        "Extra Sausage": 2,
        "Garlic Spread": 1,
        "Extra Garlic Spread": 2,
        "Domino's Herbs": 1,
        "Extra Domino's Herbs": 2,
        "Tomatoes": 1,
        "Extra Tomatoes": 2,
        "Tuna": 1,
        "Extra Tuna": 2,
        "Anchovies": 1,
        "Extra Anchovies": 2,
        "Vegan Soya Strips": 1,
        "Extra Vegan Soya Strips": 2,
        "Vegan Soya & Wheat Pepperoni": 1,
        "Extra Vegan Soya & Wheat Pepperoni": 2,
        "Heinz Tomato Ketchup": 1, # At the time of doing this, there's a promotional breakfast pizza with either ketchup or HP sauce
        "Extra Heinz Tomato Ketchup": 2,
        "HP Sauce": 1,
        "Extra HP Sauce": 2,
        }
    return toppings


def find_sauce_or_cheese_only(sauces: dict, cheeses: dict) -> list:
    sauce_or_cheese_pizzas = []
    for sauce in sauces:
        if sauce == "NO SAUCE":
            for cheese in cheeses:
                sauce_or_cheese_pizzas.append(["NO SAUCE", cheese, cheeses[cheese]])
        else:
            sauce_or_cheese_pizzas.append([sauce, "NO CHEESE", sauces[sauce]])

    return sauce_or_cheese_pizzas

def generate_possible_toppings(toppings_number: int) :
    toppings = setup_toppings_dict()
    combos = itertools.combinations(toppings, toppings_number)
    return combos

def validate_combos(combos_to_validate, points_to_spend):
    valid_combos = []
    for combo in combos_to_validate:
        valid = True
        # print("-----")
        # print(combo)
        # # We need to remove any combinations like "Ham and Extra Ham" as those are invalid
        # # This code works fine for 2 toppings, but it would be better to generalise to any length
        # if combo[0] in combo[1] or combo[1] in combo[0]:
        #     print("TRIPLE PORTION")
        # else:
        #     valid_combos.append(combo)
        contains_extra = False
        for topping in combo:

            # print(">>>", topping)

            if "Extra" in topping:
                # print("EXTRA DETECTED")
                contains_extra = True

        if contains_extra:
            # occurences = 0
            for topping in combo:
                # This checks to see if any toppings in the current combo are the singular versions of "Extra X"
                if topping[6:] in combo:
                    # occurences += 1
                    # print(occurences)
                    valid = False

        if valid:
            valid = count_topping_points(combo, points_to_spend)

        if valid:
            valid_combos.append(combo)

    return valid_combos


def count_topping_points(toppings_combo, points_target):
    topping_dict = setup_toppings_dict()
    points_total = 0
    # print(toppings_combo)
    for topping in toppings_combo:
        # print(">>>", topping)
        # print(topping_dict[topping])
        points_total += topping_dict[topping]

    # print("Points total: ", points_total)
    if points_total == points_target:
        return True
    else:
        return False


if __name__ == '__main__':
    sauce_dict, cheese_dict = setup_sauces_and_cheeses()
    topping_dict = setup_toppings_dict()
    # print(sauce_dict)
    # print(cheese_dict)
    # print(topping_dict)
    # Let's see how many pizzas with either a cheese or a sauce we can make
    # boring_pizzas = find_sauce_or_cheese_only(sauce_dict, cheese_dict)
    # print(boring_pizzas)
    # print(len(boring_pizzas))
    # print(list(topping_dict.items())[1][1])
    # topping_combos = generate_possible_toppings(8)
    # some_valid_combos = validate_combos(topping_combos, 8)
    # print(some_valid_combos)
    # print(type(some_valid_combos))
    # print(len(some_valid_combos))

    # Okay, we can now crunch the numbers on every possible valid combination of each length
    # At most, there could be 8 single toppings and a sauce OR cheese
    # As processor time is cheaper than human time, I'll just find every valid combination for each points total

    boring_pizzas = find_sauce_or_cheese_only(sauce_dict, cheese_dict)
    print("Boring Pizzas:" ,len(boring_pizzas))

    # Next is possible sauce and cheese combinations and their respective point values
    sauce_and_cheese_combos = []
    for sauce in sauce_dict:
        for cheese in cheese_dict:
            # print("---")
            # print(sauce, cheese)
            # print(sauce_dict[sauce] + cheese_dict[cheese])
            sauce_and_cheese_combos.append([sauce, cheese, sauce_dict[sauce] + cheese_dict[cheese]])
    # The NO SAUCE NO CHEESE pizza is invalid
    sauce_and_cheese_combos.remove(sauce_and_cheese_combos[0])
    print(sauce_and_cheese_combos)
    print("Sauce/Cheese Combos: ", len(sauce_and_cheese_combos))
    print("Total so far: ", abs(len(boring_pizzas) - len(sauce_and_cheese_combos)))
    # As shown in the readme, there are 11 different bases that can be used in a Domino's order
    pizza_bases = 11

    # This takes a LONG time to process!
    # total_pizza_combinations = 0
    # combo_counts = []
    # for i in range(1,9):
    #     print(i)
    #     topping_combos = generate_possible_toppings(i)
    #     valid_combos = validate_combos(topping_combos,i)
    #     total_pizza_combinations += len(valid_combos)
    #     print("Running Total: ", total_pizza_combinations)
    #     combo_counts.append([i,len(valid_combos)])
    #     print(combo_counts)
        #
        # Running
        # Total: 24
        # [[1, 24]]
        # 2
        # Running
        # Total: 300
        # [[1, 24], [2, 276]]
        # 3
        # Running
        # Total: 2324
        # [[1, 24], [2, 276], [3, 2024]]
        # 4
        # Running
        # Total: 12950
        # [[1, 24], [2, 276], [3, 2024], [4, 10626]]
        # 5
        # Running
        # Total: 55454
        # [[1, 24], [2, 276], [3, 2024], [4, 10626], [5, 42504]]
        # 6
        # Running
        # Total: 190050
        # [[1, 24], [2, 276], [3, 2024], [4, 10626], [5, 42504], [6, 134596]]
        # 7
        # Running
        # Total: 536154
        # [[1, 24], [2, 276], [3, 2024], [4, 10626], [5, 42504], [6, 134596], [7, 346104]]
        # 8
        # Running
        # Total: 1271625
        # [[1, 24], [2, 276], [3, 2024], [4, 10626], [5, 42504], [6, 134596], [7, 346104], [8, 735471]]

    # As there's no need to recalculate this number now that we have it, I'm going to store it
    points_and_toppings = [[1, 24], [2, 276], [3, 2024], [4, 10626], [5, 42504], [6, 134596], [7, 346104], [8, 735471]]
    # Now that we have every possible valid combination and their point counts, we can do some summation
    # Each pizza can have a maximum of 9 points, so we need to sum all the combinations up to that amount
    # E.g. A pizza with 4 points spent on sauce/cheese can have 0,1,2,3,4,5 points spent on toppings

    for sauce_cheese_combo in sauce_and_cheese_combos:
        # print(sauce_cheese_combo)
        combo_sum = 0
        # Sum all the possible toppings combinations that a pizza could fit given the sauce/cheese
        for i in range(9 - sauce_cheese_combo[2]):
            # print(i)
            combo_sum += points_and_toppings[i][1]

        sauce_cheese_combo.append(combo_sum)

    # print("---")
    # print(sauce_and_cheese_combos)
    possible_pizzas_per_base = 0
    for results in sauce_and_cheese_combos:
        possible_pizzas_per_base += results[3]

    print(possible_pizzas_per_base)
    # For the final calculation
    #pizza_bases * total_possible_toppings = result
    print("-----")
    print("After all that, we have...")
    print(pizza_bases * possible_pizzas_per_base, " possible pizzas!")
