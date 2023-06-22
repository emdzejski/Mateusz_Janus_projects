---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
%load_ext autoreload
%autoreload 2
```

### Problem 2

<!-- #region tags=["PL"] -->
#### Ocena różnic pomiędzy dwoma niezależnymi eksperymentami
<!-- #endregion -->

<!-- #region tags=["PL"] -->
Przeprowadzono eksperyment mający na celu zbadanie wpływu pola magnetycznego na wypływ wapna z mózgów kurczaków. Do eksperymentu użyto dwie grupy kurczaków: w grupie kontrolnej były 32 kurczaki a w grupie badanej wystawionej na działanie pola magnetycznego było 36 kurczaków. Pomiar przepływu wapna dokonany został dla każdego kurczaka w każdej z obu grup. W grupie kontrolnej średni przepływ wyniósł $1.013$ a standardowe odchylenie  wyniosło $0.24$. W grupie badanej było to odpowiednio $1.173$ i $0.20$.
<!-- #endregion -->

#### Problem 2.1

<!-- #region tags=["PL"] -->
Zakładając, że pomiary w grupie kontrolnej pochodziły z rozkładu normalnego o średniej $\mu_c$ i wariancji $\sigma_c^2$ proszę podać rozkład _a posteriori_ dla $\mu_c$. Proszę założyć  prior $\mu_c\sim 1$ i $\sigma_c^2\sim \sigma_c^{-2}$. Podobnie proszę podać rozkład _a posteriori_ dla średniej w grupie kontrolnej $\mu_t$.
<!-- #endregion -->

```python
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
```

```python
mean_c = 1.013
mean_t = 1.173
stddev_c = 0.24
stddev_t = 0.2
n_c = 32
n_t = 36 
```

```python
y_t = st.t.rvs(31, size=10**6)
y_c = st.t.rvs(35, size=10**6)
```

```python
mu_c = y_c * np.sqrt(stddev_c**2/n_c) + mean_c
mu_t = y_t * np.sqrt(stddev_t**2/n_t) + mean_t

```

#### Problem 2.2

<!-- #region tags=["PL"] -->
Jaki rozkład _a posteriori_ ma różnica średnich $\mu_t-\mu_c$? Aby to obliczyć proszę wylosować po $1e6$ (1000000) liczb dla każdej grupy z rozkładów które otrzymali Państwo w pierwszym punkcie. Proszę narysować histogram rokładu różnic $\mu_t-\mu_c$ pomiędzy dwoma grupami i oszacować 95% region największej gestości (HDR).
<!-- #endregion -->

```python
diff = mu_t - mu_c
list_diff = list(diff)
```

```python
c1,b1,p1 = plt.hist(diff, bins=50, density=True)
plt.show()
```

```python
import sys
sys.path.append('/home/mateusz/BDA_Mateusz_Janus/assignments/src')
#sys.path.append('/home/mateusz/BayesianDataAnalysis/src')
from bda.stats import hdr_d
```

```python
dist=c1
x = (b1[1:]+b1[:-1])/2
print(x)
```

```python
hdr95 = hdr_d(x, dist, 0.95)
hdr95_percent_estimate = hdr95[0]
print(hdr95_percent_estimate) #95% hdr interval
```

```python
plt.hist(diff,bins=50, density=True,histtype='step');
plt.fill_between(x,dist,0,where = ( (x>hdr95[0][0]) & (x<=hdr95[0][1])), color='lightgray' );
```

```python

```

```python

```
