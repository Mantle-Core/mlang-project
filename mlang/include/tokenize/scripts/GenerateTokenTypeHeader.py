import os

def read_token_definitions(file_path):
    token_categories = {}
    current_category = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith("//"):
                continue

            if line.startswith("#ifndef"):
                current_category = line.split()[1]
                token_categories[current_category] = []
            elif line.startswith("#define"):
                continue
            elif line.startswith("#endif"):
                current_category = None
            else:
                # Handle both macro-based and direct token definitions
                parts = line.split("(")
                if len(parts) > 1:  # Check if it's a macro-based definition
                    token_name = parts[1].split(",")[0].strip()
                else:  # Direct token definition
                    token_name = line.split()[-1].strip()
                if current_category is not None:
                    token_categories[current_category].append(token_name)

    return token_categories

def generate_enum_definitions(token_categories):
    enum_definitions = ""
    macro_prefix = "MANTLE_"
    macro_suffix = "_TOKEN"

    for macro_name in token_categories.keys():
        if macro_name.startswith(macro_prefix) and macro_name.endswith(macro_suffix):
            if macro_name == "MANTLE_TOKEN":
                enum_name = macro_name[len(macro_prefix):]
            else:                
                enum_name = macro_name[len(macro_prefix):-len(macro_suffix)]
            
            if enum_name.startswith("SYMBOL") and not enum_name == "SYMBOL":
                enum_name = enum_name[len("SYMBOL"):]
                enum_name = "SYM" + enum_name
            elif enum_name.startswith("KEYWORD"):
                enum_name = enum_name[len("KEYWORD"):]
                enum_name = "KEY" + enum_name
            
            enum_name = ''.join(word.capitalize() for word in enum_name.split('_'))

            enum_definitions += f"    enum class {enum_name} : unsigned char {{\n"
            enum_definitions += f"        #define {macro_name}(name, spelling) name,\n"
            enum_definitions += "        #include \"TokenType.def\"\n"
            enum_definitions += f"    }};\n\n"

    return enum_definitions


def generate_token_type_header(token_categories):
    header = """#ifndef MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_
#define MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_

namespace mlang::tok {
    \n"""
    header += generate_enum_definitions(token_categories)
    
    header += """}
    
#endif // MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_"""
    return header


# Define the input file path
input_file_name = "TokenType.def"
input_file_path = os.path.join(os.path.dirname(__file__), "..", input_file_name)

# Read token definitions from the input file
token_definitions = read_token_definitions(input_file_path)

# Generate TokenType.h content
header_content = generate_token_type_header(token_definitions)

# Write to file
output_file_name = "TokenType.h"
with open(output_file_name, "w") as file:
    file.write(header_content)
