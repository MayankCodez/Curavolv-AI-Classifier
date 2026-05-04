from trackmapping import track_keywords

keyword_groups = {
    "leadership": {
        "words": ["leadership", "management", "administration"],
        "phrase": "leadership and administrative intent"
    },
    "quality": {
        "words": ["quality", "improvement"],
        "phrase": "quality improvement focus"
    },
    "operations": {
        "words": ["hospital", "operations"],
        "phrase": "hospital operations interest"
    },
    "community": {
        "words": ["community", "public", "equity"],
        "phrase": "community and public health objectives"
    },
    "data": {
        "words": ["data", "informatics", "ehr", "sql"],
        "phrase": "data and informatics orientation"
    },
    "finance": {
        "words": ["finance", "revenue", "accounting"],
        "phrase": "financial and strategic focus"
    },
    "policy":{
        "words":["policy","government","legislation","advocacy"],
        "phrase":"policy and healthcare governance focus"
    }
}

def calculate_track_scores(sop_text, best_degree, experience=None):
    track_scores={}
    sop_text=sop_text.lower()

    exp_type=None

    if experience:
        exp_type=experience.get("type", "").lower()

    for track, data in track_keywords.items():
        score=0
        for keyword in data["keywords"]:
            if keyword in sop_text:
                score+=2

        if best_degree in data["degrees"]:
            score+=data["degrees"][best_degree]

        if exp_type == "clinical":
            if track in ["T01", "T04"]:
                score += 1

        elif exp_type == "technical":
            if track == "T09":
                score += 1

        elif exp_type == "finance":
            if track == "T03":
                score += 1    

        track_scores[track]=score       

    return track_scores         


def get_top_tracks(track_scores):
    sorted_tracks=sorted(track_scores, key=track_scores.get, reverse=True)
    top_3=sorted_tracks[:3]
    return top_3

def generate_rationale(top_tracks, sop_text, best_degree):
    result=[]
    sop_text=sop_text.lower()

    for track in top_tracks:
        data=track_keywords[track] 
        matched = []

        for kw in data["keywords"]:
            if kw in sop_text:
                matched.append(kw)

        parts = []

        for group in keyword_groups.values():
            if any(word in matched for word in group["words"]):
                parts.append(group["phrase"])

        parts=parts[:3]
        if parts:
            keyword_part = "Strong alignment with " + parts[0]

            if len(parts) > 1:
                keyword_part += ", supported by " + " and ".join(parts[1:])
        else:
            keyword_part = "Moderate alignment based on overall profile signals"

        if best_degree in data["degrees"]:
            degree_part=f", reinforced by {best_degree} degree fit"
        else:
            degree_part=""

        reason=f"{keyword_part}{degree_part}."

        result.append({
            "track":track,
            "reason":reason
        })    

    return result    
