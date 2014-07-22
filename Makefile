#Makefile largely taken from Zed Shaws great "Learn C The Hard Way"
CFLAGS=-g -shared -fPIC -I/usr/include/python2.7 -lpython2.7
PREFIX=/usr/local
BUILDDIR=bin/

TARGET=AudioPython.so
SOURCES=$(wildcard csrc/*.c)

#Makes everything
all:
	g++ $(CFLAGS) $(SOURCES) -o $(BUILDDIR)$(TARGET)

#Uses picky extensions and makes everything(Extensions may break compiling)
dev:
	CFLAGS+=-Wall -Wextra -DNDEBUG -O2
	make all

#Cleans directory(no uninstall!)
clean:
	rm -rf bin
	rm -rf build

#Installs into specified(or default) directory
install:
	make all
	install -d $(PREFIX)/lib/AudioPython.so
	install $(TARGET) $(DESTDIR)/lib/AudioPython.so

#Uninstalls from specified(or default)directory
uninstall:
	rm -rf $(PREFIX)/lib/AudioPython.so

#Checks for bad functions
BADFUNCS='[^_.>a-zA-Z0-9](str(n?cpy|n?cat|xfrm|n?dup|str|pbrk|tok|_)|stpn?cpy|a?sn?printf|byte_)'
check:
	@echo Files with potentially dangerous functions:
	@grep $(BADFUNCS) $(SOURCES) || echo None
