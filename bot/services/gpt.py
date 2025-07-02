import os
from openai import OpenAI
from dotenv import load_dotenv
from services.memory import add_to_history, get_history
from services.token_tracker import add_tokens
from services.persona import get_mode_prompt


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

        # Call GPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=300
        )

        # Extract response and token usage
        reply = response.choices[0].message.content.strip()
        total_tokens = response.usage.total_tokens  # ✅ this is what you track

        # Track user usage
        add_tokens(user_id, total_tokens)

        # Update memory
        await add_to_history(user_id, "user", prompt)
        await add_to_history(user_id, "assistant", reply)

        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"