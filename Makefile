override CFLAGS=-g -shared -fPIC
PREFIX=/usr
BUILDDIR=bin/

TARGET=AudioPython.so
SOURCES=$(wildcard csrc/*.c)

#Makes everything(defaults to python3)
all: python3

python3: cython
	mkdir $(BUILDDIR)
	$(CC) $(CFLAGS) `python3.4-config --cflags` `python3.4-config --ldflags` $(SOURCES) -o $(BUILDDIR)$(TARGET)

python2: cython
	mkdir $(BUILDDIR)
	$(CC) $(CFLAGS) -I/usr/include/python2.7 -lpython2.7 $(SOURCES) -o $(BUILDDIR)$(TARGET)

#Uses picky extensions and makes everything(Extensions may break compiling)
dev:
	make all CFLAGS+="-Wall -Wextra -DNDEBUG -O2"

#Makes a cython representation of AudioPython
cython:
	mkdir csrc
	cython AudioPython/*.py
	mv AudioPython/*.c csrc/

#Cleans directory(no uninstall!)
clean:
	rm -rf csrc
	rm -rf bin
	rm -rf build

#Installs into specified(or default) directory
install:
	install -d $(PREFIX)/include/AudioPython
	install $(BUILDDIR)$(TARGET) $(PREFIX)/include/AudioPython

#Uninstalls from specified(or default)directory
uninstall:
	rm -rf $(PREFIX)/include/AudioPython

#Checks for bad functions
BADFUNCS='[^_.>a-zA-Z0-9](str(n?cpy|n?cat|xfrm|n?dup|str|pbrk|tok|_)|stpn?cpy|a?sn?printf|byte_)'
check:
	@echo Files with potentially dangerous functions:
	@grep $(BADFUNCS) $(SOURCES) || echo None
