import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API OpenAI do arquivo .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

def generate_text_openai(job_description, mandatory_requirements, preferred_requirements, personal_tech_stack, language):
    """
    Você é um assistente especializado em gerar textos para candidaturas de emprego. 
Crie um texto com até 1500 caracteres que combine as informações abaixo, otimizando-o para passar por sistemas ATS e destacando palavras-chave importantes:
    """
    if language == "Português - BR":
        prompt = f"""
Você é um assistente especializado em gerar textos para candidaturas de emprego. 
Crie um texto com aproximadamente 1500 caracteres que combine as informações abaixo, otimizando-o para passar por sistemas ATS e destacando palavras-chave importantes:

- Descrição da Vaga: {job_description}
- Requisitos Obrigatórios: {mandatory_requirements}
- Requisitos Desejáveis: {preferred_requirements}
- Tech Stack do Candidato: {personal_tech_stack}

Gere um texto fluido, coerente e otimizado.
        """
    else:
        prompt = f"""
You are an assistant specialized in generating job application texts. 
Create a text with approximately 1500 characters that combines the information below, optimizing it to pass through ATS systems and highlighting important keywords:

- Job Description: {job_description}
- Mandatory Requirements: {mandatory_requirements}
- Preferred Requirements: {preferred_requirements}
- Candidate's Tech Stack: {personal_tech_stack}

Generate a fluid, coherent, and optimized text.
        """
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Você é um assistente que gera textos otimizados para candidaturas de emprego."},
                {"role": "user", "content": prompt}
            ]
        )
        generated_text = completion.choices[0].message.content 
        return generated_text
    except Exception as e:
        return f"Erro na chamada da API: {str(e)}"

def main():
    # Inicializa o contador de currículos, se ainda não estiver definido
    if "generated_count" not in st.session_state:
        st.session_state["generated_count"] = 0

    # Botão switch no topo para escolher a interface
    language = st.selectbox("Escolha o idioma / Choose the language", ["Português", "English"])

    if language == "Português - BR":
        st.title("Gerador de Texto ATS-Friendly com ChatGPT-4o")
        st.markdown(
            "Preencha os campos abaixo com as informações da vaga e seu tech stack. "
            "O texto será gerado utilizando a API do ChatGPT-4o da OpenAI."
        )
        
        # Entradas dos dados
        job_description = st.text_area(
            "Descrição da Vaga", height=150, 
            help="Insira a descrição da vaga com as principais responsabilidades."
        )
        mandatory_requirements = st.text_area(
            "Requisitos Obrigatórios", height=100, 
            help="Liste os requisitos obrigatórios."
        )
        preferred_requirements = st.text_area(
            "Requisitos Desejáveis", height=100, 
            help="Liste os requisitos desejáveis."
        )
        personal_tech_stack = st.text_area(
            "Seu Tech Stack", height=100, 
            help="Liste suas tecnologias e habilidades.  Pode ser um texto de apresentação."
        )
    else:
        st.title("ATS-Friendly Text Generator with ChatGPT-4o")
        st.markdown(
            "Fill in the fields below with the job information and your tech stack. "
            "The text will be generated using OpenAI's ChatGPT-4o API."
        )
        
        # Entradas dos dados
        job_description = st.text_area(
            "Job Description", height=150, 
            help="Enter the job description with the main responsibilities."
        )
        mandatory_requirements = st.text_area(
            "Mandatory Requirements", height=100, 
            help="List the mandatory requirements."
        )
        preferred_requirements = st.text_area(
            "Preferred Requirements", height=100, 
            help="List the preferred requirements."
        )
        personal_tech_stack = st.text_area(
            "Your Tech Stack", height=100, 
            help="List your technologies and skills.  It can be a presentation resume."
        )
    
    # Organiza o botão e o contador na mesma linha
    col1, col2 = st.columns([3, 1])
    with col1:
        generate_button = st.button("Gerar Texto" if language == "Português - BR" else "Generate Text")
    with col2:
        st.markdown("Currículos Gerados")
        st.text(f"{st.session_state['generated_count']}")

    # Ao clicar no botão, processa os dados e chama a API
    if generate_button:
        if not job_description.strip():
            st.error("A descrição da vaga não pode estar vazia." if language == "Português - BR" else "The job description cannot be empty.")
        else:
            with st.spinner("Gerando texto..." if language == "Português - BR" else "Generating text..."):
                result_text = generate_text_openai(job_description, mandatory_requirements, preferred_requirements, personal_tech_stack, language)
            st.subheader("Texto Gerado" if language == "Português - BR" else "Generated Text")
            st.text_area("Texto para Copiar" if language == "Português - BR" else "Text to Copy", value=result_text, height=800)
            st.text(f"Total de caracteres: {len(result_text)}" if language == "Português - BR" else f"Total characters: {len(result_text)}")

            # Incrementa o contador de currículos gerados
            st.session_state["generated_count"] += 1

if __name__ == '__main__':
    main()
