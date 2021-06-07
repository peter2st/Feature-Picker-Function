def feature_picker(model, features, threshold):
    scores = model.coef_
    abs_scores = abs(scores)
    new_scores = []
    new_features = []
    feat_names = []
    final_list = {}
    
    for col in features.columns:
        feat_names.append(col)
    
    for lst in abs_scores:
        res = [x for x in range(len(lst)) if lst[x] >= threshold] 
    for index in res:
        for i in scores:
            new_scores.append(i[index])
            new_features.append(feat_names[index])
            
    final_list = dict(zip(new_features, new_scores))
    return final_list