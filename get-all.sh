#!/usr/bin/env bash

for f in $(cat allfiles)
do
    wget -c http://text.b0.upaiyun.com/$f!1242x2208
done
