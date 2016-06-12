# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*- 

import ply.yacc as yacc
import os
import codecs
import re
from analizadorlexico import tokens
from sys import stdin
from ast2 import *

###############################################################################
#																			  
#							  Analizador Sintáctico							  
#																			
#
#									Hecho por:
#
#							Sebastian Ardila Agudelo.
#						   Alejandro Villegas Ocampo.
#
#
#					   Universidad Tecnológica de Pereira.
#									 2016.
#
#
###############################################################################


###############################################################################
#	
#	Tipo de variable = Tupla
#	Nombre de variable = precedence
#	Funcionamiento = 
#						* sirve para darle prioridad a los tokens que sea 
#						necesario
#
###############################################################################
precedence = (
			('left', 'UMINUS'),
			('right', 'IGUAL'),
			('left','OLOGICO'),
			('left', 'ILOGICO'),
			('left', 'IGUALIGUAL', 'DIFERENTE'),
			('left', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL'),
			('left', 'SUM', 'MEN'),
			('left', 'MULT', 'DIV', 'MOD'),
			('right', 'NEGBOOL', 'NEW'),
			('left', 'LCOR', 'RCOR', 'LPAR', 'RPAR','DOT'),
			)

###############################################################################
#	
#	Nombre de funcion = program
#	Funcionamiento = 
#						* identifica una o varias declaraciones de clase
#
###############################################################################

def p_program(p):
	'''program : program classDecl \n'''
	p[0] = program(p[1],p[2], "program")

	#print "program"

###############################################################################
#	
#	Nombre de funcion = programNull
#	Funcionamiento = 
#						* reduce en program
#
###############################################################################

def p_programNull(p):
	'''program : empty'''
	p[0] = Null()

	#print "program null"

###############################################################################
#	
#	Nombre de funcion = classDecl
#	Funcionamiento = 
#						* identifica los componentes de una declaracion de 
#						clase
#
###############################################################################

def p_classDecl(p):
	'''classDecl : CLASS ID extendsIdOp LKEY listFieldOrMethDecl RKEY'''
	p[0] = classDecl(ID(p[2],p.lineno(1)), p[3],p[5], "classDecl")
	
	#print "Declaracion de Clase"

###############################################################################
#	
#	Nombre de funcion = extendsIdOp
#	Funcionamiento = 
#						* identifica dos tokens en la declaracion de clase
#
###############################################################################

def p_extendsIdOp(p):
	'''extendsIdOp : EXTENDS ID'''
	p[0] = extendsIdOp(ID(p[2],p.lineno(1)), "extendsIdOp")

	#print "Extends ID en Declaracion de Clase"

###############################################################################
#	
#	Nombre de funcion = extendsIdOpNull
#	Funcionamiento = 
#						* produccion que genera vacio
#
###############################################################################

def p_extendsIdOpNull(p):
	'''extendsIdOp : empty'''
	p[0] = Null()

	#print 'extendsIdOpNull'

###############################################################################
#	
#	Nombre de funcion = listFieldOrMethDecl
#	Funcionamiento = 
#						* identifica una o varias declaraciones de metodo o 
#						campo
#
###############################################################################

def p_listFieldOrMethDecl(p):
	'''listFieldOrMethDecl : listFieldOrMethDecl fieldOrMethDecl'''
	p[0] = listFieldOrMethDecl(p[1], p[2], "listFieldOrMethDecl")

	#print 'lista de declaraciones de Campo o Metodo'

###############################################################################
#	
#	Nombre de funcion = listFieldOrMethDeclNull
#	Funcionamiento = 
#						* produccion que genera vacio
#
###############################################################################

def p_listFieldOrMethDeclNull(p):
	'''listFieldOrMethDecl : empty'''
	p[0] = Null()

	#print 'listFieldOrMethDeclNull'

###############################################################################
#	
#	Nombre de funcion = fieldOrMethDecl_field
#	Funcionamiento = 
#						* identifica una declaracion de campo
#
###############################################################################

def p_fieldOrMethDecl_field(p):
	'''fieldOrMethDecl : fieldDecl'''
	p[0] = fieldOrMethDecl_field(p[1], "fieldOrMethDecl_field")

	#print 'Declaracion de campo'

###############################################################################
#	
#	Nombre de funcion = listFieldOrMethDecl_meth
#	Funcionamiento = 
#						* identifica una declaracion de metodo
#
###############################################################################

def p_listFieldOrMethDecl_meth(p):
	'''fieldOrMethDecl : methDecl'''
	p[0] = listFieldOrMethDecl_meth(p[1], "listFieldOrMethDecl_meth")

	#print 'Declaracion de metodo'

###############################################################################
#	
#	Nombre de funcion = fieldDecl
#	Funcionamiento = 
#						* identifica una o varias declaraciones de campo con sus 
#						respectivos componentes.
#
###############################################################################

def p_fieldDecl(p):
	'''fieldDecl : type ID COMMA ID listId DOTCOMMA'''
	#name = 
	p[0] = fieldDecl(p[1],ID(p[2],p.lineno(1)),ID(p[4],p.lineno(1)),p[5], "fieldDecl_"+p[2])

	#print 'componentes de declaracion de campo'

###############################################################################
#	
#	Nombre de funcion = listId
#	Funcionamiento = 
#						* identifica uno o varios identificadores separados 
#						por comas
#
###############################################################################

def p_listId(p):
	'''listId : COMMA ID listId'''
	p[0] = listId(ID(p[2],p.lineno(1)),p[3], "List_ID_"+p[2])

	#print 'lista de identificadores'

###############################################################################
#	
#	Nombre de funcion = listIdNull
#	Funcionamiento = 
#						* produccion que genera vacio
#
###############################################################################

def p_listIdNull(p):
	'''listId : empty'''
	p[0] = Null()

	#print "listIdNull"

###############################################################################
#	
#	Nombre de funcion = methDecl
#	Funcionamiento = 
#						* identifica una declaracion de metodo con sus 
#						respectivos componentes
#
###############################################################################

def p_methDecl(p):
	'''methDecl : type ID LPAR formals RPAR block'''
	p[0] = methDecl(p[1],ID(p[2],p.lineno(1)),p[4],p[6], "Meth_Decl_"+p[2])

	#print 'componentes de declaracion de metodo'

###############################################################################
#	
#	Nombre de funcion = formals
#	Funcionamiento = 
#						* identifica un tipo de dato seguido del dato o
#						identificador, seguido o no de una lista con los 
#						mismos elementos. 
#
###############################################################################

def  p_formals(p):
	'''formals : type ID COMMA type ID listTypeId'''
	p[0] = formals(p[1],ID(p[2],p.lineno(1)),p[4],ID(p[5],p.lineno(1)),p[6], "formals_"+p[2])

	#print 'formals'

###############################################################################
#	
#	Nombre de funcion = formalsNull
#	Funcionamiento = 
#						* produccion que genera vacio
#
###############################################################################

def p_formalsNull(p):
	'''formals : empty'''
	p[0] = Null()

	#print "formalsNull"

###############################################################################
#	
#	Nombre de funcion = listTypeId
#	Funcionamiento = 
#						* identifica una produccion que genera un tipo y un ID
#						seguido o no por una lista con los mismos elementos
#
###############################################################################

def p_listTypeId(p):
	'''listTypeId : COMMA type ID listTypeId'''
	p[0] = listTypeId(p[2],ID(p[3],p.lineno(1)),p[4], "List_Type_ID_"+p[3])

	#print 'lista de tipos'

###############################################################################
#	
#	Nombre de funcion = listTypeIdNull
#	Funcionamiento = 
#						* produccion que genera vacio
#
###############################################################################

def p_listTypeIdNull(p):
	'''listTypeId : empty'''
	p[0] = Null()

	#print "listTypeIdNull"

###############################################################################
#	
#	Nombre de funcion = type_INT
#	Funcionamiento = 
#						* identifica una produccion que genera un entero
#
###############################################################################
def p_type_INT(p):
	'''type : INT'''
	p[0] = type_INT(p[1], "type_INT")

	#print 'tipo entero'

###############################################################################
#	
#	Nombre de funcion = type_BOOLEAN
#	Funcionamiento = 
#						* identifica una produccion que genera un booleano
#
###############################################################################

def p_type_BOOLEAN(p):
	'''type : BOOLEAN'''
	p[0] = type_BOOLEAN(p[1], "type_BOOLEAN")

	#print 'tipo booleano'

###############################################################################
#	
#	Nombre de funcion = type_STRING
#	Funcionamiento = 
#						* identifica una produccion que genera un STRING
#
###############################################################################

def p_type_STRING(p):
	'''type : STRING'''
	p[0] = type_STRING(p[1], "type_STRING")

	#print 'tipo string'

###############################################################################
#	
#	Nombre de funcion = type_ID
#	Funcionamiento = 
#						* identifica una produccion que genera un ID
#
###############################################################################

def p_type_type_ID(p):
	'''type : type ID'''
	p[0] = type_type_ID(p[1],ID(p[2],p.lineno(1)), "type_ID")

	#print 'tipo ID'

###############################################################################
#	
#	Nombre de funcion = type_type_LCOR_RCOR
#	Funcionamiento = 
#						* identifica una produccion que genera un par de
#						corchetes
#
###############################################################################

def p_type_type_LCOR_RCOR(p):
	'''type : type LCOR RCOR'''
	p[0] = type_type_LCOR_RCOR(p[1], "type_LCOR_RCOR")

	#print 'tipo []'

###############################################################################
#	
#	Nombre de funcion = block
#	Funcionamiento = 
#						* identifica una produccion que genera un bloque de
#						elementos con sus respectivos componentes
#
###############################################################################

def p_block(p):
	'''block : LKEY varDecl listVarDecl stmt listStmt RKEY'''
	p[0] = block(p[2],p[3],p[4],p[5], "block")

	#print 'block'

###############################################################################
#	
#	Nombre de funcion = listVarDecl
#	Funcionamiento = 
#						* identifica una produccion que genera una declaracion
#						de variable o una posible lista de declaraciones de 
#						variables
#
###############################################################################

def p_listVarDecl(p):
	'''listVarDecl : listVarDecl varDecl \n'''
	p[0] = listVarDecl(p[1],p[2], "list_Var_Decl")

	#print 'lista de declaraciones de variable'

###############################################################################
#	
#	Nombre de funcion = listVarDeclNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################

def p_listVarDeclNull(p):
	'''listVarDecl : empty'''
	p[0] = Null()

	#print "listVarDeclNull"

###############################################################################
#	
#	Nombre de funcion = listStmt
#	Funcionamiento = 
#						* identifica una produccion que genera un statement
#						o una lista de statement
#
###############################################################################

def p_listStmt(p):
	'''listStmt : listStmt stmt'''
	p[0] = listStmt(p[1],p[2], "List_Stmt")

	#print 'lista de statement'

###############################################################################
#	
#	Nombre de funcion = listStmtNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################	

def p_listStmtNull(p):
	'''listStmt : empty'''
	p[0] = Null()
	
	#print "listStmtNull"

###############################################################################
#	
#	Nombre de funcion = varDecl
#	Funcionamiento = 
#						* identifica una produccion que genera una declaracion
#						de variable con sus respectivos componentes
#
###############################################################################	

def p_varDecl(p):
	'''varDecl : type ID equalExprOp COMMA ID equalExprOp listIdEqExprOp DOTCOMMA'''
	p[0] = varDecl(p[1],ID(p[2],p.lineno(1)),p[3],ID(p[5],p.lineno(1)),p[6],p[7], "Var_Decl "+p[2])

	#print 'declaracion de variable'

###############################################################################
#	
#	Nombre de funcion = equalExprOp
#	Funcionamiento = 
#						* identifica una produccion que genera una asignacion
#						de una expresion
#
###############################################################################	

def p_equalExprOp(p):
	'''equalExprOp : IGUAL expr'''
	p[0] = equalExprOp(p[2], "Equal_Expr_OP")

	#print 'asignacion de una expresion'

###############################################################################
#	
#	Nombre de funcion = equalExprOpNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################	

def p_equalExprOpNull(p):
	'''equalExprOp : empty'''
	p[0] = Null()

	#print "equalExprOpNull"

###############################################################################
#	
#	Nombre de funcion = listIdEqExprOp
#	Funcionamiento = 
#						* identifica una produccion que genera una asignacion
#						de una expresion a uno o varios id 
#
###############################################################################	

def p_listIdEqExprOp(p):
	'''listIdEqExprOp : listIdEqExprOp COMMA ID equalExprOp '''
	p[0] = listIdEqExprOp(p[1],ID(p[3],p.lineno(1)),p[4], "List_ID_Equal_Expr_OP")

	#print 'lista asignacion de una o mas expresiones'

###############################################################################
#	
#	Nombre de funcion = listIdEqExprOpNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################	

def p_listIdEqExprOpNull(p):
	'''listIdEqExprOp : empty'''
	p[0] = Null()

	#print "listIdEqExprOpNull"

###############################################################################
#	
#	Nombre de funcion = stmt_assign
#	Funcionamiento = 
#						* identifica una produccion que genera una asignacion
#						seguido de un punto y coma
#
###############################################################################	

def p_stmt_assign(p):
	'''stmt : assign DOTCOMMA'''
	p[0] = stmt_assign(p[1], "Stmt_Assign")

	#print "asignacion stmt"

###############################################################################
#	
#	Nombre de funcion = stmt_call
#	Funcionamiento = 
#						* identifica una produccion que genera un llamado
#						seguido de un punto y coma
#
###############################################################################	

def p_stmt_call(p):
	'''stmt : call DOTCOMMA'''
	p[0] = stmt_call(p[1], "Stmt_Call")

	#print "call stmt"

###############################################################################
#	
#	Nombre de funcion = stmt_RETURN
#	Funcionamiento = 
#						* identifica una produccion que genera un retorno 
#						que puede o no contener lo que retorna
#
###############################################################################	

def p_stmt_RETURN(p):
	'''stmt : RETURN exprOp DOTCOMMA'''
	p[0] = stmt_RETURN(p[2], "Stmt_Return")

	#print "return stmt"

###############################################################################
#	
#	Nombre de funcion = stmt_IF
#	Funcionamiento = 
#						* identifica una produccion que genera condicional
#						if y sus respectivos componentes
#
###############################################################################	

def p_stmt_IF(p):
	'''stmt : IF LPAR expr RPAR stmt elseStmtOp'''
	p[0] = stmt_IF(p[3],p[5],p[6], "Stmt_if")

	#print "if stmt"

###############################################################################
#	
#	Nombre de funcion = stmt_WHILE
#	Funcionamiento = 
#						* identifica una produccion que genera un while y sus
#						respectivos componentes
#
###############################################################################	

def p_stmt_WHILE(p):
	'''stmt : WHILE LPAR expr RPAR stmt'''
	p[0] = stmt_WHILE(p[3],p[5], "Stmt_while")

	#print "while stmt"

###############################################################################
#	
#	Nombre de funcion = stmt_breakOrContinue
#	Funcionamiento = 
#						* identifica una produccion que genera o un break
#						o un continue, pero seguido de un punto y coma.
#
###############################################################################	

def p_stmt_breakOrContinue(p):
	'''stmt : breakOrContinue DOTCOMMA'''
	p[0] = stmt_breakOrContinue(p[1], "Stmt_Break_or_Continue")

	#print "break|continue"

###############################################################################
#	
#	Nombre de funcion = stmt_block
#	Funcionamiento = 
#						* identifica una produccion que genera un bloque de
#						codigo
#
###############################################################################	

def p_stmt_block(p):
	'''stmt : block'''
	p[0] = stmt_block(p[1], "Stmt_Block")

	#print "block stmt"

###############################################################################
#	
#	Nombre de funcion = exprOp
#	Funcionamiento = 
#						* identifica una produccion que genera una expresion
#
###############################################################################	

def p_exprOp(p):
	'''exprOp : expr'''
	p[0] = exprOp(p[1], "Expr_OP")

	#print 'expresion'

###############################################################################
#	
#	Nombre de funcion = exprOpNull
#	Funcionamiento = 
#						* identifica una produccion que genera una vacio
#
###############################################################################	


def p_exprOpNull(p):
	'''exprOp : empty'''
	p[0] = Null()

	#print "exprOpNull"

###############################################################################
#	
#	Nombre de funcion = elseStmtOpElse
#	Funcionamiento = 
#						* identifica una produccion que genera un else
#
###############################################################################	

def p_elseStmtOpElse(p):
	'''elseStmtOp : ELSE'''
	p[0] = elseStmtOpElse(p[1], "Else_Stmt_OP_ELSE")

	#print 'else'

###############################################################################
#	
#	Nombre de funcion = elseStmtOpStmt
#						* identifica una produccion que genera un stmt
#
###############################################################################		

def p_elseStmtOpStmt(p):
	'''elseStmtOp : stmt'''
	p[0] = elseStmtOpStmt(p[1], "Else_Stmt_OP_Stmt")

	#print "stmt"

###############################################################################
#	
#	Nombre de funcion = breakOrContinue_Break
#	Funcionamiento = 
#						* identifica una produccion que genera un break
#
###############################################################################	

def p_breakOrContinue_Break(p):
	'''breakOrContinue : BREAK'''
	p[0] = breakOrContinue_Break(p[1], "BREAK")

	#print 'break'

###############################################################################
#	
#	Nombre de funcion = breakOrContinue_Continue
#	Funcionamiento = 
#						* identifica una produccion que genera un continue
#
###############################################################################	

def p_breakOrContinue_Continue(p):
	'''breakOrContinue : CONTINUE'''
	p[0] = breakOrContinue_Continue(p[1], "CONTINUE")

	#print 'continue'

###############################################################################
#	
#	Nombre de funcion = assign
#	Funcionamiento = 
#						* identifica una produccion que genera una asignacion
#						de una expresion a un tipo de location
#
###############################################################################	

def p_assign(p):
	'''assign : location IGUAL expr'''
	p[0] = assign(p[1],p[3], "assign")

	#print 'asignacion de una expresion a un location'

###############################################################################
#	
#	Nombre de funcion = location_ID
#	Funcionamiento = 
#						* identifica una produccion que genera un identificador
#
###############################################################################

def p_location_ID(p):
	'''location : ID'''
	p[0] = location_ID(ID(p[1],p.lineno(1)), "Location_ID")

	#print "location id"

###############################################################################
#	
#	Nombre de funcion = location_expr_DOT_ID
#	Funcionamiento = 
#						* identifica una produccion que genera un llamado
#						al identificador de una expresion
#
###############################################################################

def p_location_expr_DOT_ID(p):
	'''location : expr DOT ID'''
	p[0] = location_expr_DOT_ID(p[1],ID(p[3],p.lineno(1)), "Location_expr_DOT_ID")

	#print "location expr.id"

###############################################################################
#	
#	Nombre de funcion = location_expr_LCOR_RCOR
#	Funcionamiento = 
#						* identifica una produccion que genera un llamado
#						al indice de una expresion
#
###############################################################################

def p_location_expr_LCOR_RCOR(p):
	'''location : expr LCOR expr RCOR'''
	p[0] = location_expr_LCOR_RCOR(p[1],p[3], "location_expr_LCOR_expr_RCOR")

	#print "location expr [expr]"

###############################################################################
#	
#	Nombre de funcion = call
#	Funcionamiento = 
#						* identifica una produccion que genera un metodo que
#						se le envian parametros
#
###############################################################################

def p_call(p):

	'''call : method LPAR actuals RPAR'''
	p[0] = call(p[1],p[3], "call")

	#print 'call'

###############################################################################
#	
#	Nombre de funcion = method_ID
#	Funcionamiento = 
#						* identifica una produccion que genera un identificador
#
###############################################################################

def p_method_ID(p):
	'''method : ID'''
	p[0] = method_ID(ID(p[1],p.lineno(1)), "method_ID")

	#print 'method ID'

###############################################################################
#	
#	Nombre de funcion = method_expr_DOT_ID
#	Funcionamiento = 
#						* identifica una produccion que genera un llamado
#						al identificador de una expresion
#
###############################################################################

def p_method_expr_DOT_ID(p):
	'''method : expr DOT ID'''
	p[0] = method_expr_DOT_ID(p[1],ID(p[3],p.lineno(1)), "method_expr_dot_ID")

	#print 'method expr.ID'

###############################################################################
#	
#	Nombre de funcion = actuals
#	Funcionamiento = 
#						* identifica una produccion que genera una o varias
#						expresiones separadas por comas
#
###############################################################################

def p_actuals(p):
	'''actuals : expr COMMA expr listExpr'''
	p[0] = actuals(p[1],p[3], "actuals")

	#print 'actuals'

###############################################################################
#	
#	Nombre de funcion = actualsNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################

def p_actualsNull(p):
	'''actuals : empty'''
	p[0] = Null()
	#print "actualsNull"

###############################################################################
#	
#	Nombre de funcion = listExpr
#	Funcionamiento = 
#						* identifica una produccion que genera una lista de
#						expresiones separadas por coma
#
###############################################################################

def p_listExpr(p):
	'''listExpr : COMMA expr listExpr'''
	p[0] = listExpr(p[2],p[3], "List_Expr")

###############################################################################
#	
#	Nombre de funcion = listExprNull
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################

def p_listExprNull(p):
	'''listExpr : empty'''
	p[0] = Null()

	#print "listExprNull"

###############################################################################
#	
#	Nombre de funcion = expr
#	Funcionamiento = 
#						* identifica una produccion que genera un location
#
###############################################################################

def p_expr(p):
	'''expr : location'''
	p[0] = expr(p[1], "expr_location")
	#print "expr LOCATION"

###############################################################################
#	
#	Nombre de funcion = expr_binary_SUM
#	Funcionamiento = 
#						* identifica una produccion que genera un suma de 
#						expresiones
#
###############################################################################

def p_expr_binary_SUM(p):
	'''expr : expr SUM expr'''
	p[0] = expr_binary_SUM(p[1],p[3], "expr_sum_expr")

	#print "expr + expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MEN
#	Funcionamiento = 
#						* identifica una produccion que genera una resta de 
#						expresiones
#
###############################################################################

def p_expr_binary_MEN(p):
	'''expr : expr MEN expr'''
	p[0] = expr_binary_MEN(p[1],p[3], "expr_men_expr")

	#print "expr - expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MULT
#	Funcionamiento = 
#						* identifica una produccion que genera una 
#						multiplicacion de expresiones
#
###############################################################################

def p_expr_binary_MULT(p):
	'''expr : expr MULT expr'''
	p[0] = expr_binary_MULT(p[1],p[3], "expr_mult_expr")

	#print "expr * expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_DIV
#	Funcionamiento = 
#						* identifica una produccion que genera una division
#						de expresiones
#
###############################################################################

def p_expr_binary_DIV(p):
	'''expr : expr DIV expr'''
	p[0] = expr_binary_DIV(p[1],p[3], "expr_div_expr")

	#print "expr / expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MOD
#	Funcionamiento = 
#						* identifica una produccion que genera un modulo
#						entre expresiones
#
###############################################################################

def p_expr_binary_MOD(p):
	'''expr : expr MOD expr'''
	p[0] = expr_binary_MOD(p[1],p[3], "expr_mod_expr")

	#print "expr %  expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_ILOGICO
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						and entre expresiones
#
###############################################################################

def p_expr_binary_ILOGICO(p):
	'''expr : expr ILOGICO expr'''
	p[0] = expr_binary_ILOGICO(p[1],p[3], "expr_and_expr")

	#print "expr && expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_OLOGICO
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						or entre expresiones
#
###############################################################################

def p_expr_binary_OLOGICO(p):
	'''expr : expr OLOGICO expr'''
	p[0] = expr_binary_OLOGICO(p[1],p[3], "expr_or_expr")

	#print "expr || expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MENORQUE
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						menor que entre expresiones
#
###############################################################################

def p_expr_binary_MENORQUE(p):
	'''expr : expr MENORQUE expr'''
	p[0] = expr_binary_MENORQUE(p[1],p[3], "expr_MENORQUE_expr")

	#print "expr < expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MENORIGUAL
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						menor igual entre expresiones
#
###############################################################################

def p_expr_binary_MENORIGUAL(p):
	'''expr : expr MENORIGUAL expr'''
	p[0] = expr_binary_MENORIGUAL(p[1],p[3], "expr_MENORIGUAL_expr")

	#print "expr <= expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MAYORQUE
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						mayor que entre expresiones
#
###############################################################################

def p_expr_binary_MAYORQUE(p):
	'''expr : expr MAYORQUE expr'''
	p[0] = expr_binary_MAYORQUE(p[1],p[3], "expr_MAYORQUE_expr")

	#print "expr > expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_MAYORIGUAL
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						mayor o igual entre expresiones
#
###############################################################################

def p_expr_binary_MAYORIGUAL(p):
	'''expr : expr MAYORIGUAL expr'''
	p[0] = expr_binary_MAYORIGUAL(p[1],p[3], "expr_MAYORIGUAL_expr")

	#print "expr >= expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_IGUALIGUAL
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						igual igual entre expresiones
#
###############################################################################

def p_expr_binary_IGUALIGUAL(p):
	'''expr : expr IGUALIGUAL expr'''
	p[0] = expr_binary_IGUALIGUAL(p[1],p[3], "expr_IGUALIGUAL_expr")

	#print "expr == expr"

###############################################################################
#	
#	Nombre de funcion = expr_binary_DIFERENTE
#	Funcionamiento = 
#						* identifica una produccion que genera una condicion
#						de diferente entre expresiones
#
###############################################################################

def p_expr_binary_DIFERENTE(p):
	'''expr : expr DIFERENTE expr'''
	p[0] = expr_binary_DIFERENTE(p[1],p[3], "exr_DIFERENTE_expr")

	#print "expr != expr"

###############################################################################
#	
#	Nombre de funcion = expr_call
#	Funcionamiento = 
#						* identifica una produccion que genera un call
#
###############################################################################

def p_expr_call(p):
	'''expr : call'''
	p[0] = expr_call(p[1], "expr_call")

	#print "expr call"

###############################################################################
#	
#	Nombre de funcion = expr_this
#	Funcionamiento = 
#						* identifica una produccion que genera un this
#
###############################################################################

def p_expr_this(p):
	'''expr : THIS'''
	p[0] = expr_this(p[1], "expr_this")

	#print "expr this"

###############################################################################
#	
#	Nombre de funcion = expr_new_id
#	Funcionamiento = 
#						* identifica una produccion que genera un nuevo
#						identificador 
#
###############################################################################

def p_expr_new_id(p):
	'''expr : NEW ID LPAR RPAR'''
	p[0] = expr_new_id(ID(p[2],p.lineno(1)), "expr_new_ID LPAR RPAR")

	#print "expr new ID"

###############################################################################
#	
#	Nombre de funcion = expr_new_type
#	Funcionamiento = 
#						* identifica una produccion que genera un nuevo tipo
#
###############################################################################

def p_expr_new_type(p):
	'''expr : NEW type LCOR expr RCOR'''
	p[0] = expr_new_type(p[2],p[4], "expr_new_type")

	#print "expr new type"

###############################################################################
#	
#	Nombre de funcion = expr_DOT_LENGTH
#	Funcionamiento = 
#						* identifica una produccion que genera la longitud
#						de una expresion
#
###############################################################################

def p_expr_DOT_LENGTH(p):
	'''expr : expr DOT LENGTH'''
	p[0] = expr_DOT_LENGTH(p[1], "expr_DOT_length")

	#print "expr.length"

###############################################################################
#	
#	Nombre de funcion = expr_uminus
#	Funcionamiento = 
#						* identifica una produccion que genera cambio de signo
#						en una expresion
#
###############################################################################

def p_expr_uminus(p):
	'''expr : UMINUS expr'''
	p[0] = expr_uminus(p[2], "minus_expr")

	#print "- expr"

###############################################################################
#	
#	Nombre de funcion = expr_negbool
#	Funcionamiento = 
#						* identifica una produccion que genera la negacion
#						de una expresion
#
###############################################################################

def p_expr_negbool(p):
	'''expr : NEGBOOL expr'''
	p[0] = expr_negbool(p[2], "negbool_expr")

	#print "! expr"

###############################################################################
#	
#	Nombre de funcion = expr_literal
#	Funcionamiento = 
#						* identifica una produccion que genera un literal
#
###############################################################################

def p_expr_literal(p):
	'''expr : literal'''
	p[0] = expr_literal(p[1], "expr_literal")

	#print "expr literal"

###############################################################################
#	
#	Nombre de funcion = expr_expr
#	Funcionamiento = 
#						* identifica una produccion que genera una expresion
#						entre parentesis
#
###############################################################################

def p_expr_expr(p):
	'''expr : LPAR expr RPAR'''
	p[0] = expr_expr(p[2], "(LPAR_expr_RPAR")

	#print "expr (expr)"



###############################################################################
#	
#	Nombre de funcion = literal_numero
#	Funcionamiento = 
#						* identifica una produccion que genera su 
#						correspondiente literal
#
###############################################################################

def p_literal_NUMERO(p): 

	'''literal : NUMERO'''
	
	p[0] = literal_CAD(Numero(p[1]), "literal_numero")

	#print "literal"

###############################################################################
#	
#	Nombre de funcion = literal_CAD
#	Funcionamiento = 
#						* identifica una produccion que genera su 
#						correspondiente literal
#
###############################################################################

def p_literal_CAD(p): 

	'''literal : CAD'''
	
	p[0] = literal_CAD(Cad(p[1]), "literal_cad")

	#print "literal"

###############################################################################
#	
#	Nombre de funcion = literal_TRUE
#	Funcionamiento = 
#						* identifica una produccion que genera su 
#						correspondiente literal
#
###############################################################################

def p_literal_TRUE(p): 

	'''literal : TRUE'''
	
	p[0] = literal_TRUE(True(p[1]), "literal_true")

	#print "literal"

###############################################################################
#	
#	Nombre de funcion = literal_FALSE
#	Funcionamiento = 
#						* identifica una produccion que genera su 
#						correspondiente literal
#
###############################################################################

def p_literal_FALSE(p): 

	'''literal : FALSE'''
	
	p[0] = literal_FALSE(False(p[1]), "literal_false")

	#print "literal"

###############################################################################
#	
#	Nombre de funcion = literal
#	Funcionamiento = 
#						* identifica una produccion que genera su 
#						correspondiente literal
#
###############################################################################

def p_literal_NULL(p): 

	'''literal : NULL'''
	
	p[0] = literal_NULL(p[1], "literal_null")

	#print "literal"

###############################################################################
#	
#	Nombre de funcion = empty
#	Funcionamiento = 
#						* identifica una produccion que genera vacio
#
###############################################################################

def p_empty(p):
	'''empty :'''
	#p[0] = empty()
	pass

def p_error(p):

	print "Error de sintaxis ", p
	print "Error en la linea "+str(p.lineno)
	# print "Error: "
	# while True:
	# 	tok = parser.token()
	# 	if not tok : break

###############################################################################
#	
#	Nombre de funcion = buscarFicheros
#	Funcionamiento = 
#						* funcion que lista las pruebas y las muestra en 
#						pantalla para elegir entre una de ellas y analizarla
#
###############################################################################

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)
	
	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del Test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]
		
#CREAR SINTACTICO---------------------------------


print "\nBienvenido al Analizador Sintáctico."
print "Por favor, elige la prueba"
print "Presiona Ctrl+z para salir\n"


directorio = "/Users/sebas/Documents/Compiladores/Tercera-Entrega/TerceraEntrega Compiladores/test/"
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
#cadena = str(cadena)
fp.close()

yacc.yacc()

raiz = yacc.parse(cadena, debug=1)
#raiz.imprimirPostOrden(" ")
#print raiz.traducir()

graphFile = open('graphvizthree.vz','w')
graphFile.write(raiz.traducir())
graphFile.close
#raiz.imprimirPostOrden()

#CONSTRUIR EL ANALIZADOR PARSER---------------
#parser = yacc.yacc()

#result = parser.parse(stdin.read(),lexer=le)
#IMPRIME EL PARSER----------------------------
#print(result)