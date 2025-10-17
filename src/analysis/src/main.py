import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================================= Carregar o dataset =================================
ds = pd.read_csv("/home/tobias/Documentos/Student-Performance-Factors/src/assets/student-por.csv", sep=",")

# ================================= Criar figura única =================================
fig, axes = plt.subplots(2, 5, figsize=(22, 8))
axes = axes.ravel()

# ------------------------------------------ 1 -----------------------------------------------------------
ds.groupby(['Medu', 'Fedu'])['G3'].mean().plot(kind='bar', ax=axes[0], color='#4CAF50')
axes[0].set_title('1. Escolaridade dos pais vs G3')
axes[0].set_xlabel('Medu/Fedu')
axes[0].set_ylabel('Nota média')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 2 -----------------------------------------------------------
axes[1].scatter(ds['studytime'], ds['G3'], alpha=0.6, color='#2196F3')
axes[1].set_title('2. Tempo de estudo vs G3')
axes[1].set_xlabel('Tempo de estudo (1–4)')
axes[1].set_ylabel('Nota final (G3)')
axes[1].grid(True, linestyle='--', alpha=0.7)

# ------------------------------------------ 3 -----------------------------------------------------------
ds.groupby('famsup')['G3'].mean().plot(kind='bar', ax=axes[2], color=['#FFC107', '#03A9F4'])
axes[2].set_title('3. Apoio familiar vs G3')
axes[2].set_xlabel('famsup')
axes[2].set_ylabel('Nota média')
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 4 -----------------------------------------------------------
ds.groupby('internet')['G3'].mean().plot(kind='bar', ax=axes[3], color=['#9C27B0', '#00BCD4'])
axes[3].set_title('4. Internet em casa vs G3')
axes[3].set_xlabel('internet')
axes[3].set_ylabel('Nota média')
axes[3].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 5 -----------------------------------------------------------
axes[4].scatter(ds['traveltime'], ds['G3'], alpha=0.6, color='#E91E63')
axes[4].set_title('5. Tempo de deslocamento vs G3')
axes[4].set_xlabel('traveltime (1–4)')
axes[4].set_ylabel('Nota final (G3)')
axes[4].grid(True, linestyle='--', alpha=0.7)

# ------------------------------------------ 6 -----------------------------------------------------------
mediaFamsize = ds.groupby('famsize')['studytime'].mean()
mediaFamsize.plot(kind='bar', ax=axes[5], color=['#4CAF50', '#2196F3'])
axes[5].set_title('6. Tamanho da família vs tempo de estudo')
axes[5].set_xlabel('famsize')
axes[5].set_ylabel('Tempo de estudo médio')
axes[5].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 7 -----------------------------------------------------------
mediaActivities = ds.groupby('activities')['G3'].mean()
mediaActivities.plot(kind='bar', ax=axes[6], color=['#FFC107', '#03A9F4'])
axes[6].set_title('7. Atividades extracurriculares vs G3')
axes[6].set_xlabel('activities')
axes[6].set_ylabel('Nota média')
axes[6].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 8 -----------------------------------------------------------
axes[7].scatter(ds['Dalc'], ds['G3'], alpha=0.6, color='#E91E63', label='Dalc')
axes[7].scatter(ds['Walc'], ds['G3'], alpha=0.6, color='#9C27B0', label='Walc')
axes[7].set_title('8. Consumo de álcool vs G3')
axes[7].set_xlabel('Nível de consumo (1–5)')
axes[7].set_ylabel('Nota final (G3)')
axes[7].legend()
axes[7].grid(True, linestyle='--', alpha=0.7)

# ------------------------------------------ 9 -----------------------------------------------------------
mediaStatus = ds.groupby('Pstatus')[['studytime', 'G3']].mean()
mediaStatus.plot(kind='bar', ax=axes[8], color=['#8BC34A', '#00BCD4'])
axes[8].set_title('9. Status dos pais vs Estudo e G3')
axes[8].set_xlabel('Pstatus (T/A)')
axes[8].set_ylabel('Média')
axes[8].grid(axis='y', linestyle='--', alpha=0.7)

# ------------------------------------------ 10 ----------------------------------------------------------
ds.groupby('higher')['G3'].mean().plot(kind='bar', ax=axes[9], color=['#009688', '#CDDC39'])
axes[9].set_title('10. Desejo de ensino superior vs G3')
axes[9].set_xlabel('higher')
axes[9].set_ylabel('Nota média')
axes[9].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
