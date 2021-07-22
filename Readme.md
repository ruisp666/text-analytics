## A not so painful introduction to applied NLP with earnings call transcripts
The human effort required to analyze individual call transcripts from publicly traded companies is significant. This is mainly
due to two factors: The size of those transcripts, and the complexity of the information they contain.
The size stems from the usual format of the call transcript, which often includes length interventions from the executives 
and detailed answers to the questions from professional analysts. The complexity of the information is usually a consequence of the highly 
specialized nature of the comments produced by the participants.

This repo gather some of my attempts a reducing the human effort in extracting meaningful information from call
transcripts. It is not meant as a recipe to full automation or generation of trading ideas.

Finally, to set expectations, a few assumptions are relevant:

1. We assume that a source of raw text is in place and do not consider for now web-scraping of textual information.
2. The main objective of this repo resides in the application of NLP techniques to a specific use case and not
   on their theoretical fundamentals. Thus, there is no pre-set degree of depth for the techniques considered, i.e.,
   depending on its relevance for a given task, I may or may not get deeper into a particular topic.
3. We divide an NLP pipeline into the following stages: Text processing, feature extraction, modelling. Each step has 
   at least one notebook related to it.
4. This repo is still in its early stages, so expect changes.