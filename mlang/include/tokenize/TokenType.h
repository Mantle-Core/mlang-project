#ifndef MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_
#define MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_

namespace mlang::tok {
    
    enum class Token : unsigned char {
        #define MANTLE_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymComparison : unsigned char {
        #define MANTLE_SYMBOL_COMPARISON_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymOperator : unsigned char {
        #define MANTLE_SYMBOL_OPERATOR_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymBitwise : unsigned char {
        #define MANTLE_SYMBOL_BITWISE_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymAssignment : unsigned char {
        #define MANTLE_SYMBOL_ASSIGNMENT_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymScope : unsigned char {
        #define MANTLE_SYMBOL_SCOPE_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class SymPunctuator : unsigned char {
        #define MANTLE_SYMBOL_PUNCTUATOR_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class Symbol : unsigned char {
        #define MANTLE_SYMBOL_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyDataType : unsigned char {
        #define MANTLE_KEYWORD_DATA_TYPE_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyControlFlow : unsigned char {
        #define MANTLE_KEYWORD_CONTROL_FLOW_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyDataStructure : unsigned char {
        #define MANTLE_KEYWORD_DATA_STRUCTURE_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyFiles : unsigned char {
        #define MANTLE_KEYWORD_FILES_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyDeclaration : unsigned char {
        #define MANTLE_KEYWORD_DECLARATION_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyBoolean : unsigned char {
        #define MANTLE_KEYWORD_BOOLEAN_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyOther : unsigned char {
        #define MANTLE_KEYWORD_OTHER_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

    enum class KeyReserved : unsigned char {
        #define MANTLE_KEYWORD_RESERVED_TOKEN(name, spelling) name,
        #include "TokenType.def"
    };

}
    
#endif // MLANG_INCLUDE_TOKENIZE_TOKENTYPE_H_