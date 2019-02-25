.. start-no-pypi
.. image:: https://dev.azure.com/lab-digital/commercetools-python-sdk/_apis/build/status/labd.commercetools-python-sdk?branchName=master
    :target: https://dev.azure.com/lab-digital/commercetools-python-sdk/_build?definitionId=3

.. image:: http://codecov.io/github/labd/commercetools-python-sdk/coverage.svg?branch=master
    :target: http://codecov.io/github/labd/commercetools-python-sdk?branch=master

.. image:: https://img.shields.io/pypi/v/commercetools.svg
    :target: https://pypi.python.org/pypi/commercetools/
.. image:: https://readthedocs.org/projects/commercetools-python-sdk/badge/?version=latest
    :target: https://commercetools-python-sdk.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. end-no-pypi


Python SDK for Commercetools
============================

This is an unofficial Python SDK for the Commercetools platform. It only
supports Python 3.6+ and uses type annotation for an improved development
experience.

The API is mostly generated using the commercetools api RAML file and uses the
attr library for the dataobjects and marshmallow for the serialization and
deserialization steps.

Installation
------------

    pip install commercetools

Example
-------

.. code-block:: python

    from commercetools import Client

    client = Client(
        project_key="<your-project-key>",
        client_id="<your-client-id>",
        client_secret="<your-client-secret>",
        scope=["<scopes>"],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

    product = client.products.get_by_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
    print(product)


The client can also be configured by setting the following environment
variables:

.. code-block:: sh

    export CTP_PROJECT_KEY="<project key>"
    export CTP_CLIENT_SECRET="<client secret>"
    export CTP_CLIENT_ID="<client id>"
    export CTP_AUTH_URL="https://auth.sphere.io"
    export CTP_API_URL="https://api.sphere.io"
    export CTP_SCOPES="<comma seperated list of scopes>"

And then constructing a client without arguments:

.. code-block:: python

    from commercetools import Client

    client = Client()

    product = client.products.get_by_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
    print(product)
