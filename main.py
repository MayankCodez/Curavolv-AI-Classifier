import json
from scoring import(
    calculate_degree_scores,
    calculate_sop_scores,
    combine_scores,
    get_best_degree
)

from trackscoring import(
    calculate_track_scores,
    get_top_tracks,
    generate_rationale
)

from mapping import(
    subject_to_cluster
)

def get_clusters(subjects):
    clusters=[]
    for sub in subjects:
        sub=sub.lower()
        for key in subject_to_cluster:
            if key in sub:
                clusters.append(subject_to_cluster[key])
                break
    return list(set(clusters))

def run_pipeline(candidate):
    subjects=candidate.get("subjects",[])
    sop=candidate.get("sop", "")

    clusters=get_clusters(subjects)

    cluster_scores=calculate_degree_scores(clusters)
    sop_scores=calculate_sop_scores(sop)
    final_degree_scores=combine_scores(cluster_scores, sop_scores)

    best_degree=get_best_degree(final_degree_scores)

    track_scores=calculate_track_scores(sop, best_degree, candidate.get("experience"))

    top_tracks=get_top_tracks(track_scores)

    rationale=generate_rationale(top_tracks, sop, best_degree)

    return{
        "top_tracks":top_tracks,
        "recommended_degree":best_degree,
        "rationale":rationale
    }   

candidate0 = {
    "subjects": [
        "anatomy",
        "physiology",
        "biochemistry",
        "pathology",
        "pharmacology",
        "community medicine",
        "oral medicine",
        "dental surgery"
    ],
    "sop": "wants to transition from clinical to administrative leadership and is interested in organizational leadership and quality improvement at a large healthcare organization",
    "experience": {
        "years": 0,
        "type": "clinical"
    },
    "strengths": [
        "judgment",
        "leadership",
        "perspective",
        "honesty",
        "social intelligence"
    ]
}         

candidate1 = {
    "subjects": [
        "sociology",
        "community development",
        "social research methods",
        "health and society",
        "cultural anthropology",
        "gender studies"
    ],
    "sop": "wants to design community health programs addressing social determinants and aims to lead health equity programs at a state health department",
    "experience": {
        "years": 1,
        "type": "community"
    },
    "strengths": [
        "kindness",
        "social intelligence",
        "teamwork",
        "fairness",
        "perspective"
    ]
}

candidate2 = {
    "subjects": [
        "financial accounting",
        "corporate finance",
        "cost accounting",
        "business law",
        "economics",
        "taxation",
        "auditing"
    ],
    "sop": "wants to move into healthcare cfo track and is interested in revenue cycle optimization, payer contracting and capital allocation",
    "experience": {
        "years": 3,
        "type": "finance"
    },
    "strengths": [
        "judgment",
        "prudence",
        "honesty",
        "perseverance",
        "self regulation"
    ]
}

candidate3 = {
    "subjects": [
        "data structures",
        "algorithms",
        "database systems",
        "python",
        "java",
        "machine learning",
        "cloud computing"
    ],
    "sop": "wants to bridge clinical workflows with technology and is interested in ehr optimization, fhir interoperability and clinical decision support with a goal to become director of health informatics",
    "experience": {
        "years": 2,
        "type": "technical"
    },
    "strengths": [
        "curiosity",
        "judgment",
        "love of learning",
        "creativity",
        "perseverance"
    ]
}

candidate4 = {
    "subjects": [
        "anatomy",
        "physiology",
        "geriatric nursing",
        "community health nursing",
        "mental health nursing",
        "pharmacology",
        "nursing administration"
    ],
    "sop": "wants to move into managing long term care facilities and is interested in memory care program design and quality improvement for aging populations",
    "experience": {
        "years": 4,
        "type": "clinical"
    },
    "strengths": [
        "kindness",
        "perspective",
        "leadership",
        "teamwork",
        "gratitude"
    ]
}

candidate5 = {
    "subjects": [
        "indian politics",
        "public policy",
        "constitutional law",
        "international relations",
        "political philosophy",
        "public administration"
    ],
    "sop": "passionate about improving healthcare access through policy and wants to work in government health policy and advocacy and shape national health legislation",
    "experience": {
        "years": 0,
        "type": "policy"
    },
    "strengths": [
        "leadership",
        "perspective",
        "judgment",
        "social intelligence",
        "fairness"
    ]
}

results={
    "candidate0":run_pipeline(candidate0),
    "candidate1":run_pipeline(candidate1),
    "candidate2":run_pipeline(candidate2),
    "candidate3":run_pipeline(candidate3),
    "candidate4":run_pipeline(candidate4),
    "candidate5":run_pipeline(candidate5)
}

with open("output.json","w") as f:
    json.dump(results,f,indent=2)