import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("../../assets/StudentPerformanceFactors.csv", sep=",")

# ================================= 5 Perguntas principais =================================
# 1.Como a renda familiar influencia o desempenho acadêmico e o acesso a recursos educacionais?

# 2.O envolvimento dos pais e o nível de escolaridade parental reduzem desigualdades de desempenho entre alunos?

# 3.Há disparidades de desempenho entre estudantes de escolas públicas e privadas?
# Variáveis
public = ds[ds["School_Type"] == "Public"]["Exam_Score"]
private = ds[ds["School_Type"] == "Private"]["Exam_Score"]
medias = ds.groupby("School_Type")["Exam_Score"].mean()

# Console
print("Notas das escolas publicas:\n")
print(public,"\n")
print("Notas das escolas privadas:\n")
print(private,"\n")
print("\nMédia das notas por tipo de escola:\n")
print(medias)

# Grafico
import matplotlib.pyplot as plt

# gráfico de barras
plt.figure(figsize=(6, 4))
medias.plot(kind="bar", color=["skyblue", "salmon"])

plt.title("Média das Notas por Tipo de Escola")
plt.ylabel("Média do Exam_Score")
plt.xlabel("Tipo de Escola")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()



# 4.Estudantes sem acesso à internet têm desempenho inferior, e isso reflete uma exclusão digital?

# 5.A distância da escola impacta negativamente o desempenho e a frequência, especialmente em áreas rurais?

# ================================= 5 Perguntas secundarias =================================
# 10 Perguntas para Análise do Dataset:
#     Qual a relação entre horas de estudo e desempenho no exame?
#         Existe correlação positiva entre horas estudadas e notas?

#     Como a frequência escolar impacta o desempenho acadêmico?
#         Estudantes com maior frequência têm notas significativamente melhores?

#     Qual gênero apresenta melhor desempenho médio nas avaliações?
#         Há diferença significativa entre homens e mulheres?

#     Qual o perfil de sono dos melhores estudantes?
#         Há um número ideal de horas de sono associado a melhores notas?

#     Qual o nível de motivação mais comum entre os estudantes e como isso afeta suas notas?
#         A motivação influencia diretamente nos resultados?

#     A participação em atividades extracurriculares melhora o desempenho acadêmico?
#         Estudantes que praticam atividades extras têm melhor rendimento?

#     Dentre todos os fatores analisados, qual tem a maior correlação com o sucesso no exame?
#         Qual é o fator mais determinante para o bom desempenho?
