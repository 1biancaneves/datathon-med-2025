Projeto de **Análise Exploratória de Dados (EDA)** e **Machine Learning** desenvolvido no Hackathon Mulheres em Dados 2025.

Este trabalho transforma dados educacionais em **decisões pedagógicas acionáveis**.

A proposta é simples:

→ parar de perguntar *"quem é bom ou ruim?"*  
→ começar a perguntar *"qual é o potencial desse aluno dadas as suas condições?"*

---

# Valor do Projeto (por que isso importa?)

Avaliar alunos apenas pela média geral é injusto.

Um estudante com defasagem severa e nota 6 pode ter feito um progresso muito maior do que um aluno com nota 8 que sempre teve apoio.

Comparações tradicionais ignoram:
- contexto social
- tempo na associação
- defasagem inicial
- apoio psicopedagógico
- engajamento

Isso gera **decisões enviesadas** e intervenções pouco eficazes.

### Este projeto resolve isso ao:

- comparar alunos com pares semelhantes (mesmo ponto de partida)  
-  medir evolução, não só nota absoluta  
-  identificar fatores que realmente impulsionam o desempenho  
-  prever probabilidade de atingir o “Ponto de Virada”  
-  apoiar intervenções personalizadas  

### Impacto prático

Com os resultados é possível:

- priorizar alunos que precisam de reforço
- personalizar trilhas de apoio (engajamento, performance, autoconfiança)
- reduzir desigualdades entre subgrupos
- usar recursos pedagógicos com mais eficiência
- tomar decisões baseadas em dados (não intuição)

Em termos simples:

> **mais alunos atingindo seu potencial com o mesmo orçamento**

---

#  Objetivos

- Comparar desempenho ajustado por contexto
- Medir gaps entre subgrupos (público vs bolsista)
- Entender fatores associados ao sucesso acadêmico
- Criar indicadores replicáveis
- Construir modelo preditivo do Ponto de Virada (IPV)

---

# Abordagens utilizadas

## Análise Exploratória (EDA)
- limpeza e padronização das bases
- média por turma
- z-score
- percentil
- comparação entre subgrupos
- visualizações estatísticas

## Engenharia de Features
- tempo de permanência na associação
- categorização de defasagem
- indicadores psicossociais
- normalização de variáveis

## Modelagem
- clusterização (K-Modes)
- regressão logística
- matriz de confusão
- importância de variáveis

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


