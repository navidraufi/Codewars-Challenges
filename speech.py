from gtts import gTTS


love_words = {
    "Love": "Amour",
    "Romance": "Romance",
    "Heart": "Cœur",
    "Passion": "Passion",
    "Kiss": "Baiser",
    "Soulmate": "Âme sœur",
    "Adore": "Adorer",
    "Devotion": "Dévotion",
    "Affection": "Affection",
    "Intimacy": "Intimité"
}

story = "Il était une fois un petit chat et une petite souris qui s'aimaient beaucoup. Mais un jour, le chat a déménagé dans une autre ville et la souris n'a jamais pu le retrouver. Elle était si triste qu'elle décida de partir à son tour à la recherche de son amour perdu. Cependant, malgré tous ses efforts, elle ne réussit jamais à le retrouver. Finalement, elle comprit que parfois, l'amour ne suffit pas à surmonter les obstacles de la vie."

tts = gTTS(story, lang="fr")
tts.save("story.mp3")
    