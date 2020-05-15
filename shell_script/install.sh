#! /bin/bash

version=$(python --version)

echo $version

test_num=5

if ((${test_num} > 3)); then
    echo "number is greater than 3"
else
    echo "number is not greater than 3"
fi
