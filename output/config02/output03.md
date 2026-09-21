| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 100(x7) |    1     |        2        |      9       |       10       |
| fdiv f3, f1, f7 |    2     |       11        |      31      |       32       |
| fdiv f3, f1, f7 |    33    |       34        |      54      |       55       |
