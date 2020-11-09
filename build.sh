#!/bin/bash
docker build -t pdf-to-txt \
  --build-arg USER_ID=$(id -u) \
  --build-arg GROUP_ID=$(id -g) .