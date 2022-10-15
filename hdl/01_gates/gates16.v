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