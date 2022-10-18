`include "gates.v"

module _not16
    #(parameter N = 16)
    (output[0:15] out_y, input[0:15] in_a);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin
            _not not_0 (out_y[i], in_a[i]);
        end
    endgenerate
endmodule

module _and16
    #(parameter N = 16)
    (output[0:15] out_y, input[0:15] in_a, in_b);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin
            _and and_0 (out_y[i], in_a[i], in_b[i]);
        end
    endgenerate
endmodule

module _or16
    #(parameter N = 16)
    (output[0:15] out_y, input[0:15] in_a, in_b);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin
            _or or_0 (out_y[i], in_a[i], in_b[i]);
        end
    endgenerate
endmodule

module _mux16
    #(parameter N = 16)
    (output[0:15] out_y, input[0:15] in_a, in_b, input sel);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin
            _mux mux_0 (out_y[i], in_a[i], in_b[i], sel);
        end
    endgenerate
endmodule

module _or8way
    (output out_y, input[0:7] in_a);
    wire a;
    wire b;
    wire c;
    wire d;
    wire e;
    wire f;

    _or or_1(a, in_a[0], in_a[1]);
    _or or_2(b, in_a[2], in_a[3]);
    _or or_3(c, in_a[4], in_a[5]);
    _or or_4(d, in_a[6], in_a[7]);
    _or or_5(e, a, b);
    _or or_6(f, c, d);
    _or or_7(out_y, e, f);
endmodule

module _mux4way16
    (output[0:15] out_y, input[0:15] in_a, in_b, in_c, in_d, input[0:1] sel);
    wire[0:15] first_mux16;
    wire[0:15] second_mux16;

    // This is different to the book, because using `input[0:1]` means that the most
    // significant bit will be in sel[0], not in sel[1].
    _mux16 mux16_ab(first_mux16, in_a, in_b, sel[1]);
    _mux16 mux16_cd(second_mux16, in_c, in_d, sel[1]);
    _mux16 mux16_out(out_y, first_mux16, second_mux16, sel[0]);
endmodule

module _mux8way16
    (output[0:15] out_y, input[0:15] in_a, in_b, in_c, in_d, in_e, in_f, in_g, in_h, input[0:2] sel);
    wire[0:15] mux16_0;
    wire[0:15] mux16_1;
    wire[0:15] mux16_2;
    wire[0:15] mux16_3;
    wire[0:15] mux16_4;
    wire[0:15] mux16_5;

    // This is different to the book, because using `input[0:1]` means that the most
    // significant bit will be in sel[0], not in sel[1].
    _mux16 mux16_ab(mux16_0, in_a, in_b, sel[2]);
    _mux16 mux16_cd(mux16_1, in_c, in_d, sel[2]);
    _mux16 mux16_ef(mux16_2, in_e, in_f, sel[2]);
    _mux16 mux16_gh(mux16_3, in_g, in_h, sel[2]);
    _mux16 mux16_abcd(mux16_4, mux16_0, mux16_1, sel[1]);
    _mux16 mux16_efgh(mux16_5, mux16_2, mux16_3, sel[1]);
    _mux16 mux16_out(out_y, mux16_4, mux16_5, sel[0]);
endmodule


module _dmux4way
    (output out_a, out_b, out_c, out_d, input in_, input[0:1] sel);

    wire sel_ab;
    wire sel_cd;

    wire sel_a_first;
    wire sel_b_first;
    wire sel_c_first;
    wire sel_d_first;

    wire sel_a;
    wire sel_b;
    wire sel_c;
    wire sel_d;

    assign sel_cd = sel[0];
    _not not_0(sel_ab, sel[0]);

    assign sel_b_first = sel[1];
    _not not_1(sel_a_first, sel[1]);
    assign sel_d_first = sel[1];
    _not not_2(sel_c_first, sel[1]);

    _and and_0(sel_a, sel_a_first, sel_ab);
    _and and_1(sel_b, sel_b_first, sel_ab);
    _and and_2(sel_c, sel_c_first, sel_cd);
    _and and_3(sel_d, sel_d_first, sel_cd);

    _and and_4(out_a, sel_a, in_);
    _and and_5(out_b, sel_b, in_);
    _and and_6(out_c, sel_c, in_);
    _and and_7(out_d, sel_d, in_);

endmodule

