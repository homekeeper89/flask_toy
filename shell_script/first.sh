#! /bin/bash

set -e

set autoindent
set shiftwidth=4
set nu

echo "Hello"
echo "world"

A=$(date)

echo $A
echo $A

file_name=$0

all_param=$*

param_length=$#

param1=$1
param2=$2
param3=$3

echo $param1 $file_name
echo $param2 $all_param
echo $param3
