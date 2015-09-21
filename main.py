
from item import Item
from parsejson import ParseJSON

test2 = ParseJSON()
items = test2.createList()

for item in items:
	item.printProperties()