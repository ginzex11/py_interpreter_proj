# BNF Grammar for the Functional Programming Language with REPL Support

This document outlines the Backus–Naur Form (BNF) grammar used to define the syntax of the functional programming language implemented in this project. The grammar has been updated to include REPL (Read-Eval-Print Loop) commands and script execution.

## Grammar

```bnf
<program> ::= <statement> | <statement> <program>

<statement> ::= <function-def> | <expression>

<function-def> ::= "Defun" "{" "name" ":" <identifier> "," "arguments" ":" <parameters> "}" <expression>
<parameters> ::= "(" <identifier-list> ")"
<identifier-list> ::= <identifier> | <identifier> "," <identifier-list>

<expression> ::= <literal> 
               | <identifier> 
               | <binary-op> 
               | <unary-op> 
               | <function-call> 
               | <lambda>
               | <comparison> 
               | <assignment> 
               | "(" <expression> ")"

<literal> ::= <integer> 
            | <boolean> 
            | <string>

<identifier> ::= <letter> <letter-digit*>

<function-call> ::= <identifier> "(" <arguments> ")"
<arguments> ::= <expression-list>
<expression-list> ::= <expression> | <expression> "," <expression-list>

<binary-op> ::= <expression> <operator> <expression>
<operator> ::= "+" | "-" | "*" | "/" | "%" | "&&" | "||" | "==" | "!=" | ">" | "<" | ">=" | "<="

<unary-op> ::= "!" <expression>

<lambda> ::= "Lambd" <identifier-list> "." <expression>

<comparison> ::= <expression> <comparison-operator> <expression>
<comparison-operator> ::= "==" | "!=" | ">" | "<" | ">=" | "<="

<assignment> ::= <identifier> "=" <expression>

<integer> ::= <digit> <digit*>
<boolean> ::= "True" | "False"
<string> ::= "'" <character*> "'"

<term> ::= <factor> | <factor> <term-operator> <term>
<term-operator> ::= "*" | "/" | "%"
<factor> ::= <integer> | <boolean> | <identifier> | <function-call> | <lambda> | <unary-op> | "(" <expression> ")"

<logical-op> ::= <expression> <logical-operator> <expression>
<logical-operator> ::= "&&" | "||"

<repl-command> ::= <load-command> | <exit-command> | <help-command>
<load-command> ::= ":load" <string>
<exit-command> ::= ":exit" | "exit" | "quit"
<help-command> ::= ":help"

<repl-input> ::= <repl-command> | <expression>
