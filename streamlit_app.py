import random
import pyttsx3
import streamlit as st
import subprocess
from gtts import gTTS
from pathlib import Path

#---------------------------------------------------------------------
    # 1. Configuração da pag
#---------------------------------------------------------------------

st.set_page_config(
    page_title= 'Honestidade Corporativa',
    page_icon= '',
    initial_sidebar_state= 'TESTE',
    layout= 'centered'
)

#---------------------------------------------------------------------
    # 2. Ler o arquivo de frases
#---------------------------------------------------------------------   
atual = Path(__file__).resolve().parent 
path_frases = atual / 'bd_frases/frases.txt'

def carregar_frases():
    '''Lê o arquivo frases.txt e retorna uma lista simples de strings.'''
    lista_frases = []
    try:
        with path_frases.open('r', encoding='utf-8') as f:
            for linha in f:
                linha_limpa = linha.strip()
                if linha_limpa:  # Ignora linhas em branco
                    lista_frases.append(linha_limpa)
    except FileNotFoundError:
        st.error(
            "Erro crítico: O arquivo 'frases.txt' não foi encontrado na raiz."
        )
    return lista_frases


# Carregar as frases
frase = carregar_frases()

#---------------------------------------------------------------------
    # 3. Interface
#---------------------------------------------------------------------  

st.title("NOME")
st.caption("v2.0.0 | Central de Injeção de Áudio Virtual (Teams, Zoom, Meet)")

st.info(
    "🔒 **Modo Infiltrado Ativo:** O áudio gerado aqui será injetado direto no "
    "canal virtual do sistema, funcionando de forma 100% digital em qualquer plataforma."
)

st.markdown("---")

if frase:
    st.markdown("### Painel de Disparo (Roleta-Russa)")
    
    ativar_caos = st.button("COLOCA NOME AÇÃO", use_container_width=True)

    if activar_caos:
        frase_final = random.choice(frase)

        with st.spinner("Gerando sintonia de voz digital..."):
            # Gera o áudio com a voz natural do Google
            tts = gTTS(text=frase_final, lang="pt", tld="com.br")
            tts.save("audio_reuniao.mp3")

        st.error(f"**SinceroBot disse na reunião:** \n\n *\"{frase_final}\"*")

        # Reproduz o áudio usando o player nativo do Linux (mpg123 ou paplay)
        # Forçamos a saída para o dispositivo padrão que vamos configurar no passo seguinte
        subprocess.run(["paplay", "audio_reuniao.mp3"], check=False)
        
        # Limpa o arquivo temporário
        if os.path.exists("audio_reuniao.mp3"):
            os.remove("audio_reuniao.mp3")

    st.markdown("---")
    st.caption(f"Sistema alimentado com {len(frase)} desaforos corporativos prontos.")
