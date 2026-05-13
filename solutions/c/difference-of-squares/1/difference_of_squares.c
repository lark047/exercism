#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number)
{
    unsigned sum = 0;
    for (unsigned i = 1; i <= number; ++i)
    {
        sum += i * i;
    }
    return sum;
}

unsigned int square_of_sum(unsigned int number)
{
    unsigned sum = 0;
    for (unsigned i = 1; i <= number; ++i)
    {
        sum += i;
    }
    return sum * sum;
}

unsigned int difference_of_squares(unsigned int number)
{
    unsigned int sum_squares = sum_of_squares(number);
    unsigned int square_sum = square_of_sum(number);
    return square_sum - sum_squares;
}
