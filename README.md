# Airflow: Utilizando os Executores Local e Celery

## 💡Objetivos
Instalação e configuração da ferramenta Airflow, juntamente com a análise e resolução de mensagens de aviso associadas ao banco de dados SQLite e ao executor Sequential. Explorar a API e integração da biblioteca YFinance, permitindo a extração eficiente de dados.. Criação de um Directed Acyclic Graph (DAG) para extrair e processar informações sobre ações de bolsas de valores. Obtendo compreensão sólida do Airflow e suas capacidades, desde a configuração inicial até a implementação de tarefas de coleta de dados financeiros.

###### Imagem 1: Processo de execução das tarefas após definição e ativação de um DAG (Crédito da imagem: Alura)
<img src="/img/001_processo-execucao-tarefas.png">


## 🖥️Desafios do Projeto
Este projeto apresenta uma série de desafios, incluindo trabalhar com APIs, criação da Directed Acyclic Graphs (DAGs), compreender o funcionamento detalhado dos principais componentes do Airflow, tais como o web server, scheduler, e o banco de dados. Focando nos executores Local e Celery, e explorando suas funcionalidades e diferenças.

Parte crucial do desafio envolve a configuração e instalação de bancos de dados Postgres e o Redis, este último desempenhando um papel vital como mediador. O uso do executor Celery também é um ponto focal, exigindo um entendimento aprofundado de seus componentes principais, incluindo filas de tarefas e a configuração de worker concurrency. Abordando a funcionalidade dos pools, definindo a quantidade máxima de tarefas que podem ser executadas em paralelo.

###### Imagem 2: Grid View - Visualização da execução do DAG
<img src="/img/002-visualizacao-execucao-dag.png">


## 📄Conhecimentos Desenvolvidos
|Atividades|Realizadas |
|----------|-----------|
| Instalar o Python no Ubuntu  | Criar e Ativar um ambiente virtual |
| Instalar o Airflow juntamente com alguns pacotes; e  | Executar o Airflow localmente |
| Utilizar a biblioteca yfinance | Extrair dados de ações da bolsa de valores |
| Criar tarefas utilizando o TaskFlow; e | Criar um DAG utilizando TaskFlow |
| Identificar como funciona o processo de execução das tarefas | Compreender o que é o Executor Local |
| Instalar o Postgres | Configurar o Executor Local |
| Analisar os parâmetros max_active_tasks_per_dag e max_active_runs_per_dag | Reconhecer o Executor Celery |
| Esquematizar o que são os workers e filas de tarefas | Instalar o Redis |
| Configurar o Executor Celery; e | Compreender o que é o Celery Flower |
| Limitar a quantidade de tarefas que um worker pode executar, utilizando o worker_concurrency | Criar um novo pool |
| Identificar como funciona a dinâmica de execução das tarefas com dois DAGs ativos | Esquematizar um pool e como utilizálo |

##  🗂️Organização dos Arquivos

* code-extra: Diretório contém scripts em Python desenvolvidos para testes e extração de dados utilizando a biblioteca YFinance.
* crypto: Neste diretório são armazenados os dados extraídos das criptomoedas de interesse.
* dags: Arquivos responsáveis por definir e executar Directed Acyclic Graphs (DAGs). Esses arquivos realizam um conjunto de tarefas para extrair dados do mercado financeiro sobre diferentes ações da bolsa de valores.
* stocks: Diretório para armazenar os dados de cada uma das ações de interesse, os quais são extraídos e processados pelos DAGs definidos na pasta "dags".

##  🎞️Imagens do Projeto

###### Imagem 3: Janela com Execução das DAGs, lado a lado, monitorando fila de execução
<img src="/img/003-execucao-dags.png">

###### Imagem 4: CeleryExecutor - Distribuindo a execução das tarefas (Crédito da imagem: Alura)
<img src="/img/004-celeryExecutor.png">

###### Imagem 5: Flower - Ferramenta do Celery que permite visualizar as tarefas que estão na fila
<img src="/img/005-flower.png">

###### Imagem 6: Arquivo de configuração do Airflow
<img src="/img/006-arquivo-configuracao-airflow.png">

## 🔍Referências
- [Alura](https://www.alura.com.br/)