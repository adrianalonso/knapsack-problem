class Knapsack:

    def __init__(self, size):
        self.elements = []
        self.size = size

    def get_available_size(self):
        available_size = self.size
        for e in self.elements:
            available_size = available_size - e.weight

        return available_size

    def get_total_value(self):
        total_value = 0
        for e in self.elements:
            total_value = total_value + e.value

        return total_value

    def add_element(self, element):
        self.elements.append(element)

        return self

    def remove_last(self):
        return self.elements.pop()
