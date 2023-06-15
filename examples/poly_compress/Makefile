CRYPTOLINE_PATH ?= /Users/miguelquaresma/Documents/workspace/tools/cryptoline
CFLAGS  ?= -Wall -Wno-unused-function -march=native -O3 -fno-lto -fomit-frame-pointer -fwrapv -fPIC -fPIE

default: main

#--
ref.s: ref.jazz
	jasminc $< -o $@

avx2.s: avx2.jazz
	jasminc $< -o $@

main: main.c ref.s avx2.s
	$(CC) $(CFLAGS) -o $@ $^

#--
ref.gas.0: main
	$(CRYPTOLINE_PATH)/scripts/itrace.py main poly_compress_ref > $@

avx2.gas.0: main
	$(CRYPTOLINE_PATH)/scripts/itrace.py main poly_compress_avx2 > $@

#--
.PHONY: clean
clean:
	rm -f ref.s avx2.s main
	rm -f ref.gas.0 avx2.gas.0
