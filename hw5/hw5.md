Devon Zuegel &nbsp; // &nbsp; 3 Nov 2015 &nbsp; // &nbsp; STATS 202

# Problem Set 5 #

[web.stanford.edu/class/stats202/content/viewhw.html?hw5](http://web.stanford.edu/class/stats202/content/viewhw.html?hw5)

## Notes ##

- The **least squares** fitting procedure estimates $B_0$, $B_1$, ..., $B_p$ by minimizing: $$\text{RSS} = \sum_i^{n} \Bigg( y_i - \beta_0 - \sum_j^{p} \beta_j x_{ij}\Bigg) ^{2}$$
- **Ridge regression** is very similar to least squares, except the coefficients are estimated by minimizing: $$\text{Ridge} = \text{RSS} + \lambda \sum_j^{p} \beta_j ^2$$

## Problem 1 ##

*Chapter 6, Exercise 3 (p. 260). NOTE: there is a typo in the expression. Each term in the first sum should be squared (this is the RSS)*

$$\sum_i^{n} \big( y_i - \beta_0 - \sum_j^{p} \beta_j x_{ij} \big) \text{ subject to } \sum_j^{p}\left|\beta_j\right|\leq s$$

a) iii, **training RSS** steadily increases –– as `s` increases, we force more of the coefficients to be set to `0` (placing tighter constraints on the model).

b) ii, **test RSS** decreases then increases –– as `s` increases initially, we will remove the noisier variables which were causing overfitting, which improves our model by decreasing variance. At some point though, the constraints will become to much and remove important coefficients.

c) iv, **variance** steadily decreases –– noiser variables will be removed as `s` increases.

d) iii, **squared bias** steadily increases –– as more variables are removed, we depend more on a smaller number of predictors and the biases they introduce.

e) v, **irreducible error** remains constant –– our decisions don't effect this, it is an immutable feature of the problem.

## Problem 2 ##

*Chapter 6, Exercise 4 (p. 260). NOTE: there is a typo in the expression. Each term in the first sum should be squared (this is the RSS)*

## Problem 3 ##

*Chapter 6, Exercise 1 (p. 259)*

## Problem 4 ##

*Chapter 6, Exercise 8 (p. 262). For consistency, in parts (b) and (f) make all non-zero coefficients equal to 1*

## Problem 5 ##

*Chapter 6, Exercise 9 (p. 263)*

## Problem 6 ##

*Chapter 6, Exercise 10 (p. 263)*

## Problem 7 ##

*Chapter 6, Exercise 6 (p. 261)*