#!/bin/bash

# Replace text e.g pytemplates with a user's desired text. 

echo "Replacing" "$1" with "$2" in "$3" 

sed -i "s/$1/$2/g" "$3"

echo "All done, happy building!"