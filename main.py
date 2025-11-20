from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    budget = input("What is your budget? H(igh)/M(edium)/L(ow): ").lower()
    if budget.startswith("h"):
        facts.append("budget_high")
    if budget.startswith("m"):
        facts.append("budget_medium")
    if budget.startswith("l"):
        facts.append("budget_low")
    if input("Are you using it for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Are you using it for creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is it for office use? (y/n): ").lower().startswith("y"):
        facts.append("office")
    os = input("What is your preferred os? M(ac)/W(indows)/L(inux): ").lower()
    if os.startswith("m"):
        facts.append("pref_os_mac")
    if os.startswith("w"):
        facts.append("pref_os_win")
    if os.startswith("l"):
        facts.append("pref_os_lin")
    if input("Does it need ai accellerated gpu? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Will you be using it while travelling often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    # if input("Is your budget low? (y/n): ").lower().startswith("y"):
    #     facts.append("budget_low")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    facts = collect_initial_facts()
    print(facts)
    # print(load_rules(KB_PATH))
    # print(facts)
    FCE = ForwardChainingEngine(load_rules(KB_PATH)) 
    FCE.assert_facts(facts)
    FCE.run()
    result = FCE.conclusions()
    if result["recs"] == []:
        result["recs"].append("No Result")
    print("\n")
    print(result["recs"][0])
    print("specs: ")
    for spec in result["spec"]: print("    ",spec)
    pass

if __name__ == "__main__":
    main()
