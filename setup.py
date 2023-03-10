import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-monitoring',
    version='1.1.2',
    packages=['django_monitoring'],
    description='A Django application include features for better monitoring of services.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Execut3',
    author_email='execut3.binarycodes@gmail.com',
    url='https://github.com/Execut3/django-monitoring',
    license='GPT',
    install_requires=[
        'Django>=2.0',
        'djangorestframework>=3.0',
    ],
    package_data={
        'django_monitoring': ['migrations/*'],
    },
)
