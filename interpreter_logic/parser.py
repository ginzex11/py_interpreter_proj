"""
Parser for a simple functional programming language.

This module defines the Parser class, responsible for parsing a sequence of tokens into
an Abstract Syntax Tree (AST). The parser processes function definitions, expressions,
logical operations, comparisons, and other language constructs based on the grammar of the
language.

Classes:
- ASTNode: Base class for all AST nodes.
- Various AST node classes (e.g., Program, FunctionDef, BinaryOp) representing different constructs.
- Parser: Implements the logic for parsing tokens into an AST.

Usage:
Create an instance of the Parser class with a list of tokens, and call the parse_program() method
to obtain the AST representation of the program.
"""

from interpreter_logic.lexer import Token, KEYWORD, IDENTIFIER, INTEGER, BOOLEAN, EOF, LPAREN, RPAREN, LBRACE, RBRACE, COMMA, \
    PLUS, MINUS, MULTIPLY, DIVIDE, MODULO, EQ, NEQ, AND, OR, NOT, GT, LT, GTE, LTE, QUESTION, COLON, STRING, DOT, ASSIGN


class ASTNode:
    """Base class for all nodes in the Abstract Syntax Tree (AST)."""
    pass


class Program(ASTNode):
    """Represents the entire program as a list of statements or expressions."""
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return f"Program(body={self.body})"


class FunctionDef(ASTNode):
    """Represents a function definition with a name, parameters, and a body."""
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f"FunctionDef(name={self.name}, params={self.params}, body={self.body})"


class Call(ASTNode):
    """Represents a function call with a function name and arguments."""
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __repr__(self):
        return f"Call(func={self.func}, args={self.args})"


class BinaryOp(ASTNode):
    """Represents a binary operation (e.g., addition, subtraction) with a left and right operand."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOp(left={self.left}, operator='{self.operator}', right={self.right})"


class UnaryOp(ASTNode):
    """Represents a unary operation (e.g., negation) with a single operand."""
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOp(operator={self.operator.value}, operand={self.operand})"


class IfExpr(ASTNode):
    """Represents an if-else expression with a condition and branches."""
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return f"IfExpr(condition={self.condition}, then_branch={self.then_branch}, else_branch={self.else_branch})"


class Literal(ASTNode):
    """Represents a literal value (e.g., integer, boolean)."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Literal(value={self.value})"


class Identifier(ASTNode):
    """Represents an identifier (e.g., variable or function name)."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier(name={self.name})"


class Lambda(ASTNode):
    """Represents a lambda expression with parameters and a body."""
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def __repr__(self):
        return f"Lambda(params={self.params}, body={self.body})"


class BooleanOp(ASTNode):
    """Represents a boolean operation (e.g., AND, OR) with a left and right operand."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BooleanOp(left={self.left}, operator={self.operator.value}, right={self.right})"


class LogicalOp(ASTNode):
    """Represents a logical operation (e.g., AND, OR) with a left and right operand."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"LogicalOp(left={self.left}, operator={self.operator}, right={self.right})"


class Comparison(ASTNode):
    """Represents a comparison operation (e.g., ==, !=, <, >) with a left and right operand."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"Comparison(left={self.left}, operator={self.operator.value}, right={self.right})"


class Assignment(ASTNode):
    """Represents an assignment of a value to a variable."""
    def __init__(self, target, value):
        self.target = target  # The variable being assigned to (e.g., 'x')
        self.value = value  # The value being assigned (e.g., 10)

    def __repr__(self):
        return f"Assignment(target={self.target}, value={self.value})"


class Parser:
    """Parses a sequence of tokens into an Abstract Syntax Tree (AST)."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        """Advance to the next token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(EOF, None)

    def peek(self):
        """Peek at the next token without advancing the position."""
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        else:
            return Token(EOF, None)

    def expect(self, token_type, value=None):
        """Expect the current token to be of a specific type and optionally value."""
        if self.current_token.type == token_type and (value is None or self.current_token.value == value):
            self.advance()
        else:
            raise Exception(
                f"Expected token {token_type} (value: {value}), got {self.current_token.type} (value: {self.current_token.value}) at position {self.pos}")

    def parse_program(self):
        """Parse the entire program and return a Program node."""
        body = []
        while self.current_token.type != EOF:
            if self.current_token.type == KEYWORD and self.current_token.value == 'Defun':
                body.append(self.parse_function_def())
            else:
                body.append(self.parse_expression())
        return Program(body)

    def parse_function_def(self):
        """Parse a function definition and return a FunctionDef node."""
        self.expect(KEYWORD, 'Defun')
        self.expect(LBRACE)

        name = self.parse_key_value_pair("name")
        if not name or not name.isidentifier():
            raise Exception("Invalid or missing function name in function definition")

        self.expect(COMMA)
        params = self.parse_key_value_pair("arguments")
        self.expect(RBRACE)

        if params is None:
            raise TypeError(f"Function '{name}' requires arguments")

        if self.current_token.type == LBRACE:
            self.advance()  # Skip the opening brace
            body = None  # Empty body
            self.expect(RBRACE)  # Expect closing brace
        else:
            body = self.parse_expression()

        return FunctionDef(Identifier(name), params, body)

    def parse_key_value_pair(self, expected_key):
        """Parse a key-value pair inside the function definition."""
        key_token = self.current_token
        if key_token.type != STRING or key_token.value != expected_key:
            raise Exception(f"Expected key '{expected_key}', got {key_token.value}")
        self.advance()

        self.expect(COLON)  # Expect ':'

        if expected_key == "name":
            name_token = self.current_token
            if name_token.type != STRING:
                raise Exception(f"Expected function name as a string, got {name_token.type}")
            self.advance()
            return name_token.value

        elif expected_key == "arguments":
            return self.parse_parameters()

    def parse_parameters(self):
        """Parse function parameters and return them as a list."""
        self.expect(LPAREN)
        params = []

        if self.current_token.type == RPAREN:
            self.advance()  # Skip ')'
            return params

        while self.current_token.type == IDENTIFIER:
            params.append(self.parse_identifier())

            if self.current_token.type == COMMA:
                self.advance()  # Skip ','
            elif self.current_token.type == RPAREN:
                self.advance()  # Skip ')'
                break
            else:
                raise Exception(f"Unexpected token while parsing parameters: {self.current_token.type}")

        self.expect(RPAREN)
        return params

    def parse_expression(self):
        """Parse an expression, including assignments, logical operations, and arithmetic operations."""
        if self.current_token.type == IDENTIFIER and self.peek().type == ASSIGN:
            return self.parse_assignment()

        return self.parse_logical_expression()

    def parse_logical_expression(self):
        """Parse a logical expression, handling operations like '&&' and '||'."""
        left = self.parse_comparison_expression()

        while self.current_token.type in (AND, OR):
            operator = self.current_token.value
            self.advance()
            right = self.parse_comparison_expression()
            left = BinaryOp(left=left, operator=operator, right=right)

        return left

    def parse_comparison_expression(self):
        """Parse a comparison expression like 'x > 0'."""
        left = self.parse_arithmetic_expression()

        while self.current_token.type in (GT, LT, GTE, LTE, EQ, NEQ):
            operator = self.current_token.value
            self.advance()
            right = self.parse_arithmetic_expression()
            left = BinaryOp(left=left, operator=operator, right=right)

        return left

    def parse_arithmetic_expression(self):
        """Parse an arithmetic expression, handling addition and subtraction."""
        left = self.parse_term()

        while self.current_token.type in (PLUS, MINUS):
            operator = self.current_token.value
            self.advance()
            right = self.parse_term()
            left = BinaryOp(left=left, operator=operator, right=right)

        return left

    def parse_logic_continuation(self, left):
        """Continue parsing logical operations starting with an existing left expression."""
        while self.current_token.type in (AND, OR):
            operator_token = self.current_token.value
            self.advance()
            right = self.parse_comparison()

            left = LogicalOp(left=left, operator=operator_token, right=right)

        return left

    def parse_lambda(self):
        """Parse a lambda expression and return a Lambda node."""
        self.expect(KEYWORD, 'Lambd')
        params = [self.parse_identifier()]

        while self.current_token.type == COMMA:
            self.advance()
            params.append(self.parse_identifier())

        self.expect(DOT)
        body = self.parse_expression()
        return Lambda(params=params, body=body)

    def parse_term(self):
        """Parse a term, handling higher precedence operations like multiplication and division."""
        left = self.parse_factor()

        while self.current_token.type in (MULTIPLY, DIVIDE, MODULO):
            operator = self.current_token.value
            self.advance()
            right = self.parse_factor()
            left = BinaryOp(left=left, operator=operator, right=right)

        return left

    def parse_factor(self):
        """Parse a factor (integer, identifier, function call, lambda, unary operation, or expression in parentheses)."""
        token = self.current_token

        if token.type == NOT:  # Handle the NOT operation
            self.advance()
            operand = self.parse_factor()
            return UnaryOp(operator=token, operand=operand)

        elif token.type == STRING:  # Ensure string literals are parsed correctly
            self.advance()
            return Literal(token.value)

        elif token.type == INTEGER:
            self.advance()
            return Literal(token.value)

        elif token.type == BOOLEAN:
            self.advance()
            return Literal(token.value == 'True')

        elif token.type == IDENTIFIER:
            func_name = token.value
            self.advance()
            if self.current_token.type == LPAREN:
                self.advance()  # Skip LPAREN
                args = []
                if self.current_token.type != RPAREN:
                    while True:
                        args.append(self.parse_expression())
                        if self.current_token.type == RPAREN:
                            break
                        self.expect(COMMA)
                self.expect(RPAREN)
                return Call(func=Identifier(func_name), args=args)
            else:
                return Identifier(func_name)

        elif token.type == LPAREN:
            self.advance()
            expr = self.parse_expression()

            if self.current_token.type in (GT, LT, GTE, LTE, EQ, NEQ):
                operator = self.current_token
                self.advance()
                right_expr = self.parse_expression()
                expr = Comparison(left=expr, operator=operator, right=right_expr)

            self.expect(RPAREN)
            return expr

        elif token.type == KEYWORD and token.value == 'Lambd':
            return self.parse_lambda()

        else:
            raise Exception(f"Unexpected token {token.type}")

    def parse_identifier(self):
        """Parse an identifier (variable or function name) and return an Identifier node."""
        token = self.current_token
        if token.type != IDENTIFIER:
            raise Exception(f"Expected identifier, got {token.type}")
        self.advance()
        return Identifier(token.value)

    def parse_comparison(self):
        """Parse a comparison operation, such as ==, !=, <, <=, >, >=."""
        left = self.parse_term()

        if self.current_token.type in (EQ, NEQ, LT, LTE, GT, GTE):
            operator = self.current_token
            self.advance()
            right = self.parse_term()
            return Comparison(left=left, operator=operator, right=right)

        return left

    def parse_logic(self):
        """Parse a logical expression."""
        left = self.parse_comparison()

        while self.current_token.type in (AND, OR):
            operator_token = self.current_token
            self.advance()
            right = self.parse_comparison()

            left = LogicalOp(left=left, operator=operator_token.value, right=right)

        return left

    def parse_assignment(self):
        """Parse an assignment expression and return an Assignment node."""
        left = self.parse_identifier()

        if self.current_token.type == ASSIGN:
            self.advance()
            right = self.parse_expression()
            return Assignment(target=left, value=right)

        raise SyntaxError(f"Invalid assignment: expected ASSIGN token after {left.name}")
