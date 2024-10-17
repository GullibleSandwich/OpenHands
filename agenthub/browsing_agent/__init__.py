from agenthub.browsing_agent.browsing_agent import BrowsingAgent
from curio.controller.agent import Agent

Agent.register('BrowsingAgent', BrowsingAgent)
