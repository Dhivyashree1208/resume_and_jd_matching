## Assignment 2: AI Screening Service

The resume–job description matching logic developed in Assignment 1 was
exposed as a REST API using FastAPI. The service accepts resume text and
job description text as input and returns a structured screening response,
simulating an early-stage Applicant Tracking System (ATS).

### Decision Logic
Screening decisions are derived directly from the match score:
- Shortlist: score ≥ 60
- Hold: score ≥ 35
- Reject: score < 35

This conservative thresholding reflects real-world hiring pipelines and
helps avoid false positives.

### Edge Case Handling
- Very short or empty resumes are automatically rejected
- Conservative scoring prevents unreliable shortlisting

### System Integration
This service can act as an early screening layer in a recruitment or ATS
pipeline, where resumes are filtered before being reviewed by recruiters
or hiring managers.

### Scalability Considerations
- Stateless FastAPI service
- Can be horizontally scaled behind a load balancer
- Scoring logic can be cached for repeated job description evaluations
- Can be integrated with resume parsers and candidate databases
