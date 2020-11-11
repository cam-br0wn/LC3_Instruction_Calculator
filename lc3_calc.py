# LC-3 Instruction Calculator
# Cam Brown because he's lazy...
# Nov 11, 2020

def help():
    print("\t\tInstructions:\t\t\n- If you want to convert from instructions to binary/hex type i:<YOUR INSTRUCTION>")
    print("Example:\ni:ADD R1,R2,R3")
    # TODO: print binary/hex conversion
    print("- If you want to convert from binary to instruction, type b:<BINARY ENTRY>")
    print("Example:\nb:0001001010000011")
    # TODO: print instruction conversion
    print("To ever print these instructions again, just type 'h' or 'help'")


def parse_instruction(str_input):
    inst = str_input[2:].split(' ')[0]
    ops_with_codes = {'ADD':0x1, 'AND':0x5, 'BR':0x0, 'JMP':0xC, 'JSR':0x4, 'JSRR':0x4, 'LD':0x2, 'LDI':0xA, 'LDR':0x6, 'LEA':0xE, 'NOT':0x9, 'RET':0xC, 'RTI':0x8, 'ST':0x3, 'STI':0xB, 'STR':0x7, 'TRAP':0xF}
    regs = str_input[2:].split(' ')[1].split(',')
    concat = []
    for item in regs:
        item.replace(" ", "")
        if item[0] == 'R':
            concat.append(str(hex(int(item[1]))))
        elif item[0] == '#':
            concat.append(str(hex(int(item[1:]))))

    hex_str = str(ops_with_codes[inst])
    for item in concat:
        hex_str += item[2:]

    bin_val = bin(int(hex_str, 16))
    bin_str = str(bin_val)

    return bin_str + " or " + hex(int(hex_str))


def main():
    print("Welcome to the LC-3 Instruction Calculator for people too lazy to convert hex/binary instructions by hand")
    help()
    run = True
    while (run):
        # user_in = input()
        user_in = 'i:LEA R1,#2'
        if user_in == 'h' or user_in == 'help':
            help()
        if user_in[0] == 'i':
            print(parse_instruction(user_in))
        run = False

    print("Goodbye!")
    quit()


if __name__ == '__main__':
    main()
