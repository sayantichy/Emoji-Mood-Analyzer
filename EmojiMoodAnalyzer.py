# Emoji Mood Analyzer
mood_dict = {
    "happy": "😊 Stay positive and keep smiling!",
    "sad": "😢 It's okay to feel sad. Better days are ahead!",
    "angry": "😡 Take a deep breath. Stay calm and strong!",
    "excited": "🤩 Enjoy the moment and make the most of it!",
    "bored": "😐 Try something new or fun to refresh yourself!"
}

mood = input("How are you feeling today? (happy/sad/angry/excited/bored) → ").lower()
print(mood_dict.get(mood, "🤔 I don't recognize that mood. But stay awesome!"))
