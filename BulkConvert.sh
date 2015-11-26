#!/bin/sh
#Using Calibre Command line utilities for the command ebook-convert
#Raw files (epub or pdf) are distributed into the respective folders named: 'epub' and 'pdf'

for book in /Users/srayanguhathakurta/Dropbox/Apps/novels/epub/*
do
        echo "Converting $book";
        ebook-convert "$book" "$(basename "$book" .epub).mobi";
done


for book in /Users/srayanguhathakurta/Dropbox/Apps/novels/pdf/*
do
        echo "Converting $book";
        ebook-convert "$book" "$(basename "$book" .pdf).mobi";
done
