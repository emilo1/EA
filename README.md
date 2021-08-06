# Flask_Boilerplate_Heroku_Template

## Managing Your Pipfile/Pipfile.lock Files

1. In your terminal, run `pip install pipenv`
2. Navigate to the root directory of this project
3. In your terminal, run `pipenv install`, which will automatically create a Pipfile and a Pipfile.lock
4. Then, for all other Python modules that are needed to run your software application, you will need to run `pipenv install name-of-module`

## Managing Your Requirements.txt File

* You will most likely want to use additional Python libraries to build your website. For example, you may want to import pandas or import sqlalchemy, in which case, you'll also need to list specific version numbers of those libraries in the `requirements.txt` file. To view the version numbers of each of the python libraries that are installed on your machine, simply open your terminal/gitbash and type the command `pip list`. This shows all downloaded libraries, so you'll need to copy/paste into the `requirements.txt` only the libraries needed to run your project's website.

