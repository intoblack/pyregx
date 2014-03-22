from setuptools import setup, find_packages



kw = dict(
    name='pyregx',
    version='0.0.1',
    description='python  Regular expressions tools',
    author='intoblack',
    author_email='intoblack86@gmail.com',
    url='https://github.com/intoblack/pyregx',
    download_url='https://github.com/intoblack/pyregx',
    platforms='all platform',
    packages=find_packages(),
    include_package_data=True
)

setup(**kw)