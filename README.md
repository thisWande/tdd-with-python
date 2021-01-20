# A simple example of Test Driven Development with Python

Dmitry Rastorguev described TDD on the [FreeCodeCamp](https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/)
>"TDD recommends writing Tests that would check the functionality of your Code prior to your writing the actual Code. Only when you are happy with your Tests and the features it Tests, do you begin to Write the actual Code in order to satisfy the Conditions imposed by the Test that would allow them to pass."

The following sequence is based on Kent Beck's book: [Test-Driven Development by Example](https://dl.acm.org/doi/book/10.5555/579193)
  1. Add a test
  2. Run all tests and see if the new test fails
  3. Write the code
  4. Run tests
  5. Refactor code

### Implementing the steps from Mr Beck's book using an example of a Shopping cart

## Code Example

  1. Add a test
  ```python
class ShoppingCartTest(unittest.TestCase):
    def test_empty_total(self):
        cart = TheCart([])
        self.assertEqual(cart.total(), 0)
```

```python
class TheCart(object):
    items: List

    def total(self):
        pass
```
2. Run all tests and see if the new test fails
```
FAILED (failures=1)
0 != None

Expected :None
Actual   :0
```
  3. Write the code
```python
class TheCart(object):
    items: List

    def total(self):
        return 0
```
  4. Run tests
```
  Ran 1 test in 0.003s
  OK
```
  5. Refactor code
 Added Class Item with unit_price and quantity as its attributes.
Class TheCart has-a relationship with Item


