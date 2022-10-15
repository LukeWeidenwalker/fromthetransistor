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

    _not not_1(not_a, a);
    _not not_2(not_b, b);

    nand(y, not_a, not_b);
endmodule

module _xor(output y, input a, b);
    wire or_1;
    wire nand_1;

    _or or_gate(or_1, a, b);
    nand(nand_1, a, b);

    _and and_1(y, or_1, nand_1);
endmodule

module _mux(output out, input a, b, sel);
    wire not_sel;
    wire and_a;
    wire and_b;

    _not not_1(not_sel, sel);
    _and and_1(and_a, a, not_sel);
    _and and_2(and_b, b, sel);
    _or or_1(out, and_a, and_b);
endmodule

module _dmux(output out_x, out_y, input in_a, sel);
    wire not_sel;
    _not not_1(not_sel, sel);
    _and and_a(out_x, in_a, not_sel);
    _and and_b(out_y, in_a, sel);
endmodule