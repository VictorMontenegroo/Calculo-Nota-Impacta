# Informar as 4 maiores notas das ACs
acs = []
for i in range(4):
    nota_ac = float(input(f"Qual a nota da AC{i+1}? "))
    acs.append(nota_ac)

media_acs = sum(sorted(acs)[-4:]) / 4 * 0.3

# Informar as 2 maiores notas da prova PAI
pais = []
for i in range(2):
    nota_pai = float(input(f"Qual a nota da prova PAI {i+1}? "))
    pais.append(nota_pai)

media_pai = sum(sorted(pais)[-2:]) / 2 * 0.4

#Informar nota final
prova_final = float(input("Qual a nota da prova final? "))
media_final = prova_final * 0.4

resultado_final = media_acs + media_pai + media_final

if resultado_final >= 6:
    print("Aprovado")

print(f"Resultado final: {resultado_final:.2f}")