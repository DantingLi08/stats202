Devon Zuegel &nbsp; // &nbsp; 29 Sept 2015 &nbsp; // &nbsp; STATS 202

# Problem Set 1 #

## Problem 1 ##

**Thoughts**
A flexible model:

- allows you to take full advantage of a large sample size (large n).
- will be necessary to find the nonlinear effect.
- fits too much of the noise in the problem (when variance of the error terms is high).
- when you have a lot of predictors, you need to:
    + pay heed to the the bias variance tradeoff
    + be careful to guard against spurious signal

(a) **large sample size `n`, small number of predictors:** When you have few predictors, your model will generally tend to have low variance but high bias; meanwhile, inflexible models tend to encourage even lower variance but higher bias, while flexible models tend to encourage the opposite. Thus, to strike a healhty balance with the variance-bias tradeoff, the *flexible model* will likely perform better.

(b) **small sample size `n`, large number of predictors:** *inflexible* will likely perform better, because with such a small sample size the flexible model would have a greater tendency to overfit the data. Also, the more predictors you have, the more carefully you need to constrain your model space to prevent overfitting. That said, with a small sample size both models will likely be quite inaccurate.

(c) **relationship between the predictors and response is highly non-linear:** assuming our non-flexible model is linear (or something that doesn't fit the true relationship), a *flexible model* will yield better results because then it can react to relationships in the data rather than trying to force the data into a strict mold like non-flexible would.

(d) **extremely high variance of the error terms:** *non-flexible* is better, because it will smooth out the noise from the high variance error terms.

## Problem 2 ##
##### Thoughts #####
- **prediction:** sing data to predict an event that has yet to occur
- **inference:** inferring the value of a population quantity such as the average income of a country or the proportion of eligible voters who say they will vote "yes"

#### PART A ####
regression, inference, `n = 500, p = 4`

#### PART B ####
classification, prediction, `n = 20, p = 13`

#### PART C ####
regression, prediction, `n = 53 (# of weeks in a year), p = 4`

## Problem 3 ##
#### PART A ####
![](/Users/devonzuegel/Github/stanford_classes/stats202/hw1/images/3a.png)

#### PART B ####
- **Variance** increases monotonically as flexibility increases, because when our computed `f'` fits the data more closely, we increase the amount by which `f'` would change if we estimated it using a different training data set.
- **Squared bias** declines monotonically as flexibility increases. With inflexible models (aka approximating data with a simple, reductionist model), we run the risk of oversimplifying the relationships within our data. If we do make this mistake, then we end up introducing systematic bias into our approximation of the true function `f`.
- **Var(ϵ), the irreducible error** is constant (though unknown to us unless we generated the data).
- **Test MSE** declines at first, because as flexibility increases the bias decreases. However, increased flexibility leads to increased variance, so at some point the benefits of decreasing bias are outweighed by the variance, which comes from the fact that we are overfitting our model to the test data. *The test MSE never drops below the irreducible error.*
- **Training MSE** declines as flexibility increases, because the `f'` curve computed from a more flexible model will fit the training data more closely, thus decreasing the mean squared error (MSE).

## Problem 4 ##
![](/Users/devonzuegel/Github/stanford_classes/stats202/hw1/images/4a.png)
![](/Users/devonzuegel/Github/stanford_classes/stats202/hw1/images/4bc.jpg)

## Problem 5 ##

(a) Yes, we can estimate the test MSE for a fixed point $x_0$ not included in $x_1,...,x_n$
(b) No, because in order to compute the bias we must know what the true function `f` is. Without it, we have nothing to compare out test data to.
(c) Yes, by definition MSE measures variance
(d) No, for the same reasons as (b)
