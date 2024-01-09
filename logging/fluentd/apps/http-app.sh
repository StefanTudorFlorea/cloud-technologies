#!/bin/sh
while true
do
    curl -X POST -d 'json={"app":"http-app"}' http://fluentd:9880/http-app.log
    sleep 1
done