import expert_system as es
from rules import rules

kb = es.KnowledgeBase(rules)
print(kb.get('фильм'))