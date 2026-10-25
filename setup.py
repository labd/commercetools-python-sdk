import re

from setuptools import find_packages, setup

install_requires = [
    "requests>=2.7.0",
    "pytz",
    "requests-oauthlib>=1.0.0",
    "requests_mock>=1.8.0",
    # marshmallow 4 removed APIs the generated schemas use
    "marshmallow>=3.10.0,<4",
    "marshmallow-enum>=1.5.1",
    "WebOb>=1.8.0",
    "Werkzeug>=0.15.2",
    "wrapt>=1.10.0",
]

docs_require = [
    "Sphinx==7.0.1",
    "sphinx-autodoc-typehints==1.23.3",
    "m2r2==0.3.1",
]

tests_require = [
    "freezegun==1.5.5",
    "mock==4.0.3",
    "pretend==1.0.9",
    "coverage[toml]>=6.2",
    "pytest-cov==7.1.0",
    "pytest==9.0.3",
    # Linting
    "ruff==0.17.2",
    "mypy==1.9.0",
]


with open("README.rst") as fh:
    long_description = re.sub(
        "^.. start-no-pypi.*^.. end-no-pypi", "", fh.read(), flags=re.M | re.S
    )

setup(
    name="commercetools",
    version="2026.10.12",
    description="SDK for Commercetools",
    long_description=long_description,
    author="Lab Digital B.V.",
    author_email="opensource@labdigital.nl",
    url="https://github.com/labd/commercetools-python-sdk",
    python_requires=">=3.11",
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
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
