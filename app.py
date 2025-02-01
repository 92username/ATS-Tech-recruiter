import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API OpenAI do arquivo .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_text_openai(job_description, mandatory_requirements, preferred_requirements, personal_tech_stack):
    """
    Gera um texto utilizando a API da OpenAI (GPT-4) a partir dos dados fornecidos.
    
    Os dados são enviados em um prompt que instrui o assistente a criar um texto
    coerente, otimizado para ATS e com até 1500 caracteres.
    """
    prompt = f"""
Você é um assistente especializado em gerar textos para candidaturas de emprego. 
Crie um texto com até 1500 caracteres que combine as informações abaixo, otimizando-o para passar por sistemas ATS e destacando palavras-chave importantes:

- Descrição da Vaga: {job_description}
- Requisitos Obrigatórios: {mandatory_requirements}
- Requisitos Desejáveis: {preferred_requirements}
- Tech Stack do Candidato: {personal_tech_stack}

Gere um texto fluido, coerente e otimizado.
    """
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-4o",
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
    st.title("Gerador de Texto ATS-Friendly com ChatGPT-4")
    st.markdown(
        "Preencha os campos abaixo com as informações da vaga e sua tech stack. "
        "O texto será gerado utilizando a API do ChatGPT-4o da OpenAI."
    )
    
    # Entradas dos dados
    job_description = st.text_area(
        "Descrição da Vaga / Requisitos e atribuições", height=150, 
        help="Insira a descrição da vaga com as principais responsabilidades."
    )
    mandatory_requirements = st.text_area(
        "Requisitos Obrigatórios", height=100, 
        help="Insira os requisitos obrigatórios."
    )
    preferred_requirements = st.text_area(
        "Requisitos Desejáveis", height=100, 
        help="Insira os requisitos desejáveis."
    )
    personal_tech_stack = st.text_area(
        "Sua Tech Stack / Currículo", height=100, 
        help="Insira suas tecnologias e habilidades."
    )
    
    # Ao clicar no botão, processa os dados e chama a API
    if st.button("Gerar Texto"):
        if not job_description.strip():
            st.error("A descrição da vaga não pode estar vazia.")
        else:
            with st.spinner("Gerando texto..."):
                result_text = generate_text_openai(job_description, mandatory_requirements, preferred_requirements, personal_tech_stack)
            st.subheader("Texto Gerado")
            st.text_area("Texto para Copiar", value=result_text, height=200)
            st.text(f"Total de caracteres: {len(result_text)}")

if __name__ == '__main__':
    main()
