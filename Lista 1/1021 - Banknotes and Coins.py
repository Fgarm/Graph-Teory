valor = float(input())

cems = 0
cinquentas = 0
vintes = 0
dezs = 0
cincos = 0
dois = 0
uns = 0
meios = 0
quartos = 0
decimos = 0
cincocents = 0
centavos = 0

while(valor>=100):
    valor -= 100
    cems += 1
    
while(valor>=50):
    valor -= 50
    cinquentas += 1

while(valor>=20):
    valor -= 20
    vintes += 1

while(valor>=10):
    valor -= 10
    dezs += 1

while(valor>=5):
    valor -= 5
    cincos += 1

while(valor>=2):
    valor -= 2
    dois += 1

while(valor>=1):
    valor -= 1
    uns += 1

while(valor>=0.5):
    valor -= 0.5
    meios += 1

while(valor>=0.25):
    valor -= 0.25
    quartos += 1

while(valor>=0.10):
    valor -= 0.10
    decimos += 1

while(valor>=0.05):
    valor -= 0.05
    cincocents += 1

while(valor>0.009):
    valor -= 0.01
    centavos += 1

print(
"NOTAS:\n"
+str(cems)+" nota(s) de R$ 100.00\n"
+str(cinquentas)+" nota(s) de R$ 50.00\n"
+str(vintes)+" nota(s) de R$ 20.00\n"
+str(dezs)+" nota(s) de R$ 10.00\n"
+str(cincos)+" nota(s) de R$ 5.00\n"
+str(dois)+" nota(s) de R$ 2.00\n"
"MOEDAS:\n"
+str(uns)+" moeda(s) de R$ 1.00\n"
+str(meios)+" moeda(s) de R$ 0.50\n"
+str(quartos)+" moeda(s) de R$ 0.25\n"
+str(decimos)+" moeda(s) de R$ 0.10\n"
+str(cincocents)+" moeda(s) de R$ 0.05\n"
+str(centavos)+" moeda(s) de R$ 0.01")