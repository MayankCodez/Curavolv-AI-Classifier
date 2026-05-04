#Mapping of Subjects to cluster IDs(C1-C10)
subject_to_cluster={
    "biology":"C1",
    "anatomy":"C1",
    "physiology":"C1",
    "biochemistry":"C1",
    "microbiology":"C1",
    "genetics":"C1",

    "physics":"C2",
    "chemistry":"C2",
    "environmental chemistry":"C2",
    "earth science":"C2",

    "statistics":"C3",
    "biostatistics":"C3",
    "calculus":"C3",
    "data science":"C3",
    "econometrics":"C3",

    "sociology":"C4",
    "psychology":"C4",
    "anthropology":"C4",
    "social":"C4",
    "community development":"C4",

    "accounting":"C5",
    "finance":"C5",
    "economics":"C5",
    "marketing":"C5",
    "management":"C5",
    "hr":"C5",
    "entrepreneurship":"C5",

    "public health":"C6",
    "epidemiology":"C6",
    "clinical medicine":"C6",
    "health policy":"C6",
    "pharmacology":"C6",
    "global health":"C6",
    "pathology": "C6",
    "oral medicine": "C6",
    "dental surgery": "C6",
    "community medicine": "C6",

    "computer science":"C7",
    "python":"C7",
    "sql":"C7",
    "database mgmt":"C7",
    "database management": "C7",
    "cybersecurity":"C7",
    "cloud":"C7",
    "cloud computing": "C7",
    "software engineering":"C7",

    "public policy":"C8",
    "political science":"C8",
    "law":"C8",
    "constitutional law":"C8",
    "regulatory":"C8",
    "ethics":"C8",

    "english":"C9",
    "writing":"C9",
    "journalism":"C9",
    "history":"C9",
    "philosphy":"C9",
    "public speaking":"C9",

    "engineering":"C10",
    "biomedical engineering":"C10",
    "quality management":"C10",
    "six sigma":"C10"

}       

cluster_degree_weights={
    "C1":{"MPH":2,"MSHI":1},
    "C2":{"MPH":2},
    "C3":{"MPH":2,"MSHI":2,"MBA-HC":1},
    "C4":{"MPH":2,"MHA":1},
    "C5": {"MBA-HC": 2, "MHA": 1},
    "C6": {"MHA": 3, "MPH": 2, "MSHI": 1},
    "C7": {"MSHI": 2, "MBA-HC": 1},
    "C8":{"MPH":2,"MHA":1},
    "C9":{"MHA":1,"MPH":1},
    "C10":{"MSHI":2,"MHA":1}
}


sop_degree_keywords = {
    "leadership": {"MHA": 4},
    "administration": {"MHA": 4},
    "management": {"MHA": 3},
    "quality": {"MHA": 2},
    "facility":{"MHA":2},
    "care":{"MHA":2},

    "community": {"MPH": 3},
    "equity":{"MPH":3},
    "social":{"MPH":2},
    "public":{"MPH":3},
    "policy": {"MPH": 2},
    "epidemiology": {"MPH": 2},

    "data": {"MSHI": 2},
    "ehr": {"MSHI": 2},
    "informatics": {"MSHI": 2},

    "finance": {"MBA-HC": 4},
    "revenue":{"MBA-HC":4},
    "accounting":{"MBA-HC":3},
    "capital":{"MBA-HC":3},
    "strategy": {"MBA-HC": 2}
}


