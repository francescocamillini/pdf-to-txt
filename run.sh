#!/bin/bash
 docker run -it --rm -v $PWD/$1:/workspace/input -v $PWD/$2:/workspace/output pdf-to-txt