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