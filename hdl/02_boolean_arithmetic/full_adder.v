`include "half_adder.v"

module full_adder(output sum, carry, input a, b, c);
    wire first_sum;
    wire first_carry;
    wire second_carry;

    half_adder add_1(first_sum, first_carry, a, b);

    half_adder add_2(sum, second_carry, first_sum, c);

    assign carry = first_carry | second_carry;
endmodule