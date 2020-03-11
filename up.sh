#!/bin/sh

if [ ! -d "$1" ]; then
  echo "no directory"
  return
fi

cp -R server/*.* $1/
cp -R models $1/
cp Dockerfile $1/

pwd=$(pwd)
port=4441

while read line; do
port=$((line+1))
done < port

echo $port > port

cd $1

docker build --build-arg wd=/home/$1 -t $1 .
docker run -dit -p $port:4443 --name $1 -v $pwd/$1:/home/$1 $1

echo "server running at port ${port}"
