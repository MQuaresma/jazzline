#include <stdint.h>

extern void rounds_inline_ref(uint32_t *k);
extern void rounds_v_avx2(uint32_t *k);

int main(void)
{
  uint32_t kref[16];
  uint32_t kavx2[16*8];

  rounds_inline_ref(kref);
  rounds_v_avx2(kavx2);

  return 0;
}
