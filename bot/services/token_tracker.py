from collections import defaultdict

user_tokens = defaultdict(int)

def add_tokens(user_id: int, token_count: int):
    user_tokens[user_id] += token_count

def get_tokens(user_id: int) -> int:
    return user_tokens.get(user_id, 0)

def reset_tokens(user_id: int):
    user_tokens[user_id] = 0
