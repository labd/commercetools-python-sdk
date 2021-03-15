import re

from setuptools import find_packages, setup

install_requires = [
    "requests>=2.7.0",
    "pytz",
    "requests-oauthlib>=1.0.0",
    "requests_mock>=1.8.0",
    "marshmallow>=3.10.0",
    "marshmallow-enum>=1.5.1",
    "WebOb>=1.8.0",
    "Werkzeug>=0.15.2",
    "wrapt>=1.10.0",
]

docs_require = [
    "Sphinx>=1.8.1",
    "sphinx-rtd-theme==0.4.2",
    "sphinx-autodoc-typehints==1.6.0",
]

tests_require = [
    "freezegun==1.0.0",
    "mock==4.0.3",
    "pretend==1.0.9",
    "coverage[toml]>=5.3",
    "pytest-cov==2.10.1",
    "pytest==6.2.1",
    # Linting
    "isort==5.6.4",
    "flake8==3.8.4",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==1.4.0",
    "flake8-imports==0.1.1",
    "mypy==0.790",
]


with open("README.rst") as fh:
    long_description = re.sub(
        "^.. start-no-pypi.*^.. end-no-pypi", "", fh.read(), flags=re.M | re.S
    )

setup(
    name="commercetools",
    version="14.0.0b3",
    description="SDK for Commercetools",
    long_description=long_description,
    author="Lab Digital B.V.",
    author_email="opensource@labdigital.nl",
    url="https://github.com/labd/commercetools-python-sdk",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "docs": docs_require,
        "test": tests_require,
    },
    entry_points={},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
