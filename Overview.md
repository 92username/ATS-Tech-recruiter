# Project Overview

1. **Main Objective**  
   - Build an application (initially using *Streamlit*) that generates a text of up to 1500 characters, merging the user’s tech stack with the requirements of an internship/job position.  
   - This text must include important *keywords* so it won’t be filtered out by Applicant Tracking Systems (ATS), such as Gupy.

2. **Scope and Features**  
   1. **Data Input**  
      - **Job Description**: A text containing the main responsibilities and tasks.  
      - **Mandatory Requirements**: A list of technologies, skills, or experiences required by the position.  
      - **Preferred Requirements**: A list of technologies or skills that would be a plus.  
      - **Personal Tech Stack**: The user’s own technologies and experiences.  

   2. **Processing**  
      - **Keyword Analysis and Extraction**:  
        - Identify relevant terms in the job description, mandatory requirements, and preferred requirements.  
      - **Comparison with Personal Tech Stack**:  
        - Check which of the user’s technologies match the job requirements.  
      - **Text Construction**:  
        - Combine the information into a coherent text incorporating both the position’s keywords and the user’s skills.  
        - Limit the text to 1500 characters.

   3. **Output/Display**  
      - **Generated Text**: Displayed on the screen, ready to be copied or fine-tuned.

3. **Implementation Approach**  
   - **Interface**:  
     - Use *Streamlit* to create a simple page where the user enters information in text fields.  
     - After clicking a button, the final text is displayed on the screen.  
   - **Internal Structure**:  
     - **Python** will handle string processing and data organization (list comprehensions, text manipulation functions, etc.).  
     ~~ - Native modules such as `re` (for regular expressions) and `textwrap` (for text handling) can be used if needed.~~
   - **Character Limit Control**:  
     - A dedicated function to check the final text size.  
   - **Future Improvements**:  
     - Potentially utilize NLP libraries (like `nltk` or `spacy`) for deeper semantic analysis in future versions.

4. **Possible Challenges**  
   1. **Keyword Filtering and Extraction**  
      - Ensuring keywords are correctly identified in the job description.  
      - Handling synonyms or varying terms with the same meaning (e.g., “Python” vs “programming in Python”).  
   2. **Character Limit**  
      - Keeping the text within 1500 characters without losing important details.  
      - Carefully preventing the truncation of critical sentences.  
   3. **Text Naturalness**  
      - Avoiding a “forced” or repetitive tone.  
      - Balancing keyword insertion with a naturally flowing text.  
   4. **Use of Streamlit**  
      - Keeping the application simple yet functional, focusing on user experience.  
   5. **Maintenance and Evolution**  
      - As the application grows, it may require storing histories, improving security, and more.

5. **Next Steps**  
   - **Define Folder Structure**: Allocate spaces for the main code, auxiliary functions, and potential tests.  
   - **Design Application Flow**: Sketch how users will interact with the interface.  
   - **Select a Text Generation Approach**: Decide whether to use basic string concatenation or some NLP techniques.  
   - **Plan Validation Tests**: Use real job descriptions to ensure the generated text is coherent, fits the character limit, and includes the necessary keywords.

---

**Summary**: The goal is to create a tool to help candidates adapt their resumes or cover letters for each job posting, ensuring the right keywords are present to pass ATS filters. We will use *Streamlit* for the interface and Python for text processing. Our immediate focus is on organizing the workflow, anticipating potential challenges, and ensuring the final output is a coherent, keyword-rich text within the 1500-character limit.
