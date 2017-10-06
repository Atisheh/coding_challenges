# Management Command Model to Dict

## Task - Django Live-Test

Create a new Django-App, containing only one Model. Define an IntegerField, a BooleanField
and a CharField on this model.

Your Task is to write a management command model_to_json. It should take one command line
parameter which is the name of a Model class.

The command should compute a list of dictionaries, each dictionary should contain the Model
field names as keys and their values as values for one instance of the specified model in your
database. The result should be returned as JSON.

This command should work for other Model classes too. Add some instances of the Model and
test your command.

## Comments

(ignore the naming of the project and variables, please :D )
- setup:
  - create a postgres db called 't_3ym' or use an existing one and change the name in the settings
  - install requirements
  - run migrations
- using the management command:
  - python manage.py model_json One
- currently the json is printed twice, once with stdout and once with pprint (pp just looks way better!)
