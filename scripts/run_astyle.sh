#!/bin/sh
find $PENGUDOG_PATH -type f -name '*.[ch]' | xargs astyle --options=$PENGUDOG_PATH/scripts/format.astyle

