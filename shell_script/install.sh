#! /bin/bash

version=$(python --version)

echo $version

test_num=5

if ((${test_num} > 3)); then
    echo "number is greater than 3"
else
    echo "number is not greater than 3"
fi

str1=abc012
str2=abcd0123

echo "${str1:1}"
echo "${str2:4}"

ver=$(python -c"import sys; print(sys.version_info.major)")

echo ">>>, ${ver}"

if ((${ver} < 3)); then
    echo "python version is low"
fi
