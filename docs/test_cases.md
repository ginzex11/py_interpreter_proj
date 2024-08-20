# Test Cases and Edge Scenarios

This document describes the test cases used to validate the functional programming language's interpreter, covering basic functionality, edge cases, and error handling.

## 1. Arithmetic Operations

### Test: Simple Addition
- **Input:** `2 + 3`
- **Expected Output:** `5`

### Test: Nested Arithmetic
- **Input:** `(2 + 3) * (4 - 1)`
- **Expected Output:** `15`

### Edge Case: Division by Zero
- **Input:** `10 / 0`
- **Expected Output:** `ZeroDivisionError`

## 2. Logical Operations

### Test: Logical AND
- **Input:** `True && False`
- **Expected Output:** `False`

### Test: Mixed Operations
- **Input:** `(4 > 2) && (3 < 5)`
- **Expected Output:** `True`

## 3. Function Definitions and Calls

### Test: Simple Function Call
- **Input:** 

Defun {'name': 'double', 'arguments': (x,)} x * 2
double(5)
- **Expected Output:** `10`

### Test: Recursive Function (Factorial)
- **Input:** 

Defun {'name': 'factorial', 'arguments': (n,)}
(n == 0) || (n * factorial(n - 1))
factorial(5)
- **Expected Output:** `120`

## 4. Error Handling

### Edge Case: Undefined Variable
- **Input:** `y + 2`
- **Expected Output:** `NameError`

### Edge Case: Invalid Comparison
- **Input:** `'hello' > 5`
- **Expected Output:** `TypeError`
