# Arquitetura de Data Warehouse e Data Marts

## Banco de dados relacional
- Criado em 1970 por Edgar Codd;
- Objetivo de compatibilizar os códigos e dados;
- Indenpendência dos dados aos programas;
- Para superar redundâncias e inconsistências;
- Forma simples e fácil de representar os dados e de fazer consultas difíceis;
- Em 1980 começaram a ficar mais usuais e dominantes;
- Empresas se destacaram:
    - **IMB** compactou drasticamento os dados de programação, possibilitando otimização do tempo;
    - **Microsoft** criou interfaces gráficas bidimensionais chamadas *Windows*;
    - **Sybase** ganhou evidência devido à sua robustez e qualidade técnica;
    - **Oracle** se destacou na área de bnaco de dados por apresentar fatores como desempenho, confiabilidade e segurança.

## Representação de dados
- Relações entre linhas que consiste em um esquema e uma instância;
- Colunas de uma tabela;
- *Esquema* especifica:
    - o nome da relação;
    - o nome e o domínio de uma coluna (Atributo ou campo da relação);
- *Domínio* do atributo:
    - é referenciado pelo nome;
    - serve para restringir valores que este atributo pode atingir;
- *Instância* de uma relação é:
    - Conjunto de linhas (tuplas ou registros) distintas entre si;
    - Compõe a relação em um dado momento;
- *Banco de dados relacional* é:
    - Conjunto de relações com nomenclaturas diferentes;
    - Tem relação com os esquemas

## Arquitetura de Sistemas
Sistemas de informações é uma ciência que estuda a coleta, armazenament9o, processamento, análise e distribuição de dados por meio de tecnologias como softwares, hardwares, banco de dados, sistemas especialistas, sistemas de apoio à gestão.

Deve conter relevância, intetgração, fluxo independente, controle e diretrizes adequadas.

## Business Intelligence
O sistema de arquitetura de BI pode estar relacionado com dados, bases, documentos, indicadores, informações.

É um conjunto de elementos que que tem o objetivo de apoiar as tomadas de decisões em serviços utilizando dados, informações e conhecimentos.

É usual em diferentes áreas.

## Data warehouse
É um sistema de armazenamento de dados que tem por objetivo auxiliar nas tomadas de decisões.

Linguagens de programação:
- Python
- SQL
- Java

Perda da privacidade dos dados aumenta a conscientização da importância da Proteção de Dados.

Torna-se cada vez mais desafiador respeitar a privacidade das pessoas

## ETL
- **Extract**: extrair
- **Transform**: transformar
- **Load**: carregar

## Banco de dados transacional

Conforme Date (2004), Banco de dadosé um grande sistema computadorizado de informações armazenadas, onde usuários podem realizar diferentes processos (inserir, buscar, excluir e alterar dados).

- **Data Warehouse**: 
    - trabalha de forma independente;
    - ideal para pesquisas de grandes volumes;
    - Não armazena dados atuais nem se atualiza em tempo eral e rápida;
    - Realiza análises de dados;
    - Centraliza dados de grnades empresas;

- **Banco de dados transacional**: é dependente no que se trata de sistemas de gerenciamento e gestão.

## Modelagem transacional

Técnica de representar dados de forma simples, objetiva e com alto desempenho. Além de compreensível

É uma etapa de implementação de uma Data Warehouse e consolidam dimensões específicas para aumentar a eficácia e rapidez de consultas orgnaizadas.

- **Dimensões regulares**: representam dados descritivos que geram contexto para os dados modeloados nas dimensões de medida. É desmembrado em grupos de informaões chamados níveis.
- **Dimensões de medidas**: Dados quantitativos descritos por dimensões regulares. Conhecida em produtos OLAP - Online Analytical Processing (Processamento Analítico Online). Contém dados de fatos.
- **Relações de escopo**: Entre dimensões de medida e regulares para definir o nível em que medidas estarão disponíveis para relatórios.

Com maior quantidade de dados em escala sem precedentes, o valor dos dados também aumentou.

### Técnicas de design de esquema Floco de neve e Estrela

Ambos são multidimensionais.

Os esquemas são concorrentes entre si. A escolha entre eles varia de acordo c9om a disponibilidade de disco e o poder de processamento computacional.

### Técnicas de design de esquema Floco de neve

- Modelagem com as dimensões da stabelas normalizadas e divididas em hierarquia
- Menor ocupação do banco de dados
- Melhor desempenho
- Inexistência de redundância

### Técnicas de design de esquema Estrela

- Mais complexo
- Mais comum
- Composto por dois tipos de tabelas:
    - **Tabela de fatos** , no centro do esquema
    - **Tabela com dimensões**, ligada à tabela principal
- Diretamente elacionado com medidas, chaves primárias (PK), chaves estrangeiras (FK), atributos e hierarquias.

## Considerações na escolha da modelagem
- Público-alvo: é necessário uma modelagem para cada atender aos diversos tipos de usuário.

## Tipos de fatos
- Fatos aditivos: Medidas de negócios podem ser agregadas em alguma dimensão;
- Fatos semi-aditivos: podem ser agregados apenas em algumas dimensões;
- Fatos não aditivos: não podem ser agregados em qualquer dimensão

## Tipos de chaves nas tabelas dimensionais
- Primárias: identifica registros exclusivos;
- Substitutivas: será a chave primária para dimensões que mudam lentamente;
- Estrangieras: unem duas tabelas. Geralmente:
    - Unem de fatos e de dimensões;
    - na tabela de fatos, sendo a chave primária na tabela de dimensão;

## Tipos de dimensões
- Tempo
- Produto
- Loja
- Cliente

## Etapas de projeto de um modelo dimensional

- Identificação de processos de negócios
- Identificação de fatos e dimensões em seu modelo de dados dimensionais
- Identificação dos atributos para dimensões
- Definição da granularidade dos fatos comerciais
- Armazenamento de informações históricas (dimensões que modam lentamente)

## Benefícios da modelagem dimensional

- otimização de desempenho;
- recuperação rápida de dados;
- flexibilidade;
- análise multidimensional;
- redução na redundância de dados.

## Hierarquia de modelos dimensionais
Hierarquia é a relação entre as dimensões e os atributos de uma determinada informação.

Ajudam a formar bases primárias sendo alinhadas em uma mesma direção nas tabwlas com bancos de dados.

Os dados são disposrtos dos níveis mais detalhados para os menos detalhados.

##  Níveis de granularidade em modelos dimensionais

Se referem a informações armazenadas em tabeelas, que devem possuir a mesma dimensão (por exemplo, datas anuais).

Esses níveis garantem uma lógica no sistema e evitam resultados confusos e imprecisos que ameacem quais processos.

## Dimensões, fatos e atributos em um Data Warehouse
Para Rocha (2023) estão relacionados aos conceitos gerais dos bancos de dados relacionais, ou seja, ao modelo dimensional onde os dados aparecem em forma de tabelas.

- Colunas = atributos = características dos dados => dimensão ou medição = representam fato.
- Linhas = instâncias.

Dados multidimensionais estão os fatos e as dimensões de um *Data Warehouse* que são relacionados entre si.

**Tabelas de fatos** são caracteriszadas por terem poucas colunas e muitas linhas com informações predominantemente numéricoas.

**Tabelas de dimensões**  armazenam mais elementos textuais com detalhamento de informações que podem ter hierarquias.

**Dimensões** atributos mais relacionados entre si que descrevem coisas organizadas. Pode ser conformada quando compartilhada com duas ou mais tabelas de fatos.

**Tabela de fatos** relação entre diferentes dimensãom onde são armazenados dados numéricos que representam medidas específicas, permitindo análises multidimensionais.

**Atributos** são campos das tabelas que descrevem características de aldo, como propriedades específicas permitindo a organização e análise detalhada de dados.

**Fatos** são uma observação do mercado, normalmente com valor numérico.

**Banco de dados** é um local de armazenamento de informações que variam de acordo com cada tipo de situação emq ue se busca guardar esses dados.

## ETL (*extract*, *transform* e *load*)
É uma ferramenta que identifica dados, os reúne, os traduz e os carrega até uma base de dados.

É a principal etapa na construção, desenvolvimento e manutenção de um *Data Warehouse*.

Por meio desta técnica os dados são otimizados para serem guardados.

Essas etapas têm o objetivo de otimizar e armazenar informações escaláveis, bem como auxiliar nas tomadas de decisões nas organizações.

Está relacionado à tecnpologia de cloud ou armazenamento em nuvem.

### Recomendações
- Fazer um devido planejamento;
- Automatizar etapas sempre que possível;
- Monitorar e validar dados;
- Garantir a segurança das informações.

### Extração
É a primeira etapa.

#### Extração de dados de fontes heterogêneas 
Se dá quando se obtém dadpos de bancos de dados diferentes, destacando os principais objetivos e características dessa extração.

Visa a preserver os sistemas existentes e manter a autonomia dos bancos de dados (dentre outros). Citam-se as principais características:
- São analisadas em 3 dimensões: distribuição dos sistemas locais, heterogeneidade e autonomia dos sistemas locais.
- É representado por nós, cada um podendo contar 1 ou mais bancos de dados locais, ligados por redes.
- Os componentes podem ter esquema (Arquitetura) conceitual global, local ou auxiliar.

#### Estudiosos
- Mapeamentos sistemáticos, por Almeida et al. (2020);
- Migração entre bancos de dados, por Rodrigues e Vieira (2019);
- Área da Saúde, por Cruz (2019);
- Área acadêmida Dias e Carvalho-Segundo (2021)

#### SGBDH
Sistema de Gestão de Banco de Dados Heterogêneos.

Também chamados de:
- bancos de dados federados
- sistemas de múltiplos bancos de dados
- multibase

#### Ferramentas
- Apache Nifi
- Talend
- Informatica PowerCenter
- Pentaho Data Integration

### Transformação
São técnicas de préprocessamento a limpeza, a agregação e a derivação. São técnicas de pré-processamento de dados essenciais na engenharia de dados.

Transformam em dados consistentes, deixando-os coerentes para análise.

- São abordados algoritmos e critérios.
- São ajustadas as regras de qualidade de dados

Utiliza algoritmos que trabalham com números e vlaores nominais e, por diferentes tipos de critérios e técnicas empregadas:

- Suavização;
- Agrupamento;
- Generalização;
- Normalização;
- Criação de novos atributos a partir de outros pré-existentes.

#### Limpeza
Visa eliminar problemas como:
- registros incompletos;
- valores errados;
- dados inconsistentes.

As técnicas vão desde remoção de registro com problemas até aplicação de técnicas de agrupamento para auxiliar descoberta de melhores valores.

#### Integração de dados
Com fontes heterogêneas (textos, planilhas, data warehouses, vídeos, imagens), surge a necessidade de integrar os dados em um repositório único sem redundâncias e denpendências entre variáveis/valores conflitantes.
Exemplos:
- categorias difernetes par aos mesmos valores
- chaves divergentes
- regras diferentes para os mesmos dados

#### Redução de dados
Às vezes os volumes de dados são tão grandes que se torna impraticável o processo de análise e de mineiração.

O processo é para redução da massa de dados sem perder a representatividade dos dados originais.

As estratégias adotadas são:
- a criação de estruturas otimizadas para os dados, 
- a seleção de um subconjunto dos atributos
- redução de dimensionalidade
- discretização

#### Ferramentas
- Apache Spark
- Pentaho Data Integration
- Microsoft SQL Server Integration Services (SSIS)

### Carregamento (load)

QOs dados são carregados em um sistema de destino que pode ser de forma completa ou nõa.

O carregamento em um *Data Warehouse*, analisa-se sua ligação direta com estratégias convencionais: *Prepared Statements* e *Bulk Load*.

É a última fase do processo.

#### Ferrramentas
- Amazon Redshift
- Google BigQuery (vídeo)
- Microsoft Azure Synapse Analytics