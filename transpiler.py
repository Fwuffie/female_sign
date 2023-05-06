import re, argparse

parser = argparse.ArgumentParser()
parser.add_argument("src_file")
parser.add_argument("out_file")
args = parser.parse_args()

print(args.src_file)

def transpile_line(line: str):
    # Remove Comments
    if "//" in line:
        return transpile_line(line.split('//')[0])
    
    # If line ends with ; replace all spaces with _
    if line.endswith(';\n'):
        return transpile_line(line.replace(' ', '_').replace(";", ""))
    
    # If accessing class variables contains a name surrounded in {} call it like a function
    if re.search("\.{.+}", line):
        return re.sub("\.{(.+)}", r".\1()"  ,line)
    return line

with open(args.src_file, 'r') as src_file:
    src_file_lines = src_file.readlines()
    trasnspiled_code = []
    for line in src_file_lines:
        trasnspiled_code.append(transpile_line(line))

    with open(args.out_file, 'w') as compiled_file:
        compiled_file.writelines(trasnspiled_code)
        
    print("Finished Compile")