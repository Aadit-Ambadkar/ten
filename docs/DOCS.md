# TEN DOCS

TEN Programming Language is created by Aadit Ambadkar
TEN Programming Language is licensed under the MIT License
TEN Programming Language is a free and open-source programming language
Please see CONTRIBUTING.md for information on how to contribute to TEN
I am not responsible for any mental, physical, metaphysical, interpersonal, intrapersonal, or other damages caused by using this language

## Syntax           
                                                    
### Loops

`{element init,condition,iteration, body}` for loop

_See /src/examples/loops.ten for specifics on loops._

### Variables

`|` type prefix\
`i` int (converts top of stack value to int, if not already int. If not possible, defaults to 0)\
`s` string (converts top of stack value to string, if not already string)\
`c` char (converts top of stack value to character. If not possible, defaults to '\x00' character)\
`$` end type prefix, begin variable naming.

_See /src/examples/variables.ten for specifics on variables_

`I` converts top of stack to int, if possible. If not, does nothing\
`S` converts top of stack to string, if possible. If not, does nothing\
`C` converts top of stack to character, if possible. If not, does nothing

Generally, the above are used for changing types without variable declaration. However, there is no functional difference between `I` or `i`, `S` or `s`, or `C` or `c`.

### Stack Operations
                                                                               
`+-*/` standard mathematical operations on the first two elements of the stack (deletes the elements)\
`^` get variable value and add to top of stack\
`~` 1 if top of stack is positive, 0 if 0, -1 if negative\
`:` variable assignment\
`[` gets an integer value at the top of the stack - index. gets an array at the second from the top of the stack - array. Removes both the index and the array from the stack. Adds array\[index\] to the top of the stack.\
`!` remove current value from stack\
`?` clears all values from stack\
`&` duplicates top of stack

_See /src/examples/stackoperations.ten for specifics on stack operations_

### True and False (and Conditionals)

`` ` `` true value\
`]` null value\
`(` and\
`)` or\
`.` not\
`=` equals\
`<body>` if statement (executes if top of stack is True)

_See /src/examples/if.ten for specifics on if statements_
### IO

`#` standard input\
`;` standard output

_See /src/examples/input.ten for specifics on input and output_

### Misc Operations
                                                                                                                                                               
`_` ends program\
`"` begin string (used to begin a string, useful if string contains whitespace, which is normally stripped)\
`'` end string (any non special characters are automatically parsed as string, unless they are number)\
`@` comment - anything after this will be ignored until the end comment (%) symbol\
`%` end comment - ends any and all comments

_See /src/examples/comments.ten for specifics on comments_

_____________

## Examples

Examples can be found in /src/examples
_________________________________________________________________________________________________________________________________________________________________________________

## Notes

* Some of the examples may be outdated, in which case refer to the syntax for proper use.
* Some (read most) errors are not displayed - Good Luck
* Variable names must only contain alphabetic characters, ie abcdefghijklmnopqrstuvwxyz and no other special characters
_________________________________________________________________________________________________________________________________________________________________________________

## Coming Soon
                                                                                          
`<name,body>` function
