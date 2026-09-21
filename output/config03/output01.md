| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld f1, 0(x1)   |    1     |        2        |      3       |       4        |
| fld f5, 0(x1)   |    2     |        3        |      4       |       5        |
| fdiv f2, f4, f5 |    3     |        6        |      16      |       17       |
| fmul f4, f8, f9 |    4     |        5        |      9       |       10       |
| fadd f1, f2, f3 |    5     |       18        |      20      |       21       |
| fsd f4, 0(x2)   |    6     |       11        |      12      |       13       |
