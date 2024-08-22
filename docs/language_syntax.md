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
- **Supported Operations:** 
  - **Addition (`+`)**: Adds two numbers.
  - **Subtraction (`-`)**: Subtracts one number from another.
  - **Multiplication (`*`)**: Multiplies two numbers.
  - **Division (`/`)**: Divides one number by another (integer division).
  - **Modulo (`%`)**: Returns the remainder of division.
- **Example:** `3 * (2 + 4)`

### Boolean Operations
- **Supported Operations:**
  - **AND (`&&`)**: Returns `True` if both operands are `True`.
  - **OR (`||`)**: Returns `True` if at least one operand is `True`.
  - **NOT (`!`)**: Returns `True` if the operand is `False`, and `False` if the operand is `True`.
- **Example:** `True && (5 > 5)`

### Comparison Operations
- **Supported Comparisons:**
  - **Equal (`==`)**: Checks if two values are equal.
  - **Not equal (`!=`)**: Checks if two values are not equal.
  - **Greater than (`>`)**: Checks if the left value is greater than the right value.
  - **Less than (`<`)**: Checks if the left value is less than the right value.
  - **Greater than or equal (`>=`)**: Checks if the left value is greater than or equal to the right value.
  - **Less than or equal (`<=`)**: Checks if the left value is less than or equal to the right value.
- **Example:** `12 >= 10`

## 3. Functions

### Function Definitions
- **Syntax:** Functions are defined using the `Defun` keyword followed by a dictionary-like structure for the name and parameters.
- **Example:** 
  ```python
  Defun {'name': 'triple', 'arguments': (x,)} x * 3 triple(5)
