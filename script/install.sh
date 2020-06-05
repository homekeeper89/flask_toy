#! /bin/bash

ver=$(python -c"import sys; print(sys.version_info.major)")

echo "python version : ${ver}"

if ((${ver} < 3)); then
    echo "python version is low"
    echo "changing python version over 3"
    echo $(pyenv 3.7.7)
fi

echo "Set python Env"

$(poetry init)
