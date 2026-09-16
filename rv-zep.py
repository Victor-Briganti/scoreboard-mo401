INST_TO_FU = {
    "fld": "int",
    "fsd": "int",
    "fadd": "add",
    "fsub": "add",
    "fmul": "mult",
    "fdiv": "div",
}

# Update all entries: replace "add" with the list ["add1", "add2"]
replacement = ["add1", "add2"]

INST_TO_FU = {
    inst: replacement if fu == "add" else [fu]
    for inst, fu in INST_TO_FU.items()
}

print(INST_TO_FU)