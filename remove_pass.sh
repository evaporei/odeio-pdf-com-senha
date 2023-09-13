#!/bin/bash

# Usage: ./remove_pass.sh input.pdf PASSWORD

OUT="${1%.*}"

# echo $1
# echo $OUT
# echo "$OUT"_out.pdf
# echo $2

# pdftk [input.pdf] input_pw [PASSWORD] output [output.pdf]
pdftk $1 input_pw 435 output "$OUT"_no_pass.pdf
