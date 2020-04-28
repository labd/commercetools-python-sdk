# Codegen

The code in this directory is responsible for generating the types and schema
files for the commercetools Python SDK. It is currently completed custom
implemented since there are no working RAML 1.0 Python parsers.

## How-to

In order to generate code:

- clone https://github.com/commercetools/commercetools-api-reference as a sibling of this repository
- run `make generate` at this repositories root level
