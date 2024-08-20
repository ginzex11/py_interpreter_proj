# Language Syntax and Features

This document describes the syntax and key features of the functional programming language.

## 1. Data Types

### Integer
- **Syntax:** Integers are whole numbers, positive or negative (e.g., `42`, `-5`).
- **Example:** `5 + 10`

### Boolean
- **Syntax:** Booleans represent truth values and can be `True` or `False`.
- **Example:** `True && False`

### String
- **Syntax:** Strings are sequences of characters enclosed in single quotes.
- **Example:** `'Hello, world!'`

## 2. Operations

### Arithmetic Operations
- **Supported Operations:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Modulo (`%`).
- **Example:** `3 * (2 + 4)`

### Boolean Operations
- **Supported Operations:** AND (`&&`), OR (`||`), NOT (`!`).
- **Example:** `True && (x > 5)`

### Comparison Operations
- **Supported Comparisons:** Equal (`==`), Not equal (`!=`), Greater than (`>`), Less than (`<`), Greater than or equal (`>=`), Less than or equal (`<=`).
- **Example:** `x >= 10`

## 3. Functions

### Function Definitions
- **Syntax:** Functions are defined using the `Defun` keyword followed by a dictionary-like structure for the name and parameters.
- **Example:** `Defun {'name': 'double', 'arguments': (x,)} x * 2`

### Function Calls
- **Syntax:** Functions are called by their name followed by arguments in parentheses.
- **Example:** `double(4)`

### Lambda Expressions
- **Syntax:** Lambda expressions are defined using the `Lambd` keyword, followed by parameters and a body.
- **Example:** `(Lambd x. x + 1)`

## 4. Recursion

- **Feature:** The language supports recursive function calls as an alternative to looping constructs.
- **Example:** 

- Defun {'name': 'factorial', 'arguments': (n,)}
(n == 0) || (n * factorial(n - 1))
factorial(5)

## 5. Immutability

- **Feature:** All variables are immutable, meaning once assigned, their values cannot be changed.
- **Rationale:** This aligns with functional programming principles and ensures that functions remain pure and predictable.
