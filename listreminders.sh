#!/bin/bash
#DATADIR="/home/antonio/Dropbox/Apps/My Notes in Gear/MyNotes"
DATADIR=$(cat ~/.remindme/config.ini | grep datadir | cut -d= -f 2)
cd "$DATADIR"
msg=""
for i in *;do

    grep 'note_Istimeactive": true' $i > /dev/null
    if [ $? -eq 0 ];then

        title=$(grep note_Title $i | tr -d \" | tr -d , | cut -d: -f 2)
        #echo "Sí: $title - $i"
        msg="$title:$msg"
    fi
done
echo $msg
#grep  note_Title * |
#$(grep -i 'timeactive": true'| cut -d: -f 1)
