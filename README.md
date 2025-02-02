[![Pylint](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/pylint.yml/badge.svg)](https://github.com/92username/ATS-Tech-recruiter/actions/workflows/pylint.yml)
# ATS Tech Recruiter - Gerador de Textos ATS-Friendly com OpenAI GPT-4o

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

ATS Tech Recruiter Ã© uma aplicaÃ§Ã£o desenvolvida em **Python** utilizando **Streamlit** para interface grÃ¡fica e **OpenAI GPT-4o** para a geraÃ§Ã£o de textos. O objetivo Ã© auxiliar candidatos na criaÃ§Ã£o de textos otimizados para processos seletivos, focando em sistemas de triagem automÃ¡tica de currÃ­culos (**ATS - Applicant Tracking System**).

## Tecnologias Utilizadas
- **Python 3.x** - Linguagem principal da aplicaÃ§Ã£o
- **Streamlit** - Framework para interface grÃ¡fica
- **OpenAI API (GPT-4o)** - Modelo de IA para geraÃ§Ã£o de texto

---

## InstalaÃ§Ã£o e ConfiguraÃ§Ã£o

### 1. Clonar o repositÃ³rio
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

### 3. Instalar dependÃªncias
```bash
pip install -r requirements.txt
```

## â ï¸ 4. Configurar a API da OpenAI

A aplicaÃ§Ã£o requer uma **chave de API** da OpenAI. Para utilizÃ¡-la, crie um arquivo **`.env`** na raiz do projeto e insira suas credenciais:

```ini
OPENAI_API_KEY=sua-chave-aqui
OPENAI_MODEL=gpt-4o  # AlterÃ¡vel para outros modelos compatÃ­veis
```

> **ð¡ Nota:** Se o `.env` nÃ£o for configurado corretamente, a aplicaÃ§Ã£o nÃ£o conseguirÃ¡ acessar a API da OpenAI. Caso ocorra um erro `"missing API key"`, verifique se a chave foi adicionada corretamente e se o arquivo `.env` estÃ¡ salvo na raiz do projeto.

Se ainda nÃ£o possui uma chave, obtenha uma conta e gere uma chave de API em:  
[https://platform.openai.com/signup](https://platform.openai.com/signup)

### 5. Executar o aplicativo
```bash
streamlit run app.py
```
O Streamlit abrirÃ¡ automaticamente a interface no navegador.

---

## Uso da AplicaÃ§Ã£o
1. Escolha o **idioma** no topo da interface (PortuguÃªs ou InglÃªs).
2. Preencha os campos obrigatÃ³rios:
   - **DescriÃ§Ã£o da Vaga**
   - **Requisitos ObrigatÃ³rios**
   - **Requisitos DesejÃ¡veis**
   - **Tech Stack**
3. Clique em **Gerar Texto**.
4. Copie o texto gerado e faÃ§a ajustes se necessÃ¡rio.
5. A aplicaÃ§Ã£o exibe o **modelo de IA utilizado** e o **contador de caracteres do texto gerado**.

---

## PersonalizaÃ§Ã£o
### Alterar o Modelo da OpenAI
Caso queira testar outro modelo, basta modificar o arquivo `.env`:
```ini
OPENAI_MODEL=gpt-4-turbo
```
Modelos disponÃ­veis:
- `gpt-4o` - Modelo mais avanÃ§ado e rÃ¡pido
- `gpt-4-turbo` - OpÃ§Ã£o mais eficiente em custo e tempo de resposta
- `gpt-3.5-turbo` - Alternativa mais econÃ´mica, porÃ©m menos precisa

Para confirmar qual modelo estÃ¡ sendo utilizado, a interface exibe essa informaÃ§Ã£o no inÃ­cio da pÃ¡gina.

---

## PossÃ­veis Problemas e SoluÃ§Ãµes

### Erro: `"invalid model ID"`
SoluÃ§Ã£o: Verifique se o modelo no `.env` estÃ¡ correto e disponÃ­vel para sua conta OpenAI.

### Erro: `"missing API key"`
SoluÃ§Ã£o: Confirme que a chave da OpenAI foi corretamente inserida no `.env`.

### Streamlit nÃ£o abre no navegador
SoluÃ§Ã£o: Acesse manualmente pelo link `http://localhost:8501/`.
  
DÃºvidas ou sugestÃµes podem ser enviadas via **GitHub Issues**.
