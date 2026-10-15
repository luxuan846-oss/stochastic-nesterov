# Research question: noise tolerance of the stochastic Fast KM algorithm with reused evaluations

Draft, 2026-10-16. Statements marked *derived* are our own computations on explicit examples; statements marked *open* are research targets, not results.

## Setting

Let $T:H\to H$ be $\theta$-averaged with $\operatorname{Fix}T\neq\emptyset$, and consider the Fast KM algorithm of Boţ–Nguyen (SINUM 2023, Algorithm 2.1), with $\alpha>2$ and $0<s\le 1/\theta$. In the stochastic version, each iteration queries the operator once,

$$
\widehat T_k(x_k)=Tx_k+e_k,\qquad \mathbb E[e_k\mid\mathcal F_k]=0,\qquad \mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]\le\sigma_k^2,
$$

and the term $T(x_{k-1})$ in (2.7) is replaced by the value $\widehat T_{k-1}(x_{k-1})$ stored at the previous iteration. This is the natural one-query implementation. With minibatches of size $b_k\asymp k^{q}$ one has $\sigma_k^2\asymp k^{-q}$.

## Question

**Which decay of $\sigma_k^2$ is necessary and sufficient for the stochastic Fast KM algorithm with reused evaluations to retain the rate $\lVert x_k-Tx_k\rVert=o(1/k)$ almost surely, and how does the answer depend on (i) what is assumed on the noise beyond its variance and (ii) the step size $s$ relative to $1/\theta$?**

The mean-square version, $\mathbb E\lVert x_k-Tx_k\rVert^2=o(1/k^2)$, serves as an intermediate step. The probabilistic tools are restricted to the Borel–Cantelli lemmas, martingale convergence (including Robbins–Siegmund) and Kronecker's lemma.

## Known sufficient conditions

The available almost-sure $o(1/k)$ results for stochastic accelerated fixed-point methods, namely VR-FKM (arXiv 2406.02413), VAPEG (arXiv 2508.16791, Cor. 3.4) and AFP (arXiv 2512.13547), require a weighted summability of the type $\sum_k k^2\sigma_k^2<\infty$, i.e. $q>3$ for power decay. AFP is itself a one-query recursion with reused values, with coefficients different from those of Fast KM. In the energy estimates, the noise of each iteration is paid for separately.

## Evidence from explicit examples (*derived*)

Take $s=1$ and write $a_k=\frac{k+\alpha/2}{k+\alpha}$, $d_k=\frac{k}{k+\alpha}$.

1. **$T=0$** ($\theta=1/2$, so $s<1/\theta$). The recursion becomes $x_{k+1}=a_kx_k+a_ke_k-d_ke_{k-1}$. After one substitution, the noise $e_{k-1}$ enters $x_{k+1}$ with the coefficient
$$
a_ka_{k-1}-d_k=\frac{\alpha(\alpha-2)}{4(k+\alpha)(k-1+\alpha)}=O(k^{-2}),
$$
so the stored noise largely cancels across two consecutive iterations. Consequently $\mathbb E\lvert x_k\rvert^2\asymp\sigma_k^2$, and the mean-square rate holds if and only if $q>2$. Under independent Gaussian noise the almost-sure threshold is also $q>2$; under second-moment bounds only, an example with rare large errors shows that the almost-sure rate fails for $2<q\le3$.
2. **$T=-I$** ($\theta=1$, so $s=1/\theta$). The recursion becomes $x_{k+1}=d_kx_{k-1}+a_ke_k-d_ke_{k-1}$. Even and odd iterates decouple, the two occurrences of $e_{k-1}$ fall into different chains, and no cancellation occurs. The mean-square rate then requires $q>3$, and so does the almost-sure rate under independent Gaussian noise.

In summary, for power decay $\sigma_k^2\asymp k^{-q}$ the almost-sure threshold in these examples is

| noise assumption | $T=0$, $s<1/\theta$ | $T=-I$, $s=1/\theta$ |
|---|---|---|
| second moments only | $q>3$ (rare large errors) | $q>3$ |
| independent Gaussian | $q>2$ | $q>3$ |

The choice $s=1$ recommended in Remark 2.1 of Boţ–Nguyen is, for nonexpansive $T$, exactly the boundary case $s=1/\theta$.

## Open problems

1. Prove the known sufficient condition for the original reused recursion: $\sum_k k^2\sigma_k^2<\infty$ implies the $o(1/k)$ rate and weak convergence of the iterates, for every $\theta$-averaged $T$ and $0<s\le1/\theta$. (*open*; the obstacle is a linear term in the old noise $e_{k-1}$ that does not vanish under conditional expectation.)
2. For $s<1/\theta$ and independent Gaussian (or sub-Gaussian) noise, decide whether $q>2$ suffices for the almost-sure rate for every $\theta$-averaged $T$; first in mean square. (*open*; a new energy function that sees the cancellation would be needed.)
3. Under second moments only, the rare-error example shows that $q>3$ is necessary already for $T=0$. For $s=1/\theta$, the example $T=-I$ shows that $q>3$ is necessary even for Gaussian noise.

## Scope with respect to the oracle cost

With a constant step size, N6 reads $\sum_k k^2\sigma_k^2<\infty$ and forces the batch size to grow faster than $k^3$. A positive answer to open problem 2 would reduce this to $k^{2+\omega}$, one order of $k$ less per iteration. It would not reach one oracle call per iteration: $q>2$ still requires the variance to decay, so the number of oracle calls per iteration still grows. A single oracle call per iteration keeps $\sigma_k^2$ bounded away from zero (N2), which with a constant step size does not yield a vanishing residual, and with decreasing step sizes leads to the slower stochastic-approximation rates, e.g. Remark 3.2 of Attouch–Fadili–Kungurtsev (JOTA 2026). That regime is a different problem and is not addressed here.

## Questions for the meeting

- N6 is too demanding because the batch size must grow. Is reducing the growth from $k^3$ to $k^2$ a meaningful answer to this concern, or should the target be one oracle call per iteration?

- Is an almost-sure statement under a Gaussian or sub-Gaussian noise assumption acceptable, with the mean-square statement as an intermediate step?
- Is the dependence on $s<1/\theta$ versus $s=1/\theta$ already known in the deterministic inexact literature on Fast KM?
- Has the cancellation of reused stochastic gradients been exploited in the analysis of stochastic Nesterov methods? Writing Nesterov's method in the extrapolated sequence gives a gradient-difference term with the same structure.
