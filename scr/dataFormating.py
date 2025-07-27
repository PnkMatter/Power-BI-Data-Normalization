import pandas as pd
import re

# Carregando dados
df = pd.read_csv(r"Path", header=[0, 1])

#Limpeza 1
df.columns = ['_'.join([str(a).strip(), str(b).strip()]).strip('_') for a, b in df.columns]

#Limpeza 2
def limpar_nome_coluna(col):
    col = re.sub(r'^Unnamed: \d+_level_0_', '', col)
    col = col.replace('_', ' ').strip()
    return col

df.columns = [limpar_nome_coluna(col) for col in df.columns]

# Separação
id_cols = ['pais', 'planta', 'marca', 'linha']

value_cols = [col for col in df.columns if col not in id_cols]

df_melt = df.melt(id_vars=id_cols, value_vars=value_cols, var_name='tipo_metrica', value_name='valor')

# Quebra
df_melt[['tipo', 'ano', 'metrica']] = df_melt['tipo_metrica'].str.extract(r'([A-Za-z\s\-]+)(20[0-9]{2})[_\s]*(Net-Sales|Intercompany %)')

# Formatação
df_melt['tipo'] = df_melt['tipo'].str.strip()
df_melt['metrica'] = df_melt['metrica'].str.strip()
df_melt['valor'] = pd.to_numeric(df_melt['valor'], errors='coerce')

# Reorganização
df_final = df_melt[['pais', 'planta', 'marca', 'linha', 'ano', 'tipo', 'metrica', 'valor']]

#df_final.to_excel('dados_normalizados_powerbi.xlsx', index=False)

df_final