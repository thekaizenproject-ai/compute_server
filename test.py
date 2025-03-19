from roles1 import career_roles  # Importing career_roles from the roles module
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.cluster import KMeans

model = SentenceTransformer('sentence-transformers/gtr-t5-large')
#model = SentenceTransformer('all-MiniLM-L6-v2')


career_embeddings = []  
for role in career_roles:
    industry_embedding = model.encode(f"{role['industry']} {role['job_family_description']}")
    career_embeddings.append({
        'id': role['id'],  # Include the 'id' in the embedding dictionary
        'name': role['name'],
        'industry': role['industry'],
        'industry_description': role['job_family_description'],
        'embedding': industry_embedding
    })

def get_similar_jobs(query, career_roles, model):
    # Generate embedding for the query
    query_embedding = model.encode(query)
    
    similarities = []
    
    for role in career_roles:
        similarity_score = cosine_similarity([query_embedding], [role['embedding']])[0][0]
        similarities.append({
            'id': role['id'],  # Include the 'id' in the similarity results
            'name': role['name'],
            'industry': role['industry'],
            'industry_description': role['industry_description'],
            'similarity': similarity_score
        })
    
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    
    for item in similarities:
        item['similarity_percentage'] = round(item['similarity'] * 100, 2)
    
    return similarities[:5]

#query = """B.tech and cyber security and i like python and programming"""

def get_query(degree,spec):
    query=f"{degree} and specilization in {spec}"
    return query 

query=get_query()

results = get_similar_jobs(career_embeddings, model)

for result in results:
    print(f"Job ID: {result['id']}")  # Print the 'id'
    #print(f"Job Name: {result['name']}")
    #print(f"Industry: {result['industry']}")
    #print(f"Industry Description: {result['industry_description']}")
    print(f"Similarity Score: {result['similarity_percentage']}%")
    print("-" * 50)
