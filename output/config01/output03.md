| Instruction     |  Issue   |  Read Operands  |  Exec Comp   |  Write Result  |
|:----------------|:--------:|:---------------:|:------------:|:--------------:|
| fld  f1, 100(x7) |    1     |        2        |      3       |       4        |
| fdiv f3, f1, f7 |    2     |        5        |      15      |       16       |
| fdiv f3, f1, f7 |    17    |       18        |      28      |       29       |
