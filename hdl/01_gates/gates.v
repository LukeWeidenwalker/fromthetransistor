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