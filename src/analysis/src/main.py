import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ================================= Carregar o dataset =================================

ds = pd.read_csv("C:/Users/tobia/OneDrive/Documents/Student-Performance-Factors/src/assets/student-por.csv", sep=",")

# ================================= Renomear colunas =================================

ds.rename(columns={
"school": "Escola",
"sex": "Sexo",
"age": "Idade",
"address": "Endereco",
"famsize": "Tamanho_Familia",
"Pstatus": "Status_Pais",
"Medu": "Escolaridade_Mae",
"Fedu": "Escolaridade_Pai",
"Mjob": "Trabalho_Mae",
"Fjob": "Trabalho_Pai",
"reason": "Razao_Escolha",
"guardian": "Responsavel",
"traveltime": "Tempo_Deslocamento",
"studytime": "Tempo_Estudo",
"failures": "Reprovacoes",
"schoolsup": "Suporte_Escolar",
"famsup": "Suporte_Familiar",
"paid": "Aulas_Pagas",
"activities": "Atividades_Extra",
"nursery": "Creche",
"higher": "Desejo_Superior",
"internet": "Internet_Casa",
"romantic": "Relacionamento",
"famrel": "Relacao_Familiar",
"freetime": "Tempo_Livre",
"goout": "Sair_Amigos",
"Dalc": "Alcool_Semana",
"Walc": "Alcool_FimSemana",
"health": "Saude",
"absences": "Faltas",
"G1": "Nota1",
"G2": "Nota2",
"G3": "Nota_Final"
}, inplace=True)

# Preparar dados de escolaridade
def categorizar_escolaridade(nivel):
    if nivel == 0:
        return 'Nenhuma'
    elif nivel <= 2:
        return 'Básica'
    elif nivel == 3:
        return 'Média'
    else:
        return 'Superior'

ds['Escolaridade_Mae_Cat'] = ds['Escolaridade_Mae'].apply(categorizar_escolaridade)
ds['Escolaridade_Pai_Cat'] = ds['Escolaridade_Pai'].apply(categorizar_escolaridade)
ds['Max_Escolaridade_Pais'] = ds[['Escolaridade_Mae', 'Escolaridade_Pai']].max(axis=1)
ds['Max_Escolaridade_Cat'] = ds['Max_Escolaridade_Pais'].apply(categorizar_escolaridade)

# ================================= Funções para criar gráficos individuais =================================

def grafico_1(ax=None):
    """Escolaridade dos pais (Média das notas finais)"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    media_escolaridade = ds.groupby('Max_Escolaridade_Cat')['Nota_Final'].agg(['mean', 'count'])
    media_escolaridade = media_escolaridade.sort_values('mean', ascending=False)
    
    colors = ['#1B5E20', '#388E3C', '#66BB6A', '#A5D6A7']
    ax.pie(media_escolaridade['count'], labels=[cat for cat in media_escolaridade.index], 
            autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title('1. Escolaridade máxima dos pais vs Nota final\n(Distribuição de alunos)', 
                 fontsize=11, fontweight='bold')
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_2(ax=None):
    """Tempo de estudo vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    # Boxplot para mostrar distribuição das notas por tempo de estudo
    dados_tempo = [ds[ds['Tempo_Estudo'] == i]['Nota_Final'].values for i in range(1, 5)]
    bp = ax.boxplot(dados_tempo, labels=['1', '2', '3', '4'], patch_artist=True)
    
    for patch in bp['boxes']:
        patch.set_facecolor('#2196F3')
        patch.set_alpha(0.7)
    
    ax.set_title('2. Tempo de estudo vs Nota final')
    ax.set_xlabel('Tempo de estudo (1–4)')
    ax.set_ylabel('Nota final')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_3(ax=None):
    """Apoio familiar vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    ds.groupby('Suporte_Familiar')['Nota_Final'].mean().plot(kind='bar', ax=ax, color=['#FFC107', '#03A9F4'])
    ax.set_title('3. Apoio familiar vs Nota final')
    ax.set_xlabel('Suporte familiar')
    ax.set_ylabel('Nota média')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_4(ax=None):
    """Internet em casa vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    ds.groupby('Internet_Casa')['Nota_Final'].mean().plot(kind='bar', ax=ax, color=['#9C27B0', '#00BCD4'])
    ax.set_title('4. Internet em casa vs Nota final')
    ax.set_xlabel('Internet em casa')
    ax.set_ylabel('Nota média')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_5(ax=None):
    """Tempo de deslocamento vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    # Boxplot para mostrar distribuição das notas por tempo de deslocamento
    dados_deslocamento = [ds[ds['Tempo_Deslocamento'] == i]['Nota_Final'].values for i in range(1, 5)]
    bp = ax.boxplot(dados_deslocamento, labels=['1', '2', '3', '4'], patch_artist=True)
    
    for patch in bp['boxes']:
        patch.set_facecolor('#E91E63')
        patch.set_alpha(0.7)
    
    ax.set_title('5. Tempo de deslocamento vs Nota final')
    ax.set_xlabel('Tempo de deslocamento (1–4)')
    ax.set_ylabel('Nota final')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_6(ax=None):
    """Tamanho da família vs tempo de estudo"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    media_familia = ds.groupby('Tamanho_Familia')['Tempo_Estudo'].mean()
    media_familia.plot(kind='bar', ax=ax, color=['#4CAF50', '#2196F3'])
    ax.set_title('6. Tamanho da família vs tempo de estudo')
    ax.set_xlabel('Tamanho da família')
    ax.set_ylabel('Tempo de estudo médio')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_7(ax=None):
    """Atividades extracurriculares vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    media_atividades = ds.groupby('Atividades_Extra')['Nota_Final'].mean()
    media_atividades.plot(kind='bar', ax=ax, color=['#FFC107', '#03A9F4'])
    ax.set_title('7. Atividades extracurriculares vs Nota final')
    ax.set_xlabel('Atividades extracurriculares')
    ax.set_ylabel('Nota média')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_8(ax=None):
    """Consumo de álcool vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    # Calcular média das notas por nível de consumo
    media_semana = ds.groupby('Alcool_Semana')['Nota_Final'].mean()
    media_fds = ds.groupby('Alcool_FimSemana')['Nota_Final'].mean()
    
    x = np.arange(1, 6)
    width = 0.35
    
    ax.bar(x - width/2, media_semana, width, label='Durante semana', color='#E91E63', alpha=0.8)
    ax.bar(x + width/2, media_fds, width, label='Fim de semana', color='#9C27B0', alpha=0.8)
    
    ax.set_title('8. Consumo de álcool vs Nota final')
    ax.set_xlabel('Nível de consumo (1–5)')
    ax.set_ylabel('Nota média')
    ax.set_xticks(x)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_9(ax=None):
    """Status dos pais vs Estudo e nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    media_status = ds.groupby('Status_Pais')[['Tempo_Estudo', 'Nota_Final']].mean()
    media_status.plot(kind='bar', ax=ax, color=['#8BC34A', '#00BCD4'])
    ax.set_title('9. Status dos pais vs Estudo e nota final')
    ax.set_xlabel('Status dos pais (Juntos/Apartados)')
    ax.set_ylabel('Média')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

def grafico_10(ax=None):
    """Desejo de ensino superior vs Nota final"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    ds.groupby('Desejo_Superior')['Nota_Final'].mean().plot(kind='bar', ax=ax, color=['#009688', '#CDDC39'])
    ax.set_title('10. Desejo de ensino superior vs Nota final')
    ax.set_xlabel('Desejo de ensino superior')
    ax.set_ylabel('Nota média')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if ax is None:
        plt.tight_layout()
    return ax

# ================================= Função para exibir gráfico escolhido =================================

def exibir_grafico(numero):
    graficos = {
        1: grafico_1,
        2: grafico_2,
        3: grafico_3,
        4: grafico_4,
        5: grafico_5,
        6: grafico_6,
        7: grafico_7,
        8: grafico_8,
        9: grafico_9,
        10: grafico_10
    }
    
    if numero == 0:
        # Exibir todos os gráficos
        fig, axes = plt.subplots(2, 5, figsize=(22, 8))
        axes = axes.ravel()
        
        for i, func in graficos.items():
            func(axes[i-1])
        
        plt.tight_layout()
        plt.show()
    elif numero in graficos:
        graficos[numero]()
        plt.show()
# ================================= Função para salvar todos os gráficos =================================

def salvar_graficos(pasta_destino="graficos"):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta '{pasta_destino}' criada.")
    
    graficos = {
        1: ("grafico_1_escolaridade_pais", grafico_1),
        2: ("grafico_2_tempo_estudo", grafico_2),
        3: ("grafico_3_apoio_familiar", grafico_3),
        4: ("grafico_4_internet_casa", grafico_4),
        5: ("grafico_5_tempo_deslocamento", grafico_5),
        6: ("grafico_6_tamanho_familia", grafico_6),
        7: ("grafico_7_atividades_extra", grafico_7),
        8: ("grafico_8_consumo_alcool", grafico_8),
        9: ("grafico_9_status_pais", grafico_9),
        10: ("grafico_10_desejo_superior", grafico_10)
    }
        
    for numero, (nome, func) in graficos.items():
        fig, ax = plt.subplots(figsize=(10, 7))
        func(ax)
        
        caminho = os.path.join(pasta_destino, f"{nome}.png")
        plt.savefig(caminho, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Gráfico {numero} salvo: {caminho}")
    
    fig, axes = plt.subplots(2, 5, figsize=(22, 8))
    axes = axes.ravel()
    
    for i, (nome, func) in graficos.items():
        func(axes[i-1])
    
    plt.tight_layout()
    caminho_completo = os.path.join(pasta_destino, "todos_graficos.png")
    plt.savefig(caminho_completo, dpi=300, bbox_inches='tight')
    plt.close()    

salvar_graficos("src/analysis/graphics")  # Salva