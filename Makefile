# List subdirectories
SUBDIRS = src/lib/Parse \
          src/lib/RootedTree \
		  src

# Default target to build all subdirectories
all:
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done

# Clean all subdirectories
clean:
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done

.PHONY: all clean $(SUBDIRS)
