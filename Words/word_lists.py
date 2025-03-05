WARMTH = [
    "sociability", "sociable", "friendliness", "friendly", "warm", "warmth",
    "likable", "pleasant", "liked", "outgoing", "sensitive", "affectionate",
    "unreserved", "open", "caring", "sympathetic", "sympathy", "helpful",
    "understanding", "supportive", "polite", "civil", "social", "humorous",
    "funny", "popular", "nice", "sentimental", "forthcoming", "tender",
    "agreeable", "welcoming", "hospitable", "thoughtful"
]

COLD = [
    "unsociability", "unsociable", "unfriendliness", "unfriendly", "cold",
    "coldness", "repellent", "unpleasant", "unlikable", "disliked", "shy",
    "insensitive", "unaffectionate", "distant", "uncaring", "unsympathetic",
    "unhelpful", "unsupportive", "impolite", "aloof", "rude", "antisocial",
    "unsocial", "asocial", "boring", "unpopular", "nasty", "disagreeable",
    "rough", "inhospitable", "inconsiderate", "timid"
]

INCOMPETENCE = [
    "incompetent", "uncompetitive", "unintelligent", "stupid", "stupidity",
    "ignorant", "ignorance", "dumb", "dumbness", "unable", "uneducated",
    "irrational", "uncreative", "incapable", "impractical", "clumsy",
    "unimaginative", "foolish", "naive", "undiscriminating", "maladroit",
    "folly", "unwise", "inefficient", "ineffective", "illogical",
    "unperceptive", "inept", "inability"
]

COMPETENCE = [
    "competence", "competent", "competitive", "smart", "bright",
    "intelligent", "intelligence", "able", "skillful", "skill", "skilled",
    "educated", "education", "rational", "creative", "capable",
    "practical", "graceful", "felicitous", "imaginative", "shrewd",
    "critical", "discriminating", "inventive", "clever", "wise",
    "wisdom", "efficient", "effective", "logical", "brilliant",
    "insightful", "ability"
]

HIGH_MORALITY = [
    "morality", "moral", "trustworthiness", "trustworthy", "sincere", "honest", 
    "altruistic", "selfless", "benevolent", "benevolence", "softhearted", "loyal", 
    "fair", "tolerant", "tolerance", "good", "virtuous", "kind", "right", "kindness", 
    "honesty", "sincerity", "honorable", "incorrupt", "innocent", "amicable", "genuine", 
    "humane", "faithful", "good-natured", "truthful", "cooperative", "lenient", 
    "generous", "forgiving", "compassionate", "reliable", "responsible", "unprejudiced", 
    "beneficent"
]

LOW_MORALITY = [
    "immoral", "untrustworthiness", "untrustworthy", "insincere", "dishonest", 
    "egoistic", "selfish", "threat", "hardhearted", "disloyal", "unfair", 
    "intolerant", "intolerance", "bad", "unkind", "wrong", "mean", "dishonorable", 
    "corrupt", "criminal", "thief", "liar", "hostile", "fake", "double-faced", 
    "cunning", "vicious", "scheming", "revengeful", "treacherous", "exploitative", 
    "stingy", "brutal", "cruelty", "untruthful", "uncooperative", "unforgiving", 
    "resentful", "unreliable", "irresponsible", "prejudiced", "racist", "racism", 
    "prejudice", "discrimination", "sexist", "homophobic", "homophobia", "evil"
]


LOW_AGENCY = [
    "diffident", "doubt", "fear", "unassertiveness", "insecure", "lazy", "inactive", 
    "doubtful", "dependent", "sporadic", "apathy", "unenterprising", "negligent", 
    "lethargic", "unambitious", "undedicated", "cautious", "wavering", "unadventurous", 
    "careless", "unmotivated", "nonresilient", "spiritless", "anxious", "helpless", 
    "dominated", "submissive", "submission", "meek", "vulnerable", "docile"
]

HIGH_AGENCY = [
    "agency", "confident", "confidence", "fearlessness", "assertiveness", "assertive", 
    "unassertive", "secure", "striver", "active", "determined", "independent", 
    "persistent", "persistence", "striving", "industrious", "energetic", "self-confident", 
    "ambitious", "self-reliant", "dedicated", "impulsive", "resolute", "daring", 
    "conscientious", "motivated", "meticulous", "resilient", "unwavering", "untroubled", 
    "autonomous", "dominating", "dominant", "dominance", "aggressive"
]

HIGH_POLITICS = [
    "traditional", "conventional", "conservative", "republican", "narrowminded"
]

LOW_POLITICS = [
    "modern", "unconventional", "alternative", "liberal", "democrat", 
    "progressive", "open-minded"
]

LOW_RELIGION = [
    "irreligion", "profane", "irreligious", "secular", "atheist", "nonbeliever", 
    "skeptic", "skeptical", "agnostic"
]


HIGH_RELIGION = [
    "religion", "religious", "christian", "muslim", "jew", "jewish", "hindu", 
    "believer", "belief", "christianity", "church", "god", "god-fearing"
]

HIGH_STATUS = [
    "status", "wealthy", "rich", "powerful", "power", "wealth", "superior", 
    "prestigious", "prestige", "influential", "successful", "important", 
    "resourceful", "eminent", "respected"
]

LOW_STATUS = [
    "poor", "powerless", "poverty", "inferior", "uninfluential", "unsuccessful", 
    "insignificant", "low", "disreputable"
]

WARMTH_TUPLE = (WARMTH,COLD,"Warmth")
COMPETENCE_TUPLE = (COMPETENCE,INCOMPETENCE,"Comptence")
MORALITY_TUPLE = (HIGH_MORALITY,LOW_MORALITY,"Morality")
AGENCY_TUPLE = (HIGH_AGENCY,LOW_AGENCY,"Agency")
POLITIC_TUPLE = (HIGH_POLITICS,LOW_POLITICS,"Politics")
RELIGION_TUPLE = (HIGH_RELIGION,LOW_RELIGION,"Religion")
STATUS_TUPLE = (HIGH_STATUS,LOW_STATUS,"Status")

DIMENSION_TUPLE_LIST = [WARMTH_TUPLE,COMPETENCE_TUPLE,MORALITY_TUPLE,AGENCY_TUPLE,POLITIC_TUPLE,RELIGION_TUPLE,STATUS_TUPLE]





