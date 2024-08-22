# Test Cases and Edge Scenarios

This document describes the test cases used to validate the functional programming language's interpreter, covering basic functionality, edge cases, and error handling.

## 1. Arithmetic Operations

### Test: Simple Addition
- **Input:** `2 + 3`
- **Expected Output:** `5`

### Test: Simple Subtraction
- **Input:** `10 - 3`
- **Expected Output:** `7`

### Test: Simple Multiplication
- **Input:** `6 * 7`
- **Expected Output:** `42`

### Test: Simple Division
- **Input:** `8 / 2`
- **Expected Output:** `4`

### Test: Simple Modulo
- **Input:** `10 % 3`
- **Expected Output:** `1`

### Test: Nested Arithmetic Operations
- **Input:** `(2 + 3) * (5 - 2)`
- **Expected Output:** `15`

### Edge Case: Division by Zero
- **Input:** `10 / 0`
- **Expected Output:** `ZeroDivisionError`

## 2. Logical Operations

### Test: Logical AND
- **Input:** `True && False`
- **Expected Output:** `False`

### Test: Logical OR
- **Input:** `True || False`
- **Expected Output:** `True`

### Test: Logical NOT
- **Input:** `!True`
- **Expected Output:** `False`

### Test: Mixed Logical Operations
- **Input:** `(4 > 2) && (3 < 5)`
- **Expected Output:** `True`

### Edge Case: Short-Circuit Evaluation (AND)
- **Input:** `False && (10 / 0)`
- **Expected Output:** `False` (should not raise `ZeroDivisionError` due to short-circuit)

### Edge Case: Short-Circuit Evaluation (OR)
- **Input:** `True || (10 / 0)`
- **Expected Output:** `True` (should not raise `ZeroDivisionError` due to short-circuit)

## 3. Comparison Operations

### Test: Simple Equality
- **Input:** `5 == 5`
- **Expected Output:** `True`

### Test: Simple Inequality
- **Input:** `5 != 4`
- **Expected Output:** `True`

### Test: Greater Than
- **Input:** `7 > 3`
- **Expected Output:** `True`

### Test: Less Than
- **Input:** `3 < 7`
- **Expected Output:** `True`

### Test: Greater Than or Equal
- **Input:** `5 >= 5`
- **Expected Output:** `True`

### Test: Less Than or Equal
- **Input:** `4 <= 5`
- **Expected Output:** `True`

### Edge Case: Type Mismatch in Comparison
- **Input:** `'hello' > 5`
- **Expected Output:** `Error`

## 4. Function Definitions and Calls

### Test: Simple Function Call
- **Input:**
  ```python
  Defun {'name': 'triple', 'arguments': (x,)} x * 3 triple(5)
**Expected Output:** `15`
