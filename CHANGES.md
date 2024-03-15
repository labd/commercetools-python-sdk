24.3.15
--------
- Regenerate code with latest RAML specifications, bringing the SDK up to date
  again with new features released by commercetools.
- Remove ML client as sunsetted

23.6.29
--------
- Regenerate code with latest RAML specifications, bringing the SDK up to date
  again with new features released by commercetools.
- Add new SDK for the new frontend and checkout api
- Fix marshmallow deprecation warnings

22.10.25
--------
- Regenerate code with latest RAML specifications, bringing the SDK up to date
   again with new features released by commercetools
- Update logic to set the HTTP User agent

22.6.4
------
Switch to CalVer format instead of the SemVer we did earlier. Since we generate
the code based on commercetools API specs at a specific time it makes more
sense to use the date as the release instead of a custom version.


14.0.0 (2022-03-05)
-------------------
- Update the request builder pattern to match the commercetools SDK's for other languages.
  This means that the old pattern:
  ```python
  from commercetools.client import Client

  client = Client()
  product = client.products.get_by_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
  ```

  is replaced with the new pattern:
  ```python
  from commercetools.platform.client import Client

  client = Client()
  product = (
    client
    .with_project_key("<your-project-key>")
    .products()
    .with_id("00633d11-c5bb-434e-b132-73f7e130b4e3")
    .get())
  ```
  The old pattern is deprecated but will remain backwards compatible for now
- Regenerated code with latest commercetools api specs as of march 2022. This
  means that new features like the product selections api's are now available.
- Allow passing custom HTTP adapter to BaseClient (@lime-green)
- Add support for custom address fields and update actions
- Testing: Add support for `Order` imports
- Testing: fixed issues with `get_by_key` lookups in certain testing backends
- Testing: Added missing actions for Cart Discounts, Discount Codes and Extensions
- Testing: Add `datetime` and `list` updater utils
- Testing: Add `setLocalizedDescription` action for shipping_method
- Testing: Add `changeAttributeConstraint` action for product_type
- Testing: Add `setLineItemCustomField` action for cart and order
- Testing: Fix helper function to set enum fields giving an error on fields that have no value


## Notes on code generation
We moved our code generation to the code generation tool from Commercetools,
see https://github.com/commercetools/rmf-codegen

Reason for this is two-fold:
 1. We can now generate the code for the `imporapi` and the `ml` api
    specifications next to the `platform` sdk.
 2. It makes it easier for us to keep the code generation in sync with
    changes to the API specification.

The major difference is that it now also use the request builder pattern,
matching the SDK's for the other languages (e.g. TypeScript).

The package is backwards compatible for now, although deprecation warnings are
shown.

13.0.0 (2021-01-04)
-------------------
- Regenerated code. This addresses errors not being able to be parsed, so upgrading is recommended.
  - Cart:
    - CartDiscountValueGiftLineItemDraft channel variables type changed ChannelReference -> ChannelResourceIdentifier
    - CartDiscount value field type changed CartDiscountValue -> CartDiscountValueDraft
    - CustomLineItemDraft custom field type changed CustomFields -> CustomFieldsDraft
    - TaxedPriceDraft total_net and total_gross fields type changed TypedMoneyDraft -> Money
  - Common:
    - Add back fraction_digits to Money draft classes
  - Errors:
    - Many commercetools errors can now be parsed instead of throwing a ValueError
    - Fixed incorrect typing of extension response errors
  - Me:
    - Added address_key to various billing/shipping address update actions
  - Product:
    - Add limit to ProductProjectionPagedSearchResponse
    - Add ProductVariantAddedMessage
  - Store:
    - Change supply_channels from ChannelResourceIdentifier to ChannelReference
  - Subscription:
    - ResourceDeletedDeliverySchema added data_erasure
- Require requests_mock 1.8.0 or up
- Testing: Added `changeName` and `setKey` actions to CustomerGroupBackend

12.0.2 (2020-11-27)
-------------------
- Testing: Fix custom object mock interface

12.0.1 (2020-11-18)
-------------------
- Testing: Support `in` for single values, f.e. `'orderState in ("Open")'`

12.0.0 (2020-10-15)
-------------------
- Regenerate types (commercetools-api-reference 5ebb3153)
- Removed `get_by_container` and replaced by `query_by_container`: It's a query endpoint, not a get custom object endpoint.

11.0.0 (2020-09-18)
-------------------
- Regenerated types (custom objects get by id has been removed)
- Fixed query parameters not being sent:
    for example: delete's dataErasure or product price query priceCurrency where not being sent

10.0.2 (2020-09-08)
-------------------
- Testing: Predicates now support 'in' syntax

10.0.1 (2020-09-04)
-------------------
- Fix product upload_image missing product id

10.0.0 (2020-09-01)
-------------------
Note this release has some breaking changes regarding optional arguments in Commercetools types.

- Regenerate types
- Mypy fixes
- Make types stricter on when they are optional and when they are not

9.0.0 (2020-08-14)
------------------
Note this release has some breaking changes regarding imports and a lot of code is now autogenerated.

- Services are now generated by the RAML specification
- Optimize import times for faster startup by only loading necessary schemas
- Breaking: rename `commercetools.schemas.*` -> `commercetools._schema.*` since they are considered an implementation detail
- Fix incorrect schema in various nested fields
- Code generation now works with Python 3.8


8.3.0 (2020-07-21)
------------------
- Testing: backend request mock parameters were case insensitive, causing expanding to fail in some cases

8.2.0 (2020-07-20)
------------------
- Regenerate types (mainly Store distribution channels functionality)
- Store: distribution channel functionality including testing actions added

8.1.5 (2020-07-15)
------------------
- Fixed API extensions endpoints
- Testing: add product change/add price actions


8.1.4 (2020-06-11)
------------------
- Testing: use languages when creating store from draft


8.1.3 (2020-06-10)
------------------
- Testing: add setLanguages to store testing backend


8.1.2 (2020-06-09)
------------------
- Testing: Add upload_image handler for product testing service
- Throw ValueError when discriminator cannot be found


8.1.1 (2020-05-20)
------------------
- Testing: Fix publish action on mock backend; already published products got overwritten
- Testing: Automatically reset token cache when using commercetools pytest fixtures


8.1.0 (2020-05-01)
------------------
- Testing: Added product publish and set prices actions on mock backend.


8.0.0 (2020-04-28)
------------------
Regenerated Commercetools types (needed missing Discount state enums).
The 'LoggedResource' no longer exists, so a lot of types got changed,
but effectively still have the same attributes.
For safety we're doing a major release.

- Testing: add support for updating product type sets in mock server


7.0.0 (20202-04-16)
-------------------
Note this release has some breaking changes regarding optional typing. If
something is required by Commercetools it is now also required when creating an instance of
a type.

- Re-generated schemas and types
- Removed Optional type from get_by_id calls
- Correctly use Optional typing according to RAML source file
- Improved error information in CommercetoolsError object
- Testing: Add setAttribute and addVariant actions to product testing backend
- Testing: Add addAttributeDefinition action to testing backend
- Testing: Add addPayment action to order testing backend
- Testing: Check for unique values in testing backend
- Testing: Fixed Attribute return object in ProductTypes testing backend


6.2.1 (2020-03-24)
------------------
- Fix marshallow breaking on missing **kwargs argument (#76)


6.2.0 (2020-03-08)
------------------
- Fix Query Predicate chaining (#75)
- Update dependencies so that code generation works with Python 3.8
- Update GitHub Actions integration


6.1.0 (2020-01-13)
------------------
- Added nested query predicate support (#72)


6.0.0 (2020-01-13)
------------------
 - Allow passing in the base auth URL when creating a Client
 - Add multiple DELETE endpoints for various backends
 - Implement mocked actions for Orders mock backend
 - Fix mock backend not properly support '<>' operator
 - Add in operator in queries (#73)
 - Fix cart replicate function (#74)


5.0.0 (2019-11-05)
------------------
This is breaking change since the commercetools api specification is moving
from the `Money` type to the `TypedMoney` type. You should generally be able to
replace references to `Money` with `CentPrecisionMoney`.

 - Sync with latest API definitions (dd371e12506af969b8edfeb1540eec1e8cd5ab9d)
 - Updated to work with marshmallow > 3.0.0
 - Implement set custom field for tests (note custom type checks are not implemented)


4.1.0 (2019-08-14)
------------------
- Fix Inventory Entry types *This may break Inventory related types*
- Add external_oauth field on project
- Small runserver fixes
- Mock ShippingMethod.setPredicate
- Mock State.setTransitions


4.0.0 (2019-07-04)
------------------
- *Breaking* Generate with new API definitions, main difference is Reference -> ResourceIdentifier type.


3.9.0 (2019-06-27)
------------------
- Implement testing/introspect token endpoint, thanks to @mbarga!


3.8.1 (2019-06-26)
------------------
- Small fixes if data was not initialized for mock shipping methods actions


3.8.0 (2019-06-26)
------------------
- Implement AddZone and RemoveZone actions for shipping methods


3.7.0 (2019-06-18)
------------------
- Added discount codes
- Added cart discounts


3.6.1 (2019-06-18)
------------------
- Fix small bug in reference expansion if value is None


3.6.0 (2019-06-17)
------------------
- Generate with new API definitions, biggest changes are Resource -> BaseResource and ResourceSchema -> BaseResourceSchema
- Add resource expansion to all applicable objects, see https://docs.commercetools.com/http-api#reference-expansion for details.


3.5.1 (2019-05-27)
------------------
- Remove WIP code on carts get_by_id call


3.5.0 (2019-05-23)
------------------
- Generate with new API definitions
- Add missing 'store' field to Order


3.4.0 (2019-05-21)
------------------
- Fix rating number type not being an integer for Review related types


3.3.0 (2019-05-20)
------------------
- Add State service


3.2.0 (2019-05-08)
------------------
- Add Store service


3.1.1 (2019-04-26)
------------------
- Fix test server not working inside docker by binding to 0.0.0.0 instead of localhost


3.1.0 (2019-04-26)
------------------
- Implement testing shipping method actions


3.0.0 (2019-04-25)
------------------
 - Add Api clients service
 - Testing server now autoreloads on python changes (using Werkzeug)
 - Regenerate types from commercetools-api-reference (fixes typos, some new fields, adds extension response errors)
 - Add X-Correlation-ID to exception class
 - Mock X-Correlation-ID header in testing framework


2.5.2 (2019-04-17)
------------------
 - Implement testing predicates gte and lte
 - Implement inventory testing actions


2.5.1 (2019-04-15)
------------------
 - Implement testing actions 'changeLabel' and 'changeLocalizedEnumValueLabel' for product type


2.5.0 (2019-04-08)
------------------
 - Generate the code normally created by the attrs package to improve the
   import time with 30%. Attrs is now also no longer a dependency
 - Add py.typed placeholder file (PEP561)
 - Add support for the ShoppingList service endpoint (including mock interface)
 - Add support for the Reviews endpoint (including mock interface)


2.4.2 (2019-03-18)
------------------
- Tax rates ids are now correctly generated


2.4.1 (2019-02-21)
------------------
- Fix cart create function using incorrect schema
- Add update actions to carts testing backend
- Add update actions to orders testing backend
- Regenerate code based on new commercetools-api-reference definition


2.4.0 (2019-02-13)
------------------
 - Refactor the code generation module to split the types.py and schemas.py file
   into multile submodules. This should be fully backwards compatible and from
   the API perspective nothing should be changed, but it makes the generated
   code more maintanable since we no longer have files with 40k lines.
 - Use timezone aware timestamps in the mocking interface
 - Rewrite the Paginator class. This is a backwards incompatible change but it
   makes the API much cleaner. It now also supports slicing etc.
 - Add a CursorPaginator class, which uses filtering instead of offsets for
   pagination.


2.3.0 (2019-01-28)
------------------
- Money -> TypedMoney conversion not setting default to CENT_PRECISION
- Improve testing interface to only raise conflict error when the data is
  actually changed


2.2.0 (2019-01-24)
------------------
 - Tax related fields now parse rate as float instead of always being 0
 - Support generating code for Python 3.7 and higher
 - Add limited testing service for orders


2.1.0 (2019-01-23)
------------------
 - Add `commercetools.predicate.QueryPredicate()` which can be used to construct
   query predicate strings using Python code.
 - Fix commercetools mock server


2.0.0 (2019-01-20)
------------------
 - When creating the client the token url should now be a complete URL. When
   using environment variables it will automatically append /oauth/token if the
   url has no path specified. See #27
 - Add a changelog :-)
 - Add support for the product discounts api endpoints


1.5.0 (2018-12-11)
------------------
 - Add ability to run the mock server standalone using:
    `python -m commercetools.testing.server`
 - Add paginator class
 - Add support for delete operations in the mock services
 - Support oauth2 authentication via basic auth and querystring in the mock
   service
 - Properly support predicate filtering in the mock endpoints using a custom
   query parser.


1.4.0 (2018-11-16)
------------------
 - Add HTTP retry logic for status codes 502, 503, 504 (retry 3 times).
 - Add Client.products.upload_image() endpoint
 - Add Inventory endpoints


1.3.0 (2018-11-05)
------------------
 - Add documentation via read the docs


1.2.0 (2018-11-03)
------------------
 - Add support for custom objects (including mock endpoints)
 - Fix handling of discriminator fields


1.1.0 (2018-11-02)
------------------
 - Add support for channels endpoint
 - Fix packaging issues
 - Workaround a bug in marshmallow_enum ini combination with many=True

1.0.0 (2018-11-02)
------------------
This is the initial opensource release of the Commercetools Python SDK.

 - Add travis support in combination with tox
 - Properly support passing list and scalar values to where, sort and expand


0.6.0 (2018-10-26)
------------------
 - Fix project projections mock service
 - Store product type in the product mock service


0.5.1 (2018-10-25)
------------------
 - No longer require full token url, instead append /oauth/token automatically


0.5.0 (2018-10-24)
------------------
 - Sync with latest commercetools api reference
 - Update product projections mock endpoint to use same products as product
   mock endpoint.
 - Update payment and transaction endpoints
 - Add ability to run the mock server standalone using:
    `python -m commercetools.testing.server`


0.4.1 (2018-10-19)
------------------
 - Add mock endpoint for product projections


0.4.0 (2018-10-11)
------------------
 - Add support for expand parameter in product projections endpoint
 - Add support for product types
 - Sync with latest commercetools api reference


0.3.1 (2018-10-09)
------------------
 - Use the cached oauth2 token if present


0.3.0 (2018-10-09)
------------------
 - Implement ability to customize the oauth2 token saver and implement a proper
   default mechanism which uses threading.local()


0.2.0 (2018-10-05)
------------------
 - Add categories mock endpoint for testing
 - Update product and category unittests


0.1.0 (2018-10-02)
------------------
Initial release of a code generated Python SDK.
