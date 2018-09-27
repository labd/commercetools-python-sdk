# Python SDK for Commercetools

[![Travis Build Status](https://travis-ci.org/labd/commercetools-python-sdk.svg?branch=master)](https://travis-ci.org/labd/commercetools-python-sdk)
[![codecov](https://codecov.io/gh/LabD/commercetools-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/LabD/commercetools-python-sdk)

This is an unofficial Python SDK for the Commercetools platform. It only
supports Python 3.6+ and uses type annotation for an improved development
experience.

The API is mostly generated using the commercetools api RAML file and uses the
attr library for the dataobjects and marshmallow for the serialization and
deserialization steps. 


# Example

```python

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
```
