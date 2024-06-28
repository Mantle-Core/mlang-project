# Path to Python script for generating xmacro header
GENERATE_XMACRO_HEADER_PY = scripts/GenerateXMacroHeader.py
GENERATE_TOKENTYPE_HEADER_PY = scripts/GenerateTokenTypeHeader.py

# xmacro header file
XMACRO_HEADER = TokenType.def
ENUM_HEADER = TokenType.h

# Generate xmacro header and enum header
all: $(XMACRO_HEADER) $(ENUM_HEADER)

# Generate xmacro header
$(XMACRO_HEADER): $(GENERATE_XMACRO_HEADER_PY)
	python $(GENERATE_XMACRO_HEADER_PY) > $(XMACRO_HEADER)

# Generate enum header
$(ENUM_HEADER): $(GENERATE_TOKENTYPE_HEADER_PY)
	python $(GENERATE_TOKENTYPE_HEADER_PY) > $(ENUM_HEADER)

# Clean up generated files
clean:
	rm -rf $(XMACRO_HEADER) $(ENUM_HEADER)

.PHONY: all clean
