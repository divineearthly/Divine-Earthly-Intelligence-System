
import json
import os
import datetime
from trend_analyzer import TrendAnalyzer
from research_reader import ResearchReader

class EvolutionEngine:
    def __init__(self, log_path='DEIOS/agents/self_evolution_log.json'):
        self.log_path = log_path
        self.analyzer = TrendAnalyzer()
        self.reader = ResearchReader()

    def generate_upgrade_proposal(self):
        trends = self.analyzer.scan_trends()
        insights = self.reader.parse_abstracts()

        proposal = {
            'timestamp': str(datetime.datetime.now()),
            'trend_discovery': trends[0] if trends else 'None',
            'research_insight': insights[0] if insights else 'None',
            'proposed_upgrade': f"Integrate {trends[0]['tech']} based on research regarding {insights[0][:30]}...",
            'status': 'LOGGED'
        }

        self._log_proposal(proposal)
        return proposal

    def _log_proposal(self, proposal):
        logs = []
        if os.path.exists(self.log_path):
            with open(self.log_path, 'r') as f:
                try: logs = json.load(f)
                except: logs = []
        logs.append(proposal)
        with open(self.log_path, 'w') as f:
            json.dump(logs, f, indent=2)
