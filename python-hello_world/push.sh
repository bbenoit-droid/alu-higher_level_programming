#!/bin/bash
read -p "name of fille" file
git add $file
read -p "enter commit sms" commit
git commit -m "$commit"
git push
