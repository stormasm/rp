#!/bin/bash
set -e

cd "$(dirname "$(dirname "$0")")"

rustpython asdl_rs.py -D ast_gen.rs -M gen.rs Python.asdl
