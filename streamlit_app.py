import os
import time
import random
import platform
import streamlit as st
import subprocess
from gtts import gTTS
from pathlib import Path

#---------------------------------------------------------------------
    # 1. Configuração da página
#---------------------------------------------------------------------

st.set_page_config(
    page_title= 'Honestidade Corporativa',
    page_icon= '🎯',
    initial_sidebar_state= 'auto', # CORRIGIDO: de 'TESTE' para 'auto'
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

st.title("Honestidade Corporativa")
st.caption("v2.0.0 | Central de Injeção de Áudio Virtual (Teams, Zoom, Meet)")

st.info(
    "🔒 **Modo Infiltrado Ativo:** O áudio gerado aqui será injetado direto no "
    "canal virtual do sistema, funcionando de forma 100% digital em qualquer plataforma."
)

st.markdown("---")

if frase:
    st.markdown("### Painel de Disparo (Roleta-Russa)")
    
    # Definido o nome do botão na interface
    ativar_caos = st.button("Disparar Sinceridade", use_container_width=True)

    if ativar_caos: # CORRIGIDO: Erro de digitação corrigido de 'activar_caos' para 'ativar_caos'
        frase_final = random.choice(frase)

        with st.spinner("Gerando sintonia de voz digital..."):
            # Gera o áudio com a voz natural do Google
            tts = gTTS(text=frase_final, lang="pt", tld="com.br")
            tts.save("audio_reuniao.mp3")

        st.error(f"**SinceroBot disse na reunião:** \n\n *\"{frase_final}\"*")

        # --- SISTEMA DE REPRODUÇÃO MULTI-PLATAFORMA (try/except + if/else) ---
        sistema = platform.system()
        try:
            if sistema == "Linux":
                # No Linux, usa o comando nativo paplay
                subprocess.run(["paplay", "audio_reuniao.mp3"], check=False)
                
            elif sistema == "Darwin":
                # No macOS, usa o comando nativo afplay
                subprocess.run(["afplay", "audio_reuniao.mp3"], check=False)
                
            elif sistema == "Windows":
                # No Windows, tenta usar o pygame para não abrir nenhuma janela (Modo Infiltrado)
                try:
                    import pygame
                    pygame.mixer.init()
                    pygame.mixer.music.load("audio_reuniao.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
                    pygame.mixer.music.unload()
                except ImportError:
                    # Se não tiver o pygame instalado no Windows, abre o áudio com o player padrão do sistema
                    os.startfile("audio_reuniao.mp3")
                    time.sleep(4) # Dá 4 segundos para o player ler o arquivo antes de o tentar apagar
                    
        except Exception as e:
            st.warning(f"Não foi possível reproduzir o áudio automaticamente: {e}")
        
        # Limpa o arquivo temporário com segurança
        if os.path.exists("audio_reuniao.mp3"):
            try:
                os.remove("audio_reuniao.mp3")
            except Exception:
                pass # Evita que a app trave caso o Windows ainda esteja a usar o arquivo

    st.markdown("---")
    st.caption(f"Sistema alimentado com {len(frase)} desaforos corporativos prontos.")