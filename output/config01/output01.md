| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld f1, 0(x1)   |    1     |        2        |      3       |       4        |
| fld f5, 0(x1)   |    5     |        6        |      7       |       8        |
| fdiv f2, f4, f5 |    6     |        9        |      19      |       20       |
| fmul f4, f8, f9 |    7     |        8        |      12      |       13       |
| fadd f1, f2, f3 |    8     |       21        |      23      |       24       |
| fsd f4, 0(x2)   |    9     |       14        |      15      |       16       |
