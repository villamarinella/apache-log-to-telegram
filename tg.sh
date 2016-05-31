#!/bin/bash

## here your recipient name
to=Klaus_Werner
## here ist the telegram binary located
cd /root/tg/bin

function show_usage {
        echo "Usage $0 [message]"
        exit
}

if [ $# -lt 1 ]
then
  show_usage
fi

(echo "contact_list";sleep 5;echo "msg $to $1"; echo "safe_quit") | ./telegram-cli

cd 
cd tg
