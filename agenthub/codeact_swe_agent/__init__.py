from agenthub.codeact_swe_agent.codeact_swe_agent import CodeActSWEAgent
from curio.controller.agent import Agent

Agent.register('CodeActSWEAgent', CodeActSWEAgent)
