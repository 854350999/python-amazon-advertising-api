
from setuptools import setup, find_packages


setup(
    name="python-amazon-advertising-api",
    version="0.7.6",
    install_requires=[
        "requests"
    ],
    packages=find_packages(),
    url="https://github.com/854350999/python-amazon-advertising-api",
    license="MIT",
    author="WT",
    author_email="854350999@qq.com",
    description="Python wrapper for the Amazon Advertising API",
    long_description="Python wrapper for the Amazon Advertising API",
    include_package_data=True,
    zip_safe=False,
)

