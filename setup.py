from setuptools import setup, find_packages

setup(
    name='ddd_clima',
    version='0.1.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask_sqlalchemy',
        'dynaconf',
        'jose',
        'flask-restx',
    ],
    entry_points={
        'console_scripts': [
            'ddd_clima=app:main',
        ],
    },
    include_package_data=True
)