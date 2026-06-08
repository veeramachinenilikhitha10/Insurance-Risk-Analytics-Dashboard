import pandas as pd

# Built-in word scoring list (No downloads required)
positive_words = {'excellent', 'good', 'helpful', 'satisfied', 'great', 'happy', 'smooth', 'easy', 'friendly', 'creative'}
negative_words = {'bad', 'slow', 'confusing', 'poor', 'issue', 'wrong', 'delay', 'difficult', 'long', 'unhelpful'}

def generate_score(text):
    if pd.isna(text):
        return 0.5
    
    words = str(text).lower().split()
    pos_count = sum(1 for w in words if any(p in w for p in positive_words))
    neg_count = sum(1 for w in words if any(n in w for n in negative_words))
    
    total = pos_count + neg_count
    if total == 0:
        return 0.5 # Neutral
        
    # Scale score smoothly between 0.1 and 0.9 based on word counts
    raw_score = (pos_count - neg_count) / total
    return round(((raw_score + 1) / 2) * 0.8 + 0.1, 4)

# Generate the column automatically
dataset['Score sentiment'] = dataset['Feedback'].apply(generate_score)
