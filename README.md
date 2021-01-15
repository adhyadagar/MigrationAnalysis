# MigrationAnalysis
This work was done as a part of my internship project under Dr. Aaditeshwar Seth, IIT Delhi.

## Contents include - 

1. Census Data about Migration at district and state levels.
2. Computed labels from the census data (1/2/3) for various migration indicators.
3. Correlation plots between migration indicators and other socioeconomic indicators(ADI, type of industry, type of growth)
4. Hypotheses and their proofs. (at district level)
5. Migration maps - I. Maps for individual indicators II. Top 5 inbound migrations districts: source--> destination
6. Complete migration deck - I. PPT II. Document 
7. Resources for reference 

## Introduction

One important facet of study on population is the study of migration arising out of various social, economic or political reasons. For a large country like India, the study of movement of population in different parts of the country helps in understanding the dynamics of the society better. At this junction in the economic development, in the country, especially when many states are undergoing faster economic development, particularly in areas, such as, manufacturing, information technology or service sectors, data migration profile of population has become more important.

According to the Indian census, when a person is enumerated in census at a different place than his / her place of birth, she / he is considered a migrant. This may be due to marriage, which is the most common reason for migration among females-or for work, what is the case as generally among males, etc. It also happens that many return to their place of birth after staying out. To capture such movements of population census collect information on migration by last helps to understand the current migration scenario better.
    
Migration is often driven by the search for better livelihoods and new opportunities. Indeed, global and regional social and economic inequalities are expressed most powerfully through the figure of the migrant, as one who crosses borders in search of work, education and new horizons. Hence it is important to study this phenomenon as it can serve as an proxy to study socioeconomic development of an area.
    
    
This study is a continuation to the research done by Goswami et al.and uses the results given in the paper.
    
__In this paper, the intent has been to complete the following tasks:__ 
        - To download data from web to create a comprehensive table of variables based on Census 2001 & Census 2011 for analysis.
        - To discretize the continuous variables by using clustering algorithms with an aim to keep the labels consistent over the two Census and to enable a simple                  comparison of the migration states over the years.
        - To study the pattern of Census 2011 and finally use statistical analysis to formulate hypothesis based on observed patterns and test them using statistical tests.
        - To study association between migration and socioeconomic development in Indian districts
        - To seek answers to questions like:
            – Does migration lead to social development or vice versa?
            – Do men and women migrate in a similar way?
            – What are the prominent migration hubs in India and what causes this?
           
## Methodology 

### Discretization of Migration Variables

It's always difficult to interpret the overall change in socioeconomic conditions specially when each socioeconomic parameter has multiple variables representing it. Here we present a novel idea of discretization which is useful for several reasons. First, as shown in the book Factfulness by Hans Rosling who used a similar 4-level mapping for different stages of development of countries and regions, such a coarse mapping is easy for people to interpret and to easily compare different districts with one another. Second, it reduces the variables to a single quantity without assigning arbitrary weights to club together multiple parameters for each variable. 

Folling this argument, continuous values in the D-table of the census have been normalised based on the enumerated population and total number of migrants wherever necessary.

These values are then taken to make mutually exclusive clusters which help us identify a district based on the level of indicator – level 1/level 2/level3. K means clustering has been chosen to perform this task and the value of k has been decided carefully after looking at elbow and shadow plots for various number of clusters. Clusters and their respective plots have been shown in the next section.

### Hypothesis Testing
Around seven migration indicators derived from the census tale, we construct eight hypotheses and test these hypotheses. These hypotheses mainly revolve around the differences noticed between how, where, which and why people migrate. These emperical insights can help us identify migration clusters in India which can aid the government to drive targeted development backed by what trends predict.

## Results - Hypotheses

### 1. Hypothesis 1: Districts with better socioeconomic indicators (like Assets, MSL, CHH, LIT) have higher incidence of inbound migrants. Equivalently, districts with higher ADI values have higher incidence of inbound migrants.Alternatively, migrants tend to migrate more towards districts with higher ADI values.
    
### 2. Hypothesis 2: Districts with better socioeconomic indicators (like Assets, MSL, CHH, LIT) have higher incidence of literate migrants. Equivalently, districts with higher ADI values have higher incidence of inbound migrants.Alternatively, literate migrants tend to migrate more towards districts with higher ADI values.

### 3. Hypothesis 3: Districts with high ADI values see high inbounds of male migrants and districts with low ADI values see higher inbounds of female migrants.Alternatively, male migrants tend to migrate more towards districts with higher ADI values, while female migrants move to districts with lower ADI values.
   
### 4. Hypothesis 4: Districts with manufacturing and service industries see high inbounds of male migrants, while the districts with low and moderate industries see higher inbounds of female migrants.Districts with manufacturing and service industries see high inbounds of male migrants, while the districts with low and moderate industries see higher inbounds of female migrants.

### 5. Hypothesis 5: Districts with manufacturing and service industries see high inbound migration, while the districts with low and moderate industries see lower inbounds of migration.Converse is not true.

### Hypothesis 6: Migrants who travel for professional reasons travel to districts with service industries.
 
### Hypothesis 7: Inter state migrants tend to migrate more towards districts with manufacturing and service industry opportunities.}
  
### Hypothesis 8: Long term migrants migrate to districts with low level industries in contrast to short term migrants, who move to districts with service industries.





            
            

