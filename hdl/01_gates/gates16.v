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