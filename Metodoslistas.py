class ListasPOO:
  def ingreso(self,L,tam):
    i=0
    while(i<tam):
      num=int(input("ingrese el dato: "))
      L.append(num)
      i=i+1
  def imprimir(self, L):
    print(L)
  def factorial(self, num):
    i=1
    fact=1
    while(i<=num):
      fact=fact*i
      i=i+1
    return fact
  def fibonacci(self, tam):
    fibo=[0]*tam
    fibo[0]=1
    fibo[1]=1
    for i in range(2,tam):
      fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo
