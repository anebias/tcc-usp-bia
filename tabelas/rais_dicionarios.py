# =============================================================================
# rais_dicionarios.py
# Dicionários de decodificação RAIS — extraídos do layout oficial MTE
# Fonte: RAIS_vinculos_layout.xls (ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/Layouts/)
#
# USO:
#   from rais_dicionarios import *
#   df['sexo'] = df['Sexo - Código'].map(SEXO)
# =============================================================================

# -----------------------------------------------------------------------------
# Sexo (col: "Sexo - Código")
# -----------------------------------------------------------------------------
SEXO = {
    '1':  'Masculino',
    '2':  'Feminino',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Grau de instrução / Escolaridade após 2005 (col: "Escolaridade Após 2005 - Código")
# -----------------------------------------------------------------------------
ESCOLARIDADE = {
    '1':  'Analfabeto',
    '2':  'Até 5ª incompleto',
    '3':  '5ª completo fundamental',
    '4':  '6ª a 9ª fundamental',
    '5':  'Fundamental completo',
    '6':  'Médio incompleto',
    '7':  'Médio completo',
    '8':  'Superior incompleto',
    '9':  'Superior completo',
    '10': 'Mestrado',
    '11': 'Doutorado',
    '-1': 'Ignorado',
}

# Agrupamento simplificado útil para gráficos
ESCOLARIDADE_GRUPO = {
    '1':  'Até fundamental',
    '2':  'Até fundamental',
    '3':  'Até fundamental',
    '4':  'Até fundamental',
    '5':  'Até fundamental',
    '6':  'Médio',
    '7':  'Médio',
    '8':  'Superior',
    '9':  'Superior',
    '10': 'Pós-graduação',
    '11': 'Pós-graduação',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Faixa etária (col: "Faixa Etária - Código")
# -----------------------------------------------------------------------------
FAIXA_ETARIA = {
    '1': '10 a 14 anos',
    '2': '15 a 17 anos',
    '3': '18 a 24 anos',
    '4': '25 a 29 anos',
    '5': '30 a 39 anos',
    '6': '40 a 49 anos',
    '7': '50 a 64 anos',
    '8': '65 anos ou mais',
}

# Ordem correta para gráficos (use como category order)
FAIXA_ETARIA_ORDEM = [
    '10 a 14 anos', '15 a 17 anos', '18 a 24 anos', '25 a 29 anos',
    '30 a 39 anos', '40 a 49 anos', '50 a 64 anos', '65 anos ou mais',
]

# -----------------------------------------------------------------------------
# Raça/Cor (col: "Raça Cor - Código")
# -----------------------------------------------------------------------------
RACA_COR = {
    '1':  'Indígena',
    '2':  'Branca',
    '4':  'Preta',
    '6':  'Amarela',
    '8':  'Parda',
    '9':  'Não identificado',
    '-1': 'Ignorado',
}

# Agrupamento para análise de disparidades raciais
RACA_COR_GRUPO = {
    '1':  'Outros',       # Indígena
    '2':  'Branca',
    '4':  'Preta/Parda',  # Preta
    '6':  'Outros',       # Amarela
    '8':  'Preta/Parda',  # Parda
    '9':  'Não identificado',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Tamanho do estabelecimento (col: "Tamanho Estabelecimento - Código")
# Empregados ativos em 31/12
# -----------------------------------------------------------------------------
TAMANHO_ESTAB = {
    '1':  'Zero empregados',
    '2':  'Até 4',
    '3':  'De 5 a 9',
    '4':  'De 10 a 19',
    '5':  'De 20 a 49',
    '6':  'De 50 a 99',
    '7':  'De 100 a 249',
    '8':  'De 250 a 499',
    '9':  'De 500 a 999',
    '10': '1000 ou mais',
    '-1': 'Ignorado',
}

# Agrupamento por porte (útil para análise de senioridade/porte de empresa)
TAMANHO_ESTAB_PORTE = {
    '1':  'Micro',
    '2':  'Micro',       # até 4
    '3':  'Micro',       # 5–9
    '4':  'Pequena',     # 10–19
    '5':  'Pequena',     # 20–49
    '6':  'Média',       # 50–99
    '7':  'Média',       # 100–249
    '8':  'Grande',      # 250–499
    '9':  'Grande',      # 500–999
    '10': 'Grande',      # 1000+
    '-1': 'Ignorado',
}

TAMANHO_PORTE_ORDEM = ['Micro', 'Pequena', 'Média', 'Grande']

# -----------------------------------------------------------------------------
# Faixa de remuneração média do ano (col: "Faixa Rem Média (SM) - Código")
# Em salários mínimos
# -----------------------------------------------------------------------------
FAIXA_REMUN_MEDIA = {
    '00': 'Até 0,50 SM',
    '01': '0,51 a 1,00 SM',
    '02': '1,01 a 1,50 SM',
    '03': '1,51 a 2,00 SM',
    '04': '2,01 a 3,00 SM',
    '05': '3,01 a 4,00 SM',
    '06': '4,01 a 5,00 SM',
    '07': '5,01 a 7,00 SM',
    '08': '7,01 a 10,00 SM',
    '09': '10,01 a 15,00 SM',
    '10': '15,01 a 20,00 SM',
    '11': 'Mais de 20,00 SM',
}

FAIXA_REMUN_ORDEM = [
    'Até 0,50 SM', '0,51 a 1,00 SM', '1,01 a 1,50 SM', '1,51 a 2,00 SM',
    '2,01 a 3,00 SM', '3,01 a 4,00 SM', '4,01 a 5,00 SM', '5,01 a 7,00 SM',
    '7,01 a 10,00 SM', '10,01 a 15,00 SM', '15,01 a 20,00 SM', 'Mais de 20,00 SM',
]

# -----------------------------------------------------------------------------
# Faixa de remuneração de dezembro (col: "Faixa Rem Dez (SM) - Código")
# -----------------------------------------------------------------------------
FAIXA_REMUN_DEZ = {
    '01': 'Até 0,50 SM',
    '02': '0,51 a 1,00 SM',
    '03': '1,01 a 1,50 SM',
    '04': '1,51 a 2,00 SM',
    '05': '2,01 a 3,00 SM',
    '06': '3,01 a 4,00 SM',
    '07': '4,01 a 5,00 SM',
    '08': '5,01 a 7,00 SM',
    '09': '7,01 a 10,00 SM',
    '10': '10,01 a 15,00 SM',
    '11': '15,01 a 20,00 SM',
    '12': 'Mais de 20,00 SM',
}

# -----------------------------------------------------------------------------
# Faixa de horas contratuais (col: "Faixa Hora Contrat - Código")
# -----------------------------------------------------------------------------
FAIXA_HORAS = {
    '01': 'Até 12h',
    '02': '13 a 15h',
    '03': '16 a 20h',
    '04': '21 a 30h',
    '05': '31 a 40h',
    '06': '41 a 44h',
}

# -----------------------------------------------------------------------------
# Tipo de vínculo (col: "Tipo Vínculo - Código")
# Agrupado — lista completa no layout
# -----------------------------------------------------------------------------
TIPO_VINCULO = {
    '10': 'CLT urbano PJ ind.',
    '15': 'CLT urbano PF ind.',
    '20': 'CLT rural PJ ind.',
    '25': 'CLT rural PF ind.',
    '30': 'Estatutário',
    '31': 'Estatutário RGPS',
    '35': 'Estatutário não efetivo',
    '40': 'Avulso',
    '50': 'Temporário',
    '55': 'Aprendiz',
    '60': 'CLT urbano PJ det.',
    '65': 'CLT urbano PF det.',
    '70': 'CLT rural PJ det.',
    '75': 'CLT rural PF det.',
    '80': 'Diretor',
    '90': 'Contrato prazo det.',
    '95': 'Contrato temp. det.',
    '96': 'Contrato lei estadual',
    '97': 'Contrato lei municipal',
    '-1': 'Ignorado',
}

# Agrupamento simplificado
TIPO_VINCULO_GRUPO = {
    '10': 'CLT', '15': 'CLT', '20': 'CLT', '25': 'CLT',
    '60': 'CLT', '65': 'CLT', '70': 'CLT', '75': 'CLT',
    '30': 'Estatutário', '31': 'Estatutário', '35': 'Estatutário',
    '96': 'Estatutário', '97': 'Estatutário',
    '40': 'Avulso',
    '50': 'Temporário/Aprendiz', '55': 'Temporário/Aprendiz',
    '90': 'Temporário/Aprendiz', '95': 'Temporário/Aprendiz',
    '80': 'Diretor',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Vínculo ativo em 31/12 (col: "Ind Vínculo Ativo 31/12 - Código")
# -----------------------------------------------------------------------------
VINCULO_ATIVO = {
    '0': 'Não ativo em 31/12',
    '1': 'Ativo em 31/12',
}

# -----------------------------------------------------------------------------
# Portador de deficiência (col: "Ind Portador Defic - Código")
# -----------------------------------------------------------------------------
PORT_DEFIC = {
    '0': 'Não',
    '1': 'Sim',
}

TIPO_DEFIC = {
    '0':  'Não deficiente',
    '1':  'Física',
    '2':  'Auditiva',
    '3':  'Visual',
    '4':  'Mental',
    '5':  'Múltipla',
    '6':  'Reabilitado',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Tipo de admissão (col: "Tipo Admissão Trabalhador - Código")
# -----------------------------------------------------------------------------
TIPO_ADM = {
    '0':  'Não admitido no ano',
    '1':  'Primeiro emprego',
    '2':  'Reemprego',
    '3':  'Transferência c/ ônus',
    '4':  'Transferência s/ ônus',
    '5':  'Outros',
    '6':  'Reintegração',
    '7':  'Recondução',
    '8':  'Reversão',
    '9':  'Exercício provisório',
    '10': 'Requisição',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Motivo de desligamento (col: "Motivo Desligamento - Código")
# Agrupado para análise
# -----------------------------------------------------------------------------
MOTIVO_DESLIG_GRUPO = {
    '10': 'Demissão c/ justa causa',
    '11': 'Demissão s/ justa causa',
    '12': 'Término de contrato',
    '20': 'Pedido de demissão c/ justa causa',
    '21': 'Pedido de demissão',
    '22': 'Posse em outro cargo',
    '30': 'Transferência',
    '31': 'Transferência',
    '32': 'Readaptação/Redistribuição',
    '33': 'Cessão',
    '34': 'Redistribuição',
    '40': 'Mudança de regime',
    '50': 'Reforma militar',
    '60': 'Falecimento',
    '62': 'Falecimento (acidente típico)',
    '63': 'Falecimento (acidente trajeto)',
    '64': 'Falecimento (doença profissional)',
    '70': 'Aposentadoria c/ rescisão',
    '71': 'Aposentadoria s/ rescisão',
    '72': 'Aposentadoria por idade c/ rescisão',
    '73': 'Aposentadoria por invalidez (acidente)',
    '74': 'Aposentadoria por invalidez (doença)',
    '75': 'Aposentadoria compulsória',
    '76': 'Aposentadoria por invalidez (outros)',
    '78': 'Aposentadoria por idade s/ rescisão',
    '79': 'Aposentadoria especial c/ rescisão',
    '80': 'Aposentadoria especial s/ rescisão',
    '0':  'Não desligado no ano',
    '-1': 'Ignorado',
}

# -----------------------------------------------------------------------------
# Cores padrão para gráficos do TCC
# -----------------------------------------------------------------------------
CORES_GENERO = {
    'Masculino': '#2196F3',
    'Feminino':  '#E91E63',
}

CORES_RACA = {
    'Branca':           '#90CAF9',
    'Preta/Parda':      '#5D4037',
    'Indígena':         '#66BB6A',
    'Amarela':          '#FFF176',
    'Não identificado': '#BDBDBD',
    'Ignorado':         '#EEEEEE',
}

CORES_ESCOLARIDADE = {
    'Até fundamental': '#EF9A9A',
    'Médio':           '#FFCC80',
    'Superior':        '#A5D6A7',
    'Pós-graduação':   '#1565C0',
    'Ignorado':        '#EEEEEE',
}

# -----------------------------------------------------------------------------
# Função utilitária: decodifica uma coluna e preserva não mapeados
# -----------------------------------------------------------------------------
def decodificar(serie, dicionario, rotulo_desconhecido='Não mapeado'):
    """
    Aplica um dicionário de decodificação a uma Series pandas.
    Converte para string antes de mapear (os códigos RAIS são VARCHAR).
    Preserva valores não mapeados com o rótulo indicado.
    """
    return serie.astype(str).map(dicionario).fillna(rotulo_desconhecido)
