from setuptools import setup


setup(
    name='snow-jinja-lint',
    description='a pre-commit hook for formatting sql',
    version='0.0.1',
    install_requires=[
        'jinja2'
    ],
)