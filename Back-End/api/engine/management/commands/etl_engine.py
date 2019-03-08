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

    def add_arguments(self, parser):
        pass
        # parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # r=root, d=directories, f = files
        cont = 0
        for r, d, f in os.walk(PATH):
            for file in f:
                file_path = self.get_file_path(r, file)
                if cont == 0:
                    self.open_file(file_path)
                    cont += cont + 1
    def get_file_path(self, root, file):

        return os.path.join(root, file)

    def open_file(self, path):
        lines=0
        words=0
        total_words=0
        characters=0
        with open(path, 'r') as all_text:
            for l in all_text:
                words=l.split()
                lines+=1
                total_words+=len(words)
                for i in words:
                    characters+=len(i)
        print('Total lines: {}'.format(lines))
        print('Total Words: {}'.format(total_words))
        print('Total Characters: {}'.format(characters))
                