# services/rate_limiter.py
from typing import Tuple
from collections import defaultdict
import time



# Limits
TOKEN_LIMIT_PER_DAY = 10000
MESSAGE_LIMIT_PER_DAY = 100

# Storage: user_id → [tokens_today, messages_today, reset_timestamp]
usage_data = defaultdict(lambda: {
    "tokens": 0,
    "messages": 0,
    "reset": time.time() + 86400  # 24 hours from first use
})

def check_and_update_usage(user_id: int, tokens_used: int) -> Tuple[bool, str]:
    now = time.time()
    data = usage_data[user_id]

    # Reset if day passed
    if now >= data["reset"]:
        data["tokens"] = 0
        data["messages"] = 0
        data["reset"] = now + 86400

    # Check limits
    if data["tokens"] + tokens_used > TOKEN_LIMIT_PER_DAY:
        return False, "❌ Daily token limit reached."
    if data["messages"] + 1 > MESSAGE_LIMIT_PER_DAY:
        return False, "❌ Daily message limit reached."

    # Update usage
    data["tokens"] += tokens_used
    data["messages"] += 1
    return True, ""
