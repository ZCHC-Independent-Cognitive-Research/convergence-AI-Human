
import spacy

nlp = spacy.load("es_core_news_sm")

with open("session.txt", "r", encoding="utf-8") as f:
    text = f.read()


doc = nlp(text)


emotion_words = {

    "miedo", "rabia", "odio", "dolor", "triste", "tristeza", "morir", "morirme", "morirme", "desaparecer", 
    "soledad", "vacío", "fracaso", "culpa", "vergüenza", "colapso", "sufrimiento", "abandono", "quebrarse",
    "derrumbe", "pérdida", "llorar", "infierno", "nada", "fracturarme", "resistir", "agonía", "hundirme",
    "saturado", "agotado", "saturación", "indiferencia", "desconexión", "quebrado", "ansiedad", "asfixia",

   
    "paz", "feliz", "felicidad", "esperanza", "renacer", "claridad", "dignidad", "valor", "amor", 
    "resiliencia", "luz", "honor", "sentido", "tregua", "calma", "alivio", "consuelo", "presencia", 
    "quietud", "descanso", "permanecer", "acompañado", "abrazo", "sostén", "ternura", "vivir"
}

clause_markers = {
    ",", ";", "y", "e", "o", "u", "pero", "aunque", "porque", "que", "pues", "como", "cuando", "donde", "mientras", 
    "si", "ya que", "sin embargo", "entonces", "además", "incluso"
}


total_tokens = 0
total_sentences = 0
emotion_count = 0
clause_estimate = 0
unique_tokens = set()


for sent in doc.sents:
    words = [token.text.lower() for token in sent if token.is_alpha]
    total_tokens += len(words)
    unique_tokens.update(words)
    total_sentences += 1
    emotion_count += sum(1 for word in words if word in emotion_words)
    clause_estimate += sum(1 for word in words if word in clause_markers) + 1

tokens_per_sentence = total_tokens / total_sentences if total_sentences else 0
lexical_diversity = len(unique_tokens) / total_tokens if total_tokens else 0
emotion_per_sentence = emotion_count / total_sentences if total_sentences else 0
clauses_per_sentence = clause_estimate / total_sentences if total_sentences else 0


print(f"Total Tokens: {total_tokens}")
print(f"Avg Tokens/Sentence: {tokens_per_sentence:.2f}")
print(f"Lexical Diversity: {lexical_diversity:.3f}")
print(f"Emotion Markers/Sentence: {emotion_per_sentence:.2f}")
print(f"Avg Clauses/Sentence: {clauses_per_sentence:.2f}")
