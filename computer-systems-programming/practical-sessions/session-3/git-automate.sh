#!/bin/bash

# Directory to watch
WATCHED_DIR="/Users/ysmagulov/Documents/Growthhungry Academy/gh-academy-practice/"

# Function to commit local git changes
commit_to_github() {
    cd "$WATCHED_DIR" || exit
    git add .
    git commit -m "Automated bash script - add new files."
}

# Function to push new files to GitHub
push_to_github() {
    git push
}

# Watch for new files and push them to GitHub
if [[ -n $(git status --porcelain) ]]; then
    echo "New file detected"
    commit_to_github
    push_to_github
fi