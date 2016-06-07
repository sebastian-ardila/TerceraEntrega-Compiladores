txt=""

class Node():
	def __init__(self,listA, name):
		#numHijos = 0
		self.name = name
		self.listA = listA

	def imprimirPostOrden(self, ident):
	#def imprimirPostOrden(self):

		if type(self.listA) == list:
			numHijos = 0
			while(numHijos <= len(self.listA)-1):
				self.listA[numHijos].imprimirPostOrden("  " +ident)
				#self.listA[numHijos].imprimirPostOrden()
				numHijos = numHijos+1
			#return ident + "Nodo: " + self.name
			print ident + "Nodo: " + self.name

		elif type(self.listA) == unicode:
			print ident + "Nodo: "+ self.name

		elif type(self.listA) == float:
			print ident + "Nodo: "+ self.name

		else:
			self.listA.imprimirPostOrden("\t"+ ident)
			#self.listA.imprimirPostOrden()
			print ident + "Nodo: "+ self.name

	def traducir(self):
		global txt

		if type(self.listA) == list:
			numHijos = 0
			#print type(self.listA[0])
			while(numHijos <= len(self.listA)-1):

				if 'ast.Node' in self.listA[numHijos]:
					txt += self.listA[numHijos].traducir()

				numHijos = numHijos+1

		elif type(self.listA) == unicode:
			txt += str(self.name)
			#print ident + "Nodo: "+ self.name

		elif type(self.listA) == float:
			txt += str(self.name)
			#print ident + "Nodo: "+ self.name

		else:
			pass
			txt += self.listA.traducir()
			#self.listA.imprimirPostOrden()
			#print ident + "Nodo: "+ self.name
		# if "program" in self.name:
		# 	numHijos = 0
		# 	while(numHijos <= len(self.listA)-1):
		# 		txt += self.listA[numHijos].traducir()
		# 		numHijos = numHijos+1

		return txt

class ID(Node):
	def __init__(self, name, lineno):
		self.name = name
		self.lineno = lineno
	def imprimirPostOrden(self, ident):
		print ident + "ID: "+ self.name
	def traducir(self):
		global txt
		txt += self.name

class Numero(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "NUM: "+ str(int(self.name))

	def traducir(self):
		global txt
		txt += str(int(self.name))

class Cad(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "CAD: "+ str(self.name)

	def traducir(self):
		global txt
		txt += str(self.name)

class True(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "TRUE: "+ str(self.name)

	def traducir(self):
		global txt
		txt += str(self.name)

class False(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "FALSE: "+ str(self.name)

	def traducir(self):
		global txt
		txt += str(self.name)

class Null(Node):
	def __init__(self):
		self.type = 'void'

	def imprimirPostOrden(self, ident):
		print ident + 'node null'

	def traducir(self):
		global txt
		txt += "nodo null"
		return

 
class empty(Node):
	def __init__(self):
		pass
	#'''empty :'''
	
	