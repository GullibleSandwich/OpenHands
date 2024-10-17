from agenthub.codeact_agent.codeact_agent import CodeActAgent
from curio.controller.agent import Agent

Agent.register('CodeActAgent', CodeActAgent)
