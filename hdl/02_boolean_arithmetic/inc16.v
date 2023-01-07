`include "add16.v"

module inc16
    (output[0:15] out, input[0:15] a);
    localparam [0:15] one=1; 
    _add16 add16_0 (out, a, one);
endmodule
