AS = ca65
LD = ld65
SREC = srec_cat
SOURCES = $(wildcard *.asm)
INCLUDES = $(wildcard *.inc)
OBJECTS = $(patsubst %.asm,%.o,$(SOURCES))
CFG = wdc.cfg
OFFSET = 512
BASE = puzzle1
MAP = $(BASE).map
BINARY = $(BASE).bin
TARGET = $(BASE).srec

.phony: all
.phony: clean

all: $(TARGET)

$(TARGET): $(BINARY)
	$(SREC) $(BINARY) -binary -offset $(OFFSET) -output $(TARGET) -motorola -address-length=3

$(BINARY): $(OBJECTS) $(CFG)
	$(LD) -C $(CFG) -o $(BINARY) -m $(MAP) $(OBJECTS)

%.o: %.asm $(INCLUDES)
	$(AS) -l $(subst .asm,.lst,$<) -o $@ $<

clean:
	rm -f $(TARGET)
	rm -f $(BINARY)
	rm -f $(MAP)
	rm -f $(OBJECTS)
	rm -f *.lst
