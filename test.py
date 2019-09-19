import unittest
from app import camel_case

class TestCamelCase(unittest.TestCase):
  def test_text(self):
    self.assertEqual(camel_case('i do not like green eggs and ham'), 'IDoNotLikeGreenEggsAndHam')
    self.assertEqual(camel_case("test case"), "TestCase")
    self.assertEqual(camel_case("camel case method"), "CamelCaseMethod")
    self.assertEqual(camel_case("say hello "), "SayHello")
    self.assertEqual(camel_case(" camel case word"), "CamelCaseWord")

if __name__ == '__main__':
  unittest.main()