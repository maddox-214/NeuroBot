🤖 ChatGPT Discord Bot (GPT-4o)
An intelligent, multi-user Discord bot powered by OpenAI’s GPT-4o with real-time conversation memory, persona support, and Dockerized deployment.

🧠 Features
!ask <question> — Ask anything and get smart, contextual answers

✅ GPT-4o model (lightweight, fast, and multi-modal-ready)

🧵 Per-user memory using Redis (conversation persistence)

🌐 Environment-configurable via .env for secure token and key storage

🐳 Docker-ready for deployment anywhere

⚙️ Clean project structure for extensibility

🛠 Tech Stack
Python (async)

discord.py – Bot framework

OpenAI SDK (openai>=1.0.0)

Redis – Per-user memory store

Docker – Containerized deployment

dotenv – Config management

🚀 Setup
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/chatgpt-discord-bot.git
cd chatgpt-discord-bot
Create .env file

env
Copy
Edit
DISCORD_TOKEN=your-discord-bot-token
OPENAI_API_KEY=your-openai-api-key
REDIS_URL=redis://localhost:6379
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Start Redis

bash
Copy
Edit
# Option 1: Local
brew install redis && redis-server

# Option 2: Docker
docker run -p 6379:6379 redis
Run the bot

bash
Copy
Edit
python bot/main.py
