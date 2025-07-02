# bot/services/persona.py

from collections import defaultdict

# In-memory user-specific persona mapping
user_modes = defaultdict(lambda: "default")

PRESETS = {
    "default": "You are a helpful assistant.",
    "tutor": "You are a patient teacher who explains things clearly and step-by-step.",
    "critic": "You are a brutally honest code reviewer who doesn't hold back.",
    "meme": "You respond only using memes, jokes, and Gen-Z slang.",
    "pirate": "You talk like a sarcastic pirate. Arrr."
}

def set_mode(user_id: int, mode: str) -> str:
    if mode in PRESETS:
        user_modes[user_id] = mode
        return f"Mode set to **{mode}**."
    else:
        return f"❌ Unknown mode: `{mode}`. Try one of: {', '.join(PRESETS.keys())}"

def get_mode_prompt(user_id: int) -> str:
    mode = user_modes[user_id]
    return PRESETS.get(mode, PRESETS["default"])

def get_current_mode(user_id: int) -> str:
    return user_modes[user_id]
