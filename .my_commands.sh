#!/bin/bash

function yourcustomcommand() {
    cd
    source .env
    python autopush.py $1
    cd $PATH$1
    git init
    git remote add origin git@github.com:$MYUNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}
