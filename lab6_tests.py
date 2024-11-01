import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input = ["One Fish Two Fish", "Animal Farm", "Lord of the Flies"]
        expected = ["Animal Farm","Lord of the Flies","One Fish Two Fish"]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)
    def test_selection_sort_books_2(self):
        input = ["Charlotte's Web", "Brave New World", "Do Androids Dream of Electric Sheep?"]
        expected = ["Brave New World", "Charlotte's Web", "Do Androids Dream of Electric Sheep?"]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)
    # Part 2
    def test_swap_case_1(self):
        input = 'HallOwEeN TiMe!'
        expected = 'hALLoWeEn tImE!'
        result = lab6.swap_case(input)
        self.assertEqual(expected, result)
    def test_swap_case_2(self):
        input = "my name is RisHub"
        expected = "MY NAME IS rIShUB"
        result = lab6.swap_case(input)
        self.assertEqual(expected, result)
    # Part 3
    def test_str_translate_1(self):
        input1, input2, input3 = ("Toy","T","B")
        expected = "Boy"
        result = lab6.str_translate(input1, input2, input3)
        self.assertEqual(expected, result)
    def test_str_translate_2(self):
        input1, input2, input3 = ("woman","a","e")
        expected = "women"
        result = lab6.str_translate(input1, input2, input3)
        self.assertEqual(expected, result)
    # Part 4
    def test_histogram_1(self):
        input = "Mississippi contains the Mississippi river."
        expected = {'Mississippi': 2, 'contains': 1, 'river.': 1, 'the': 1}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)
    def test_histogram_2(self):
        input = "I think I am greater than I am now"
        expected = {'I': 3, 'am': 2, 'greater': 1, 'now': 1, 'than': 1, 'think': 1}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
