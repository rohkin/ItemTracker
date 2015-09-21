import json
from pprint import pprint
from item import Item

class ParseJSON:
	def __init__(self):
		with open('data.json') as data_file:
			self.data = json.load(data_file)

	def createList(self):
		list = []
		for item in self.data['active']:
			list.append(Item(item['name'], item['icon'], item['description'], item['recharge']))

		return list