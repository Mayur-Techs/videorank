def safe_int(value):
    try:
        return int(value)
    except:
        return 0
    

def format_views(views):
    if views >= 1_000_000:
        return f"{views/1_000_000:.1f}M"
    elif views >= 1_000:
        return f"{views/1_000:.1f}K"
    return str(views)

def clean_text(text):
    if not text:
        return ""
    return text.replace("\n", " ").strip()

def calculate_score(views, multiplier=1):
    return round((views / 100000) * multiplier, 2)