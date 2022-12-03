#!/bin/bash
g++ $1.cc -o $1 && ./$1
rm $1