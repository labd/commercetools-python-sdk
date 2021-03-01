.. start-no-pypi

.. image:: https://github.com/labd/commercetools-python-sdk/workflows/Python%20Tests/badge.svg
    :target: https://github.com/labd/commercetools-python-sdk/actions

.. image:: http://codecov.io/github/labd/commercetools-python-sdk/coverage.svg?branch=main
    :target: http://codecov.io/github/labd/commercetools-python-sdk?branch=main

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

The API is generated using the commercetools api RAML file and uses
marshmallow for the serialization and deserialization.

Installation
------------

    pip install commercetools

Example
-------

.. code-block:: python

    from commercetools.platform import Client

    client = Client(
        client_id="<your-client-id>",
        client_secret="<your-client-secret>",
        scope=["<scopes>"],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io",
    )

    product = (
        client
        .with_project_key("<your-project-key>")
        .products()
        .with_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
        .get())
    print(product)

The client can also be configured by setting the following environment
variables:

.. code-block:: sh

    export CTP_CLIENT_SECRET="<client secret>"
    export CTP_CLIENT_ID="<client id>"
    export CTP_AUTH_URL="https://auth.sphere.io"
    export CTP_API_URL="https://api.sphere.io"
    export CTP_SCOPES="<comma seperated list of scopes>"

And then constructing a client without arguments:

.. code-block:: python

    from commercetools.platform import Client

    client = Client()

    product = (
        client
        .with_project_key("<your-project-key>")
        .products()
        .with_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
        .get())

    print(product)


Releasing
---------

To release this package first (pip) install bump2version and update the
CHANGES file. Then update the version (either major/minor/patch depending on
the change)


.. code-block:: sh

    bumpversion --tag <major,minor,patch>

bumpversion is naive because it string replaces, so do a sanity check it
didn't accidentally update a Pypi dependency. If not, push the code:


.. code-block:: sh

    git push --follow-tags

We use GitHub actions so make sure the build succeeds and then go to the tags
tab (https://github.com/labd/commercetools-python-sdk/tags).

Click the dots to trigger a release action. Copy the changelog items in the
release description and enter the release version. This will upload the
release to PyPi.

