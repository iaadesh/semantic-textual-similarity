# Semantic Textual Similarity

## Part-A: Building Semantic Textual Similarity Model 

First I did some Data Analysis and some research about Semantic Textual Models.

For building a Semantic Textual Similarity model, we will first convert both the sentences into Vectors representation and we will be calculating Cosine Similarity between those two vectors to find the Semantic Similarity.

Then to convert Sentence into Vectors, I did research on Sentence Embeddings to find the best Sentence Embedding Model available.

So “all-mpnet-base-v2” is the best available open source Sentence Embedding Model, and I decided to use it as it gives the best results.

I then used the Sklearn library for calculating the Cosine Similarity.



## Part-B: Deploying the Semantic Textual Similarity Model    using Docker on GCP

Deployed the Semantic Textual Similarity Model web application using Flask Web Framework.

Then used Docker to containerize the Web application and its dependencies.

Then created a Docker Image which can be used to deploy applications consistently across various environments and infrastructure platforms.

Decided to use GCP for the cloud deployment, then first pushed the Docker Image to GCP’s Artifact Registry and then ran the pushed Docker Image on GCP’s Cloud Run.
