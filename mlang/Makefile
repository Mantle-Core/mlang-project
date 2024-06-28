# Compiler
CC = clang++

# Compiler flags
CFLAGS = -std=c++20 -Wall -Wextra
CFLAGS_DEBUG = $(CFLAGS) -g

OBJ_DIR = obj
OBJ_DEBUG_DIR = $(OBJ_DIR)/debug
OBJ_RELEASE_DIR = $(OBJ_DIR)/release

LIB_DIRS = lib/tokenize \
            lib

# Separate LIB_OBJS for debug and release builds
LIB_OBJS_RELEASE = $(foreach dir,$(LIB_DIRS),$(wildcard $(dir)/$(OBJ_RELEASE_DIR)/*.o))
LIB_OBJS_DEBUG = $(foreach dir,$(LIB_DIRS),$(wildcard $(dir)/$(OBJ_DEBUG_DIR)/*.o))

SRCS = Start.cpp
OBJ_SRCS_RELEASE = $(addprefix $(OBJ_RELEASE_DIR)/,$(SRCS:.cpp=.o)) $(LIB_OBJS_RELEASE)
OBJ_SRCS_DEBUG = $(addprefix $(OBJ_DEBUG_DIR)/,$(SRCS:.cpp=.o)) $(LIB_OBJS_DEBUG)

BIN_DIR = ../bin
EXECS = $(BIN_DIR)/mlang
EXECS_DEBUG = $(BIN_DIR)/mlang-debug
VALGRIND_FLAGS = --leak-check=full --show-leak-kinds=all

# Default target (release build)
all: release

$(BIN_DIR):
# Create object directories if they don't exist
	mkdir -p $(BIN_DIR)

$(OBJ_RELEASE_DIR):
	mkdir -p $(OBJ_RELEASE_DIR)

$(OBJ_DEBUG_DIR):
	mkdir -p $(OBJ_DEBUG_DIR)

# Release build
release: $(BIN_DIR) $(EXECS)

$(EXECS): $(OBJ_RELEASE_DIR) $(OBJ_SRCS_RELEASE)
	$(CC) -lstdc++ $(CFLAGS) $(OBJ_SRCS_RELEASE) -o $(EXECS)

$(OBJ_RELEASE_DIR)/%.o: %.cpp | $(OBJ_RELEASE_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Debug build
debug: $(BIN_DIR) $(EXECS_DEBUG)

$(EXECS_DEBUG): $(OBJ_DEBUG_DIR) $(OBJ_SRCS_DEBUG)
	$(CC) -lstdc++ $(CFLAGS_DEBUG) $(OBJ_SRCS_DEBUG) -o $(EXECS_DEBUG)

$(OBJ_DEBUG_DIR)/%.o: %.cpp | $(OBJ_DEBUG_DIR)
	$(CC) $(CFLAGS_DEBUG) -c $< -o $@

# Valgrind test target
valgrind: $(EXECS)
	valgrind $(VALGRIND_FLAGS) ./$(EXECS)

# Clean up generated files
clean:
	rm -rf $(OBJ_DIR)
	rm -rf $(BIN_DIR)

# Debugger
debugger: $(EXECS_DEBUG)
	lldb ./$(EXECS_DEBUG)

.PHONY: all release debug clean valgrind debugger
