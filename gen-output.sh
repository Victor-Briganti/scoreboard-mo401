#!/usr/bin/env bash

set -e

mkdir -p output/config{01..04}

for i in {1..4}; do
    for j in {1..15}; do
        uv run scoreboard \
            -c "configs/config$(printf '%02d' "$i").conf" \
            -f "examples/example$(printf '%02d' "$j").s" \
            > "output/config$(printf '%02d' "$i")/output$(printf '%02d' "$j").md"
    done
done