import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("../../assets/student-por.csv", sep=",")

# ================================= 5 Perguntas principais =================================
# 1. Como o nível de escolaridade dos pais influencia o desempenho acadêmico dos estudantes?
# infos que podem ajudar:

# 2. Há relação entre o tempo de estudo semanal e as notas finais (G3)?
# infos que podem ajudar: final grade (numeric: from 0 to 20, output target)

# 3. O apoio familiar (famsup) afeta positivamente o rendimento escolar?
# infos que podem ajudar: famsup=5family educational support (binary: yes or no)

# 4. O acesso à internet em casa está associado a melhores resultados escolares?
# infos que podem ajudar:

# 5. A distância entre casa e escola (traveltime) interfere no desempenho do aluno?
# infos que podem ajudar:

# ================================= 5 Perguntas secundarias =================================
# 6. O tamanho da família (famsize) impacta o tempo dedicado aos estudos?
# infos que podem ajudar: famsize=family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)

# 7. Alunos que participam de atividades extracurriculares (activities) apresentam melhor desempenho escolar?
# infos que podem ajudar: activities=extra-curricular activities (binary: yes or no)
# Agrupar por 'activities' e calcular a média de G3
print("\nAlunos que participam de atividades extracurriculares (activities) apresentam melhor desempenho escolar?")
media_por_grupo = ds.groupby('activities')['G3'].mean()
mediaYesActivities = media_por_grupo['yes']
mediaNoActivities = media_por_grupo['no']
print("Médias das notas finais (G3) por grupo: ")
print("Média das que fizeram atividades: ",mediaYesActivities)
print("Média das que não fizeram atividades: ",mediaNoActivities)
if mediaYesActivities > mediaNoActivities:
    print("Conclusão: Alunos que participam de atividades extracurriculares apresentam melhor desempenho escolar.")
elif mediaYesActivities < mediaNoActivities:
    print("Conclusão: Alunos que participam de atividades extracurriculares apresentam desempenho inferior.")
else:
    print("Conclusão: Não há diferença significativa no desempenho escolar entre os grupos.")

# 8. Há uma correlação entre o consumo de álcool (Dalc, Walc) e as notas finais?
# infos que podem ajudar: Dalc=workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
# Walc=weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)

# 9. O status de relacionamento dos pais (pstatus) influencia a motivação e desempenho dos estudantes?
# infos que podem ajudar: pstatus=parent's cohabitation status (binary: 'T' - living together or 'A' - apart)

# 10. Alunos que desejam cursar o ensino superior (higher) obtêm notas mais altas por maior motivação?
# infos que podem ajudar: