`include "full_adder.v"

module add16
    (output[0:15] out, input[0:15] a, b);
    
    wire[0:15] carries; 

    half_adder half_add_0 (out[15], carries[15], a[15], b[15]);

    genvar i;
    generate 
        for (i=14; i>=0; i=i-1) begin
            full_adder full_add_0 (out[i], carries[i], a[i], b[i], carries[i+1]);
        end
    endgenerate
endmodule