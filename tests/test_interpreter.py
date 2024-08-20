"""
Unit tests for the Interpreter class from the interpreter_logic.interpreter module.

This test suite uses the unittest framework to validate that the Interpreter class correctly
evaluates Abstract Syntax Trees (ASTs) produced by the parser. The tests cover arithmetic
operations, logical operations, function definitions, function calls, and error handling.

Classes:
- TestInterpreter: Contains test methods to validate the functionality of the Interpreter.

Methods:
- run_test_case: Helper method to compare the expected result with the actual result of interpreting the input code.
- run_test_case_with_exception: Helper method to assert that the Interpreter raises the expected exception.
- Various test methods to validate the correct evaluation of different language constructs.
"""

import unittest
from interpreter_logic.lexer import Lexer
from interpreter_logic.parser import Parser
from interpreter_logic.interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    """
    Test case class for validating the Interpreter class functionality.
    """

    def run_test_case(self, input_code, expected_result):
        """
        Asserts that the Interpreter correctly evaluates the input code to produce the expected result.

        Args:
            input_code (str): The input source code.
            expected_result (any): The expected result of interpreting the input code.
        """
        lexer = Lexer(input_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse_program()
        interpreter = Interpreter()
        result = interpreter.eval(ast)
        self.assertEqual(result, expected_result, f"Expected: {expected_result}, but got: {result}")

    def run_test_case_with_exception(self, input_code, expected_exception):
        """
        Asserts that the Interpreter raises the expected exception when evaluating the input code.

        Args:
            input_code (str): The input source code.
            expected_exception (Exception): The exception type expected to be raised.
        """
        lexer = Lexer(input_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse_program()
        interpreter = Interpreter()
        with self.assertRaises(expected_exception):
            interpreter.eval(ast)

    # Arithmetic operations
    def test_subtraction(self):
        """Tests subtraction operation."""
        self.run_test_case("10 - 3", 7)

    def test_multiplication(self):
        """Tests multiplication operation."""
        self.run_test_case("6 * 7", 42)

    def test_division(self):
        """Tests division operation."""
        self.run_test_case("8 / 2", 4)

    def test_modulo(self):
        """Tests modulo operation."""
        self.run_test_case("10 % 3", 1)

    def test_nested_arithmetic_operations(self):
        """Tests nested arithmetic operations."""
        self.run_test_case("(2 + 3) * (5 - 2)", 15)

    # Logical operations
    def test_logical_and(self):
        """Tests logical AND operation."""
        self.run_test_case("(4 > 2) && (3 < 5)", True)

    def test_logical_or(self):
        """Tests logical OR operation."""
        self.run_test_case("(4 > 5) || (3 < 5)", True)

    # Function definitions and calls
    def test_function_definition_and_call(self):
        """Tests function definition and its call."""
        self.run_test_case("Defun {'name': 'double', 'arguments': (x,)} x * 2 double(4)", 8)

    def test_recursive_function_factorial(self):
        """Tests a recursive function (factorial) definition and call."""
        self.run_test_case("Defun {'name': 'factorial', 'arguments': (n,)} (n == 0) || (n * factorial(n - 1)) factorial(5)", 120)

    # Error Handling
    def test_division_by_zero(self):
        """Tests division by zero error handling."""
        self.run_test_case_with_exception("10 / 0", ZeroDivisionError)

    def test_undefined_variable(self):
        """Tests undefined variable error handling."""
        self.run_test_case_with_exception("x + 5", NameError)

    def test_nested_function_calls(self):
        """Tests nested function calls."""
        input_code = """
        Defun {'name': 'add', 'arguments': (x, y,)} x + y
        Defun {'name': 'double_add', 'arguments': (a, b,)} add(a, b) * 2
        double_add(3, 4)
        """
        self.run_test_case(input_code, 14)

    # Additional tests can be uncommented and added as needed
    # def test_passing_function_as_argument(self):
    #     """Tests passing a function as an argument to another function."""
    #     input_code = """
    #     Defun {'name': 'apply', 'arguments': (f, x,)} f(x)
    #     Defun {'name': 'increment', 'arguments': (n,)} n + 1
    #     apply(increment, 5)
    #     """
    #     self.run_test_case(input_code, 6)

    # def test_lambda_within_function(self):
    #     """Tests using a lambda within a function."""
    #     input_code = """
    #     Defun {'name': 'double_apply', 'arguments': (f, x,)} f(f(x))
    #     double_apply((Lambd y. y * 2), 5)
    #     """
    #     self.run_test_case(input_code, 20)


if __name__ == '__main__':
    unittest.main()
