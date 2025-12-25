# LexiRus: Word-Aligned Translation for Russian Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Llama 3](https://img.shields.io/badge/AI-Llama%203-orange)](https://llama.meta.com/)

**LexiRus** is an open-source software system designed to bridge the linguistic gap for international students studying in Russia. While traditional translation tools focus on sentence-level fluency, LexiRus provides **word-level alignment**. This allows students to decode Russian morphology and syntax directly into their native languages while keeping the original structure of their academic materials intact.

---

## 🚀 Features

* **Word-Level Granularity**: Translates individual tokens to help students map Russian cases and verbal aspects to their native syntax.
* **Document Structure Preservation**: Processes academic PDFs and generates dual-language versions that maintain the original layout.
* **Extensive Language Support**: Native support for **Swahili, Umbundu, French, Spanish, English, Portuguese, Arabic, and Chinese**.
* **Context-Aware Engine**: Leverages the **Llama 3 Open Source Model** to ensure translations are accurate within an academic context.
* **Linguistic Equity**: Removes the dependency on English as a "bridge language," ensuring all students have equal access to materials regardless of their English proficiency.

---

## 🛠️ Technical Stack



LexiRus is built using a modern, scalable stack:

* **Core Logic**: Python 3.8+
* **Natural Language Processing**: `spaCy` and `NLTK` for Russian tokenization and lemmatization.
* **AI Backend**: Llama 3 (via Transformer architecture) for context-sensitive translation and alignment.
* **Web Framework**: Django (Backend) & NuxtJS (Frontend).
* **Database**: PostgreSQL for translation caching to optimize performance and minimize API costs.

---

## 💻 Installation

```bash
# Clone the repository
git clone [https://github.com/damotiva/lexirus.git](https://github.com/damotiva/lexirus.git)
cd lexirus

# Install dependencies
pip install -r requirements.txt
```


## 📖 Usage

```bash

from lexirus import PDFTranslator

# Initialize translator for your target language (e.g., Swahili)
translator = PDFTranslator(target_language='sw')

# Translate a Russian academic PDF
translated_doc = translator.translate_document('chemistry_lecture.pdf')

# Save the aligned output
translated_doc.save('chemistry_lecture_aligned.pdf')
```


## Command Line Interface (CLI)

```bash
lexirus translate material.pdf --target-lang ar --output material_arabic.pdf
```

## 📊 Comparison with Existing Tools

| Feature | LexiRus | Google / DeepL | Duolingo / Babbel |
| :--- | :--- | :--- | :--- |
| **Granularity** | Word-Aligned | Sentence/Paragraph | Discrete Exercises |
| **Material Source** | Custom Academic PDFs | Web/User Input | Proprietary Curriculum |
| **Pedagogical Focus** | Structural/Academic | Fluency-oriented | Gamified/Basic |
| **Offline Use** | Exportable PDFs | Limited | Required App |


## 🗺️ Roadmap (Future Work)

- Audio Integration: Add text-to-speech (TTS) pronunciation for both Russian and native terms.

- Mobile Applications: Develop native iOS and Android versions for use during live lectures.

- Morphological Tagging: Color-coding Russian case endings to assist with grammar recognition.

## 🎓 Research & Citation
LexiRus is based on principles of second language acquisition and computer-assisted language learning (CALL). If you use this software in your research, please cite:

```
@article{2026lexirus,
  title={LexiRus: Word-Aligned Translation of Russian Learning Materials for International Students},
  author={Kondrashova, Nataliya Vladimirovna and Masanga, Elijah Edward},
  journal={Journal of Open Source Software (Not Yet Submitted)},
  year={2026}
}
```

## 🤝 Acknowledgments
We acknowledge the support of ITMO University. Special thanks to Associate Professor Nataliya Kondrashova Vladimirovna for her pedagogical guidance and the students who participated in the pilot program.

