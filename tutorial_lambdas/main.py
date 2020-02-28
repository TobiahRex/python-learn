import unittest
from functools import partial

def multipy(multiplier, num):
    return multiplier * num

class Multiply():
    def __init__(self):
        self.multipy = partial(multipy, 2)
    def double(self, num):
        return self.multipy(num)


class MultiplyTest(unittest.TestCase):
    def test_double(self):
        # assert_true = self.assertTrue
        
        # def validate_results():
        #     assert_true
        assert_double = Multiply()
        result = assert_double.double(3)
        self.assertTrue(result == 6)
        self.assertTrue(result == 5)
        self.assert

  

if __name__ == '__main__':
    unittest.main()
    # print(f'result: {result == 6}')
