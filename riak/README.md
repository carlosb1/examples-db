docker pull lapax/riak
docker run -d -t -i \
    -h "riak1" \
    -v /path/to/local/directory:/var/lib/riak \
     -name "riak1" \
     "lapax/riak"

or 
docker run -d -t -i lapax/riak

