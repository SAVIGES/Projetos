# app.py
import streamlit as st
import pandas as pd
import altair as alt
from questions_data import load_questions
st.logo("images/logo1.png", size="large", link="https://www.instagram.com/escola_renato/")

# configurações da página
st.set_page_config(
    page_title="Algoritmo De Análise De Perfil",
    page_icon="🎓",
    layout="wide"
)

# Carrega CSS externo
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def calcular_resultados(answers, questions):
    scores = {}
    for q_idx, answer_idx in answers.items():
        if answer_idx is not None:
            pesos = questions[q_idx]["pesos"][answer_idx]
            for materia, peso in pesos.items():
                scores[materia] = scores.get(materia, 0) + peso
    return scores



def show_results(scores):

    df = pd.DataFrame(list(scores.items()), columns=["Curso/Área", "Pontuação"])
    df = df.sort_values("Pontuação", ascending=False).reset_index(drop=True)

    
    if not df.empty:
        curso_top = df.iloc[0]["Curso/Área"]
        pontuacao = df.iloc[0]["Pontuação"]
    else:
        st.warning("Não foi possível determinar uma área de afinidade. Tente novamente.")
    
    st.subheader(f"Resultado:{curso_top}")
    esq,dir = st.columns(2)
    dir.markdown(
        f"<div class='recomendacao'>"
        f"<h4>🎯 Curso mais compatível: <span class='destaque'>{curso_top}</span></h4>"
        f"<p>Com base nas suas respostas, você demonstra maior afinidade com "
        f"<b>{curso_top}</b> </p>"
        f"<p>Esse curso combina com o seu modo de pensar e preferências gerais. "
        f"Vale a pena pesquisar mais sobre ele e ver se se identifica!</p>"
        f"</div>",
        unsafe_allow_html=True
    )


    

    esq.table(df)



if "tela_inicial" not in st.session_state:
    st.session_state.tela_inicial = True

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "questions" not in st.session_state:
    st.session_state.questions = load_questions()

if "submitted" not in st.session_state:
    st.session_state.submitted = False


if st.session_state.tela_inicial:
    



    st.title("Algoritmo para Análise de Perfil")
    esq,mid,dir = st.columns(3)
    esq.markdown(
        """
        Bem-vindo(a)!  
        Este teste foi criado para te ajudar a descobrir qual curso ou área combina mais com o seu perfil estudantil.

        Você responderá perguntas simples sobre como pensa, age e aprende.
        Ao final, verá o curso mais compatível e um gráfico com outras áreas que também se encaixam.

        
        """
    )


    esq,mid,dir = st.columns(3)
    if st.button("Iniciar Teste"):
        st.session_state.tela_inicial = False
        st.rerun()

else:
    total = len(st.session_state.questions)
    progress = (
        st.session_state.current_question / total
        if not st.session_state.submitted
        else 1.0
    )
    

    if not st.session_state.submitted:
        q = st.session_state.questions[st.session_state.current_question]
        
        esq,mid,dir = st.columns(3)
        mid.markdown(f"""<div id="Perguntas">  <center><h4>Pergunta {st.session_state.current_question + 1} de {total}</h4></center> </div>""", unsafe_allow_html=True)
        
        st.progress(progress)
        st.markdown(f"<strong>{q['pergunta']}</strong></center>", unsafe_allow_html=True)
        



        key = f"q_{st.session_state.current_question}"
        resposta = st.radio("Escolha uma opção:", q["alternativas"], key=key)
        idx = q["alternativas"].index(resposta)
        st.session_state.answers[st.session_state.current_question] = idx

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.session_state.current_question > 0 and st.button("⬅️ Anterior"):
                st.session_state.current_question -= 1
                st.rerun()

        with col2:
            if st.session_state.current_question < total - 1:
                if st.button("Próximo ➡️"):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Finalizar ✅"):
                    st.session_state.submitted = True
                    st.rerun()

    else:
        scores = calcular_resultados(st.session_state.answers, st.session_state.questions)
        show_results(scores)

        if st.button("🔁 Reiniciar Teste"):
            st.session_state.tela_inicial = True
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.rerun()


st.markdown(
    """
    <div class="sobre_nos">
        <center><p><a href="https://github.com/SAVIGES/Projetos">Sobre nós</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

