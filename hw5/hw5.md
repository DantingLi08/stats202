Devon Zuegel &nbsp; // &nbsp; 3 Nov 2015 &nbsp; // &nbsp; STATS 202

# Problem Set 5 #

[web.stanford.edu/class/stats202/content/viewhw.html?hw5](http://web.stanford.edu/class/stats202/content/viewhw.html?hw5)

## Notes ##

- The **least squares** fitting procedure estimates $B_0$, $B_1$, ..., $B_p$ by minimizing: $$\text{RSS} = \sum_i^{n} \Bigg( y_i - \beta_0 - \sum_j^{p} \beta_j x_{ij}\Bigg) ^{2}$$
- **Ridge regression** is very similar to least squares, except the coefficients are estimated by minimizing: $$\text{Ridge} = \text{RSS} + \lambda \sum_j^{p} \beta_j ^2$$

## Problem 1 ##

*Chapter 6, Exercise 3 (p. 260)*

$$\sum_i^{n} \bigg( y_i - \beta_0 - \sum_j^{p} \beta_j x_{ij} \bigg)^{2} \text{ subject to } \sum_j^{p}\left|\beta_j\right|\leq s$$

a. iii, **training RSS** steadily increases –– as `s` increases, we force more of the coefficients to be set to `0` (placing tighter constraints on the model).
b. ii, **test RSS** decreases then increases –– as `s` increases initially, we will remove the noisier variables which were causing overfitting, which improves our model by decreasing variance. At some point though, the constraints will become to much and remove important coefficients.
c. iv, **variance** steadily decreases –– noiser variables will be removed as `s` increases.
d. iii, **squared bias** steadily increases –– as more variables are removed, we depend more on a smaller number of predictors and the biases they introduce.
e. v, **irreducible error** remains constant –– our decisions don't effect this, it is an immutable feature of the problem.

## Problem 2 ##

*Chapter 6, Exercise 4 (p. 260)*

$$\sum_i^{n} \bigg( y_i - \beta_0 - \sum_j^{p} \beta_j x_{ij} \bigg)^{2} + \lambda \sum_j^{p} \beta_j^{2} $$

a. iii, **training RSS** steadily increases –– (same reasoning as 1a)
b. ii, **test RSS** decreases then increases –– (same reasoning as 1b)
c. iv, **variance** steadily decreases –– (same reasoning as 1c)
d. iii, **squared bias** steadily increases –– (same reasoning as 1d)
e. v, **irreducible error** remains constant –– (same reasoning as 1e)

## Problem 3 ##

*Chapter 6, Exercise 1 (p. 259)*

We perform best subset, forward stepwise, and backward stepwise selection on a single data set. For each approach, we obtain p + 1 models, containing 0, 1, 2, . . . , p predictors.

#### Part A ####

*Which of the three models with k predictors has the **smallest training RSS**?*

We will get the smallest training RSS by using **best subset selection**. Forward and backward won't be able to minimize the training RSS as much, because best chooses the model with the lowest training RSS out of all *all possible `k`-predictor models*. Forward and backward can come up with this same model, but because they explore the space of models heuristically rather than how best explores the space exhaustively.

#### Part B ####

> *Which of the three models with k predictors has the **smallest test RSS**?*

The answer to this question depends on the specifics of the problem. Any of these methods can overfit to the data.

#### Part C ####

###### SUBPART I ######

> *The predictors in the `k`-variable model identified by forward stepwise are a subset of the predictors in the `k + 1`-variable model identified by forward stepwise selection.*

**True** –– the variable model with `k + 1` predictors has the same group of predictors as in the model with just `k` predictors, with the addition of the `k + 1`th-best predictor predictor (a.k.a. the next predictor that results in the largest improvement to RSS).

###### SUBPART II ######

> *The predictors in the `k`-variable model identified by backward stepwise are a subset of the predictors in the `k + 1`- variable model identified by backward stepwise selection.*

**True** -- similar to part i, the `k`-predictor model has all of the predictors in the `k + 1`-predictor model, minus the worst predictor (a.k.a. the predictor that results in the smallest improvement to RSS).

###### SUBPART III ######

> *The predictors in the `k`-variable model identified by backward stepwise are a subset of the predictors in the `k + 1`- variable model identified by forward stepwise selection.*

**False** –– Forward and backward can result in different / disjoint sets.

###### SUBPART IV ######

> *The predictors in the `k`-variable model identified by forward stepwise are a subset of the predictors in the `k + 1`-variable model identified by backward stepwise selection.*

**False** –– Forward and backward can result in different / disjoint sets.

###### SUBPART V ######

> *The predictors in the `k`-variable model identified by best subset are a subset of the predictors in the `k + 1`-variable model identified by best subset selection.*

**False** –– Forward and backward can result in different / disjoint sets.

## Problem 4 ##

*Chapter 6, Exercise 8 (p. 262). For consistency, in parts (b) and (f) make all non-zero coefficients equal to 1*

## Problem 5 ##

*Chapter 6, Exercise 9 (p. 263)*

## Problem 6 ##

*Chapter 6, Exercise 10 (p. 263)*

## Problem 7 ##

*Chapter 6, Exercise 6 (p. 261)*