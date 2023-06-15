#include<stdint.h>

extern void poly_compress_ref(uint8_t *rp, uint8_t *a);
extern void poly_compress_avx2(uint8_t *rp, uint8_t *a);


int main(void){
  uint8_t p[512];
  uint8_t out0[128];
  uint8_t out1[128];

  poly_compress_ref(out0, p);
  poly_compress_avx2(out1, p);

  return 0;
}
