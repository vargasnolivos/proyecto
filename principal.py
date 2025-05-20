from Metodoslistas import ListasPOO
tam=int(input("ingrese un tamaño de la lista "))
List=[]
c=ListasPOO()
c.ingreso(List,tam)
c.imprimir(List)
print(c.factorial(tam))
print(c.fibonacci(tam))