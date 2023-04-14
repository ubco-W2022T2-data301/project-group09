# Final Report (Group 09)

## Introduction 
Our Group Project aims to explore the issue of Gun Deaths in America , which has become a significant concern in the United States in the recent years. We will be focusing on specific aspects of gun violence, including the age of the victim, intent, race, place of incident and education level of the victim involved in the incident. By analyzing these variables, we hope to identify trends and patterns that may reveal insights into the demographics circumstances surrounding gun violence in America. To conduct our analysis, we have used a dataset sourced from the FiveThirtyEight's Gun Deaths in America Project, which contains detailed records of around 100,000 gun-related incidents that occurred in the US between 2012 and 2014. Our ultimate goal is to contribute a better understanding of Gun deaths and gun safety so as to prevent such incidents from occurring in the future, and to help facilitate change in the appopriate legislation so that the issue of gun-deaths decrease over time in the country. 


## Exploratory Data Analysis
- Below is a Heatmap that shows the correlation between the numeric columns particularly age, police involved, month anf year, and taking a look at them.

![EDA_1](images//EDA(1).png)

- Below is a violin plot that shows us how education, race and intent are related to gun deaths and if any trends are visible to us.  

![EDA_2](images//EDA(2).png)

- Below is a violin plot that shows us how the number of gun-related suicides differ in terms of sex and race.

![EDA_3](screenshots/graph.png)
## RESEARCH QUESTION 1:
*How does Educational attainment relate to gun deaths in America and what other factors affect this relationship ?*

The following are a few sub questions that helped me achieve my objectives:
- Is there a correlation between educational attainment and gun deaths rates in the United States after controlling for other demographic and contextual factors, such as age, gender, race, religion and gun ownership rates ? This could be done using regression analysis to examine the contribution of education while keeping the other factors constant.
- To what extent does the knowledge of gun safety or ownership meditate the relationship between gun deaths and education ? This could be monitored by using the "intent" column of the dataset.
- Are there differences in the relationship between education and gun deaths across different age groups, race, or geographical regions? We could explore whether the protective effects of education are stronger for younger or elder individuals for certain racial groups.

If you are interested in looking at the entire analysis , you can click [here](https://github.com/ubco-W2022T2-data301/project-group09/blob/main/analysis/analysis1.ipynb)

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


## RESEARCH QUESTION 2:
**To what extent are the gun violence incidents classified as homicides affected by demographic factors ?**

For full analysis, click [here](https://github.com/ubco-W2022T2-data301/project-group09/blob/main/analysis/analysis2.ipynb)

Sub questions:
1. What relation do gun violence incidents that are classified as homicides (we can see this in the 'intent' column) have with demographic factors (specifically age, race and sex)? This sub-question will have 3 parts and will be explored while keeping other factors such as education and location constant. The three parts will be:
    - What relation do gun violence incidents that are classified as homicides (we can see this in the 'intent' column) have with the age of the perpetrator?
    - What relation do gun violence incidents that are classified as homicides have with the race of the perpetrator?
    - What relation do gun violence incidents that are classified as homicides have with the sex of the perpetrator?
    


2. How is the relation between homicides and demographics affected by differing education? For this sub question, we will be using the 'education column' to look into how the initially explored relation between homicides and demographics can vary with the education of the perpetrator. Will a less educated individual be more likely to be involved in a homicide? 

![Figure1](images//RQ2_img1.png)


From the above graphs, we can see the various trends that directly answer our first sub-question. 
1. We can see a distinct pattern from the leftmost plot above, the highest number of homicides are being perpetrated by those between the ages of 20 and 40. 
2. From the plot in the middle, we can see that the highest number of homicides are perpetrated by the Black race, and 'White' is following up in second. 
3. From the plot on the right we can see that gun violence incidents classified as homicides occur significantly more when a male is involved, when compared to a female. 

Next we went into slighlty more complex visualisations to factor in Education for our second sub question. 

![Figure 2](images//RQ2_img2.png)


From this graph we can see even though, overall the black race had the highest number of homicides, when education is brought into the frame the numbers change drastically. When a person has education of HS/GED or college education, white people are generally more involved in homicides. However when observing more carefully, the black race has a higher density of homicides around the ages of 20, when compared to any other race.
Nonetheless, this shows that on average or in general the black race will not be as involved once education is taken into consideration, and education definitely influences the likelihood of being involved in homicides.


![Figure 2](images//RQ2_img3.png)

Through this second graph we can see that when education is put into consideration, the male sex can in general be involved more in homicides if they are in the education categories -"HS/GED", "Less than HS" or "Some College". However, it does seem much closer in the categories of 'Less than high school' and 'Some college', hinting towards the fact that a lower level of education will directly corelate with a higher number of homicides(especially in the age range of 20-40)

## Research Question 3:
**How do the number of gun-related suicides commited in the US differ when talking about demographic variebles like age, sex, race, and type of location?**

For a full analysis click [here](https://github.com/ubco-W2022T2-data301/project-group09/blob/main/analysis/analysis3.ipynb)

Sub problems:

- How does the suicide rate vary with different age groups (For eg. rate for people 13-19, 20-40, and 40 above)?

We graph the number of suicides against the age of the victims and get the following graph:

![ageplot](screenshots/ageplot3.png)

From the graph, we see that:

The age group 50 - 60 had the most incidents of gun-related suicides
Teens (< 20 years) were involved in surprisingly little gun-related suicide incidents as compared to people in older age groups
It is also important to note that even though there may seem like a decline in the number of suicides between the ages 25-35, this is not that significant of a decline since there is only a difference of less than 500 cases over the span of two years (2012 - 2014).

Next we move on to:
- Is there a significant difference between the number of Black and Hispanic teenagers and young adults that commit gun-related suicide and the number of White people belonging to the same age group?

We achieve this by isolating victime that belong to White, Black, or Hispanic communities and looking at the distribution in terms of age. We get the following graph:

![](screenshots/3races.png)

We see that there is quite a big disparity between gun-related suicides among White young adults vs Black and Hispanic young adults.

We also see that this plot is limited in terme of age i.e. it only looks at record upto age 30. What if we look beyond age 30?

![](screenshots/allraces.png)

We now see that the peak for the data for white victims is at around 50 yrs, while the peak for Black and Hispanic victime is **much younger**, being around 20 yrs.

Next we move to the question:

- Is there a correlation betwen a person's age and the type of location that they commit suicide?

We achieve the following plot by plotting the distribution in terms of age, and spitting it into multiple graphs for each of the different location variables. On overlaying the split graphs, we get:

![](screenshots/place.png)

We see that generally more street suicides involve younger victims, while suicides in places of work (Farms, Industrial areas) involve older victims.

Another interesting thing that the plot tells us is that a majority of victims aged above 70 commit a gun-related suicide in residential institutions.

Finally, let's consider the role of education and how it affects our data.

- Is there a correlation between educational status and suicide rate? Does this correlation change when we factor in race?

Now, it is important to note that a huge majority of cases in this databases involve white victims, which can sometimes make it harder to look at data involving victims of minroty groups. Therefore, it seems best to look past white victims in order to find hidden trends in our data.

We thus get the graph:

![](screenshots/education.png)

We note that:
- The second largest majority of suicide victims in our dataset are Black.
- A majority of gun-related suicide victims are High School graduates.
- In the Asian community, more college graduates than high school graduates commit gun-related suicide, which is not the case for any other racial group.





## Conclusion 
 Individuals with greater education have a longer life expectancy (>45 years) than those with less education, such as a high school diploma or a college degree. Suicide rates are highest among high school graduates and it is one of the leading causes of mortality for persons of all educational levels. Individuals with a greater level of education , often a BA+ or some college, have a better understanding of gun safety, which reduces the chance of homicides and undetermined deaths. We discovered that higher educational attainment is related with reduced gun death rates when we used regression analysis to investigate the effect of education while controlling for other characteristics. The association coefficient (-0.380) implies that as educational attainment rises, so does the rate of gun deaths. Furthermore, gun ownership rates, age , gender, race, religion and race were found to be significant predictors of gun deaths in the United States. After reviewing the intent column, we discovered that the majority of gun deaths in the dataset (62.7 %) were caused by suicide, followed by homicide (34.7%). The remaining deaths were either unintentional (2.2%) or accidental (0.4%). According to the findings, the association between educational attainment and gun deaths is mostly driven by education's protective impact on suicide deaths. According to our findings, the protective effects of education are larger for older people (those over the age of 65) than for younger people (below 25 years). 
 We also concluded that there is a huge disparity between the trends of gun-related suicide between different racial groups, especially between White and Black/Hispanic victims. There is also a disparity when considering educational backgrounds. We found that there was no change in the average number of gun-related suicides during the time period when the data was collected (2012-2014).
 
 Overall our analysis suggests that higher educational attainment is associated with lower gun death rates and lower homicides in the United States after controlling the demographic factors. 

 
