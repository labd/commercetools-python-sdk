.. start-no-pypi

.. image:: https://github.com/labd/commercetools-python-sdk/workflows/Python%20Tests/badge.svg
    :target: https://github.com/labd/commercetools-python-sdk/actions

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
        token_url="https://auth.sphere.io",
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


Releasing
---------

To release this package first (pip) install bump2version and update the CHANGES file.
Then update the version (either major/minor/patch depending on the change)


.. code-block:: sh

    bumpversion --tag <major,minor,patch>

bumpversion is naive because it string replaces, so do a sanity check it didn't
accidentally update a Pypi dependency. If not, push the code:


.. code-block:: sh

    git push --follow-tags

We use GitHub actions so make sure the build succeeds and then go to the release tab.
GitHub will already have created a release for the tag, but ignore that for now and
draft a new release and enter the tag which you created.

Copy the changelog items in in the release description and save. This will then 
automatically trigger a GitHub action to create and upload the package to PyPi.

Then go to Azure Pipelines and wait for the build to create an artifact.
Once the build succeeded go to Releases and create a release with the correct artifact.
This will release the package to Pypi.

