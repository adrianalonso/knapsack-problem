import unittest
import element
import knapsack
import algorithm


class KnapsackUnitTest(unittest.TestCase):

    def test_algorithm_with_3_elements_and_size_50(self):
        elements = []
        elements.append(element.Element(weight=10, value=60))
        elements.append(element.Element(weight=20, value=100))
        elements.append(element.Element(weight=30, value=120))
        bag = knapsack.Knapsack(size=50)

        result = algorithm.knapsack_algorithm(bag, elements, len(elements))

        self.assertEqual(result, 220)

    def test_algorithm_with_4_elements_and_size_8(self):
        elements = []
        elements.append(element.Element(weight=4, value=10))
        elements.append(element.Element(weight=3, value=40))
        elements.append(element.Element(weight=5, value=30))
        elements.append(element.Element(weight=2, value=20))
        bag = knapsack.Knapsack(size=8)

        result = algorithm.knapsack_algorithm(bag, elements, len(elements))

        self.assertEqual(result, 70)
