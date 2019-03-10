#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.conf import settings

from django.core.management.base import BaseCommand, CommandError
from engine.models import File, Word

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
FOLDER = 'Data'
PATH = os.path.join(settings.BASE_DIR, FOLDER)


class Command(BaseCommand):
    help = '''                 ETL 
            -------------------------------------------------
            Extract, Transform, Load (ETL) is the general 
            procedure of copying data from one or more sources 
            into a destination system which represents the data differently from the source(s).
           Steps:
            1. Get all files from a confident resource.
            2. Access and extract all the words from those files.
            3. Transform/Clean all the words and insert into the DB!
           '''

    def handle(self, *args, **options):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(PATH):
            for file in f:
                file_path = self.get_file_path(r, file)
                self.open_file(file_path)

    def get_file_path(self, root, file):
        return os.path.join(root, file)

    def get_file_name(self, path):
        return os.path.basename(path)

    def open_file(self, path):
        # File properties
        lines=0
        words=0
        total_words=0
        characters=0

        # Word Properties
        words_to_insert = []

        with open(path, 'r') as all_text:
            for l in all_text:
                # Get file props.
                words=l.split()
                lines+=1
                total_words+=len(words)

                
                for i in words:
                    # Get Words in-line
                    words_to_insert.append((i, lines))
                    # Get all characters per word
                    characters+=len(i)

        print('Loading...\n')
        _file = self.perform_insert_file(path, self.get_file_name(path), characters, lines)
        self.perform_insert_words(_file, words_to_insert)

        print('---- File: {} ---- \n'.format(self.get_file_name(path)))
        print('Total lines: {}'.format(lines))
        print('Total Words: {}'.format(total_words))
        print('Total Characters: {}'.format(characters))
        print('--------------------------------- \n')
                
                
    def perform_insert_file(self, path, name, characters, lines):
        return File.objects.create(path=path, name=name, nchars=characters, nlines=lines)

    def perform_insert_words(self, file, words):
        entity_words = [Word(value=word[0], line=word[1], file=file) for word in words]
        # Bulk Creation in order to improve the insert perform
        # https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create

        Word.objects.bulk_create(entity_words)
            