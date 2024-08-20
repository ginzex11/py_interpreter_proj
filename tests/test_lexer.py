"""
Unit tests for the Lexer class from the interpreter_logic.lexer module.

This test suite uses the unittest framework to validate that the Lexer class
correctly tokenizes input text into a sequence of tokens, including handling
integers, identifiers, keywords, operators, comparisons, logical operators,
special characters, and comments.

Classes:
- TestLexer: Contains various test methods to validate Lexer functionality.

Methods:
- assert_tokens: Helper method to compare expected tokens with the actual output from the Lexer.
- Various test methods to validate correct tokenization of different language constructs.
"""

import unittest
from interpreter_logic.lexer import Lexer, Token, INTEGER, BOOLEAN, IDENTIFIER, KEYWORD, PLUS, MINUS, MULTIPLY, DIVIDE, \
    MODULO, LPAREN, RPAREN, COMMA, DOT, LBRACE, RBRACE, QUESTION, COLON, AND, OR, NOT, EQ, NEQ, GT, LT, GTE, LTE, EOF, \
    LAMBDA, LBRACE, RBRACE, QUESTION, COLON, ASSIGN, KEYWORDS


class TestLexer(unittest.TestCase):
    """
    Test case class for validating the Lexer class functionality.
    """

    def assert_tokens(self, text, expected_tokens):
        """
        Asserts that the Lexer correctly tokenizes the input text into the expected sequence of tokens.

        Args:
            text (str): The input text to be tokenized.
            expected_tokens (list): The expected list of Token objects.
        """
        lexer = Lexer(text)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, expected_tokens)

    def test_integer(self):
        """
        Tests that integers are correctly tokenized.
        """
        self.assert_tokens(
            "123 456",
            [Token(INTEGER, 123), Token(INTEGER, 456), Token(EOF, None)]
        )

    def test_identifier(self):
        """
        Tests that identifiers are correctly tokenized.
        """
        self.assert_tokens(
            "foo bar",
            [Token(IDENTIFIER, 'foo'), Token(IDENTIFIER, 'bar'), Token(EOF, None)]
        )

    def test_keywords(self):
        """
        Tests that keywords are correctly tokenized.
        """
        self.assert_tokens(
            "Defun True False",
            [Token(KEYWORD, 'Defun'), Token(BOOLEAN, 'True'), Token(BOOLEAN, 'False'), Token(EOF, None)]
        )

    def test_operators(self):
        """
        Tests that arithmetic operators are correctly tokenized.
        """
        self.assert_tokens(
            "+ - * / %",
            [Token(PLUS, '+'), Token(MINUS, '-'), Token(MULTIPLY, '*'), Token(DIVIDE, '/'), Token(MODULO, '%'),
             Token(EOF, None)]
        )

    def test_comparisons(self):
        """
        Tests that comparison operators are correctly tokenized.
        """
        self.assert_tokens(
            "== != > >= < <=",
            [Token(EQ, '=='), Token(NEQ, '!='), Token(GT, '>'), Token(GTE, '>='), Token(LT, '<'), Token(LTE, '<='),
             Token(EOF, None)]
        )

    def test_logical_operators(self):
        """
        Tests that logical operators are correctly tokenized.
        """
        self.assert_tokens(
            "&& || !",
            [Token(AND, '&&'), Token(OR, '||'), Token(NOT, '!'), Token(EOF, None)]
        )

    def test_special_characters(self):
        """
        Tests that special characters are correctly tokenized.
        """
        self.assert_tokens(
            "( ) , . { } ? :",
            [Token(LPAREN, '('), Token(RPAREN, ')'), Token(COMMA, ','), Token(DOT, '.'), Token(LBRACE, '{'),
             Token(RBRACE, '}'), Token(QUESTION, '?'), Token(COLON, ':'), Token(EOF, None)]
        )

    def test_unexpected_characters(self):
        """
        Tests that unexpected characters raise an exception.
        """
        with self.assertRaises(Exception):
            lexer = Lexer("~")
            lexer.tokenize()

    def test_comments(self):
        """
        Tests that comments are correctly ignored by the lexer.
        """
        self.assert_tokens(
            "# this is a comment\n123 # another comment\n456",
            [Token(INTEGER, 123), Token(INTEGER, 456), Token(EOF, None)]
        )

    def test_empty_string(self):
        """
        Tests that an empty string is tokenized correctly.
        """
        self.assert_tokens(
            "",
            [Token(EOF, None)]
        )

    def test_large_input(self):
        """
        Tests that the lexer handles a large input efficiently.
        """
        large_input = " ".join(["foo"] * 10000)  # Simulate a large input with 10,000 identifiers
        self.assert_tokens(
            large_input,
            [Token(IDENTIFIER, 'foo')] * 10000 + [Token(EOF, None)]
        )

    def test_complex_sequence(self):
        """
        Tests that a complex sequence of different tokens is tokenized correctly.
        """
        self.assert_tokens(
            "123 + foo - (True * 4.5)",
            [Token(INTEGER, 123), Token(PLUS, '+'), Token(IDENTIFIER, 'foo'),
             Token(MINUS, '-'), Token(LPAREN, '('), Token(BOOLEAN, 'True'),
             Token(MULTIPLY, '*'), Token(INTEGER, 4), Token(DOT, '.'), Token(INTEGER, 5),
             Token(RPAREN, ')'), Token(EOF, None)]
        )

    def test_assignment_operator(self):
        """
        Tests that the assignment operator '=' is correctly tokenized.
        """
        self.assert_tokens(
            "x = 10",
            [Token(IDENTIFIER, 'x'), Token(ASSIGN, '='), Token(INTEGER, 10), Token(EOF, None)]
        )

    def test_equality_operator(self):
        """
        Tests that the equality operator '==' is correctly tokenized.
        """
        self.assert_tokens(
            "x == 10",
            [Token(IDENTIFIER, 'x'), Token(EQ, '=='), Token(INTEGER, 10), Token(EOF, None)]
        )


if __name__ == '__main__':
    unittest.main()
