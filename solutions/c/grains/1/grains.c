#include "grains.h"

uint64_t square(uint8_t index)
{
    return 1 <= index && index <= 64 ? 1ULL << (index - 1) : 0;
}

uint64_t total(void)
{
    uint64_t total = 0;
    for (uint8_t i = 1; i <= 64; ++i)
    {
        total += square(i);
    }
    return total;
}
