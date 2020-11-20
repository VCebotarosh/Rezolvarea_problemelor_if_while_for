from fractions import Fraction
numarator1,numitor1=eval(input('Dati numaratorul si numitorul primei fractii   = '))
numarator2,numitor2=eval(input('Dati numaratorul si numitorul freactiei a doua   = '))
print('Suma fractiilor este = ',Fraction(numarator1,numitor1)+Fraction(numarator2,numitor2))
print('Produsul fractiilor este = ',Fraction(numarator1,numitor1)*Fraction(numarator2,numitor2))