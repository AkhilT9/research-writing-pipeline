
# Research–Writing Agents using CrewAI

This project demonstrates a **multi-agent AI system** built using **CrewAI** and **AWS Bedrock**, where specialized agents collaborate to research a topic and generate a simplified explanation.  
A **Gradio-based UI** is included for easy testing and live demonstration of the agent workflow.

---

## 📌 Project Overview

Instead of relying on a single AI model, this project uses a **multi-agent architecture**:
- One agent focuses on research
- Another agent focuses on writing
- Tasks are orchestrated sequentially using CrewAI

This approach improves clarity, structure, and scalability for complex tasks.

---

## 🧠 Agents Used

### 1️⃣ Researcher Agent
- Researches the given topic
- Produces structured and informative content
- Uses AWS Bedrock (Claude)

### 2️⃣ Writer Agent
- Takes research output as input
- Converts it into a simple, user-friendly explanation

---

## 🔄 Workflow / Process Flow

```

User Input
↓
Gradio UI
↓
Crew Initialization
↓
Task 1: Research
↓
Researcher Agent
↓
AWS Bedrock (Claude)
↓
Research Output
↓
Task 2: Writing
↓
Writer Agent
↓
AWS Bedrock (Claude)
↓
Final Output

```

---

## 🛠️ Tech Stack

- Python
- CrewAI (Multi-agent orchestration)
- AWS Bedrock (Claude LLM)
- Gradio (UI for testing)
- python-dotenv
- boto3

---

## 📂 Project Structure

```

research-writing-agents/
│
├── app.py              # Gradio UI
├── llm.py              # AWS Bedrock LLM configuration
├── agents.py           # Agent definitions
├── tasks.py            # Task definitions
├── crew.py             # Crew orchestration
├── main.py             # CLI execution
├── requirements.txt    # Dependencies
├── .env                # AWS credentials (ignored by git)
├── .gitignore
└── venv/

````

---

## ⚙️ Setup Instructions (Windows Only)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/research-writing-agents.git
cd research-writing-agents
````

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate virtual environment (Windows)

```bash
venv\Scripts\activate
```

You should see:

```
(venv)
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-south-1
```

> Ensure AWS Bedrock access is enabled for Claude models.

---

## ▶️ Running the Project

### Option 1: Run via CLI

```bash
python main.py
```

---

### Option 2: Run with Gradio UI (Recommended)

```bash
python app.py
```

* Browser opens automatically
* Enter a topic
* Click **Run Crew**
* View multi-agent output live

---

## ✅ Key Features

* Role-based multi-agent design
* Task decomposition and orchestration
* AWS Bedrock integration (no OpenAI dependency)
* Gradio-based interactive UI
* Clean and modular project structure

---

## 🚀 Future Enhancements

* Add fact-checking or verification agent
* Integrate external tools or documents
* Store outputs in AWS S3
* Convert to FastAPI backend
* Add RAG (Retrieval-Augmented Generation)

---

## 🎯 Learning Outcomes

* Understanding multi-agent AI workflows
* Hands-on experience with CrewAI
* AWS Bedrock LLM integration
* Agent collaboration and orchestration
* Rapid AI prototyping using Gradio

---

## 📌 Author

Developed as a learning and demonstration project to explore **multi-agent AI systems** using CrewAI and AWS Bedrock.
Designed and implemented a multi-agent AI system using CrewAI with role-based agents for research and content generation.

Integrated AWS Bedrock (Claude LLM) for secure, cloud-based inference without OpenAI dependency.

Built a task-oriented workflow enabling agent collaboration, memory sharing, and sequential task execution.

Developed an interactive Gradio UI to test and demonstrate real-time multi-agent AI workflows.

Implemented modular architecture separating agents, tasks, orchestration, and UI for scalability
```
