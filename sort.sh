grep '10.1.192.38' log.txt | sed 's/^.*sid=\///;s/\/&type.*//' | sort

