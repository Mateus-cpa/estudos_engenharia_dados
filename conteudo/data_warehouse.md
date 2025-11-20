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

Ambos são multidimensionais

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
- Diretamente elacionado com medidas, chaves primárias (PK), chaves estrangeiras (FK), atributos e hierarquias

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