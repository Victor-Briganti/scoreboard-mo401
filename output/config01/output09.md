| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 0(x1)  |    1     |        2        |      3       |       4        |
| fadd f2, f1, f3 |    2     |        5        |      7       |       8        |
| fsub f4, f2, f5 |    9     |       10        |      12      |       13       |
| fmul f6, f4, f7 |    10    |       14        |      18      |       19       |
| fsd  f6, 0(x2)  |    11    |       20        |      21      |       22       |
