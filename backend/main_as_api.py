from flask import Flask, jsonify
from agents.setup_agents import setup_agents
from tasks.setup_tasks import setup_tasks
from crewai import Crew

app = Flask(__name__)

@app.route("/")
def home():
    return "CrewAI SCM Agent System is running!"

@app.route("/run", methods=["GET"])
def run_agents():
    try:
        from agents.setup_agents import setup_agents
        from tasks.setup_tasks import setup_tasks

        print("✅ setup_agents and setup_tasks imported")

        agents = setup_agents()
        print("✅ Agents set up")

        tasks = setup_tasks(agents)
        print("✅ Tasks set up")

        from crewai import Crew
        crew = Crew(agents=list(agents.values()), tasks=tasks, memory=True, verbose=True)
        print("✅ Crew initialized")

        result = crew.run()
        print("✅ Crew run complete")

        return jsonify({"status": "completed", "result": result})
    except Exception as e:
        import traceback
        print("❌ Exception in /run:")
        print(traceback.format_exc())
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
