sizes = ["Personal", "Small", "Medium", "Large"]
crusts = ["Classic", "Italian", "Thin & Crispy", "Stuffed Crust"]


def setup_dictionaries():
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
    toppings = {
        "NO TOPPINGS": 0,
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
        "Heinz Tomato Ketchup": 1,
        # At the time of doing this, there's a promotional breakfast pizza with either ketchup or HP sauce
        "Extra Heinz Tomato Ketchup": 2,
        "HP Sauce": 1,
        "Extra HP Sauce": 2,
    }
    return [sauces, cheeses, toppings]


def find_sauce_or_cheese_only(sauces: dict, cheeses: dict) -> list:
    sauce_or_cheese_pizzas = []
    for sauce in sauces:
        if sauce == "NO SAUCE":
            for cheese in cheeses:
                sauce_or_cheese_pizzas.append(["NO SAUCE", cheese, cheeses[cheese]])
        else:
            sauce_or_cheese_pizzas.append([sauce, "NO CHEESE", sauces[sauce]])

    return sauce_or_cheese_pizzas


if __name__ == '__main__':
    sauce_dict, cheese_dict, topping_dict = setup_dictionaries()
    print(sauce_dict)
    print(cheese_dict)
    print(topping_dict)
    # Let's see how many pizzas with either a cheese or a sauce we can make
    boring_pizzas = find_sauce_or_cheese_only(sauce_dict, cheese_dict)
    print(boring_pizzas)
    print(len(boring_pizzas))
