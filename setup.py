from setuptools import setup, find_packages

requirements = [
    'pandas',
    'python-docx'
]

setup(
    name='itgelt-html-docx-parser',
    version='0.0.1',
    description='HTML file to DOCX',
    packages=find_packages("docx", "html", "itgelt"),
    install_requires=requirements
)
