CRYPTOLINE_PATH ?=
CFLAGS  ?= -Wall -Wno-unused-function -march=native -O3 -fno-lto -fomit-frame-pointer -fwrapv -fPIC -fPIE

#--
amd64_ref.s: amd64_ref.jazz
	jasminc $< -o $@

amd64_avx2.s: amd64_avx2.jazz
	jasminc $< -o $@

main: main.c amd64_ref.s amd64_avx2.s
	$(CC) $(CFLAGS) -o $@ $^

#--
amd64_ref.gas.0: main
	$(CRYPTOLINE_PATH)/scripts/itrace.py main rounds_inline_ref > $@

amd64_avx2.gas.0: main
	$(CRYPTOLINE_PATH)/scripts/itrace.py main rounds_v_avx2 > $@

#--
.PHONY: clean
clean:
	rm -f amd64_ref.s amd64_avx2.s main
	rm -f amd64_ref.gas.0 amd64_avx2.gas.0
