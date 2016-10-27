try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pyfix',
    'author': 'Tom Fewster',
    'url': 'https://github.com/wannabegeek/PyFIX/',
    'download_url': 'https://github.com/wannabegeek/PyFIX/',
    'author_email': 'tom@wanabegeek.com.',
    'version': '0.1',
    'install_requires': ['aenum'],
    'packages': ['pyfix', 'pyfix/FIX44', 'pyfix/FIXT11'],
    'scripts': [],
    'name': 'pyfix'
}

setup(**config)
