from agenthub.planner_agent.agent import PlannerAgent
from curio.controller.agent import Agent

Agent.register('PlannerAgent', PlannerAgent)
