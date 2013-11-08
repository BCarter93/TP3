import ast
print
print("   Bienvenido al analizador de ambientes Estaticos y Dinamicos")

global Estatico
global Dinamico
global EstaticoLet
global DinamicoLet
Estatico= []
Dinamico= []
EstaticoLet= []
DinamicoLet= []

def Inicio():
	print
	NombreArchivo=input("Ingrese el nombre del archivo que desea analizar: ") ##RAWIMPUT
	return LeerArchivo(NombreArchivo)

def LeerArchivo(NombreArchivo):
	Archivo=open(NombreArchivo,"r")
	Lineas=Archivo.read()
	Archivo.close()
	return CrearListaInfo(Lineas)

def CrearListaInfo(Lineas):
        Tokens=Lineas.replace("\n"," ")
        Tokens=Tokens.replace("\t"," ")		
        Tokens=Tokens.replace("  "," ")		
        Tokens=Tokens.split(" ")
        print (Tokens)
        return BuscarValores(Tokens,0)

def BuscarValores(Tokens,indicadorLet):
        i=0
        while i<len(Tokens):
                if Tokens[i]=="val" and Tokens[i+2]=="=":
                        if Tokens[i+3]=="if":
                                PosicionEnd=VerificarElseLet(Tokens[i+3:])
                                if PosicionEnd!=0:
                                        ValorDinamico=EvaluarIf[Tokens[i+3]:PosicionEnd+i+3]
                                        global Dinamico
                                        global Estatico
                                        Dinamico+=[[Tokens[i+1],ValorDinamico,""]]
                                        Estatico+=[[Tokens[i+1],VerificarTipo(ValorDinamico),""]]
                                        i+=PosicionEnd+i+3
                                        print(Dinamico)
                                        print(Estatico)
                                else:
                                        PosicionElse=VerificarElse(Tokens[i+3:])
                                        ValorDinamico=EvaluarIf[Tokens[i+3]:PosicionElse+i+3]
                                        global Dinamico
                                        global Estatico
                                        Dinamico+=[[Tokens[i+1],ValorDinamico,""]]
                                        Estatico+=[[Tokens[i+1],VerificarTipo(ValorDinamico),""]]
                                        i+=PosicionElse+i+3
                                        print(Dinamico)
                                        print(Estatico)
                        else:
                                global Dinamico
                                global Estatico
                                Dinamico+=[[Tokens[i+1],Tokens[i+3],""]]
                                Estatico+=[[Tokens[i+1],VerificarTipo(Tokens[i+3]),""]]
                                i+=4
                                print(Dinamico)
                                print(Estatico)
        return Imprimir()


def VerificarElseLet(Tokens):
        i=0
        while i<len(Tokens):
                if Tokens[i]=="else" and Tokens[i+1]=="let":
                        j=i+2
                        while Tokens[j]!="end":
                                j+=1
                        return j
                else:
                        i+=1
        return 0

def ExpresionLet(Tokens):
        i=1
        while i<len(Tokens):
                if Tokens[i]!="let":
                        i+=1
                else:
                        Let=Tokens[1:i]
                        In=Tokens[i+1:-1]
                        i+=1000000
                        
def EvaluarIf(Tokens):
        i=1
        while i<len(Tokens):
                if Tokens[i]!="then":
                        i+=1
                else:
                        If=Tokens[1:i]
                        Then=Tokens[i+1:-1]
                        i+=1000000
        VerificarIf(If)
                        
def VerificarElse(Tokens):
        i=0
        while i<len(Tokens):
                if Tokens[i]=="else":
                        j=i+1
                        while Tokens[j]!="=":
                                j+=1
                        k=j+1
                        while k<len(Tokens):
                                if Tokens[k]!="eval" or Tokens[k]!="if":
                                        k+=1
                                else:
                                        return k-1
                        return k-1
                else:
                        i+=1
        return 0

def VerificarTipo(Dato):  ###Falta sgragar mas tipos
        try:
                if isinstance(int(Dato),int):
                        return "int"
        except:
                x=ast.literal_eval(Dato)
                print(x)
                if type(x) is list:
                        return "list"
                else:
                        return "str"

                

def Espacios():
        print()
        print()
        print()
        return Inicio()

def Imprimir():
	print
	print(" Variable    Ambiente Estatico     Ambiente Dinamico")
	global Estatico
	for i in range(0,len(Estatico)):
		print("     "+Estatico[i][0]+"              "+Estatico[i][1]+ "                  "+str(Dinamico[i][1]))
	return Espacios()

Inicio()
