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