#TOLERÂNCIA ZERO AO DESMATAMENTO ILEGAL E AOS INCÊNDIOS FLORESTAIS
'''A base de dados fornecida se refere a um plano de ação intitulado "Tolerância Zero ao Desmatamento Ilegal e aos Incêndios Florestais". Este plano contém informações sobre diversos objetivos, metas e ações específicas voltadas para a redução do desmatamento e o controle dos incêndios florestais no Brasil.'''

#DESCRIÇÃO DA BASE DE DADOS:

'''
1.Objetivos:

Reduzir o desmatamento e aperfeiçoar o controle ambiental.
Fortalecer e aperfeiçoar os sistemas de monitoramento e disponibilização de informações para prevenção e controle dos incêndios florestais.
Promover a responsabilização por crimes e infrações ambientais.

2.Linhas de Ação:

Redução do desmatamento.
Presença institucional em campo.
Aprimorar o Sistema Nacional de Informações sobre Incêndios Florestais (Sisfogo).
Monitoramento dos incêndios em vegetação.
Ampliar a punibilidade por crimes e infrações ambientais relacionadas a desmatamento ilegal e incêndios florestais.

3.Biomas:

A maioria das ações é destinada a todos os biomas, com algumas específicas para a Amazônia.

4.Metas 2020-2023:

Estabelecem percentuais de redução incremental do desmatamento, aumento das ações de fiscalização, desenvolvimento de sistemas de monitoramento e aperfeiçoamento de indicadores de incêndios.

5.Indicadores:

Quantificam a redução de desmatamento em km², o número de ações de fiscalização, funcionalidades do sistema Sisfogo, número de focos de calor monitorados, e processos judiciais relacionados a crimes ambientais.

6.Resultados Esperados:

Redução progressiva do desmatamento.
Aumento da presença institucional em campo para fiscalização.
Funcionalidades aprimoradas e disponíveis do Sisfogo.
Monitoramento eficiente das áreas atingidas por incêndios.
Melhoria contínua na prevenção e combate aos crimes ambientais.

7.Instituições Responsáveis:

Diversas instituições estão envolvidas, incluindo o Ministério do Meio Ambiente (MMA), Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis (IBAMA), Instituto Chico Mendes de Conservação da Biodiversidade (ICMBio), Polícia Federal, Instituto Nacional de Pesquisas Espaciais (INPE), Ministério da Ciência, Tecnologia e Inovações (MCTI), Centro Gestor e Operacional do Sistema de Proteção da Amazônia (Censipam), e Ministério da Defesa (MD).

Essa base de dados é fundamental para a elaboração e acompanhamento de políticas públicas voltadas para a proteção ambiental no Brasil, fornecendo metas claras e indicadores mensuráveis para avaliar o progresso das ações de combate ao desmatamento ilegal e aos incêndios florestais.'''

import pandas as pd

df = pd.read_csv("C:/Users/Kadu/OneDrive/Documents/Conjunto de Dados/plano_operativo_2020_2023_Tolerância Zero Desmatamento.csv", encoding = "utf-8",sep = ';')

tipos_dados = df.dtypes
print("Tipos de Dados das Colunas")
print(tipos_dados)

resumo_estatistico = df.describe()
print("\nResumo Estatístico:")
print(resumo_estatistico)
