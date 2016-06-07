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

				#----------------------------------------------------
				# if 'ast.Node' in self.listA[numHijos]:
				# 	txt += "[label= "+self.listA[numHijos].traducir()+"]\n\t"
				#----------------------------------------------------
				# if self.listA[numHijos].traducir() == type(None):
				# 	Null(A[numHijos].traducir())
				# else:
				# 	txt += "[label= "+self.listA[numHijos].traducir()+"]\n\t"
				#----------------------------------------------------
				#txt += "[label= "+self.listA[numHijos].traducir()+"]\n\t"
				#----------------------------------------------------
				if type(self.listA[numHijos].traducir()) == type(None):
					name = self.listA[numHijos].traducir()
					#txt += "[label= "+name+"]\n\t"

				elif type(self.listA[numHijos].traducir()) == unicode:
					#txt += "-> "+self.listA.traducir()+"]\n\t"
					txt += "[label= "+self.name+"]\n\t"
					#txt += " -> "+self.listA[numHijos].traducir()+"\n\t"

				elif type(self.listA[numHijos].traducir()) == float:
					#txt += "-> "+self.listA[numHijos].traducir()+"]\n\t"
					txt += "[label= "+str(self.name)+"]\n\t"
					#txt += " -> "+self.listA[numHijos].traducir()+"\n\t"

				else:
					txt += "[label= "+str(self.name)+"]\n\t"
					#txt += " -> "+self.listA[numHijos].traducir()+"\n\t"

				numHijos = numHijos+1

		# elif type(self.listA) == unicode:

		# 	txt += "-> "+self.listA.traducir()+"\n\t"
			#----------------------------------------------------
			#txt += "[label= "+str(self.name)+"]\n\t"
			#----------------------------------------------------
			#txt += "-> "+str(self.name)+"]\n\t"
			#----------------------------------------------------
			#txt += "[label= "+str(self.listA.traducir())+"]\n\t"
			#----------------------------------------------------

		# elif type(self.listA) == float:
		# 	txt += "-> "+self.listA.traducir()+"\n\t"
			#----------------------------------------------------
			#txt += "[label= "+str(self.name)+"]\n\t"
			#----------------------------------------------------
			#txt += "-> "+str(self.name)+"]\n\t"
			#----------------------------------------------------
			#txt += "[label= "+str(self.listA.traducir())+"]\n\t"
			#----------------------------------------------------

		# else:
		# 	pass
			#txt += self.listA.traducir()

			#----------------------------------------------------
			#self.listA.imprimirPostOrden()
			#print ident + "Nodo: "+ self.name
		# if "program" in self.name:
		# 	numHijos = 0
		# 	while(numHijos <= len(self.listA)-1):
		# 		txt += self.listA[numHijos].traducir()
		# 		numHijos = numHijos+1
		#----------------------------------------------------

		return "digraph G {\n"+txt+"\n}"

class ID(Node):
	def __init__(self, name, lineno):
		self.name = name
		self.lineno = lineno
	def imprimirPostOrden(self, ident):
		print ident + "ID: "+ self.name
	def traducir(self):
		global txt
		txt += "[label= "+self.name+"]\n\t"
		#txt += "-> "+self.traducir()+"\n\t"

class Numero(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "NUM: "+ str(int(self.name))

	def traducir(self):
		global txt
		txt += "[label= "+str(int(self.name))+"]\n\t"

class Cad(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "CAD: "+ str(self.name)

	def traducir(self):
		global txt
		txt += "[label= "+str(self.name)+"]\n\t"

class True(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "TRUE: "+ str(self.name)

	def traducir(self):
		global txt
		txt += "[label= "+str(self.name)+"]\n\t"

class False(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "FALSE: "+ str(self.name)

	def traducir(self):
		global txt
		txt += "[label= "+str(self.name)+"]\n\t"

class Null(Node):
	def __init__(self):
		self.type = 'void'

	def imprimirPostOrden(self, ident):
		print ident + 'node null'

	def traducir(self):
		global txt
		txt += "[label= "+"nodo null"+"]\n\t"
		return

 
class empty(Node):
	def __init__(self):
		pass
	#'''empty :'''
	
	