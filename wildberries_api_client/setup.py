# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "wildberries_api_client"
VERSION = "0.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="API Wildberries",
    author_email="letby",
    url="https://openapi.wildberries.ru",
    keywords=["Swagger", "Wildberries"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)

