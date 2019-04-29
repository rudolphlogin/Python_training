class Kls(object)
	def __init__(self,data):
		self.data = data
	def printd(self):
		print(self.data)
	@staticmethod
		def smethod(*arg):
			print('Static:',arg)
	@classmethod
		def cmethod(*arg):
			print('Class:',arg)
			
			
ik=KLs(23)
ik.printd()
ik.smethod()
ik.cmethod()