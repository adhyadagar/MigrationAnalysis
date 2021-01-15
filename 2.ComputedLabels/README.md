## Analysis done at District level

## Methodology

It's always difficult to interpret the overall change in socioeconomic conditions specially when each socioeconomic parameter has multiple variables representing it. Here we present a novel idea of discretization which is useful for several reasons. First, as shown in the book Factfulness by Hans Rosling who used a similar 4-level mapping for different stages of development of countries and regions, such a coarse mapping is easy for people to interpret and to easily compare different districts with one another. Second, it reduces the variables to a single quantity without assigning arbitrary weights to club together multiple parameters for each variable. 

Following this argument, continuous values in the D-table of the census have been normalised based on the enumerated population and total number of migrants wherever necessary.


These values are then taken to make mutually exclusive clusters which help us identify a district based on the level of indicator – level 1/level 2/level3. K means clustering has been chosen to perform this task and the value of k has been decided carefully after looking at elbow and shadow plots for various number of clusters.
