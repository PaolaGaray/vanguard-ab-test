**Project Title: Vanguard - AB test**
    by Tania Zakowski and Paola Garay

# Project overview

This project evaluates the impact of a new, modern User Interface (UI) and in-context prompts on a multi-step process for Vanguard, a financial services company. The goal was to determine whether the changes would increase user completion rates and reduce abandonment, improving the client experience during an online process. The project analyzes client behaviour, session durations, demographic trends, and client tenure to gain actionable insights.

# Questions / Hypotheses

1) Primary Question: Does the new UI and in-context prompts increase the number of users who complete the process?

2) Hypothesis: Users with the new UI and prompts will be more likely to complete the process compared to the control group with the old UI.

3) Additional Questions:
   - How does user age affect the likelihood of completing the process?
   - How does client tenure influence completion or abandonment rates?
   - What are the key points in the process where users tend to drop off?
   - Does session duration correlate with process completion or abandonment?

# Dataset 

The datasets include user behaviour data from an A/B test, split into a control group (old UI) and a test group (new UI). Key features include:
- Client age: Age of the user at the time of the process.
- Client tenure: How long the user has been a customer of the company.
- Session duration: Time spent by users during the process.
- Step completion status: Whether a user completed each of the process steps.
- Completion/Abandonment status: Whether the user finished or dropped out of the process.

## Main Dataset Issues
- Missing Data: Some fields, particularly user age and tenure, were incomplete or missing for certain users.
- Skewed Distribution: The tenure distribution is left-skewed with three distinct peaks, making standard data transformations inefficient (the mode is 6 years).
- Imbalanced Outcomes: A relatively high proportion of users completed the process, but drop-offs were concentrated in specific demographics (older users, long-tenured clients).

# Conclussions
1) The new UI and in-context prompts improved completion rates for most users, especially those with shorter client tenures (0-5 years) and middle-aged users (30-60 years).
2) Session duration was significantly longer for users who abandoned the process, particularly in the test group, indicating potential confusion or difficulty with the new UI.
3) Younger users (under 30) and older users (over 60) were more likely to abandon the process, suggesting the need for age-specific design improvements.
4) Long-term clients (10+ years) struggled with the new UI, possibly due to discomfort with newer digital interfaces, leading to higher abandonment rates.
5) Recommendations include refining the UI for different demographics, simplifying the experience for long-tenured clients, and providing real-time support for users who struggle with the process.
