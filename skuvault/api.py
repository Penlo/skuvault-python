import requests


def getHeaders():
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    return headers


def getToken(payload):
    response = requests.post('https://app.skuvault.com/api/gettokens', headers=getHeaders(), json=payload)
    return response.json()


def addItem(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/addItem', headers=getHeaders(), json=payload)
    return response.json()


def addItemBulk(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/addItemBulk', headers=getHeaders(), json=payload)
    return response.json()


def addShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/addShipments', headers=getHeaders(), json=payload)
    return response.json()


def createBrands(payload):
    response = requests.post('https://app.skuvault.com/api/products/createBrands', headers=getHeaders(), json=payload)
    return response.json()


def createHolds(payload):
    response = requests.post('https://app.skuvault.com/api/sales/createHolds', headers=getHeaders(), json=payload)
    return response.json()


def createKit(payload):
    response = requests.post('https://app.skuvault.com/api/products/createKit', headers=getHeaders(), json=payload)
    return response.json()


def createPO(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/createPO', headers=getHeaders(), json=payload)
    return response.json()


def createProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/createProduct', headers=getHeaders(), json=payload)
    return response.json()


def createProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/createProducts', headers=getHeaders(), json=payload)
    return response.json()


def createSuppliers(payload):
    response = requests.post('https://app.skuvault.com/api/products/createSuppliers', headers=getHeaders(), json=payload)
    return response.json()


def getAvailableQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getAvailableQuantities', headers=getHeaders(), json=payload)
    return response.json()


def getBrands(payload):
    response = requests.post('https://app.skuvault.com/api/products/getBrands', headers=getHeaders(), json=payload)
    return response.json()


def getClassifications(payload):
    response = requests.post('https://app.skuvault.com/api/products/getClassifications', headers=getHeaders(), json=payload)
    return response.json()


def getExternalWarehouseQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getExternalWarehouseQuantities', headers=getHeaders(), json=payload)
    return response.json()


def getExternalWarehouses(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getExternalWarehouses', headers=getHeaders(), json=payload)
    return response.json()


def getHandlingTime(payload):
    response = requests.post('https://app.skuvault.com/api/products/getHandlingTime', headers=getHeaders(), json=payload)
    return response.json()


def getIncomingItems(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getIncomingItems', headers=getHeaders(), json=payload)
    return response.json()


def getIntegrations(payload):
    response = requests.post('https://app.skuvault.com/api/integration/getIntegrations', headers=getHeaders(), json=payload)
    return response.json()


def getInventoryByLocation(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getInventoryByLocation', headers=getHeaders(), json=payload)
    return response.json()


def getItemQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getItemQuantities', headers=getHeaders(), json=payload)
    return response.json()


def getKitQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getKitQuantities', headers=getHeaders(), json=payload)
    return response.json()


def getKits(payload):
    response = requests.post('https://app.skuvault.com/api/products/getKits', headers=getHeaders(), json=payload)
    return response.json()


def getLocations(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getLocations', headers=getHeaders(), json=payload)
    return response.json()


def getOnlineSaleStatus(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getOnlineSaleStatus', headers=getHeaders(), json=payload)
    return response.json()


def getPOs(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getPOs', headers=getHeaders(), json=payload)
    return response.json()


def getProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/getProduct', headers=getHeaders(), json=payload)
    return response.json()


def getProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/getProducts', headers=getHeaders(), json=payload)
    return response.json()


def getSerialNumbers(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getSerialNumbers', headers=getHeaders(), json=payload)
    return response.json()


def getReceivesHistory(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/getReceivesHistory', headers=getHeaders(), json=payload)
    return response.json()


def getSaleItemCost(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSaleItemCost', headers=getHeaders(), json=payload)
    return response.json()


def getSales(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSales', headers=getHeaders(), json=payload)
    return response.json()


def getSalesByDate(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getSalesByDate', headers=getHeaders(), json=payload)
    return response.json()


def getShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/getShipments', headers=getHeaders(), json=payload)
    return response.json()


def getSuppliers(payload):
    response = requests.post('https://app.skuvault.com/api/products/getSuppliers', headers=getHeaders(), json=payload)
    return response.json()


def getTransactions(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getTransactions', headers=getHeaders(), json=payload)
    return response.json()


def getWarehouseItemQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouseItemQuantities', headers=getHeaders(), json=payload)
    return response.json()


def getWarehouseItemQuantity(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouseItemQuantity', headers=getHeaders(), json=payload)
    return response.json()


def getWarehouses(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/getWarehouses', headers=getHeaders(), json=payload)
    return response.json()


def pickItem(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/pickItem', headers=getHeaders(), json=payload)
    return response.json()


def pickItemBulk(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/pickItemBulk', headers=getHeaders(), json=payload)
    return response.json()


def receivePOItems(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/receivePOItems', headers=getHeaders(), json=payload)
    return response.json()


def releaseHeldQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/sales/releaseHeldQuantities', headers=getHeaders(), json=payload)
    return response.json()


def removeItem(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/removeItem', headers=getHeaders(), json=payload)
    return response.json()


def removeItemBulk(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/removeItemBulk', headers=getHeaders(), json=payload)
    return response.json()


def setItemQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/setItemQuantities', headers=getHeaders(), json=payload)
    return response.json()


def setItemQuantity(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/setItemQuantity', headers=getHeaders(), json=payload)
    return response.json()


def setShipmentFile(payload):
    response = requests.post('https://app.skuvault.com/api/sales/setShipmentFile', headers=getHeaders(), json=payload)
    return response.json()


def syncOnlineSale(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncOnlineSale', headers=getHeaders(), json=payload)
    return response.json()


def syncOnlineSales(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncOnlineSales', headers=getHeaders(), json=payload)
    return response.json()


def syncShippedSaleAndRemoveItems(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncShippedSaleAndRemoveItems', headers=getHeaders(), json=payload)
    return response.json()


def syncShippedSaleAndRemoveItemsBulk(payload):
    response = requests.post('https://app.skuvault.com/api/sales/syncShippedSaleAndRemoveItems/bulk', headers=getHeaders(), json=payload)
    return response.json()


def updateAltSKUsCodes(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateAltSKUsCodes', headers=getHeaders(), json=payload)
    return response.json()


def updateExternalWarehouseQuantities(payload):
    response = requests.post('https://app.skuvault.com/api/inventory/updateExternalWarehouseQuantities', headers=getHeaders(), json=payload)
    return response.json()


def updateHandlingTime(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateHandlingTime', headers=getHeaders(), json=payload)
    return response.json()


def updateOnlineSaleStatus(payload):
    response = requests.post('https://app.skuvault.com/api/sales/updateOnlineSaleStatus', headers=getHeaders(), json=payload)
    return response.json()


def updatePOs(payload):
    response = requests.post('https://app.skuvault.com/api/purchaseorders/updatePOs', headers=getHeaders(), json=payload)
    return response.json()


def updateProduct(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateProduct', headers=getHeaders(), json=payload)
    return response.json()


def updateProducts(payload):
    response = requests.post('https://app.skuvault.com/api/products/updateProducts', headers=getHeaders(), json=payload)
    return response.json()


def updateShipments(payload):
    response = requests.post('https://app.skuvault.com/api/sales/updateShipments', headers=getHeaders(), json=payload)
    return response.json()

