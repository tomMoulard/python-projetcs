# MCQ

mcq parser for simple mcq revisions

## How to use
```bash
mcq.py <mcq file>
```

## MCQ file format
It is a list of questions to ask like:
```mcq
log2(128) =
-13
-8
*7
-12
```
Where the first line is a question, and all other lines are possible answers.
There is two options for answers:
    - Starting with `-`: this is a false answer
    - Starting with `*`: this is a true answer

There can be multiple {true|false} answer

To have multiple questions in a file, just add a blank line between questions,
like:
```mcq
A & b = 1
*A = 1 && B = 1
-A = 1 && B = 0
-A = 0 && B = 1
-A = 0 && B = 0

A ^ b = 1
-A = 1 && B = 1
*A = 1 && B = 0
*A = 0 && B = 1
-A = 0 && B = 0
```