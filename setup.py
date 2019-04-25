import re

from setuptools import find_packages, setup

install_requires = [
    "requests>=2.7.0",
    "pytz",
    "requests-oauthlib>=1.0.0",
    "requests_mock>=0.7.0",
    "marshmallow>=3.0.0b17",
    "marshmallow-enum>=1.4.1",
    "WebOb>=1.8.0",
    "Werkzeug>=0.15.2",
    "wrapt>=1.10.0",
]

codegen_requires = [
    "astunparse==1.6.2",
    "attrs>=18.2.0",
    "black==18.9b0",
    "isort",
    "PyYAML==3.13",
]

docs_require = [
    "Sphinx>=1.8.1",
    "sphinx-rtd-theme==0.4.2",
    "sphinx-autodoc-typehints==1.6.0",
]

tests_require = [
    "freezegun==0.3.8",
    "mock==2.0.0",
    "pretend==1.0.8",
    "pytest-cov==2.5.1",
    "pytest==3.1.3",
    # Linting
    "isort==4.2.15",
    "flake8==3.3.0",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==1.4.0",
    "flake8-imports==0.1.1",
    "mypy==0.700",
]


with open("README.rst") as fh:
    long_description = re.sub(
        "^.. start-no-pypi.*^.. end-no-pypi", "", fh.read(), flags=re.M | re.S
    )

setup(
    name="commercetools",
    version="3.0.0",
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
        "codegen": codegen_requires,
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
