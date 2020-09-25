#!/bin/bash

# Build and push the image for the application stated.
usage()
{
  echo "#####################"
  echo "# build.sh #"
  echo "#####################"
  echo "Build and push a docker image. Run this script from the same directory "
  echo "containing the Dockerfile.  The script will set the image name to the "
  echo "name of the current directory containing the Dockerfile."

}

if [[ ! -f "Dockerfile" ]]; then
  echo "Couldn't find a Dockerfile in the current directory"
  echo
  usage
  exit
fi

TAGNAME=${PWD##*/}
GITHASH=`git rev-parse HEAD`

echo "Building image for $TAGNAME"
docker build -t shaggydog/$TAGNAME:$GITHASH \
             -t shaggydog/$TAGNAME:latest \
             .
docker push shaggydog/$TAGNAME