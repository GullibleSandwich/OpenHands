from agenthub.dummy_agent.agent import DummyAgent
from curio.controller.agent import Agent

Agent.register('DummyAgent', DummyAgent)
