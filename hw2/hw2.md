Devon Zuegel &nbsp; // &nbsp; 7 Oct 2015 &nbsp; // &nbsp; STATS 202

# Problem Set 2 #

## Problem 1 ##

#### Part A ####

![](/Users/devonzuegel/Github/stanford_classes/stats202/hw2/images/1a1.jpg)
![](/Users/devonzuegel/Github/stanford_classes/stats202/hw2/images/1a2.jpg)


#### Part B ####

**Theorem:** The K-means clustering algorithm decreases the objective at each iteration (until it reaches a stable local minimum).

**Proof:** Let `c` be an arbitrary centroid. On each iteration, we update `c` for a particular cluster to be the mean of all the observations in that group (assigned to the nearest centroid earlier in the iteration). This update will change `c`'s value iff there is some possible `c'` that is on average closer to all of the observations in the group. Thus, the portion of the objective determined by `c` decreases with every iteration until the stopping point (the iteration at which no centroids are updated).

<!-- Then, we iterate through all observations and update their labels to reflect the updated centroids. Take a single observation `o`, which we'll say is currently in cluster 1, whose initial centroid we'll call `c1`. This iteration will change `o`'s value iff there is some other centroid `cn` that is closer to it. Thus,  -->

## Problem 2 ##

#### Misc ####

**Common linkage types in hierarchical clustering**

*Complete* -- Maximal intercluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster A and the observations in cluster B, and record the largest of these dissimilarities.

*Single* -- Minimal intercluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster A and the observations in cluster B, and record the smallest of these dissimilarities. Single linkage can result in extended, trailing clusters in which single observations are fused one-at-a-time.

*Average* -- Mean intercluster dissimilarity. Compute all pairwise dissimilarities
between the observations in cluster A and the observations in cluster B, and record the average of these dissimilarities.

*Centroid* -- Dissimilarity between the centroid for cluster A (a mean vector of length p) and the centroid for cluster B. Centroid linkage can result in undesirable inversions.

![](/Users/devonzuegel/Github/stanford_classes/stats202/hw2/images/2.png)

## Problem 4 ##

$$y_{\text{linear}} = \beta_0 + \beta_1X + \epsilon$$

$$y_{\text{cubic}} = \beta_0 + \beta_1X + \beta_2X_2 + \beta_3X_3 + \epsilon$$

#### Part A ####

Despite the fact that the true relationship between X and Y is linear, I would expect the **training** residual sum of squares (RSS) for the cubic regression to be lower than that of the linear regression. The relationship may be linear, but the cubic regression will do a better job of capturing the noise / random error in the training set, which will cause the error to be lower.

#### Part B ####

The **test** RSS for linear regression will likely be lower than that of the cubic regression, because it will not overtrain to that random error.

#### Part C ####

The cubic will be at least as good as the linear, because it can "train away" its $\beta_2$ and $\beta_3$ coefficients to a 0 value, effectively making it a linear function.

#### Part D ####

There is not enough information to tell. If the true relationship is some even-powered polynomial (e.g. $x^{2}$ , $x^{4}$, ...) then linear is slightly better because it can at least generally increase/decrease in the same directions as $x \rightarrow ±\infty$. However, if it's some odd-powered polynomial, then cubic is slightly better because *it* can at least generally increase/decrease in the same directions as $x \rightarrow ±\infty$.




