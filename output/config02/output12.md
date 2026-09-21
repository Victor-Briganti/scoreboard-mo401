| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 0(x1)  |    1     |        2        |      9       |       10       |
| fdiv f2, f1, f4 |    2     |       11        |      31      |       32       |
| fadd f4, f5, f6 |    3     |        4        |      7       |       12       |
| fsub f7, f8, f9 |    4     |        5        |      8       |       9        |
| fsd  f4, 0(x2)  |    5     |       13        |      20      |       21       |
