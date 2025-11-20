from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        # if rule.consequent.split(":")[0] == "recommend":
        # for fact in self.facts:
        #     if rule.consequent.split(":")[0] == fact.split(":")[0]:
        #         return False
        if rule.consequent in self.facts:
            return False
        for r in rule.antecedents:
            if r not in self.facts:
                break
        else:
            return True
        return False

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        running = True
        while running:
            running = False
            for r in self.rules:
                # print("thinking abt ", r )
                if self.can_fire(r):
                    running = True
                    # print("\n\ncan fire " , r)
                    self.facts.add(r.consequent)
                # self.trace.append()
        # print(self.facts)
        
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        pass

    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""
        conc = {"recs":[], "spec": []}
        for f in self.facts:
            if ":" in f:
                splitStr = f.split(":")
                if splitStr[0] == "recommend":
                    for r in self.rules:
                        if r.consequent == f:
                            if conc["recs"] == []:
                                conc["recs"].append(r.name)
                                conc["recs"].append(r.priority)
                            else:
                                if r.priority < conc["recs"][1]:
                                    conc["recs"][0] = r.name
                                    conc["recs"][1] = r.priority
                elif splitStr[0] == "spec":
                    for r in self.rules:
                        if r.consequent == f:
                            conc["spec"].append(r.name)
                        pass

        return conc
        pass
