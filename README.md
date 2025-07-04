# 🤖 ChatGPT Discord Bot (GPT-4o)

An intelligent, multi-user Discord bot powered by **OpenAI’s GPT-4o**, designed for fast, contextual conversations with real-time memory, personality modes, rate limiting, and Dockerized deployment.

---

## 🧠 Features

- `!ask <message>` — Ask anything and receive smart, contextual replies from GPT-4o.
- ✅ **GPT-4o model** — Fast, lightweight, and supports multi-modal inputs (future-ready).
- 🧵 **Per-user memory** — Persist user conversations using Redis.
- 🧬 **Personas** — Choose between assistant styles like `tutor`, `critic`, `meme`, and more.
- 📊 **Rate limiting** — Enforces per-user message and token quotas.
- 🌐 **Environment-based config** — Secure token/key management via `.env`.
- 🐳 **Docker-ready** — Easy to deploy in any environment with Docker.
- ⚙️ **Modular codebase** — Clean, extensible service-layer architecture.

---

## 🛠️ Tech Stack

| Component     | Description                     |
|---------------|---------------------------------|
| `Python (async)` | Async I/O for scalable operations |
| `discord.py`  | Discord bot framework          |
| `OpenAI SDK`  | Interface to GPT-4o             |
| `Redis`       | Per-user memory storage         |
| `dotenv`      | Environment config              |
| `Docker`      | Containerized deployment        |

---
💬 Bot Commands
Command	Description
!ask <message>	Ask GPT-4o a question.
!mode <type>	Change assistant persona (tutor, critic, etc.).
!modes	List all available modes.
!reset	Reset memory and persona for your session.
!tokens	Show your total token usage.
!usage	Show your daily usage and limits.

🧩 Available Modes (Personas)
default – A helpful assistant.

tutor – A patient, step-by-step teacher.

critic – A brutally honest code reviewer.

meme – Replies with memes and Gen-Z slang.

pirate – Talks like a sarcastic pirate.

📈 Rate Limits (Default)
Limit Type	Value
Tokens/day	10,000
Messages/day	100

(Limits can be changed in services/rate_limiter.py)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatgpt-discord-bot.git
cd chatgpt-discord-bot

Create a .env File
DISCORD_TOKEN=your-discord-bot-token
OPENAI_API_KEY=your-openai-api-key

Install Dependencies
pip install -r requirements.txt

Run the Bot
python bot/main.py

