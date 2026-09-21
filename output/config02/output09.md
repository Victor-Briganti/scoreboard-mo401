| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 0(x1)  |    1     |        2        |      9       |       10       |
| fadd f2, f1, f3 |    2     |       11        |      14      |       15       |
| fsub f4, f2, f5 |    3     |       16        |      19      |       20       |
| fmul f6, f4, f7 |    4     |       21        |      29      |       30       |
| fsd  f6, 0(x2)  |    5     |       31        |      38      |       39       |
