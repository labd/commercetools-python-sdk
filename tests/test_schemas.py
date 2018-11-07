from commercetools import schemas, types


def test_extension_input_schema():
    data = {
        "action": "Create",
        "resource": {
            "typeId": "order",
            "id": "dea60382-cca5-4e29-93d7-bf2bb6615501",
            "obj": {
                "type": "Order",
                "id": "dea60382-cca5-4e29-93d7-bf2bb6615501",
                "version": 1,
                "lastMessageSequenceNumber": 1,
                "createdAt": "2018-11-03T07:35:07.622Z",
                "lastModifiedAt": "2018-11-03T07:35:07.622Z",
                "customerId": "e6938b64-0721-42dc-9cc5-82ddbd43dbf2",
                "customerEmail": "m.vantellingen@labdigital.nl",
                "totalPrice": {
                    "type": "centPrecision",
                    "currencyCode": "EUR",
                    "centAmount": 10500,
                    "fractionDigits": 2,
                },
                "taxedPrice": {
                    "totalNet": {
                        "type": "centPrecision",
                        "currencyCode": "EUR",
                        "centAmount": 8677,
                        "fractionDigits": 2,
                    },
                    "totalGross": {
                        "type": "centPrecision",
                        "currencyCode": "EUR",
                        "centAmount": 10500,
                        "fractionDigits": 2,
                    },
                    "taxPortions": [
                        {
                            "rate": 0.21,
                            "amount": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 1823,
                                "fractionDigits": 2,
                            },
                            "name": "TEMP",
                        }
                    ],
                },
                "orderState": "Open",
                "syncInfo": [],
                "returnInfo": [],
                "shippingInfo": {
                    "shippingMethodName": "TEMP",
                    "price": {
                        "type": "centPrecision",
                        "currencyCode": "EUR",
                        "centAmount": 500,
                        "fractionDigits": 2,
                    },
                    "shippingRate": {
                        "price": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 500,
                            "fractionDigits": 2,
                        },
                        "tiers": [],
                    },
                    "taxRate": {
                        "name": "TEMP",
                        "amount": 0.21,
                        "includedInPrice": True,
                        "country": "NL",
                        "id": "viljsTSo",
                        "subRates": [],
                    },
                    "taxCategory": {
                        "typeId": "tax-category",
                        "id": "e589180a-8096-4ef5-afd1-550a3ead1d1d",
                    },
                    "deliveries": [],
                    "shippingMethod": {
                        "typeId": "shipping-method",
                        "id": "09b99a41-17f6-4e8d-9812-8790a4b6acd3",
                    },
                    "taxedPrice": {
                        "totalNet": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 413,
                            "fractionDigits": 2,
                        },
                        "totalGross": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 500,
                            "fractionDigits": 2,
                        },
                    },
                    "shippingMethodState": "MatchesCart",
                },
                "taxMode": "Platform",
                "inventoryMode": "None",
                "taxRoundingMode": "HalfEven",
                "taxCalculationMode": "LineItemLevel",
                "origin": "Merchant",
                "lineItems": [],
                "customLineItems": [
                    {
                        "totalPrice": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 10000,
                            "fractionDigits": 2,
                        },
                        "id": "0cefd1ca-82b1-4dd5-ac14-20f06fb07d4d",
                        "name": {"en-GB": "Test"},
                        "money": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 10000,
                            "fractionDigits": 2,
                        },
                        "slug": "toyota-c-hr-18-hybrid-122pk-cvt-energy",
                        "quantity": 1,
                        "discountedPricePerQuantity": [],
                        "taxCategory": {
                            "typeId": "tax-category",
                            "id": "e589180a-8096-4ef5-afd1-550a3ead1d1d",
                        },
                        "taxRate": {
                            "name": "TEMP",
                            "amount": 0.21,
                            "includedInPrice": True,
                            "country": "NL",
                            "id": "viljsTSo",
                            "subRates": [],
                        },
                        "state": [
                            {
                                "quantity": 1,
                                "state": {
                                    "typeId": "state",
                                    "id": "d09c7259-7ba4-479f-b8d2-8d2c6d2a807a",
                                },
                            }
                        ],
                        "taxedPrice": {
                            "totalNet": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 8264,
                                "fractionDigits": 2,
                            },
                            "totalGross": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 10000,
                                "fractionDigits": 2,
                            },
                        },
                    }
                ],
                "transactionFee": True,
                "discountCodes": [],
                "cart": {
                    "typeId": "cart",
                    "id": "737c2868-55bd-4c44-a332-f3b93122bfd7",
                },
                "shippingAddress": {
                    "id": "2x5-gO75",
                    "streetName": "Kanaalweg",
                    "streetNumber": "14",
                    "postalCode": "3526KL",
                    "city": "Utrecht",
                    "country": "NL",
                },
                "billingAddress": {
                    "id": "2x5-gO75",
                    "streetName": "Kanaalweg",
                    "streetNumber": "14",
                    "postalCode": "3526KL",
                    "city": "Utrecht",
                    "country": "NL",
                },
                "itemShippingAddresses": [],
                "refusedGifts": [],
            },
        },
    }
    result = schemas.ExtensionInputSchema().load(data)
    assert result.action == types.ExtensionAction.CREATE
    assert result.resource.type_id == types.ReferenceTypeId.ORDER

    data = schemas.ExtensionInputSchema().dump(result)


def test_project_schema():
    data = {
        "key": "unittest",
        "name": "SDK Test",
        "countries": ["AT", "NL", "CH", "BE", "GB", "DE", "IT", "LU", "ES"],
        "currencies": ["EUR", "GBP", "CHF"],
        "languages": [
            "en-GB",
            "de-DE",
            "fr-FR",
            "nl-BE",
            "nl-NL",
            "fr-BE",
            "it-IT",
            "es-ES",
            "pt-PT",
        ],
        "createdAt": "2018-10-24T08:58:22.935Z",
        "trialUntil": "2018-12",
        "messages": {"enabled": False, "deleteDaysAfterCreation": 15},
        "version": 9,
    }

    result = schemas.ProjectSchema().load(data)
    data = schemas.ProjectSchema().dump(result)
