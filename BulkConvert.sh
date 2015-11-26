#!/bin/sh
#Using Calibre Command line utilities for the command ebook-convert
#Raw files (epub or pdf) are distributed into the respective folders named: 'epub' and 'pdf'

epubPATH=/path/to/epub/*
pdfPATH=/path/to/pdf/*
for book in $epubPATH
do
        echo "Converting $book";
        ebook-convert "$book" "$(basename "$book" .epub).mobi";
done


for book in $pdfPATH
do
        echo "Converting $book";
        ebook-convert "$book" "$(basename "$book" .pdf).mobi";
done
