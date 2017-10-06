from django.core.management.base import BaseCommand
from django.apps import apps
from django.core import serializers
import pprint
import json

class Command(BaseCommand):
    help = 'Model to JSON'

    def add_arguments(self, parser):
        parser.add_argument('modelname', nargs=1, type=str, help='give the name of a db model')

    def handle(self, *args, **options):
        try:
            # get model by string
            model_class = apps.get_model(app_label='t_3ym', model_name=options['modelname'][0])
            # get all instances for the model
            model_qs = model_class.objects.all()
            # django serializer to change queryset format
            model_json = json.loads(serializers.serialize("json", model_qs))
            json_dict = []
            for item in model_json:
                json_dict.append(item['fields'])

            # pp looks way better than the stdout
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(json_dict)

            # style for colored output
            self.stdout.write(self.style.SUCCESS(json_dict))
            #self.stdout.write(fun)

        except LookupError:
            self.stdout.write(self.style.SUCCESS('no model with name {}'.format(options['modelname'][0])))
