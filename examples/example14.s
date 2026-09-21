fld f1, 0(x7)             
fld f2, 0(x8)             
fmul f3, f1, f2         
fld f1, 0(x11)            
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 0(x11)            
fld f1, 8(x7)             
fld f2, 16(x8)            
fmul f3, f1, f2         
fld f1, 0(x11)            
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 0(x11)            
fld f1, 0(x7)             
fld f2, 8(x8)             
fmul f3, f1, f2         
fld f1, 8(x11)            
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 8(x11)            
fld f1, 8(x7)             
fld f2, 24(x8)            
fmul f3, f1, f2         
fld f1, 8(x11)            
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 8(x11)            
fld f1, 16(x7)            
fld f2, 0(x8)             
fmul f3, f1, f2         
fld f1, 16(x11)           
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 16(x11)           
fld f1, 24(x7)            
fld f2, 16(x8)            
fmul f3, f1, f2         
fld f1, 16(x11)           
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 16(x11)           
fld f1, 16(x7)            
fld f2, 8(x8)             
fmul f3, f1, f2         
fld f1, 24(x11)           
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 24(x11)           
fld f1, 24(x7)            
fld f2, 24(x8)            
fmul f3, f1, f2         
fld f1, 24(x11)           
fadd f1, f1, f3         
fmul f2, f1, f3         
fdiv f3, f2, f1         
fsub f1, f1, f3         
fadd f1, f1, f3         
fsd f1, 24(x11)