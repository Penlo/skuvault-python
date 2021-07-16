# **SKUVAULT-PYTHON**
##### A Python library for the SkuVault API
More documentation for the SkuVault API can be found at https://dev.skuvault.com/reference

## **Installation**
```
pip install skuvault-python
```

## **Example Usage**
```
import skuvault.api as sv

payload = {
    "TenantToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "Usertoken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

response = sv.getInventoryByLocation(payload)

print(response)
```
Responses are returned as JSON Objects