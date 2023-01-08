`include "gates16.v"
`include "add16.v"


module alu
    (input[0:15] x, y, input zx, nx, zy, ny, f, no, output[0:15] out, output zr, ng);

    reg[0:15] ZERO = 16'd0;
    reg[0:15] x_zeroed;
    reg[0:15] not_x;
    reg[0:15] x_preset;
    reg[0:15] y_zeroed;
    reg[0:15] not_y;
    reg[0:15] y_preset;
    reg[0:15] add_xy;
    reg[0:15] and_xy;
    reg signed[0:15] compute_result;
    reg signed[0:15] compute_result_inversed;

    // Preset x
    // If zx then x=0
    _mux16 preset_x_to_zero (x_zeroed, x, ZERO, zx);
    
    // If nx then x = !x
    _not16 not_x_0 (not_x, x_zeroed);
    _mux16 negate_x (x_preset, x_zeroed, not_x, nx);

    // // Preset y
    // // If zy then y=0
    _mux16 preset_y_to_zero (y_zeroed, y, ZERO, zy);
    
    // If ny then y = !y
    _not16 not_y_0 (not_y, y_zeroed);
    _mux16 negate_y (y_preset, y_zeroed, not_y, ny);

    // // Computing + or &
    _add16 add_0 (add_xy, x_preset, y_preset);
    _and16 and_0 (and_xy, x_preset, y_preset);
    _mux16 compute (compute_result, and_xy, add_xy, f);

    // // Post-setting output
    _not16 not_result (compute_result_inversed, compute_result);
    _mux16 compute_inverse (out, compute_result, compute_result_inversed, no);

    // // Is output zero?
    // // This can be done with not(and(or()))
    // assign zr = out === ZERO;

    // // Is output negative?
    // assign ng = out < ZERO;
endmodule