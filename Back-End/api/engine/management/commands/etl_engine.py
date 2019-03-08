from django.core.management.base import BaseCommand, CommandError

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
        print('TODO')