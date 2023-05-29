# Informar as 4 maiores notas das ACs
AC1 = float(input("Qual a nota da AC1 ? "))
AC2 = float(input("Qual a nota da AC2 ? "))
AC3 = float(input("Qual a nota da AC3 ? "))
AC4 = float(input("Qual a nota da AC4 ? "))

Media_ACs = (((AC1+AC2+AC3+AC4) / 4) * 0.30)

# Informar as 2 maiores notas da prova PAI

PAI1 = float(input("Qual a nota da prova pai 1 ? "))
PAI2 = float(input("Qual a nota da prova pai 2 ? "))

Media_PAI = (((PAI1 + PAI2) / 2) * 0.4) 
Media_PAI_formatada = "{:.2f}".format(Media_PAI)

MediasProvisorias = float(Media_ACs) + float(Media_PAI_formatada)
if MediasProvisorias >= 6:
    print("Aprovado")

print(Media_ACs)
print( Media_PAI_formatada)
print(MediasProvisorias)