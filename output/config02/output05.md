| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld   f6, 32(x1) |    1     |        2        |      9       |       10       |
| fadd  f2, f6, f0 |    2     |       11        |      14      |       15       |
| fmul  f4, f2, f8 |    3     |       16        |      24      |       25       |
| fsub  f10, f4, f2 |    4     |       26        |      29      |       30       |
| fsd   f10, 64(x1) |    5     |       31        |      38      |       39       |
