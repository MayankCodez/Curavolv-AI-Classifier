# Curavolv AI Internship Phase 1 Assessment

## 1. Overview

This project implements a rule based classification system that evaluates candidate profiles and recommends the top 3 healthcare career tracks and the most suitable graduate degree.

The system processes structured candidate data and generates interpretable outputs using academic background, statement of purpose and experience.

## 2. Approach

The solution follows a multi signal weighted scoring system.

### 2.1 Subject to Cluster Mapping

Candidate subjects are mapped into predefined academic clusters C1 to C10 such as Life Sciences, Social and Behavioral Sciences, Information Technology and Policy and Law.

Each cluster contributes weighted signals toward relevant degrees.

### 2.2 Degree Scoring

Two signals are combined.

1. Cluster based scoring derived from academic background  
2. SOP based scoring derived from intent and goals  

The final degree score is the sum of cluster score and SOP score. The degree with the highest score is selected.

### 2.3 Track Scoring

Each career track is evaluated using:

1. Keyword matching from the SOP  
2. Degree alignment weights  
3. A light experience based signal  

The top 3 tracks are selected based on final scores.

### 2.4 Rationale Generation

The system generates human readable explanations using keyword grouping such as leadership, policy and data.

It uses structured phrasing like Strong alignment with and Moderate alignment based on overall profile signals to ensure outputs are interpretable and easy to review.

## 3. Output Format

The final output is a structured JSON containing top tracks, recommended degree and rationale.

Each rationale entry includes the track and the reasoning behind its selection.

## 4. Test Cases

The system was evaluated on 6 candidate profiles provided in the assessment.

### 4.1 Results Summary

Clinical to Administrative transition results in MHA with T01  
Community Health results in MPH with T05  
Finance results in MBA HC with T03  
Health Technology results in MSHI with T09  
Nursing long term care results in MHA with T01  
Policy results in MPH with T07  

## 5. Design Decisions

### 5.1 Rule Based Approach

A rule based system was chosen to ensure interpretability, ease of debugging and alignment with structured problem constraints.

### 5.2 Strengths Handling

Although strengths are included in the input schema they are not used in scoring because they are subjective and lack consistent mapping to career tracks.

Including them could introduce noise instead of meaningful signal.

### 5.3 Experience Usage

Experience is incorporated as a light contextual signal to refine track scoring without overpowering academic and intent based signals.

## 6. Project Structure

Curavolv/

- main.py  
- mapping.py  
- scoring.py  
- trackmapping.py  
- trackscoring.py  
- output.json  
- README.md  

## 7. How to Run

Run the following command in the project directory:

python main.py

This will generate an output.json file containing results for all candidates.

## 8. Future Improvements

1. Introduce NLP based semantic matching instead of keyword matching  
2. Incorporate strengths as soft signals for tie breaking  
3. Train a machine learning model for adaptive weighting  
4. Improve reasoning generation for more natural explanations  

## 9. Conclusion

This solution combines structured logic, weighted scoring and explainable outputs to deliver a robust and interpretable classification system aligned with Curavolv’s CARA pipeline objectives.
