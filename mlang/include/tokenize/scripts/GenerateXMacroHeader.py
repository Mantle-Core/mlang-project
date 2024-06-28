# Python script to generate xmacro definitions, max size macros, and string literal arrays

# Define tokens
tokens = [
    "Unidentified", 
    "StartOfFile", 
    "EndOfFile",
    "Identifier", 
    "IntegerLiteral", 
    "StringLiteral", 
    "RealLiteral"
]

symbol_comparison_tokens = [
    ("Less", "<"), 
    ("Greater", ">"), 
    ("LessEqual", "<="), 
    ("GreaterEqual", ">="), 
    ("EqualEqual", "=="), 
    ("ExclaimEqual", "!=")
]

symbol_operator_tokens = [
    ("Plus", "+"), 
    ("PlusPlus", "++"), 
    ("Minus", "-"), 
    ("MinusMinus", "--"),
    ("Slash", "/"),
    ("Percent", "%")
]

symbol_bitwise_tokens = [
    ("LessLess", "<<"), 
    ("GreaterGreater", ">>"), 
    ("Tilde", "~"), 
    ("Caret", "^"), 
    ("Pipe", "|")
]

symbol_assignment_tokens = [
    ("Equal", "="), 
    ("StarEqual", "*="), 
    ("SlashEqual", "/="), 
    ("PercentEqual", "%="), 
    ("PlusEqual", "+="), 
    ("MinusEqual", "-="), 
    ("LessLessEqual", "<<="), 
    ("GreaterGreaterEqual", ">>="), 
    ("PipeEqual", "|="), 
    ("AmpersandEqual", "&=")
]

symbol_scope_tokens = [
    ("ColonColon", "::"),
    ("OpenSquareBracket", "["), 
    ("CloseSquareBracket", "]"), 
    ("OpenParentheses", "("), 
    ("CloseParentheses", ")"), 
    ("OpenCurlyBracket", "{"), 
    ("CloseCurlyBracket", "}")
]

symbol_punctuator_tokens = [
    ("QuestionMark", "?"),
    ("Colon", ":"), 
    ("Comma", ","), 
    ("Dot", "."), 
    ("SemiColon", ";")
]

symbol_tokens = [
    ("Star", "*"),                  # pointers and multiplication
    ("MinusGreater", "->"),         # function return arrow
    ("Ampersand", "&"),             # bitwise and, and get address of
    ("AmpersandAmpersand", "&&")    # pointer dereference
]

keyword_data_type_tokens = [
    "S8", 
    "S16", 
    "S32", 
    "S64", 
    "S128", 
    "U8", 
    "U16", 
    "U32", 
    "U64", 
    "u128", 
    "F32", 
    "F64",
    "F128",
    "String", 
    "Bool"
]

keyword_control_flow_tokens = [
    "Extern", 
    "Break", 
    "Case", 
    "Switch", 
    "Default", 
    "Do", 
    "While", 
    "Skip", 
    "For", 
    "If", 
    "Guard", 
    "Else", 
    "Return", 
    "Try",
    "Throw", 
    "Or", 
    "And" 
]

keyword_data_structure_tokens = [
    "Component", 
    "Blueprint", 
    "Extension", 
    "Struct", 
    "System", 
    "Enum", 
    "Union"    
]

keyword_files_tokens = [
    "Module", 
    "Import"
]

keyword_declaration_tokens = [
    "Unique", 
    "Readonly", 
    "Function", 
    "Macro", 
    "Typealias", 
    "Inline", 
    "Constexpr"
]

keyword_boolean_tokens = [
    "True", 
    "False"
]

keyword_other_tokens = [
    "Sizeof",
    "Nullptr" 
]

keyword_reserved_tokens = [
    "AlignAs",
    "AlignOf",
    "Atomic",
    "Complex",
    "Imaginary",
    "NoReturn",
    "StaticAssert",
    "ThreadLocal"
]

# Generate xmacro header
def generate_xmacro_header():
    header = []

    header.append("//======================================================")
    header.append("//")
    header.append("// x-macro header, we do this to write once use everywhere")
    header.append("//")
    header.append("//======================================================")
    header.append("//")
    header.append("// X-macros are a technique in C/C++ programming that use macros to generate repetitive code.")
    header.append("// This approach involves defining a list of macro invocations that are included wherever needed.")
    header.append("//")
    header.append("// We define our x-macros as so:")
    header.append("// ")
    header.append("// MANTLE_TOKEN(name)")
    header.append("// ")
    header.append("// The MANTLE_TOKEN macro is used as a placeholder that can be defined differently depending on the context.")
    header.append("// This way, we can declare all our tokens once and reuse this list in various parts of our codebase,")
    header.append("// such as in token definitions, debugging output, and more.")
    header.append("//")
    header.append("// Below are the different categories of tokens defined using this technique:")
    header.append("//")

    header.append("#ifndef MANTLE_TOKEN")
    header.append("#define MANTLE_TOKEN(name)")
    header.append("#endif")
    header.append("")

    def append_tokens(tokens, macro_name):
        if "SYMBOL" in macro_name or "KEYWORD" in macro_name:
            header.append(f"#ifndef {macro_name}")
            header.append(f"#define {macro_name}(Name, Spelling) MANTLE_TOKEN(Name)")
            header.append("#endif")
            header.append("")

        for token in tokens:
            if isinstance(token, tuple):
                header.append(f"{macro_name}({token[0]}, \"{token[1]}\")")
            elif "SYMBOL" in macro_name or "KEYWORD" in macro_name:
                header.append(f"{macro_name}({token}, \"{token.lower()}\")")
            else:
                header.append(f"{macro_name}({token})")
        header.append("")
        header.append(f"#undef {macro_name}")
        header.append("")

    # Append each token category with its specific macro type
    append_tokens(symbol_comparison_tokens, "MANTLE_SYMBOL_COMPARISON_TOKEN")
    append_tokens(symbol_operator_tokens, "MANTLE_SYMBOL_OPERATOR_TOKEN")
    append_tokens(symbol_bitwise_tokens, "MANTLE_SYMBOL_BITWISE_TOKEN")
    append_tokens(symbol_assignment_tokens, "MANTLE_SYMBOL_ASSIGNMENT_TOKEN")
    append_tokens(symbol_scope_tokens, "MANTLE_SYMBOL_SCOPE_TOKEN")
    append_tokens(symbol_punctuator_tokens, "MANTLE_SYMBOL_PUNCTUATOR_TOKEN")
    append_tokens(symbol_tokens, "MANTLE_SYMBOL_TOKEN")
    append_tokens(keyword_data_type_tokens, "MANTLE_KEYWORD_DATA_TYPE_TOKEN")
    append_tokens(keyword_control_flow_tokens, "MANTLE_KEYWORD_CONTROL_FLOW_TOKEN")
    append_tokens(keyword_data_structure_tokens, "MANTLE_KEYWORD_DATA_STRUCTURE_TOKEN")
    append_tokens(keyword_files_tokens, "MANTLE_KEYWORD_FILES_TOKEN")
    append_tokens(keyword_declaration_tokens, "MANTLE_KEYWORD_DECLARATION_TOKEN")
    append_tokens(keyword_boolean_tokens, "MANTLE_KEYWORD_BOOLEAN_TOKEN")
    append_tokens(keyword_other_tokens, "MANTLE_KEYWORD_OTHER_TOKEN")
    append_tokens(keyword_reserved_tokens, "MANTLE_KEYWORD_RESERVED_TOKEN")
    append_tokens(tokens, "MANTLE_TOKEN")

    return "\n".join(header)

# Write the header to a file
with open("TokenType.def", "w") as file:
    file.write(generate_xmacro_header())
