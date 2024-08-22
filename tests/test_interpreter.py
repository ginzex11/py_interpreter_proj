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

    def run_test_case(self, input_code, expected_output):
        lexer = Lexer(input_code)
        tokens = lexer.tokenize()
        print(f"Tokens: {tokens}")  # Debug print

        parser = Parser(tokens)
        ast = parser.parse_program()
        print(f"AST: {ast}")  # Debug print

        interpreter = Interpreter()
        result = interpreter.eval(ast)
        print(f"Result: {result}")  # Debug print

        self.assertEqual(result, expected_output, f"Expected: {expected_output}, but got: {result}")

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
        self.run_test_case(
            "Defun {'name': 'factorial', 'arguments': (n,)} (n == 0) || (n * factorial(n - 1)) factorial(5)", 120)

    # Error Handling

    # In your interpreter tests (e.g., test_interpreter.py)
    def test_type_mismatch_in_comparison(self):
        """
        Tests that an invalid comparison that could cause a type mismatch raises a TypeError.
        """
        input_code = "'hello' > 5"
        with self.assertRaises(TypeError):
            lexer = Lexer(input_code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse_program()
            interpreter = Interpreter()
            interpreter.eval(ast)

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

    def test_unary_op(self):
        """Tests unary operation."""
        input_code = "!(3 < 4)"
        self.run_test_case(input_code, False)

    def test_lambda_manual_debugging(self):
        """
        Manual debugging for lambda expression evaluation.
        """
        input_code = "(Lambd x. (Lambd y. (x + y))) (3) (5)"
        lexer = Lexer(input_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse_program()
        parsed_lambda_expr = ast.body[0]  # Getting the lambda expression from the AST

        interpreter = Interpreter()

        # Step 1: Evaluate the outer lambda expression
        lambda_expr = interpreter.eval(parsed_lambda_expr)
        print("Outer lambda result (should be a function):", lambda_expr)

        # Step 2: Apply the first argument (3) to the lambda
        partial_application = lambda_expr(3)
        print("Result after applying the first argument (should be a function):", partial_application)

        # Step 3: Apply the second argument (5) to the resulting lambda
        final_result = partial_application(5)
        print("Final result (should be 8):", final_result)
        self.assertEqual(final_result, 8)


if __name__ == '__main__':
    unittest.main()
