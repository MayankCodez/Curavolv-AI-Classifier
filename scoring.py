from mapping import cluster_degree_weights, sop_degree_keywords

def calculate_degree_scores(clusters):
    degree_scores={}
    for cluster in clusters:
        mapping=cluster_degree_weights.get(cluster,{})
        for degree, weight in mapping.items():
            degree_scores[degree]=degree_scores.get(degree,0)+weight
    return degree_scores

def calculate_sop_scores(sop_text):
    sop_scores={}
    sop_text=sop_text.lower()
    
    for keyword, degree_map in sop_degree_keywords.items():
        if keyword in sop_text:
            for degree, weight in degree_map.items():
                sop_scores[degree]=sop_scores.get(degree,0)+weight
    return sop_scores

def combine_scores(degree_scores, sop_scores):
    final_scores=degree_scores.copy()
    for degree,score in sop_scores.items():
        final_scores[degree]=final_scores.get(degree,0)+score
        
    return final_scores

def get_best_degree(final_scores):
    best= max(final_scores,key=final_scores.get)
    return best
