# Restocks-Image-Scraper


# It's very sipmle (micro)API which returns URL to image

## Usage
- send GET request to (by default) localhost:5000/image-api?sku={ITEM_SKU}
`http://localhost:5000/image-api?sku=CK3022-600`
- if sku is found it returns json: {"img": PHOTO_URL}
- if not {"img": "error"}