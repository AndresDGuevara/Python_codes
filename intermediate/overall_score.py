#A partir del ejercicio anterior, vamos a suponer que cada número es una nota, 
# y lo que queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual: *
 #   La primera nota vale un 15% del total
  #  La segunda nota vale un 35% del total
   # La tercera nota vale un 50% del total

print( "{:>20}".format("Hello Students \n") )

print( "{:>20}".format("First Score is Worth 15% of the Total ") )
Score_1 = float(input('First Test Score: '))

print( "\n {:>20}".format("Second Score is Worth 35% of the Total ") )
Score_2 = float(input('Second Test Score: '))

print( "\n {:>20}".format("Third Score is Worth 50% of the Total ") )
Score_3 = float(input('Third Test Score: '))

o_v = (Score_1 * 0.15) + (Score_2 * 0.35) + (Score_3 * 0.50)
print("\n Overall Score is: ", o_v)