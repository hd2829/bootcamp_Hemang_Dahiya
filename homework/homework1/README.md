# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Online educational platforms struggle with high dropout rates, as many students disengage and exit courses before completion. This lowers learning outcomes, damages the platform’s reputation, and negatively impacts revenue. Current efforts to boost engagement are mostly reactive rather than proactive, lacking data-driven insights into when, why, and which students are likely to drop out.

## Stakeholder & User
**Primary Stakeholder:** Platform administrators and course designers decide on investments in engagement tools and curriculum changes.  
**End Users:** Course instructors, who can act on predictions to support at-risk students, and students themselves, who may benefit from personalized interventions. Alerts and actionable insights must fit instructors’ workflows so they can intervene in time—ideally within their regular course management activities.

## Useful Answer & Decision
**Type:** Predictive—identifying students at risk of dropping out in the coming two weeks.  
**Decision Informed:** Determining which students should be targeted for outreach (e.g., mentoring, reminders) and which course materials may need redesign.  
**Deliverable:** Dashboard and alert system for instructors notifying them of at-risk students, with supporting details and a list of suggested interventions.

## Assumptions & Constraints
- Reliable, timely data is available on student activities (e.g., logins, assignment submissions, forum interaction).
- Instructors and/or support staff are able to intervene (e.g., send emails, arrange check-ins) promptly.
- Platform allows integration of the alert/dashboard system with instructor workflows.
- Compliance with student data privacy policies and regulations is maintained.

## Known Unknowns / Risks
- Data privacy requirements may restrict availability or granularity of student-level data.
- Out-of-platform factors (work, health, family) affecting dropout risk may not be captured.
- The actual effectiveness of interventions based on predictions is uncertain and should be monitored.

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Reduce student dropout → Problem Framing & Scoping (Stage 01) → Project framing and requirements  
- Identify at-risk students → Data Exploration & Modeling → Predictive model, dashboard  
- Enable timely response → Deployment & Integration → Alert system for instructors  
- Monitor effectiveness → Evaluation & Monitoring → Intervention & retention reports

## Repo Plan
/data/ — student activity and engagement data  
/src/ — processing and modeling scripts  
/notebooks/ — EDA, prototyping, and reports  
/docs/ — stakeholder memos, slides  
README will be updated as the project advances. Repo link and updates shared with collaborators and instructors.

