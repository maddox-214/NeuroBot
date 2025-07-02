# bot/services/memory.py

user_memory = {}
MAX_HISTORY = 6

async def add_to_history(user_id: int, role: str, content: str):
    if user_id not in user_memory:
        user_memory[user_id] = []
    user_memory[user_id].append({"role": role, "content": content})
    user_memory[user_id] = user_memory[user_id][-MAX_HISTORY*2:]  # Keep only N turns

async def get_history(user_id: int):
    return user_memory.get(user_id, [])

async def reset_user_history(user_id: int):
    user_memory.pop(user_id, None)
