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

|Starting with|Answer type|
|:--:|:--:|
|`-`|false|
|`*`|true|

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

## How to answer
Type in the prompt a CSV(Coma Separated Values) answer:
```bash
$ mcq.py binop.txt
A ^ b = 1
0) A = 1 && B = 1
1) A = 1 && B = 0
2) A = 0 && B = 1
3) A = 0 && B = 0
> 1,2

score: 1/1
```

## Return value
|Number of errors|Return value of the script|
|:--:|:--:|
|== 0|0|
|>= 1|1|