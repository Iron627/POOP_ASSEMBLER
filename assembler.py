instructions = {
    "NOP": "0000",
    "ADD": "0001",
    "SUB": "0010",
    "LDI": "0011",
    "ADI": "0100",
    "OR": "0101",
    "NOR": "0110",
    "AND": "0111",
    "XOR": "1000",
    "RSH": "1001",
    "CPY": "1010",
    "PLD": "1011",
    "JMP": "1100",
    "BRH": "1101",
    "PRT": "1110",
    "HLT": "1111"
}

def parse_register(reg):
    if not reg.lower().startswith('r'):
        raise ValueError("invalid register syntax")
    elif len(reg) == 1:
        raise ValueError("register must be a number")
    elif not reg[1:].isdigit():
        raise ValueError("register must be a number")
    elif int(reg[1:]) > 15:
        raise ValueError("attempted to address register that does not exist")
    else:
        return bin(int(reg[1:]))[2:].zfill(4)
def parse_mnemonic(mnemonic):
    if mnemonic not in instructions:
        raise ValueError("invalid instruction")
    else:
        return instructions[mnemonic]
def parse_immediate(immediate):
    if not immediate.isdigit():
        raise ValueError("immediate must be a number")
    elif int(immediate) > 255:
        raise ValueError("immediate is too large")
    else:
        return bin(int(immediate))[2:].zfill(8)
def parse_port(port):
    if not port.lower().startswith('p'):
        raise ValueError("invalid port syntax")
    elif len(port) == 1:
        raise ValueError("port must be a number")
    elif not port[1:].isdigit():
        raise ValueError("port must be a number")
    elif int(port[1:]) > 3:
        raise ValueError("attempted to address port that does not exist")
    else:
        return bin(int(port[1:]))[2:].zfill(2)
def parse_instruction(instruction):
    if not instruction:
        return "0000000000000000"
    elif instruction == "NOP":
        return "0000000000000000"
    elif instruction == "HLT":
        return "1111000000000000"
    instruction = instruction.split(" ")
    if parse_mnemonic(instruction[0]) == "0001":
        return("0001" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "0010":
        return("0010" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "0011":
        return("0011" + parse_register(instruction[1]) + parse_immediate(instruction[2]))
    elif parse_mnemonic(instruction[0]) == "0100":
        return("0100" + parse_register(instruction[1]) + parse_immediate(instruction[2]))
    elif parse_mnemonic(instruction[0]) == "0101":
        return("0101" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "0110":
        return("0110" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "0111":
        return("0111" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "1000":
        return("1000" + parse_register(instruction[1]) + parse_register(instruction[2]) + parse_register(instruction[3]))
    elif parse_mnemonic(instruction[0]) == "1001":
        return("1001" + parse_register(instruction[1]) + "0000" + parse_register(instruction[2]))
    elif parse_mnemonic(instruction[0]) == "1010":
        return("1010" + parse_register(instruction[1]) + "0000" + parse_register(instruction[2]))
    elif parse_mnemonic(instruction[0]) == "1011":
        return("1011" + parse_register(instruction[1]) + "1" + parse_port(instruction[2])[::-1] + "00000")
    elif parse_mnemonic(instruction[0]) == "1100":
        return("1100") + "0000" + parse_immediate(instruction[1])
    elif parse_mnemonic(instruction[0]) == "1101":
        if instruction[1] == "carry":
            return("1101" + "0000" + parse_immediate(instruction[2]))
        elif instruction[1] == "zero":
            return("1101" + "0001" + parse_immediate(instruction[2]))
        else:
            raise ValueError("invalid branch instruction")
    elif parse_mnemonic(instruction[0]) == "1110":
        return("1110" + parse_register(instruction[1]) + "0" + parse_port(instruction[2])[::-1] + "10000")

def assemble(code):
    assembled = []
    for line in code.splitlines():
        line = line.strip()
        if line.startswith("#"):
            continue  
        binary = parse_instruction(line)
        assembled.append(binary)
    return assembled
