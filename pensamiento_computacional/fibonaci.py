def recur_fibo(n):
    """
    recur_fibo es simplemente recursibidad fibonacci
    donde calucularemos la secuencia, le pediremos al ususario 
    que ingrese cuantas veces quiere que se calcule y el resultado
    sera la secuencia fibonacci de las veces que el usuario ingreso
    """
    
    if n <= 1:
        return n
    else:
      return(recur_fibo(n - 1) + recur_fibo(n - 2))


def run():
    nterms = int(input('How many terms? '))
    if nterms <= 0:
        print('Please enter a positive Integer')
    else:
        print('Fibonacci Sequence is: ')
        for i in range(nterms):
            print(recur_fibo(i))


if __name__ == '__main__':
    run()