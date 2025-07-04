import os
from openai import OpenAI
from dotenv import load_dotenv
from services.memory import add_to_history, get_history
from services.token_tracker import add_tokens
from services.persona import get_mode_prompt
from services.rate_limiter import check_and_update_usage



load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_gpt(prompt: str, user_id: int) -> str:
    try:
        # Get chat history
        history = await get_history(user_id)

        # Insert persona-based system prompt
        system_prompt = get_mode_prompt(user_id)
        messages = [{"role": "system", "content": system_prompt}] + history
        messages.append({"role": "user", "content": prompt})

        # Estimate token usage before actual call (optional)
        estimated_tokens = sum(len(m["content"]) for m in messages) // 4  # Rough guess

        # ✅ Check rate limit BEFORE API call
        allowed, reason = check_and_update_usage(user_id, estimated_tokens)
        if not allowed:
            return reason

        # Call GPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=300
        )

        # Extract response and token usage
        reply = response.choices[0].message.content.strip()
        total_tokens = response.usage.total_tokens

        # Track usage after call
        add_tokens(user_id, total_tokens)

        # Update memory
        await add_to_history(user_id, "user", prompt)
        await add_to_history(user_id, "assistant", reply)

        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"