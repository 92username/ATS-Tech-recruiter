[![Pylint](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/pylint.yml/badge.svg)](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/pylint.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/5af46814f5704138a7066c1d23abf174)](https://app.codacy.com/gh/92username/ATS-Tech-recruiter/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Docker Image CI](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/docker-image.yml/badge.svg)](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/docker-image.yml)

# ATS Tech Recruiter - Gerador de Textos ATS-Friendly com OpenAI GPT-4o

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

ATS Tech Recruiter é uma aplicação desenvolvida em **Python** utilizando **Streamlit** para interface gráfica e **OpenAI GPT-4o** para a geração de textos. O objetivo é auxiliar candidatos na criação de textos otimizados para processos seletivos, focando em sistemas de triagem automática de currículos (**ATS - Applicant Tracking System**).

Acesse o aplicativo clicando na badge ao lado => [![Hostinger](https://img.shields.io/badge/Hostinger-673DE6?style=for-the-badge&logo=hostinger&logoColor=white)](http://147.79.82.234:8501/)

## Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal da aplicação
- **Streamlit** - Framework para interface gráfica
- **OpenAI API (GPT-4o)** - Modelo de IA para geração de texto

---

## Instalação e Configuração

> **Nota:** Caso a aplicação não funcione por causa dos créditos da API da OpenAI terem se esgotado, rode localmente utilizando sua própria chave da API. Instruções de como rodar localmente a seguir.

### 1. Clonar o repositório

```bash
git clone https://github.com/92username/ATS-Tech-recruiter.git
cd ATS-Tech-recruiter
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate      # Para Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## ⚠️ 4. Configurar a API da OpenAI

A aplicação requer uma **chave de API** da OpenAI. Para utilizá-la, crie um arquivo **`.env`** na raiz do projeto e insira suas credenciais:

```ini
OPENAI_API_KEY=sua-chave-aqui
OPENAI_MODEL=gpt-4o  # Alterável para outros modelos compatíveis
```

> **💡 Nota:** Se o `.env` não for configurado corretamente, a aplicação não conseguirá acessar a API da OpenAI. Caso ocorra um erro `"missing API key"`, verifique se a chave foi adicionada corretamente e se o arquivo `.env` está salvo na raiz do projeto.

Se ainda não possui uma chave, obtenha uma conta e gere uma chave de API em:  
[https://platform.openai.com/signup](https://platform.openai.com/signup)

### 5. Executar o aplicativo

```bash
streamlit run app.py
```
O Streamlit abrirá automaticamente a interface no navegador.

---

## Uso da Aplicação

1. Escolha o **idioma** no topo da interface (Português ou Inglês).
2. Preencha os campos obrigatórios:
   - **Descrição da Vaga**
   - **Requisitos Obrigatórios**
   - **Requisitos Desejáveis**
   - **Tech Stack**
3. Clique em **Gerar Texto**.
4. Copie o texto gerado e faça ajustes se necessário.
5. A aplicação exibe o **modelo de IA utilizado** e o **contador de caracteres do texto gerado**.

---

## Personalização

### Alterar o Modelo da OpenAI

Caso queira testar outro modelo, basta modificar o arquivo `.env`:
```ini
OPENAI_MODEL=gpt-4-turbo
```
Modelos disponíveis:

- `gpt-4o` - Modelo mais avançado e rápido
- `gpt-4-turbo` - Opção mais eficiente em custo e tempo de resposta
- `gpt-3.5-turbo` - Alternativa mais econômica, porém menos precisa

Para confirmar qual modelo está sendo utilizado, a interface exibe essa informação no início da página.

---

## Possíveis Problemas e Soluções

### Erro: `"invalid model ID"`

Solução: Verifique se o modelo no `.env` está correto e disponível para sua conta OpenAI.

### Erro: `"missing API key"`

Solução: Confirme que a chave da OpenAI foi corretamente inserida no `.env`.

### Streamlit não abre no navegador

Solução: Acesse manualmente pelo link `http://localhost:8501/`.
  
Dúvidas ou sugestões podem ser enviadas via **GitHub Issues**.
