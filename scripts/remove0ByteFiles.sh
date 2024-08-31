#!/bin/sh

echo "Moving 0 byte files due to bug in sortphotos..."
mkdir ../emptyfiles/
find ../SortTest_sort/ -size 0 -exec mv '{}' ../emptyfiles/ \;

echo "Executing photo backup..."
#python ~/photos/sortphotos/src/sortphotos.py --recursive --sort %Y/%m ~/sync/ ~/photos/sorted/

echo "Done!"