import re
import sys

from setuptools import find_packages, setup

install_requires = [
    "requests>=2.7.0",
    "pytz",
    "requests-oauthlib>=1.0.0",
    "attrs>=18.2.0",
    "marshmallow==3.0.0b13",
]

docs_require = ["sphinx>=1.4.0"]

tests_require = [
    "freezegun==0.3.8",
    "mock==2.0.0",
    "pretend==1.0.8",
    "pytest-cov==2.5.1",
    "pytest==3.1.3",
    "requests_mock>=0.7.0",
    # Linting
    "isort==4.2.15",
    "flake8==3.3.0",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==1.4.0",
    "flake8-imports==0.1.1",
]


with open("README.rst") as fh:
    long_description = re.sub(
        "^.. start-no-pypi.*^.. end-no-pypi", "", fh.read(), flags=re.M | re.S
    )

setup(
    name="commercetools-python-sdk",
    version="0.0.1",
    description="SDK for Commercetools",
    long_description=long_description,
    author="Lab Digital B.V.",
    author_email="opensource@labdigital.nl",
    url="https://github.co/labd/commercetools-python-sdk",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"docs": docs_require, "test": tests_require},
    entry_points={},
    package_dir={"": "src"},
    packages=["commercetools"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
