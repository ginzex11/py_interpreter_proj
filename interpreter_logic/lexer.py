# interpreter_logic/lexer.py
"""
Lexer for a simple functional programming language.

This module defines the Lexer class, responsible for tokenizing the input source code
into a sequence of tokens, based on the language's syntax. The lexer handles different
token types such as integers, booleans, identifiers, keywords, operators, and special characters.

Classes:
- Token: Represents a single token with a type and value.
- Lexer: Implements the logic for scanning the input text and generating a list of tokens.

Usage:
Create an instance of the Lexer class with the source code as input, and call the tokenize()
method to obtain a list of tokens.
"""

import re

# Define token types
INTEGER = 'INTEGER'
BOOLEAN = 'BOOLEAN'
IDENTIFIER = 'IDENTIFIER'
KEYWORD = 'KEYWORD'
STRING = 'STRING'

PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
MODULO = 'MODULO'

AND = 'AND'
OR = 'OR'
NOT = 'NOT'

EQ = 'EQ'
NEQ = 'NEQ'
GT = 'GT'
LT = 'LT'
GTE = 'GTE'
LTE = 'LTE'

LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
COMMA = 'COMMA'
DOT = 'DOT'
EOF = 'EOF'  # End of file/input

# Special characters
LAMBDA = 'LAMBDA'  # Lambda expression keyword
LBRACE = 'LBRACE'  # Left brace '{'
RBRACE = 'RBRACE'  # Right brace '}'
QUESTION = 'QUESTION'  # Question mark '?'
COLON = 'COLON'  # Colon ':'
ASSIGN = 'ASSIGN'  # Assignment '='

# Keywords in the language
KEYWORDS = {
    'Defun': KEYWORD,   # Function definition keyword
    'Lambd': KEYWORD,   # Lambda expression keyword
    'True': BOOLEAN,    # Boolean literal 'True'
    'False': BOOLEAN    # Boolean literal 'False'
}

# Token class to represent each token with a type and value
class Token:
    """
    Token class represents a single token with a type and a value.
    """
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return self.type == other.type and self.value == other.value

    def __hash__(self):
        return hash((self.type, self.value))

# Lexer class to tokenize the input source code
class Lexer:
    """
    Lexer class takes the input source code and tokenizes it according
    to the defined token types and language syntax rules.
    """
    def __init__(self, text):
        self.text = text  # The input text to tokenize
        self.pos = 0  # Current position in the input text
        self.current_char = self.text[self.pos] if self.text else None  # Current character being processed

    def advance(self):
        """Advance the 'pos' and update 'current_char'."""
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        """Skip over any whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        """Skip comments starting with #."""
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def identifier(self):
        """
        Return an identifier or keyword token.

        Identifiers are sequences of alphanumeric characters and underscores.
        Keywords are predefined identifiers such as 'Defun' and 'Lambd'.
        """
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in KEYWORDS:
            return Token(KEYWORDS[result], result)
        else:
            return Token(IDENTIFIER, result)

    def integer(self):
        """
        Return a multi-digit integer token consumed from the input.
        """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def string(self):
        """
        Return a string token consumed from the input.

        Strings are enclosed in single quotes and may contain any character
        except a newline or the closing quote.
        """
        result = ''
        self.advance()  # Skip the opening quote
        while self.current_char is not None and self.current_char != "'":
            result += self.current_char
            self.advance()
        if self.current_char == "'":
            self.advance()  # Skip the closing quote
            return result  # Return the string directly, not a Token
        else:
            raise Exception("Unterminated string literal")

    def tokenize(self):
        """
        Tokenize the entire input and return a list of tokens.

        This method loops through the input text, recognizing tokens
        based on the current character and the language's syntax rules.
        """
        tokens = []

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.advance()
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                tokens.append(Token(INTEGER, self.integer()))
                continue

            if self.current_char.isalpha():
                token = self.identifier()
                if token.value == 'or':
                    tokens.append(Token(OR, 'or'))
                elif token.value == 'and':
                    tokens.append(Token(AND, 'and'))
                elif token.value == 'not':
                    tokens.append(Token(NOT, 'not'))
                else:
                    tokens.append(token)
                continue

            if self.current_char == "'":
                tokens.append(Token(STRING, self.string()))  # Pass the string result to Token
                continue

            if self.current_char == '+':
                tokens.append(Token(PLUS, '+'))
                self.advance()
                continue

            if self.current_char == '-':
                tokens.append(Token(MINUS, '-'))
                self.advance()
                continue

            if self.current_char == '*':
                tokens.append(Token(MULTIPLY, '*'))
                self.advance()
                continue

            if self.current_char == '/':
                tokens.append(Token(DIVIDE, '/'))
                self.advance()
                continue

            if self.current_char == '%':
                tokens.append(Token(MODULO, '%'))
                self.advance()
                continue

            if self.current_char == '(':
                tokens.append(Token(LPAREN, '('))
                self.advance()
                continue

            if self.current_char == ')':
                tokens.append(Token(RPAREN, ')'))
                self.advance()
                continue

            if self.current_char == ',':
                tokens.append(Token(COMMA, ','))
                self.advance()
                continue

            if self.current_char == '.':
                tokens.append(Token(DOT, '.'))
                self.advance()
                continue

            if self.current_char == '{':
                tokens.append(Token(LBRACE, '{'))
                self.advance()
                continue

            if self.current_char == '}':
                tokens.append(Token(RBRACE, '}'))
                self.advance()
                continue

            if self.current_char == '?':
                tokens.append(Token(QUESTION, '?'))
                self.advance()
                continue

            if self.current_char == ':':
                tokens.append(Token(COLON, ':'))
                self.advance()
                continue

            if self.current_char == '&':
                self.advance()
                if self.current_char == '&':
                    tokens.append(Token(AND, '&&'))
                    self.advance()
                else:
                    raise Exception(f"Unexpected character '&'")
                continue

            if self.current_char == '|':
                self.advance()
                if self.current_char == '|':
                    tokens.append(Token(OR, '||'))
                    self.advance()
                else:
                    raise Exception(f"Unexpected character '|'")
                continue

            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(NEQ, '!='))
                    self.advance()
                else:
                    tokens.append(Token(NOT, '!'))
                continue

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(EQ, '=='))  # Equality operator
                    self.advance()
                else:
                    tokens.append(Token(ASSIGN, '='))  # Assignment operator
                continue

            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(GTE, '>='))
                    self.advance()
                else:
                    tokens.append(Token(GT, '>'))
                continue

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(LTE, '<='))
                    self.advance()
                else:
                    tokens.append(Token(LT, '<'))
                continue

            raise Exception(f"Unexpected character '{self.current_char}'")

        tokens.append(Token(EOF, None))  # Add end-of-file token
        return tokens
