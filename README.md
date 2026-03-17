# Sistema de Análise de Desempenho Acadêmico

## 1. Sobre o Projeto

Este projeto foi desenvolvido para ajudar a coordenação a **organizar e analisar as notas dos alunos de forma mais rápida e confiável**.

O sistema recebe uma estrutura de dados com **nomes de alunos e suas notas**, calcula as médias, identifica alunos em **recuperação** e destaca o **Top Student** (aluno com maior média).
No final, é gerado um **relatório em arquivo `.txt`** com os resultados.

---

# 2. Estrutura de Dados

Os dados dos alunos são organizados no formato:

Cada aluno possui um **nome** e uma **lista de notas**, que pode ter quantidade diferente para cada aluno.


# 3. Requisitos

## Requisitos Funcionais (RF)

O sistema deve:

* Validar se a lista de notas não está vazia ou corrompida
* Calcular a média de cada aluno
* Identificar alunos em **recuperação (média < 7.0)**
* Identificar o **Top Student** da turma
* Gerar um relatório final em **resultado.txt**

---

## Requisitos Não Funcionais (RNF)

* Código organizado em **módulos**
* Separação entre **main.py** e **processamento.py**
* Uso de **listas, tuplas, funções e loops**
* Código simples e fácil de entender

---

## Regras de Negócio (RN)

* A média do aluno é calculada pela soma das notas dividida pela quantidade de notas
* Alunos com média **menor que 7.0** estão em recuperação
* O aluno com **maior média da turma** é considerado o Top Student
* Listas de notas vazias devem ser ignoradas ou tratadas

---

# 4. Estrutura do Projeto

```
projeto/
│
├── main.py
├── processamento.py
├── resultado.txt
└── README.md
```

* **main.py** → executa o sistema
* **processamento.py** → contém as funções de processamento das notas
* **resultado.txt** → relatório gerado pelo programa

---

# 5. Mapa da Empatia (Design Thinking)

# 6. Kanban (Gestão Ágil)

# 7. Versionamento (Git)

O projeto foi desenvolvido utilizando **branches para cada funcionalidade**.
Após finalizar cada funcionalidade, foi realizado **merge para a branch main**.


---
