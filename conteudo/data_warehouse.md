# Arquitetura de Data Warehouse e Data Marts

## Banco de dados relacional
- Criado em 1970 por Edgar Codd;
- Objetivo de compatibilizar os códigos;
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
- 