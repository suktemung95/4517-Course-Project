from math import sqrt

def parse_signature(signature: str):
    return [float(x) for x in signature.split(",") if x]

def compare_image_similarity(a, b):
    vec_a = parse_signature(a)
    vec_b = parse_signature(b)

    dot = sum(x*y for x,y in zip(vec_a, vec_b))
    norm_a = sqrt(sum(x*x for x in vec_a))
    norm_b = sqrt(sum(x*x for x in vec_b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)