---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"tags": ["EN"]}

# Rounded data  (from "Bayesian Data Analysis")

+++ {"tags": ["EN"]}

It is a common problem for measurements to be observed in rounded form. For a simple example, suppose we weigh an object five times and measure weights, rounded to the nearest pound, of 10, 10, 12, 11, 9. Assume the unrounded measurements are normally distributed with some mean $\mu$ and variance $\sigma^2$.

```{code-cell} ipython3
import numpy as np
import scipy.stats as st
from scipy.special import logsumexp
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
def make_grid(f,xs,ys):
    grid = np.zeros((len(ys), len(xs)))
    for iy in range(len(ys)):
         for ix in range(len(xs)):
                grid[iy,ix]=f(xs[ix],ys[iy])
            
    return grid    
```

## Problem 1

+++ {"tags": ["EN"]}

Give the posterior distribution for $(\mu, \sigma^2)$ obtained by pretending that the observations are exact unrounded measurements. Assume a noninformative prior on $\mu$ and $\sigma$

+++

$$\mu\propto 1\qquad \sigma^2\propto \frac{1}{\sigma^2}$$

```{code-cell} ipython3
y = np.array([10,10,11,12,9])
```

```{code-cell} ipython3
mus = np.linspace(5,15,100)
var = np.linspace(0.1, 3, 150)

def post_maker(mu,sigma):
    return np.sum(st.norm.logpdf(y, mu,sigma)) - np.log(sigma)


grid = make_grid(post_maker,mus,var)
grid -= logsumexp(grid)
grid_unrounded = np.exp(grid)
```

```{code-cell} ipython3
plt.contourf(mus,var,grid_unrounded)
plt.show()
```

## Problem 2

+++ {"tags": ["EN"]}

Give the correct posterior distribution for $(\mu, \sigma^2)$ treating the measurements as rounded.

+++

Proszę podać rozkład a posteriori dla zaokrąglonych danych

```{code-cell} ipython3
def post_for_rounded(mean, var):
    logpost = [np.log((st.norm.cdf(x+0.5, mean, var)) - st.norm.cdf(x-0.5, mean, var)) for x in y] 
    return np.sum(logpost) - np.log(var)
    

grid_2 = make_grid(post_for_rounded, mus, var)
grid_2 -= logsumexp(grid_2) 
grid_rounded = np.exp(grid_2)
```

```{code-cell} ipython3
plt.contourf(mus,var,grid_rounded)
plt.show()
```

## Problem 3

+++ {"tags": ["EN"]}

How do the incorrect and correct posterior distributions differ? Compare means, variances, and contour plots.

+++ {"tags": ["EN"]}

#### Marginal distribution

+++ {"tags": ["EN"]}

To calculate mean and variance of $\mu$ and $\sigma^2$ we need marginal distributions. We can approximate them  numerically by symming over one axis of the grid.
Do not forget to exponentiate the log of probability before summing!

+++

Do obliczenia średniej i wariancji

```{code-cell} ipython3
#marginal distributions
marginal_sigma_unrounded = grid_unrounded.sum(axis=1)

marginal_mu_unrounded = grid_unrounded.sum(axis=0)

marginal_sigma_rounded = grid_rounded.sum(axis=1)

marginal_mu_rounded = grid_rounded.sum(axis=0)
```

```{code-cell} ipython3
#means and variances for data treated as unrounded
sigma_unrounded_mean = np.sum(var*marginal_sigma_unrounded)/np.sum(marginal_sigma_unrounded)

mu_unrounded_mean = np.sum(mus*marginal_mu_unrounded)/np.sum(marginal_mu_unrounded)

sigma_unrounded_variance = np.sum((var-sigma_unrounded_mean)**2 *marginal_sigma_unrounded)

mu_unrounded_variance = np.sum((mus-mu_unrounded_mean)**2 *marginal_mu_unrounded)
```

```{code-cell} ipython3
#means and variances for data treated as rounded
sigma_rounded_mean = np.sum(var*marginal_sigma_rounded)/np.sum(marginal_sigma_rounded)

mu_rounded_mean = np.sum(mus*marginal_mu_rounded)/np.sum(marginal_mu_rounded)

sigma_rounded_variance = np.sum((var-sigma_rounded_mean)**2 *marginal_sigma_rounded)

mu_rounded_variance = np.sum((mus-mu_rounded_mean)**2 *marginal_mu_rounded)
```

```{code-cell} ipython3
print("comparison:")
print(f"Mean and variance for mu in unrounded data: {mu_unrounded_mean}, {mu_unrounded_variance}")
print()
print(f"Mean and variance for mu in rounded data: {mu_rounded_mean}, {mu_rounded_variance}")
print()
print(f"Mean and variance for sigma in unrounded data: {sigma_unrounded_mean}, {sigma_unrounded_variance}")
print()
print(f"Mean and variance for sigma in rounded data: {sigma_rounded_mean}, {sigma_rounded_variance}")
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
