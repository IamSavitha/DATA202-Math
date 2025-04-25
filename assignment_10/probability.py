def posterior_probability(prior, sensitivity, specificity):
    return (sensitivity * prior) / ((sensitivity * prior) + ((1 - specificity) * (1 - prior)))