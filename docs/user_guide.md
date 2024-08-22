# User Guide for the Functional Programming Language Interpreter

This document provides instructions for setting up and using the functional programming language interpreter.

## 1. Installation

### Requirements
- Python 3.7 or higher

### Setup
- Clone the repository:

git clone <https://github.com/ginzex11/py_interpreter_proj.git>


## 2. Running the Interpreter

### Interactive Mode (REPL)
- Start the REPL:

- Use the REPL to enter commands interactively. 
Example:
Interactive Functional Language Shell
Type ':load <filename>' to load a file.
Type ':exit' to quit.
Type ':help' for a list of commands.
```markdown
>>> 3+5
Tokens: [Token(INTEGER, 3), Token(PLUS, +), Token(INTEGER, 5), Token(EOF, None)]
AST: Program(body=[BinaryOp(left=Literal(value=3), operator='+', right=Literal(value=5))])
Result: 8
```

- run a script.
example : 
```bash
- python -m repl samples/boolean_ops.lambda
- (base) PS E:\PythonProjects\py_interpreter> python -m repl samples/boolean_ops.lambda       
Tokens: [Token(INTEGER, 3), Token(LT, <), Token(INTEGER, 4), Token(AND, &&), Token(INTEGER, 4), Token(LT, <), Token(INTEGER, 3), Token(EOF, None)]
AST: Program(body=[BinaryOp(left=BinaryOp(left=Literal(value=3), operator='<', right=Literal(value=4)), operator='&&', right=BinaryOp(left=Literal(value=4), operator='<', right=Literal(value=3)))])
Result: False                                                                                                                                                                                        
(base) PS E:\PythonProjects\py_interpreter> 
```

another example with using the repl load file options :
```markdown
>>> :load samples/boolean_ops.lambda
Tokens: [Token(INTEGER, 3), Token(LT, <), Token(INTEGER, 4), Token(AND, &&), Token(INTEGER, 4), Token(LT, <), Token(INTEGER, 3), Token(EOF, None)]
AST: Program(body=[BinaryOp(left=BinaryOp(left=Literal(value=3), operator='<', right=Literal(value=4)), operator='&&', right=BinaryOp(left=Literal(value=4), operator='<', right=Literal(value=3)))])
Result: False

```
## 5. Troubleshooting

### Common Errors
- **NameError:** Occurs if you try to use a variable that hasn't been defined.
- **TypeError:** Occurs if you attempt to perform an operation on incompatible types.
- **ZeroDivisionError:** Raised when attempting to divide by zero.

### Debugging
- The REPL provides detailed error messages to help you diagnose issues. If you encounter an error, review the message for hints on what went wrong.



