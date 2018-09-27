from commercetools import schemas, types

data = """
{
  "id": "00633d11-c5bb-434e-b132-73f7e130b4e3",
  "version": 1,
  "productType": {
    "typeId": "product-type",
    "id": "4759ab14-094a-4e43-a385-c6b27f51e5f9"
  },
  "catalogs": [],
  "masterData": {
    "current": {
      "name": { "en": "MB PREMIUM TECH T" },
      "description": { "en": "Sample description" },
      "categories": [
        { "typeId": "category", "id": "83782393-ca52-4951-841d-632483a650d5" }
      ],
      "categoryOrderHints": {},
      "slug": { "en": "mb-premium-tech-t1534589737933" },
      "masterVariant": {
        "id": 1,
        "sku": "sku_MB_PREMIUM_TECH_T_variant1_1534589737933",
        "prices": [
          {
            "value": {
              "type": "centPrecision",
              "currencyCode": "EUR",
              "centAmount": 10000,
              "fractionDigits": 2
            },
            "id": "1c1ef7fb-08e5-46cd-98f0-364e99dadd94"
          }
        ],
        "images": [
          {
            "url": "https://www.commercetools.com/cli/data/253245821_1.jpg",
            "dimensions": { "w": 1400, "h": 1400 }
          }
        ],
        "attributes": [],
        "assets": []
      },
      "variants": [],
      "searchKeywords": {}
    },
    "staged": {
      "name": { "en": "MB PREMIUM TECH T" },
      "description": { "en": "Sample description" },
      "categories": [
        { "typeId": "category", "id": "83782393-ca52-4951-841d-632483a650d5" }
      ],
      "categoryOrderHints": {},
      "slug": { "en": "mb-premium-tech-t1534589737933" },
      "masterVariant": {
        "id": 1,
        "sku": "sku_MB_PREMIUM_TECH_T_variant1_1534589737933",
        "prices": [
          {
            "value": {
              "type": "centPrecision",
              "currencyCode": "EUR",
              "centAmount": 10000,
              "fractionDigits": 2
            },
            "id": "1c1ef7fb-08e5-46cd-98f0-364e99dadd94"
          }
        ],
        "images": [
          {
            "url": "https://www.commercetools.com/cli/data/253245821_1.jpg",
            "dimensions": { "w": 1400, "h": 1400 }
          }
        ],
        "attributes": [],
        "assets": []
      },
      "variants": [],
      "searchKeywords": {}
    },
    "published": true,
    "hasStagedChanges": false
  },
  "catalogData": {},
  "taxCategory": {
    "typeId": "tax-category",
    "id": "6152845a-3a0c-43f5-b6da-7674636d53bf"
  },
  "lastVariantId": 1,
  "createdAt": "2018-08-18T10:55:38.153Z",
  "lastModifiedAt": "2018-08-18T10:55:38.153Z",
  "lastMessageSequenceNumber": 1
}
"""


def test_product_deserialize():
    obj = schemas.ProductSchema().loads(data)
    assert isinstance(obj, types.Product)
    assert obj.master_data.staged.master_variant.prices[0].value.cent_amount == 10000
