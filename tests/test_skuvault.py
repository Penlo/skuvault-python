from skuvault import api

b = api.Inventory()

data = b.getAvailableQuantities('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                 UserToken='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', ExpandAlternateSkus=True, PageNumber=0)

for x in data.get('Items'):
    print(x)
