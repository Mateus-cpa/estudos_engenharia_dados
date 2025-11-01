# Estudos — Engenharia de Dados

Este repositório reúne notas e materiais de estudo pessoais sobre tópicos importantes para quem está aprendendo Engenharia de Dados.

> Observação: o repositório é organizado como um caderno de estudos. Existe também uma ferramenta opcional (um app Streamlit) que permite visualizar esses arquivos como mapas mentais para revisão visual, mas o foco principal aqui é o conteúdo escrito — as notas e explicações em Markdown.

## Conteúdo
- `conteudo/` — anotações em Markdown organizadas por tema (ex.: `cloud_computing.md`).

## Como usar como material de estudos

1. Abra os arquivos em `conteudo/` no seu editor preferido (VS Code, Obsidian, etc.).
2. Leia os tópicos na ordem sugerida pelos títulos e subtítulos. Use os headings (H1/H2/H3) como índice para revisar os conceitos.
3. Faça anotações adicionais e exercícios diretamente nos arquivos Markdown ou crie novos arquivos para tópicos específicos.
4. Para revisão ativa, tente explicar cada tópico com suas próprias palavras ou transforme partes em pequenos exercícios práticos.

## Dicas de estudo
- Comece pelos conceitos fundamentais (por exemplo: modelos de armazenamento, ETL, arquitetura em camadas) antes de partir para serviços específicos.
- Relacione teoria com exemplos práticos: construa um pipeline simples com dados fictícios, execute transformações e faça análises.
- Revisite e refatore suas anotações: resuma capítulos, destaque pontos-chave e crie flashcards a partir das seções mais importantes.

## Ferramenta opcional — visualização como mapa mental

Existe um app Streamlit (`streamlit_markmap.py`) que transforma arquivos Markdown em mapas mentais interativos. Ele é útil para revisão visual rápida, mas não substitui a leitura atenta do conteúdo.

## Executar o app (opcional)

```bash
pyenv install 3.10.11
pyenv local 3.10.11
poetry env use 3.10.11
poetry install
poetry run streamlit run streamlit_markmap.py
```

## Contribuindo

- Adicione ou atualize arquivos dentro da pasta `conteudo/` para melhorar o material.
- Melhore exemplos, incorpore exercícios com soluções e inclua referências bibliográficas.

## Licença

Escolha uma licença adequada (ex.: MIT) e adicione um arquivo `LICENSE` se desejar tornar o material reutilizável publicamente.
