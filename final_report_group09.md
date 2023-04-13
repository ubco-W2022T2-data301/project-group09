# Final Report (Group 09)

## Introduction 
Our Group Project aims to explore the issue of Gun Deaths in America , which has become a significant concern in the United States in the recent years. We will be focusing on specific aspects of gun violence, including the age of the victim, intent, race, place of incident and education level of the victim involved in the incident. By analyzing these variables, we hope to identify trends and patterns that may reveal insights into the demographics circumstances surrounding gun violence in America. To conduct our analysis, we have used a dataset sourced from the FiveThirtyEight's Gun Deaths in America Project, which contains detailed records of around 100,000 gun-related incidents that occurred in the US between 2012 and 2014. Our ultimate goal is to contribute a better understanding of Gun deaths and gun safety so as to prevent such incidents from occurring in the future. 


## Exploratory Data Analysis
- Below is a Heatmap that shows the correlation between the numeric columns particularly age, police involved, month anf year, and taking a look at them.

![EDA_1](images//EDA(1).png)

- Below is a violin plot that shows us how education, race and intent are related to gun deaths and if any trends are visible to us.  

![EDA_2](images//EDA(2).png)

## RESEARCH QUESTION 1:
*How does Educational attainment relate to gun deaths in America and what other factors affect this relationship ?*

The following are a few sub questions that helped me achieve my objectives:
- Is there a correlation between educational attainment and gun deaths rates in the United States after controlling for other demographic and contextual factors, such as age, gender, race, religion and gun ownership rates ? This could be done using regression analysis to examine the contribution of education while keeping the other factors constant.
- To what extent does the knowledge of gun safety or ownership meditate the relationship between gun deaths and education ? This could be monitored by using the "intent" column of the dataset.
- Are there differences in the relationship between education and gun deaths across different age groups, race, or geographical regions? We could explore whether the protective effects of education are stronger for younger or elder individuals for certain racial groups.

![Figure1](images//RQ1_img1.png)
Figure 1: Education v/s Intent graph for Gun Deaths in America

- In the above graph we have decreased the number of record taken into account to clearly see how high the rate of suicide and homicide is as compared Accidental or Undetermined deaths.
- We can also notice that people with education of BA+ have really low rates of deaths irrespective of the intent whereas people with Some college , HS or less than HS education have comparatively higher rates of deaths.
- In each intent type, people HS education have highest rates of deaths and then some college , less than HS and then BA+ respectively. But Homicide has a different trend where less than HS education people have second highest rates of deaths compared to the others.

![Figure2](images//RQ1_img2.png)
Figure 2: Age v/s Education graph based on different intents of Gun Deaths

The above graph suggests that there is a correlation between education level and age with the likelihood of experiencing premature death by suicide or homicide. Individuals with a higher education level have a lower chance of dying at an early age compared to those with a high school education or lower. People with any education level are more likely to commit suicide at an older age, and homicides are more likely to involve younger individuals, particularly those with a less school education.


![Figure3](images//RQ1_img3.png)
Figure 3: Age v/s Place of Death Heatmap 

The age group of 20-80 years old have the highest probability of dying i their homes as compared to any other places.We can also see that the younger population (specifically in the age groups of 20-40 years) also have records of death on the streets and some other unspecified locations which shows how unsafe it is for them outside.



**Summary/Conclusion**: A brief paragraph that highlights your key results and what you learned from doing this project.