
def knapsack_algorithm(bag, elements, position):
    if position == 0:
        return bag.get_total_value()

    current_element = elements[position-1]

    if(bag.get_available_size() - current_element.weight < 0):
        return knapsack_algorithm(bag, elements, position-1)

    bag.add_element(elements[position-1])
    included = knapsack_algorithm(bag, elements, position-1)
    bag.remove_last()
    non_included = knapsack_algorithm(bag, elements, position-1)

    return max(included, non_included)
