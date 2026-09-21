| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 0(x1)  |    1     |        2        |      3       |       4        |
| fadd f2, f1, f3 |    2     |        5        |      7       |       8        |
| fsub f4, f2, f5 |    3     |        9        |      11      |       12       |
| fmul f6, f4, f7 |    4     |       13        |      17      |       18       |
| fsd  f6, 0(x2)  |    5     |       19        |      20      |       21       |
