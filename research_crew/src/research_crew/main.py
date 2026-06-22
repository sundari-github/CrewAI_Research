#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from dotenv import load_dotenv

from datetime import datetime

from research_crew.crew import ResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

load_dotenv(Path(__file__).resolve().parents[2] / "env.config")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    This is your primary, "production" way to start the crew.
    It takes the inputs (like `topic`), passes them to the crew, and kicks off the execution process from start to finish.
    """
    # Get inputs for the agents
    input_topic = input("Enter the topic: ")
    email_recipient = input("Enter the recipient email address: ")
    current_year = str(datetime.now().year)
    inputs = {
        "topic": input_topic,
        "current_year": current_year,
        "recipient_email_addr": email_recipient
    }

    try:
        ResearchCrew(topic = input_topic).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    Used when developing the crew to improve performance. The crew evaluates its own outputs
    over multiple iterations and saves a fine-tuning file to perform better in the future.
    """
    # Get inputs for the agents
    topic = input("Enter the topic: ")
    email_recipient = input("Enter the recipient email address: ")
    current_year = str(datetime.now().year)
    inputs = {
        "topic": topic,
        "current_year": current_year,
        "recipient_email_addr": email_recipient
    }
    try:
        ResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    Used when your crew fails in the middle of a long execution. Provide a specific Task ID,
    and CrewAI will skip all successful tasks before that ID, resuming from the failure point.
    """
    try:
        ResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    Used to programmatically benchmark the quality of your crew's output by using another LLM
    (the "evaluator") to score your crew's outputs across multiple runs.
    """
    # Get inputs for the agents
    topic = input("Enter the topic: ")
    email_recipient = input("Enter the recipient email address: ")
    current_year = str(datetime.now().year)
    inputs = {
        "topic": topic,
        "current_year": current_year,
        "recipient_email_addr": email_recipient
    }

    try:
        ResearchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    Used to deploy the crew to a server (like AWS Lambda or Webhook) and start it programmatically.
    It expects a JSON payload containing all inputs instead of asking the user for terminal input.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": trigger_payload.get("topic", ""),
        "current_year": trigger_payload.get("current_year", str(datetime.now().year)),
        "recipient_email_addr": trigger_payload.get("recipient_email_addr", "")
    }

    try:
        result = ResearchCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

