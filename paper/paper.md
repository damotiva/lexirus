---
title: 'LexiRus: Word-Aligned Translation of Russian Learning Materials for International Students'
tags:
  - Python
  - education
  - natural language processing
  - Russian language
  - computer-assisted language learning
  - word alignment
authors:
  - name: Nataliya Kondrashova Vladimirovna
    affiliation: 1
  - name: Elijah Edward Masanga
    orcid: 0000-0003-2397-9680
    affiliation: 2
affiliations:
  - name: ITMO University, Saint Petersburg, Russian Federation
    index: 1
  - name: Damotiva, Mbeya, Tanzania
    index: 2
date: 25 December 2024
bibliography: paper.bib
---

# Summary

Russia attracts numerous international students seeking advanced education in modern technologies and specialized academic programs. However, a significant barrier exists: most undergraduate courses and technical subjects are taught exclusively in Russian. To address this challenge, preparatory courses have been established to teach the Russian language to international students before they begin their main studies. 

A critical problem in these programs is that Russian is often taught using Russian itself, despite students arriving with diverse native backgrounds—including **Swahili, French, Spanish, English, Portuguese, Arabic, Chinese, and Umbundu**. This necessitates constant manual translation by students, significantly impeding their learning progress. Furthermore, the occasional adoption of English as a bridge language by instructors creates an "instructional asymmetry," providing an unfair advantage to students with English proficiency while further marginalizing those from non-Anglophone backgrounds.

We present `LexiRus`, an open-source software system that provides word-level translation of Russian learning materials into students' native languages. By enabling immediate vocabulary comprehension, preserving the visual structure of learning materials, and providing transparent sentence structure analysis, this tool accelerates Russian language acquisition and helps international students transition more rapidly into their intended academic programs.

# Statement of Need

Language acquisition fundamentally requires mastering vocabulary (nouns and verbs) and understanding syntactic patterns [@krashen1982principles; @nation2013learning]. International students in Russian preparatory programs face a unique challenge: they must simultaneously decode Russian instruction while learning the language itself. Traditional teaching methods that use the target language to teach the target language create a "circular dependency" that extends learning time and increases cognitive load.

Existing translation tools typically operate at the sentence or paragraph level, often obscuring the word-to-word correspondence essential for language learning [@warschauer2004computer; @o2020neural]. Students need to understand not just the general meaning of a sentence, but how individual words combine to create meaning—a critical step in developing linguistic competence.

`LexiRus` addresses this gap by providing word-level translations that:

1. **Preserve structural relationships**: Students see direct correspondences between Russian and their native language syntax.
2. **Enable pattern recognition**: Grammatical structures become visible through aligned translations.
3. **Reduce cognitive friction**: Immediate vocabulary access eliminates the translation bottleneck and reliance on external dictionaries.
4. **Accelerate learning**: Students progress faster when they can focus on language patterns rather than tedious dictionary lookups.
5. **Ensure Linguistic Equity**: By supporting a wide range of native languages, the tool removes the dependency on English as an intermediary bridge.

# Implementation

`LexiRus` is built as a modular system designed to handle the complexities of Russian morphology and PDF structure preservation.



## Architecture

The system implements a modular architecture with the following core components:

1. **Document Parser**: Extracts text and layout metadata from various learning material formats (primarily PDF).
2. **Tokenization Engine**: Segments Russian text into individual words while preserving grammatical context using `spaCy` and `NLTK` [@honnibal2020spacy; @bird2009natural].
3. **Translation Module**: Interfaces with high-performance translation APIs to provide context-aware, word-level translations.
4. **Alignment System**: Maintains correspondence between source and target language words across different syntactic structures.
5. **User Interface**: Presents aligned translations in an accessible, learner-friendly PDF format.

## Core Features

- **Word-level granularity**: Each Russian word is individually translated and aligned with the original text.
- **Context preservation**: Grammatical relationships are maintained in the translation to ensure accuracy.
- **Multiple language support**: Full support for **Swahili, Umbundu, French, Spanish, English, Portuguese, Arabic, and Chinese**.
- **Interactive learning**: Users can comprehend new vocabulary while studying the original layout of their course materials.
- **Export functionality**: Processed materials are saved in PDF format for high-fidelity offline study.
- **Caching mechanism**: A **PostgreSQL** database stores previously translated words to improve system performance and reduce latency.

## Technical Stack

The implementation leverages a modern, robust technology stack:

- **Python 3.8+**: The core engine for text processing and logic.
- **NLP Libraries**: `spaCy` and `NLTK` for tokenization and linguistic analysis.
- **AI Backend**: Contextual word alignment and translation powered by the **Llama 3 Open Source Model**, which utilizes the Transformer architecture [@vaswani2017attention].
- **Web Framework**: **Django** for backend management and user data handling.
- **Frontend**: **NuxtJS** for a responsive and intuitive user interface.

## Installation and Usage

```bash
# Installation
pip install lexirus

# Basic usage
from lexirus import PDFTranslator

# Initialize translator for Swahili
translator = PDFTranslator(target_language='sw')

# Translate a document
translated_doc = translator.translate_document('learning_material.pdf')

# Save output
translated_doc.save('learning_material_sw.pdf')

```

# Research Context

This work builds upon established principles in second language acquisition [@krashen1982principles] and computer-assisted language learning (CALL) [@warschauer2004computer]. The word-level translation approach aligns with research showing that explicit vocabulary instruction combined with contextual exposure produces optimal learning outcomes [@nation2013learning; @laufer2005focus]. 

Previous studies have demonstrated that learners benefit from seeing structural correspondences between their native language and the target language [@lado1957linguistics; @jarvis2008crosslinguistic]. `LexiRus` operationalizes this insight by making these correspondences explicit and immediately accessible. The approach is particularly relevant for morphologically rich languages like Russian, where understanding word formation patterns and case systems is crucial [@timberlake2004reference].

# Comparison with Existing Tools

Unlike general-purpose translation tools (such as Google Translate, DeepL, and Yandex.Translate), our system provides unique pedagogical value:

* **Word-Level Alignment**: Specifically designed for language learning and structural analysis rather than just general communication.
* **Grammatical Visibility**: Helps the learner "see" the underlying grammar instead of hiding it behind a fluent, sentence-level translation.
* **Direct Material Integration**: Specifically optimized for the PDF formats and technical layouts used in academic settings.

Compared to existing language learning platforms like Duolingo, Babbel, or Rosetta Stone [@vesselinov2012duolingo], `LexiRus` offers distinct advantages for university-level students:

* **Authentic Materials**: Works with actual university textbooks and specialized technical curricula rather than fixed, generic exercises.
* **Curriculum-Agnostic**: Allows instructors to continue using their established curricula while providing an automated layer of accessibility.
* **Technical Focus**: Specifically optimized for the complex vocabulary challenges found in Russian preparatory programs.

# Future Work

Planned enhancements for the `LexiRus` ecosystem include:

1.  **Audio Integration**: Implementation of pronunciation guides and text-to-speech (TTS) for both the translated words and the original Russian terms to aid phonetic acquisition.
2.  **Mobile Applications**: Development of native iOS and Android applications to facilitate mobile learning and real-time translation during university lectures.
3.  **Morphological Tagging**: Visualizing Russian case endings and verbal aspects through color-coded highlights to further assist in grammar recognition.

# Acknowledgments

We acknowledge ITMO University and Associate Professor Nataliya Kondrashova Vladimirovna. Special thanks to Nataliya Kondrashova Vladimirovna for her pedagogical oversight and the students who participated in the pilot program, providing the feedback necessary to refine the system.

# References