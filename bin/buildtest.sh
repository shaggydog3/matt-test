#!/bin/bash

# Build and push the test harness, then deploy it.

usage()
{
  echo "#####################"
  echo "# buildtest.sh #"
  echo "#####################"
  echo "Build and push a the test framework docker image. Run this script from "
  echo "the repository root."
  echo "After building and pushing the image, the script will start the "
  echo "kubernetes deployment using this image."
}

if [[ ! -f "matttest/Dockerfile" ]]; then
  echo "Couldn't find the test dockerfile."
  echo
  usage
  exit
fi

TAGNAME=matttest
GITHASH=`git rev-parse HEAD`

echo "Building image for $TAGNAME"
docker build -f matttest/Dockerfile \
             -t shaggydog/$TAGNAME:$GITHASH \
             -t shaggydog/$TAGNAME:latest \
             .
docker push shaggydog/$TAGNAME

# the following  is included just for testing the setup of the Dockerfile:
docker run -it shaggydog/matttest:latest