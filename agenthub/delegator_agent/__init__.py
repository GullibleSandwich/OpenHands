from agenthub.delegator_agent.agent import DelegatorAgent
from curio.controller.agent import Agent

Agent.register('DelegatorAgent', DelegatorAgent)
