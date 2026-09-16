fld f1, 0(x7)             
fld f2, 8(x7)             
fld f4, 16(x7)            
fld f6, 24(x7)            
fsd f1, 0(x11)            
fsd f2, 8(x11)            
fadd f3, f1, f2         
fmul f5, f3, f4         
fdiv f7, f5, f4         
fsd f3, 16(x11)           
fsub f1, f3, f1         
fadd f2, f3, f7         
fsub f2, f2, f7
fadd f3, f1, f2         
fmul f5, f3, f6         
fdiv f7, f5, f4         
fsub f7, f7, f6         
fsd f3, 24(x11)           
fsub f1, f3, f1         
fadd f2, f3, f7         
fadd f3, f1, f2         
fmul f5, f2, f4         
fsub f5, f5, f1         
fdiv f7, f5, f6         
fsd f3, 32(x11)           
fsub f1, f3, f1         
fmul f2, f3, f7         
fadd f3, f1, f2         
fmul f5, f3, f4         
fdiv f7, f5, f4         
fsd f3, 40(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fmul f5, f1, f6         
fsub f5, f5, f7         
fdiv f7, f3, f4         
fsd f3, 48(x11)           
fsub f1, f3, f1         
fadd f2, f3, f5         
fsub f2, f2, f7         
fadd f3, f1, f2         
fmul f5, f2, f4         
fsub f5, f5, f6         
fdiv f7, f5, f3         
fsd f3, 56(x11)           
fsub f1, f3, f1         
fmul f2, f3, f7         
fadd f3, f1, f2         
fdiv f5, f3, f6         
fmul f7, f5, f6         
fsd f3, 64(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fdiv f5, f3, f4         
fmul f7, f5, f4         
fsd f3, 72(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fmul f5, f3, f4         
fdiv f7, f5, f4         
fsd f3, 80(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fmul f5, f3, f6         
fdiv f7, f5, f6         
fsd f3, 88(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fdiv f5, f3, f4         
fdiv f5, f5, f6         
fmul f7, f5, f6         
fmul f7, f7, f4         
fsd f3, 96(x11)           
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fmul f5, f3, f4         
fdiv f7, f5, f4         
fsd f3, 104(x11)          
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fmul f5, f3, f6         
fdiv f7, f5, f6         
fsd f3, 112(x11)          
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fdiv f5, f3, f4         
fmul f7, f5, f4         
fsd f3, 120(x11)          
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3         
fadd f3, f1, f2         
fdiv f5, f3, f6         
fmul f7, f5, f6         
fsd f3, 128(x11)          
fsub f1, f3, f1         
fsub f2, f3, f7         
fadd f2, f2, f3