import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("../../assets/student-por.csv", sep=",")

# ================================= 5 Perguntas principais =================================
# 1. Como o nível de escolaridade dos pais influencia o desempenho acadêmico dos estudantes?
# 2. Há relação entre o tempo de estudo semanal e as notas finais (G3)?
# 3. O apoio familiar (famsup) afeta positivamente o rendimento escolar?
# 4. O acesso à internet em casa está associado a melhores resultados escolares?
# 5. A distância entre casa e escola (traveltime) interfere no desempenho do aluno?

# ================================= 5 Perguntas secundarias =================================
# 6. O tamanho da família (famsize) impacta o tempo dedicado aos estudos?
# 7. Alunos que participam de atividades extracurriculares (activities) apresentam melhor desempenho escolar?
# 8. Há uma correlação entre o consumo de álcool (Dalc, Walc) e as notas finais?
# 9. O status de relacionamento dos pais (pstatus) influencia a motivação e desempenho dos estudantes?
# 10. Alunos que desejam cursar o ensino superior (higher) obtêm notas mais altas por maior motivação?