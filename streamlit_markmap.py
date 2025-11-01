"""streamlit_markmap.py
Streamlit app que mostra arquivos Markdown da pasta conteudo/ como mapas mentais interativos
usando Markmap embutido via CDN.

Uso:
  poetry run streamlit run streamlit_markmap.py

Features:
- lista todos os arquivos .md da pasta conteudo/
- mostra o conteúdo original do arquivo selecionado
- converte e exibe como mapa mental interativo
- permite baixar o mapa mental como HTML standalone
"""

import streamlit.components.v1 as components
import streamlit as st
import html
import os
import glob

ST_REPO_CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conteudo")

HTML_TEMPLATE = """<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{title}</title>
    <style>
        body {{ margin: 0; padding: 20px; }}
        #mindmap {{ height: 100%; width: 100%; min-height: 500px; }}
    </style>
</head>
<body>
    <svg id="mindmap"></svg>
    <script src="https://cdn.jsdelivr.net/npm/d3@6.7.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader"></script>
    <script>
        const markdown = `{markdown}`;
        window.addEventListener('load', () => {{
            const svg = document.querySelector('#mindmap');
            markmap.autoLoader.renderString(markdown, svg);
        }});
    </script>
</body>
</html>
"""

def build_html(md_text: str, title: str = "Markmap") -> str:
    # Escapar caracteres especiais no markdown
    safe_md = md_text.replace('\\', '\\\\').replace('`', '\\`').replace('"', '\\"')
    return HTML_TEMPLATE.format(title=html.escape(title), markdown=safe_md)

def list_local_md_files():
    if not os.path.exists(ST_REPO_CONTENT_DIR):
        return []
    pattern = os.path.join(ST_REPO_CONTENT_DIR, "**", "*.md")
    return sorted(glob.glob(pattern, recursive=True))

def read_md_from_path(filepath: str) -> str:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"Erro ao ler {filepath}: {e}")
        return ""

def main():
    st.set_page_config(page_title="Material de Estudos", layout="wide")
    st.title("📚 Material de Estudos em Engenharia de Dados")

    # Lista de arquivos .md disponíveis
    local_files = list_local_md_files()
    
    if not local_files:
        st.error("Nenhum arquivo .md encontrado na pasta `conteudo/`")
        return

    # Seleção do arquivo na barra lateral
    with st.sidebar:
        st.markdown("### Configurações")
        selected_file = st.selectbox(
            "Selecione um arquivo:",
            options=['Selecione um arquivo'] + local_files,
            index=0,
            format_func=lambda x: os.path.splitext(os.path.basename(x))[0].replace('_', ' ').title()
        )
        
        title = st.text_input(
            "Título do mapa mental",
            value=os.path.splitext(os.path.basename(selected_file))[0].replace('_', ' ').title()
        )
        height = st.number_input("Altura do mapa (px)", min_value=300, max_value=5000, value=600)

        st.markdown("---")
        st.markdown("### Sobre")
        st.markdown("Este app converte arquivos Markdown da pasta `conteudo/` em mapas mentais interativos usando [Markmap](https://markmap.js.org/).")

    # Carregar e exibir o conteúdo do arquivo selecionado
    if selected_file == 'Selecione um arquivo':
        st.info("Por favor, selecione um arquivo na barra lateral.")
        # Mostrar Readme como introdução
        readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
        readme_text = read_md_from_path(readme_path)
        st.markdown(readme_text)
        return
    filepath = os.path.abspath(selected_file)
    md_text = read_md_from_path(filepath)
    
    if md_text:
        # Exibir o conteúdo original do Markdown
        st.markdown("### Conteúdo Original")
        with st.expander("Ver conteúdo Markdown", expanded=True):
            st.markdown(md_text)
        
        st.markdown("### Mapa Mental Interativo")
        
        try:
            html_text = build_html(md_text, title)
            
            # Exibir o mapa mental
            components.html(
                html_text,
                height=height,
                scrolling=True
            )
            
            # Botão para baixar o HTML gerado
            filename = os.path.splitext(os.path.basename(selected_file))[0]
            st.download_button(
                "📥 Baixar mapa mental como HTML",
                data=html_text,
                file_name=f"{filename}_markmap.html",
                mime="text/html",
                help="Baixe o arquivo HTML para visualizar offline"
            )
        except Exception as e:
            st.error(f"Erro ao gerar/renderizar o mapa mental: {str(e)}")

if __name__ == "__main__":
    main()