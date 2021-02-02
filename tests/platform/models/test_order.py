from commercetools.platform.models import order


def test_deserialize_order_paged_query_response():
    response = order.OrderPagedQueryResponse.deserialize(
        {
            "limit": 20,
            "offset": 0,
            "count": 20,
            "total": 612,
            "results": [
                {
                    "type": "Order",
                    "id": "c28ba890-0595-475f-8c8b-ca96d7c5c602",
                    "version": 4,
                    "lastMessageSequenceNumber": 4,
                    "createdAt": "2020-12-17T12:45:22.407Z",
                    "lastModifiedAt": "2021-01-18T09:07:07.198Z",
                    "lastModifiedBy": {
                        "isPlatformClient": True,
                        "user": {
                            "typeId": "user",
                            "id": "cf8fd14f-384d-4a13-a81a-fdb1fc76623a",
                        },
                    },
                    "createdBy": {
                        "clientId": "1qGcTSsoGLHvmiRUnMOut5__",
                        "isPlatformClient": False,
                        "anonymousId": "75c0fe8c-d4b8-40b2-9138-a39278acf406",
                    },
                    "orderNumber": "5000158",
                    "customerEmail": "test@example.org",
                    "anonymousId": "75c0fe8c-d4b8-40b2-9138-a39278acf406",
                    "locale": "nl-NL",
                    "totalPrice": {
                        "type": "centPrecision",
                        "currencyCode": "EUR",
                        "centAmount": 5716,
                        "fractionDigits": 2,
                    },
                    "taxedPrice": {
                        "totalNet": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 4724,
                            "fractionDigits": 2,
                        },
                        "totalGross": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 5716,
                            "fractionDigits": 2,
                        },
                        "taxPortions": [
                            {
                                "rate": 0.21,
                                "amount": {
                                    "type": "centPrecision",
                                    "currencyCode": "EUR",
                                    "centAmount": 992,
                                    "fractionDigits": 2,
                                },
                                "name": "21% BTW",
                            }
                        ],
                    },
                    "country": "NL",
                    "orderState": "Confirmed",
                    "paymentState": "Pending",
                    "syncInfo": [],
                    "returnInfo": [],
                    "shippingInfo": {
                        "shippingMethodName": "Standard shipping method",
                        "price": {
                            "type": "centPrecision",
                            "currencyCode": "EUR",
                            "centAmount": 5000,
                            "fractionDigits": 2,
                        },
                        "shippingRate": {
                            "price": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 5000,
                                "fractionDigits": 2,
                            },
                            "freeAbove": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 50000,
                                "fractionDigits": 2,
                            },
                            "tiers": [],
                        },
                        "taxRate": {
                            "name": "21% BTW",
                            "amount": 0.21,
                            "includedInPrice": True,
                            "country": "NL",
                            "id": "Z0wLUuYw",
                            "subRates": [],
                        },
                        "taxCategory": {
                            "typeId": "tax-category",
                            "id": "ac8b6c6c-424f-4cbb-aec5-d3754fb8dd78",
                        },
                        "deliveries": [],
                        "shippingMethod": {
                            "typeId": "shipping-method",
                            "id": "fdf53457-487f-4b0e-bfbb-3124e44686e7",
                        },
                        "taxedPrice": {
                            "totalNet": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 4132,
                                "fractionDigits": 2,
                            },
                            "totalGross": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 5000,
                                "fractionDigits": 2,
                            },
                        },
                        "shippingMethodState": "MatchesCart",
                    },
                    "taxMode": "Platform",
                    "inventoryMode": "ReserveOnOrder",
                    "taxRoundingMode": "HalfEven",
                    "taxCalculationMode": "LineItemLevel",
                    "origin": "Customer",
                    "lineItems": [
                        {
                            "id": "7c0e2cbf-3434-494a-89cb-6fc0f8881662",
                            "productId": "02e00188-0f19-4b43-9c35-55ae702fd1be",
                            "name": {"nl-NL": "Some Product"},
                            "productType": {
                                "typeId": "product-type",
                                "id": "109caecb-abe6-4900-ab03-7af5af985ff3",
                                "version": 1,
                            },
                            "productSlug": {"nl-NL": "some-product"},
                            "variant": {
                                "id": 1,
                                "sku": "PRODUCT1",
                                "key": "PRODUCT1",
                                "prices": [
                                    {
                                        "value": {
                                            "type": "centPrecision",
                                            "currencyCode": "EUR",
                                            "centAmount": 895,
                                            "fractionDigits": 2,
                                        },
                                        "id": "36506ccc-e770-4937-a027-3e4ff0e7e70e",
                                        "channel": {
                                            "typeId": "channel",
                                            "id": "d75c2a23-fb85-4916-bd9c-9862dca9138c",
                                        },
                                        "discounted": {
                                            "value": {
                                                "type": "centPrecision",
                                                "currencyCode": "EUR",
                                                "centAmount": 716,
                                                "fractionDigits": 2,
                                            },
                                            "discount": {
                                                "typeId": "product-discount",
                                                "id": "57b26c6e-ebea-4197-ac24-ed602d1a0c04",
                                            },
                                        },
                                    }
                                ],
                                "images": [
                                    {
                                        "url": "http://example.org/image.jpg",
                                        "dimensions": {"w": 1200, "h": 800},
                                    },
                                ],
                                "attributes": [
                                    {"name": "brand", "value": {"nl-NL": "SomeBrand"}},
                                ],
                                "assets": [],
                                "availability": {
                                    "channels": {
                                        "d75c2a23-fb85-4916-bd9c-9862dca9138c": {
                                            "isOnStock": False,
                                            "restockableInDays": 12,
                                            "availableQuantity": -1,
                                        }
                                    }
                                },
                            },
                            "price": {
                                "value": {
                                    "type": "centPrecision",
                                    "currencyCode": "EUR",
                                    "centAmount": 895,
                                    "fractionDigits": 2,
                                },
                                "id": "36506ccc-e770-4937-a027-3e4ff0e7e70e",
                                "channel": {
                                    "typeId": "channel",
                                    "id": "d75c2a23-fb85-4916-bd9c-9862dca9138c",
                                },
                                "discounted": {
                                    "value": {
                                        "type": "centPrecision",
                                        "currencyCode": "EUR",
                                        "centAmount": 716,
                                        "fractionDigits": 2,
                                    },
                                    "discount": {
                                        "typeId": "product-discount",
                                        "id": "57b26c6e-ebea-4197-ac24-ed602d1a0c04",
                                    },
                                },
                            },
                            "quantity": 1,
                            "discountedPricePerQuantity": [],
                            "supplyChannel": {
                                "typeId": "channel",
                                "id": "d75c2a23-fb85-4916-bd9c-9862dca9138c",
                            },
                            "distributionChannel": {
                                "typeId": "channel",
                                "id": "d75c2a23-fb85-4916-bd9c-9862dca9138c",
                            },
                            "taxRate": {
                                "name": "21% BTW",
                                "amount": 0.21,
                                "includedInPrice": True,
                                "country": "NL",
                                "id": "Z0wLUuYw",
                                "subRates": [],
                            },
                            "addedAt": "2020-12-17T12:43:22.773Z",
                            "lastModifiedAt": "2020-12-17T12:43:22.773Z",
                            "state": [
                                {
                                    "quantity": 1,
                                    "state": {
                                        "typeId": "state",
                                        "id": "f1d9531d-41f0-46a7-82f2-c4b0748aa9f5",
                                    },
                                }
                            ],
                            "priceMode": "Platform",
                            "totalPrice": {
                                "type": "centPrecision",
                                "currencyCode": "EUR",
                                "centAmount": 716,
                                "fractionDigits": 2,
                            },
                            "taxedPrice": {
                                "totalNet": {
                                    "type": "centPrecision",
                                    "currencyCode": "EUR",
                                    "centAmount": 592,
                                    "fractionDigits": 2,
                                },
                                "totalGross": {
                                    "type": "centPrecision",
                                    "currencyCode": "EUR",
                                    "centAmount": 716,
                                    "fractionDigits": 2,
                                },
                            },
                            "lineItemMode": "Standard",
                        }
                    ],
                    "customLineItems": [],
                    "transactionFee": True,
                    "discountCodes": [],
                    "cart": {
                        "typeId": "cart",
                        "id": "a25425a1-f557-44a6-b2ab-c06f5134bb99",
                    },
                    "custom": {
                        "type": {
                            "typeId": "type",
                            "id": "05ce0769-40bf-4246-a72a-7a5064e49cd1",
                        },
                        "fields": {
                            "customerNotes": "<p>&#x1F525</p>\n👍",
                            "dateOfBirth": "1919-12-31",
                        },
                    },
                    "paymentInfo": {
                        "payments": [
                            {
                                "typeId": "payment",
                                "id": "5b8e9bbe-a6dd-47cf-bc16-1f81d8c0e9dd",
                            }
                        ]
                    },
                    "shippingAddress": {"country": "NL"},
                    "billingAddress": {
                        "firstName": "is",
                        "lastName": "emoji accepted",
                        "streetName": "sdafsdf",
                        "streetNumber": "11111111111111111111111111111111111111111111111111111111111111111111",
                        "postalCode": "1234hh",
                        "city": "sdffd",
                        "country": "NL",
                        "company": "",
                        "building": "",
                        "phone": "06123456789",
                    },
                    "itemShippingAddresses": [],
                    "refusedGifts": [],
                    "store": {"typeId": "store", "key": "store"},
                },
            ],
        }
    )
