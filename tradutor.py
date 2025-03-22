from gtts import gTTS
from gtts.tokenizer import pre_processors
import PyPDF2
# coding: utf-8
import sys
import pymupdf

coding = sys.stdout.encoding

# Caminho do arquivo PDF
pdf_path = "apostila_agroecologia_para_audio_cap1.pdf"

# Abrir o PDF e extrair texto
with pymupdf.open(pdf_path) as doc:
    # with open(pdf_path, "rb") as file:
    # reader = PyPDF2.PdfReader(file, strict=True)
    # text = chr(12).join([page.extract_text(space_width=200)
    #                 for page in doc.pages if page.extract_text()])
    text = chr(12).join([page.get_text() for page in doc])

print(text)
# Gerar áudio usando gTTS (Google Text-to-Speech)
tts = gTTS(text, slow=False, lang_check=False,
           pre_processor_funcs=[pre_processors.tone_marks,
                                pre_processors.end_of_line,
                                pre_processors.abbreviations,
                                pre_processors.word_sub],
           lang='pt', tld='com.br')

# Definir caminho para salvar o arquivo de áudio
audio_path = "apostila_agroecologia_para_audio_cap1.mp3"
tts.save(audio_path)

# Retornar o caminho do arquivo gerado
# audio_path
