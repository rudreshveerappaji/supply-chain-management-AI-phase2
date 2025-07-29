from flask import Flask, jsonify
from agents import setup_agents
from tasks import setup_tasks
from crewai import Crew

app = Flask(__name__)

@app.route("/")
def home():
    return "CrewAI SCM Agent System is running!"

@app.route("/run", methods=["GET"])
def run_agents():
    agents = setup_agents()
    tasks = setup_tasks(agents)
    crew = Crew(agents=list(agents.values()), tasks=tasks, memory=True, verbose=True)
    result = crew.run()
    return jsonify({"status": "completed", "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)