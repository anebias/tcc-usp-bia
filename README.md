# Supressão de células e equidade de gênero entre Cientistas de Dados (RAIS 2023–2025)

Código e tabelas do artigo **"Supressão de dados e qualidade analítica na análise da equidade de gênero entre Cientistas de Dados"** (TCC, MBA em Business Intelligence & Analytics, USP/ECA).

O estudo usa os **microdados públicos da RAIS Vínculos** (MTE) dos anos-base 2023, 2024 e 2025 para a ocupação **CBO 2112-20 – Cientista de dados**, simula a supressão de células (limiares k = 3, 5 e 10; supressão primária e complementar) e mede o efeito sobre indicadores de equidade de gênero.

## Estrutura

```
notebooks/
  01_carga_rais.ipynb     # microdados (.COMT) -> um banco DuckDB por ano
  01_carga_rais_v2.ipynb  # microdados (.COMT) -> um banco DuckDB por ano (versão otimizada para uso de memória)
  02_analise_rais.ipynb   # validação, resultados, simulação de supressão e apêndice
tabelas/
  tabelas_tcc_rais.xlsx   # tabelas finais do artigo (agregadas, sem identificação individual)
rais_dicionarios.py       # dicionários de códigos da RAIS (necessário para o notebook 02)
requirements.txt
```

## Como reproduzir

1. **Baixar os microdados** (RAIS Vínculos Públicos, um arquivo compactado por região, para cada ano) em  
   `ftp://ftp.mtps.gov.br/pdet/microdados/` → `RAIS/<ano>/`.  
   Regiões dos arquivos: `CENTRO_OESTE`, `MG_ES_RJ`, `NI`, `NORDESTE`, `NORTE`, `SP`, `SUL`.
2. **Descompactar** para a estrutura abaixo (o `.COMT` é texto separado por vírgula, codificação latin-1):
   ```
   <DADOS_PATH>/<ano>/RAIS_VINC_PUB_<REGIAO>/RAIS_VINC_PUB_<REGIAO>.COMT
   ```
3. **Definir o diretório de dados**: variável de ambiente `RAIS_DADOS_PATH` (no Google Colab, o padrão é  
   `/content/drive/MyDrive/MBA_USP_BIA/TCC/CAGED`).
4. **Executar `notebooks/01_carga_rais.ipynb`** → cria `<DADOS_PATH>/<ano>/rais_<ano>.duckdb` (tabela por região + view `rais_vinc_brasil`; colunas extras `ano`, `regiao_arquivo`, `uf` e `regiao_geografica`).
5. **Executar `notebooks/02_analise_rais.ipynb`** ("Executar tudo"). A seção 2 compara os totais de vínculos ativos por sexo com os do Sumário Executivo da RAIS; os três anos devem aparecer como ✅. Figuras e tabelas são gravadas em `<DADOS_PATH>/figuras` e `<DADOS_PATH>/tabelas`.

Os bancos DuckDB e os microdados **não** estão neste repositório (tamanho; os microdados já são públicos no site do MTE).

### Execução local

```bash
pip install -r requirements.txt
export RAIS_DADOS_PATH=/caminho/para/os/dados      # Windows: set RAIS_DADOS_PATH=...
jupyter lab
```

## Definições principais

- **Estoque:** vínculos ativos em 31/12 (`Ind Vínculo Ativo 31/12 - Código = '1'`), excluídos os abandonados (`Ind Vínculo Abandonado - Código = '0'`) e registros sem sexo identificado (códigos 1 e 2). O filtro é definido uma única vez no notebook 02.
- **UF e região** vêm dos dois primeiros dígitos do **código do município do estabelecimento**, não da residência do trabalhador.
- **Célula:** combinação de categorias (por exemplo, sexo × UF), com grade completa (células sem vínculos contam como zero e não são suprimidas).
- **Supressão primária:** oculta células com 1 a k−1 vínculos. **Complementar:** heurística iterativa que oculta células adicionais para impedir a dedução por diferença (totais por UF e nacional publicados).
- **Remuneração:** média nominal do vínculo (`Vl Rem Média Nom`), estabelecimentos com 100+ empregados, valores entre 0,3 e 150 salários mínimos do ano, razão calculada apenas com pelo menos 3 mulheres e 3 homens (comparável ao painel do Relatório de Transparência Salarial).

## Colunas dos microdados usadas

`Sexo - Código`, `Ind Vínculo Ativo 31/12 - Código`, `Ind Vínculo Abandonado - Código`, `CBO 2002 Ocupação - Código`, `Município - Código`, `Raça Cor - Código`, `Escolaridade Após 2005 - Código`, `Tamanho Estabelecimento - Código`, `Tipo Vínculo - Código`, `Vl Rem Média Nom`.

## Fontes

- MTE. Microdados RAIS. `ftp://ftp.mtps.gov.br/pdet/microdados/`
- MTE. RAIS 2025: Sumário Executivo e Nota Técnica (totais de referência e critérios de estoque).
- MTE e Ministério das Mulheres. Painel do Relatório de Transparência Salarial (dez/2025).

## Observações

- A simulação de supressão é feita sobre contagens agregadas geradas pelos autores; não representa regra adotada pelo MTE na divulgação da RAIS.
- A supressão complementar usa heurística e não garante o menor conjunto de células ocultas.
- Os valores em reais são nominais; a comparação com o painel do Ministério é indicativa.

## Autoria

Alessandra Mara Nébias; Luana Lopes de Oliveira (orientação).
