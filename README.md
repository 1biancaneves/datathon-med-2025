#  Passos Mágicos — Análise de Potencial do Aluno (PEDE)

Projeto de **Análise Exploratória de Dados (EDA)** e **Machine Learning** desenvolvido no Hackathon Mulheres em Dados 2025.

O objetivo é usar os dados da pesquisa **PEDE (Pesquisa Extensiva do Desenvolvimento Educacional)** para:

- comparar alunos com pares de perfil semelhante  
- medir desempenho de forma justa (ajustando por contexto e defasagem)  
- identificar fatores que mais influenciam o **Indicador de Ponto de Virada (IPV)**  
- apoiar decisões pedagógicas baseadas em dados  

---

##  Problema

Como avaliar o potencial de um aluno sem compará-lo injustamente com realidades diferentes?

A proposta do projeto é:

→ comparar alunos com **subgrupos semelhantes**  
→ analisar **defasagens entre contextos (escola pública vs bolsista)**  
→ modelar **probabilidade de atingir o Ponto de Virada**  
→ gerar **insights acionáveis para intervenção pedagógica**

---

##  Abordagens utilizadas

###  Análise Exploratória (EDA)
- tratamento e padronização das bases
- cálculo de médias por turma
- z-score por sala
- percentis
- comparação entre subgrupos
- visualizações estatísticas

###  Engenharia de Features
- tempo de permanência na associação
- categorização de defasagem
- normalização de indicadores psicossociais
- codificação de variáveis categóricas

###  Modelagem
- clusterização (K-Modes)
- regressão logística
- análise de importância de variáveis
- matriz de confusão

---

##  Estrutura do repositório

datathon-med-2025/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│ └── raw/ → dados brutos originais
│
├── scripts/ → scripts Python executáveis
│ ├── hackaton_med_2025.py
│ └── teste_passos_magicos_ml.py
│
├── docs/
│ ├── references/ → relatórios, dicionário, regras de pontuação
│ └── apresentações
│
└── reports/
└── figures/ → gráficos gerados automaticamente


##  Dados

Os dados incluem:

- PEDE 2022
- PEDE 2023
- PEDE 2024
- relatórios oficiais
- dicionário de dados
- tabelas de pontuação dos indicadores:
  - IAA (Autoavaliação)
  - IPS (Psicossocial)
  - IPP (Psicopedagógico)
  - IPV (Ponto de Virada)

Todos os materiais de referência estão em:    docs/references/


---

## Tecnologias

- Python
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- kmodes

---

##  Como executar

### 1. Clonar o repositório
git clone <github.com/1biancaneves/datathon-med-2025>
cd datathon-med-2025

### 2. Criar ambiente virtual
Windows:
python -m venv .venv
.venv\Scripts\activate

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Executar análises

python scripts/hackaton_med_2025.py
python scripts/teste_passos_magicos_ml.py


---

## Saídas geradas

Após execução:

- gráficos → `reports/figures/`
- dataset tratado → exportado como CSV
- métricas do modelo → terminal

---

##  Reprodutibilidade

O projeto foi organizado para:

- separar dados brutos  
- manter código versionado  
- garantir execução com requirements.txt  
- permitir replicação das análises por qualquer pessoa  

---

## Autoria

Projeto desenvolvido durante o **Hackathon Mulheres em Dados 2025**  

---

## Licença

Uso educacional e de pesquisa.


## Criado por

Bianca Neves  


