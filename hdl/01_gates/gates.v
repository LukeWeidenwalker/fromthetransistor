module _not(output y, input a);
    nand(y, a, a);
endmodule

module _and(output y, input a, b);    
    wire nand_1;

    nand(nand_1, a, b);

    _not not_0(y, nand_1);
endmodule

module _or(output y, input a, b);
    wire not_a;
    wire not_b;

    not(not_a, a);
    not(not_b, b);

    nand(y, not_a, not_b);
endmodule

module _xor(output y, input a, b);
    wire or_1;
    wire nand_1;

    _or or_gate(or_1, a, b);
    nand(nand_1, a, b);

    _and and_1(y, or_1, nand_1);
endmodule