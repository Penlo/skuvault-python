import requests
from .exceptions import SkuVaultAuthenticationError


class SkuVault(object):
    def __init__(self):
        self.base_url = 'https://app.skuvault.com/api'

    @property
    def inventory(self):
        return Inventory()

    @property
    def tokens(self):
        return GetTokens()

    def send_request(self, method, url, payload=None, request_headers=None):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if request_headers:
            headers.update(request_headers)

        response = None
        if method == 'POST':
            response = requests.post(url, json=payload, headers=headers)

        if response is not None:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                if response.status_code == 401 | response.status_code == 400:
                    raise SkuVaultAuthenticationError((
                        "Invalid client_id or client_secret. Please verify your TenantToken and UserToken"
                    ))
                raise
        try:
            return response.json()
        except ValueError:
            # In case of reports, there is no JSON response, so return the
            # content instead which contains the actual report
            return response.text


class GetTokens(SkuVault):
    def getToken(self, email, password):
        endpoint = 'gettokens'
        payload = {
            "Email": email,
            "Password": password
        }
        return self.send_request(
            method='POST',
            url=f'{self.base_url}/{endpoint}',
            payload=payload
        )


class Inventory(SkuVault):
    path = 'inventory'

    def addItem(self, warehouseid, locationcode, quantity, reason, TenantToken, UserToken, note=None, sku=None,
                code=None, serialnumbers=None):

        """Adds quantity to a warehouse location.

        :param warehouseid: Int
        :param locationcode: String
        :param quantity: Int
        :param reason: String
        :param TenantToken: String
        :param UserToken: String
        :param note: String
        :param sku: String
        :param code: String
        :param serialnumbers: List of strings ['string1', 'string2', 'string3]

        """

        endpoint = 'addItem'

        payload = {
            "WarehouseId": int(warehouseid),
            "LocationCode": str(locationcode),
            "Quantity": int(quantity),
            "Reason": str(reason),
            "TenantToken": str(TenantToken),
            "UserToken": str(UserToken),
        }
        if serialnumbers is not None and type(serialnumbers) == list:
            payload["SerialNumbers"] = serialnumbers
        elif serialnumbers is not None and type(serialnumbers) != list:
            raise Exception("serialnumbers must be of type: list")
        if note is not None:
            payload["Note"] = str(note)
        if sku is not None and code is not None:
            raise Exception("You can not specify both Sku and Code, you must use one or the other")
        if sku is not None:
            payload["Sku"] = str(sku)
        if code is not None:
            payload["Code"] = str(code)

        return self.send_request(
            method='POST',
            url=f'{self.base_url}/{self.path}/{endpoint}',
            payload=payload
        )

    def addItemBulk(self, payload):

        endpoint = 'addItemBulk'
        response = requests.post('https://app.skuvault.com/api/inventory/addItemBulk', headers=self.headers,
                                 json=payload)
        return response.json()

    def getAvailableQuantities(self, TenantToken, UserToken, ModifiedAfterDateTimeUtc=None,
                               ModifiedBeforeDateTimeUtc=None, PageNumber=None, ExpandAlternateSkus=False):
        """Retrieve a list of SKUs and their total available quantities across all warehouses.
           Available Quantity is the quantity that is actually available to sell across all your sales channels.

        :param TenantToken: String
        :param UserToken: String
        :param ModifiedAfterDateTimeUtc: date "0000-00-00T00:00:00.0000000Z"
        :param ModifiedBeforeDateTimeUtc: date "0000-00-00T00:00:00.0000000Z"
        :param PageNumber: Int
        :param ExpandAlternateSkus: True or False

        """
        endpoint = 'getAvailableQuantities'

        payload = {
            "TenantToken": str(TenantToken),
            "UserToken": str(UserToken),
            "ExpandAlternateSkus": ExpandAlternateSkus
        }

        if ModifiedAfterDateTimeUtc is not None:
            payload["ModifiedAfterDateTimeUtc"] = ModifiedAfterDateTimeUtc
        if ModifiedBeforeDateTimeUtc is not None:
            payload["ModifiedBeforeDateTimeUtc"] = ModifiedBeforeDateTimeUtc
        if PageNumber is not None:
            payload["PageNumber"] = int(PageNumber)

        return self.send_request(
            method='POST',
            url=f'{self.base_url}/{self.path}/{endpoint}',
            payload=payload
        )

    def getExternalWarehouseQuantities(self, payload):
        response = requests.post('https://app.skuvault.com/api/inventory/getExternalWarehouseQuantities',
                                 headers=self.headers, json=payload)
        return response.json()

    def getExternalWarehouses(self, payload):
        response = requests.post('https://app.skuvault.com/api/inventory/getExternalWarehouses', headers=self.headers,
                                 json=payload)
        return response.json()

    def getInventoryByLocation(self, payload):
        response = requests.post('https://app.skuvault.com/api/inventory/getInventoryByLocation', headers=self.headers,
                                 json=payload)
        return response.json()

    def getItemQuantities(self, payload):
        response = requests.post('https://app.skuvault.com/api/inventory/getItemQuantities', headers=self.headers,
                                 json=payload)
        return response.json()

    def getKitQuantities(self, payload):
        response = requests.post('https://app.skuvault.com/api/inventory/getKitQuantities', headers=self.headers,
                                 json=payload)
        return response.json()



def addShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/addShipments', headers=self.headers, json=payload)
    return response.json()


def createBrands(payload):
    response = requests.post('https://app.skuvault.com/api/products/createBrands', headers=self.headers, json=payload)
    return response.json()


def createHolds(payload):
    response = requests.post('https://app.skuvault.com/api/sales/createHolds', headers=self.headers, json=payload)
    return response.json()


def createKit(payload):
    response = requests.post('https://app.skuvault.com/api/products/createKit', headers=self.headers, json=payload)
    return response.json()


def createPO(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/createPO', headers=self.headers, json=payload)
    return response.json()


def createProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/createProduct', headers=self.headers, json=payload)
    return response.json()


def createProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/createProducts', headers=self.headers, json=payload)
    return response.json()


def createSuppliers(payload):
    response = requests.post('https://app.skuvault.com/api/products/createSuppliers', headers=self.headers, json=payload)
    return response.json()


def getBrands(payload):
    response = requests.post('https://app.skuvault.com/api/products/getBrands', headers=self.headers, json=payload)
    return response.json()


def getClassifications(payload):
    response = requests.post('https://app.skuvault.com/api/products/getClassifications', headers=self.headers, json=payload)
    return response.json()





def getHandlingTime(payload):
    response = requests.post('https://app.skuvault.com/api/products/getHandlingTime', headers=self.headers, json=payload)
    return response.json()


def getIncomingItems(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getIncomingItems', headers=self.headers, json=payload)
    return response.json()


def getIntegrations(payload):
    response = requests.post('https://app.skuvault.com/api/integration/getIntegrations', headers=self.headers, json=payload)
    return response.json()





def getKits(payload):
    response = requests.post('https://app.skuvault.com/api/products/getKits', headers=self.headers, json=payload)
    return response.json()


def getLocations(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getLocations', headers=self.headers, json=payload)
    return response.json()


def getOnlineSaleStatus(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getOnlineSaleStatus', headers=self.headers, json=payload)
    return response.json()


def getPOs(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getPOs', headers=self.headers, json=payload)
    return response.json()


def getProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/getProduct', headers=self.headers, json=payload)
    return response.json()


def getProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/getProducts', headers=self.headers, json=payload)
    return response.json()


def getSerialNumbers(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getSerialNumbers', headers=self.headers, json=payload)
    return response.json()


def getReceivesHistory(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getReceivesHistory', headers=self.headers, json=payload)
    return response.json()


def getSaleItemCost(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSaleItemCost', headers=self.headers, json=payload)
    return response.json()


def getSales(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSales', headers=self.headers, json=payload)
    return response.json()


def getSalesByDate(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSalesByDate', headers=self.headers, json=payload)
    return response.json()


def getShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getShipments', headers=self.headers, json=payload)
    return response.json()


def getSuppliers(payload):
    response = requests.post('https://app.skuvault.com/api/products/getSuppliers', headers=self.headers, json=payload)
    return response.json()


def getTransactions(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getTransactions', headers=self.headers, json=payload)
    return response.json()


def getWarehouseItemQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouseItemQuantities', headers=self.headers, json=payload)
    return response.json()


def getWarehouseItemQuantity(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouseItemQuantity', headers=self.headers, json=payload)
    return response.json()


def getWarehouses(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouses', headers=self.headers, json=payload)
    return response.json()


def pickItem(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/pickItem', headers=self.headers, json=payload)
    return response.json()


def pickItemBulk(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/pickItemBulk', headers=self.headers, json=payload)
    return response.json()


def receivePOItems(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/receivePOItems', headers=self.headers, json=payload)
    return response.json()


def releaseHeldQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/sales/releaseHeldQuantities', headers=self.headers, json=payload)
    return response.json()


def removeItem(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/removeItem', headers=self.headers, json=payload)
    return response.json()


def removeItemBulk(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/removeItemBulk', headers=self.headers, json=payload)
    return response.json()


def setItemQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/setItemQuantities', headers=self.headers, json=payload)
    return response.json()


def setItemQuantity(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/setItemQuantity', headers=self.headers, json=payload)
    return response.json()


def setShipmentFile(payload):
    response = requests.post('https://app.skuvault.com/api/sales/setShipmentFile', headers=self.headers, json=payload)
    return response.json()


def syncOnlineSale(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncOnlineSale', headers=self.headers, json=payload)
    return response.json()


def syncOnlineSales(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncOnlineSales', headers=self.headers, json=payload)
    return response.json()


def syncShippedSaleAndRemoveItems(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncShippedSaleAndRemoveItems', headers=self.headers, json=payload)
    return response.json()


def syncShippedSaleAndRemoveItemsBulk(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncShippedSaleAndRemoveItems/bulk', headers=self.headers, json=payload)
    return response.json()


def updateAltSKUsCodes(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateAltSKUsCodes', headers=self.headers, json=payload)
    return response.json()


def updateExternalWarehouseQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/updateExternalWarehouseQuantities', headers=self.headers, json=payload)
    return response.json()


def updateHandlingTime(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateHandlingTime', headers=self.headers, json=payload)
    return response.json()


def updateOnlineSaleStatus(payload):
    response = requests.post('https://app.skuvault.com/api/sales/updateOnlineSaleStatus', headers=self.headers, json=payload)
    return response.json()


def updatePOs(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/updatePOs', headers=self.headers, json=payload)
    return response.json()


def updateProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateProduct', headers=self.headers, json=payload)
    return response.json()


def updateProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateProducts', headers=self.headers, json=payload)
    return response.json()


def updateShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/updateShipments', headers=self.headers, json=payload)
    return response.json()

