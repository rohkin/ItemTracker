class Item:
	def __init__(self,name,icon,description,recharge):
		self.name = name
		self.icon = icon
		self.description = description
		self.recharge = recharge

	def printProperties(self):
		print ('name: %s' % self.name)
		print ('icon: %s' % self.icon)
		print ('description: %s' % self.description)
		print ('recharge: %s' % self.recharge)
		print ('\n')

	