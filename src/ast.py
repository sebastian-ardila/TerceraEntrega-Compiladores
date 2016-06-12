txt=""

cont=0
def incrementarContador():
    global cont 
    cont += 1
    return "%d " % cont

class Node():
	pass


class program(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return "digraph G {\n\t"+txt+"}"

	#print "program"

###############################################################################

class classDecl(Node):
	def __init__(self, son1, son2, son3, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"


		return id

	
	#print "Declaracion de Clase"

###############################################################################

class extendsIdOp(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print "Extends ID en Declaracion de Clase"

###############################################################################

class listFieldOrMethDecl(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


	#print 'lista de declaraciones de Campo o Metodo'

###############################################################################

class fieldOrMethDecl_field(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print 'Declaracion de campo'

###############################################################################

class listFieldOrMethDecl_meth(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print 'Declaracion de metodo'

###############################################################################

class fieldDecl(Node):
	def __init__(self, son1, son2, son3, son4, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)
		self.son4.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id


	#print 'componentes de declaracion de campo'

###############################################################################

class listId(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


	#print 'lista de identificadores'


###############################################################################

class methDecl(Node):
	def __init__(self, son1, son2, son3, son4, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)
		self.son4.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id


	#print 'componentes de declaracion de metodo'

###############################################################################

class formals(Node):
	def __init__(self, son1, son2, son3, son4, son5, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)
		self.son4.imprimirPostOrden(" "+ident)
		self.son5.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

	#print 'formals'

###############################################################################

class listTypeId(Node):
	def __init__(self, son1, son2, son3, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id


	#print 'lista de tipos'

###############################################################################

class type_INT(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		#self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id


	#print 'tipo entero'

###############################################################################


class type_BOOLEAN(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		#self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id


	#print 'tipo booleano'

###############################################################################


class type_STRING(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		#son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		#txt += id + " -> " + son1 + "\n\t"

		return id


	#print 'tipo string'

###############################################################################


class type_type_ID(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


	#print 'tipo ID'

###############################################################################


class type_type_LCOR_RCOR(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	
###############################################################################

class block(Node):
	def __init__(self, son1, son2, son3, son4, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)
		self.son4.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id


###############################################################################

class listVarDecl(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################

class listStmt(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################	

class varDecl(Node):
	def __init__(self, son1, son2, son3, son4, son5, son6, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5
		self.son6 = son6

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)
		self.son4.imprimirPostOrden(" "+ident)
		self.son5.imprimirPostOrden(" "+ident)
		self.son6.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()
		son5 = self.son5.traducir()
		son6 = self.son6.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"
		txt += id + " -> " + son6 + "\n\t"

		return id


###############################################################################

class equalExprOp(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class listIdEqExprOp(Node):
	def __init__(self, son1, son2, son3, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son1 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id


###############################################################################
	

class stmt_assign(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class stmt_call(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class stmt_RETURN(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class stmt_IF(Node):
	def __init__(self, son1, son2, son3, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)
		self.son3.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id


###############################################################################


class stmt_WHILE(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################
	

class stmt_breakOrContinue(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class stmt_block(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################
	

class exprOp(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################
	

class elseStmtOpElse(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		#self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id


###############################################################################
		

class elseStmtOpStmt(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################
	

class breakOrContinue_Break(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		#self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id


###############################################################################


class breakOrContinue_Continue(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		#son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		#txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################
	

class assign(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class location_ID(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class location_expr_DOT_ID(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		#son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		#txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class location_expr_LCOR_RCOR(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class call(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class method_ID(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class method_expr_DOT_ID(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class actuals(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class listExpr(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################

class expr_binary_SUM(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_MEN(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_MULT(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_DIV(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_MOD(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_ILOGICO(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_OLOGICO(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_MENORQUE(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	

###############################################################################


class expr_binary_MENORIGUAL(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	

###############################################################################


class expr_binary_MAYORQUE(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	
###############################################################################


class expr_binary_MAYORIGUAL(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id


###############################################################################


class expr_binary_IGUALIGUAL(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	

###############################################################################


class expr_binary_DIFERENTE(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	

###############################################################################


class expr_call(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	

###############################################################################


class expr_this(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		#son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		#txt += id + " -> " + son1 + "\n\t"

		return id

	

###############################################################################


class expr_new_id(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	
###############################################################################


class expr_new_type(Node):
	def __init__(self, son1, son2, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)
		self.son2.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

	

###############################################################################


class expr_DOT_LENGTH(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	

###############################################################################


class expr_uminus(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	

###############################################################################


class expr_negbool(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	
###############################################################################


class expr_literal(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id

	

###############################################################################


class expr_expr(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class literal_NUMERO(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id



###############################################################################


class literal_CAD(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


###############################################################################


class literal_TRUE(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print "literal"

###############################################################################


class literal_FALSE(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print "literal"

###############################################################################


class literal_NULL(Node):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1

	def imprimirPostOrden(self,ident):
		self.son1.imprimirPostOrden(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"

		txt += id + " -> " + son1 + "\n\t"

		return id


	#print "literal"

#----------------------------------------------------------------
#----------------------------------------------------------------
class ID(Node):
	def __init__(self, name, lineno):
		self.name = name
		self.lineno = lineno
	def imprimirPostOrden(self, ident):
		print ident + "ID: "+ self.name
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+self.name+"]\n\t"

		return id

class Numero(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "NUM: "+ str(int(self.name))

	def traducir(self):
		global txt
		id = incrementarContador()



		txt += id+"[label= "+str(int(self.name))+"]\n\t"



		return id

class Cad(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "CAD: "+ str(self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+str(self.name)+"]\n\t"
		return id

class True(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "TRUE: "+ str(self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+str(self.name)+"]\n\t"
		return id

class False(Node):
	def __init__(self, name):
		self.name = name

	def imprimirPostOrden(self, ident):
		print ident + "FALSE: "+ str(self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+str(self.name)+"]\n\t"
		return id


class Null(Node):
	def __init__(self):
		self.type = 'void'

	def imprimirPostOrden(self, ident):
		print ident + 'node null'

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+"nodo_nulo"+"]\n\t"
		return id

 
class empty(Node):
	def __init__(self):
		pass
	#'''empty :'''