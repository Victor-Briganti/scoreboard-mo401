| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld   f6, 32(x1) |    1     |        2        |      3       |       4        |
| fadd  f2, f6, f0 |    2     |        5        |      7       |       8        |
| fmul  f4, f2, f8 |    3     |        9        |      13      |       14       |
| fsub  f10, f4, f2 |    4     |       15        |      17      |       18       |
| fsd   f10, 64(x1) |    5     |       19        |      20      |       21       |
