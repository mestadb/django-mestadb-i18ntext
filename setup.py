import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-i18ntext',
    version = '0.1.0',
    packages = ['i18ntext'],
    license = 'MIT License', # example license
    description = 'Multilingual texts for Django apps.',
    long_description = README,
    url = 'https://github.com/mestadb/django-i18ntext',
    author = 'Aapo Rista',
    author_email = 'aapris@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data = True,
    package_data = {
        "i18ntext": [
            "templatetags/*.py",
#            "templates/*.html",
#            "locale/*/LC_MESSAGES/*.po",
#            "locale/*/LC_MESSAGES/*.mo",
#            "static/js/*",
#            "static/css/*.css",
#            "static/img/*"
        ],
    },
    zip_safe=False,
    install_requires=['django>1.4,<1.6',
                      'django-modeltranslation',
                     ],
)
