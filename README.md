# Functional Programming Language Interpreter

## Overview

This project is a simple interpreter for a functional programming language that emphasizes function definitions, lambda expressions, and immutable values. The language is designed to explore key concepts of functional programming, such as recursion, higher-order functions, and the avoidance of mutable state.

The interpreter can be used interactively via a Read-Eval-Print Loop (REPL) or by executing script files. It supports basic arithmetic and logical operations, function definitions, anonymous functions (lambdas), and recursive function calls.

## Features

- **Data Types:** Supports integers, booleans, and strings.
- **Operations:** Includes arithmetic, boolean, and comparison operations.
- **Functions:** Allows named function definitions, anonymous functions (lambdas), and function application.
- **Recursion:** Supports recursive function calls, a key feature in functional programming.
- **Immutability:** All values are immutable, promoting a functional programming style without side effects.
- **Interactive REPL:** Provides an interactive shell for evaluating expressions and running scripts.
- **Error Handling:** Robust error handling with meaningful error messages for syntax, type, and runtime errors.

## Installation

### Requirements

- Python 3.7 or higher

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ginzex11/py_interpreter_proj.git
   cd py_interpreter_proj


Usage
Running the Interpreter
Interactive Mode (REPL)
Start the REPL to interactively evaluate expressions:
python -m repl

Once in the REPL, you can type expressions to evaluate them:
```bash
>>> 3 + 5
Tokens: [Token(INTEGER, 3), Token(PLUS, +), Token(INTEGER, 5), Token(EOF, None)]
AST: Program(body=[BinaryOp(left=Literal(value=3), operator='+', right=Literal(value=5))])
Result: 8

```

Running a Script
To execute a script file, use the following command:
python -m repl <filename>

Example:
```bash
python -m repl samples/boolean_ops.lambda

Output:
Tokens: [Token(INTEGER, 3), Token(LT, <), Token(INTEGER, 4), Token(AND, &&), Token(INTEGER, 4), Token(LT, <), Token(INTEGER, 3), Token(EOF, None)]
AST: Program(body=[BinaryOp(left=BinaryOp(left=Literal(value=3), operator='<', right=Literal(value=4)), operator='&&', right=BinaryOp(left=Literal(value=4), operator='<', right=Literal(value=3)))])
Result: False
```

Troubleshooting
Common Errors:
```bash
NameError: Occurs if you try to use a variable that hasn't been defined.
TypeError: Occurs if you attempt to perform an operation on incompatible types.
ZeroDivisionError: Raised when attempting to divide by zero.
Debugging
The REPL provides detailed error messages to help diagnose issues. Review the message for hints on what went wrong.
```
Contributing
Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to open an issue or submit a pull request.