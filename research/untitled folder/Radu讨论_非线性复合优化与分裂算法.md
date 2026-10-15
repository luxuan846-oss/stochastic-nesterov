# 0914 Discussion

We consider

\[
\min_x P(x):=f(x)+r(A(x)),
\] where:

- \(A:\mathbb R^d\to\mathbb R^m\) is smooth and nonlinear;
- \(r\) is proper, closed, and convex;
- \(f\) is smooth and possibly nonconvex. 

# I. Related Work

## 1. Prox-Linear Composite Optimization

Drusvyatskiy and Paquette study

\[
\min_x g(x)+h(c(x)),
\]

where \(g\) and \(h\) are convex and \(c\) is smooth and nonlinear. The resulting objective may be nonconvex. Their prox-linear method linearizes \(c\) and solves a regularized convex subproblem at every iteration. They establish an \(O(\varepsilon^{-2})\) outer-iteration bound for exact subproblem solves and a \(\widetilde O(\varepsilon^{-3})\) first-order complexity bound using smoothing and inexact solves.

Its core iteration is

\[
x_{k+1}=\arg\min_x\left\{
g(x)+h\bigl(c(x_k)+\nabla c(x_k)(x-x_k)\bigr)
+\frac{1}{2t}\|x-x_k\|^2
\right\}.
\]

> D. Drusvyatskiy and C. Paquette, *Efficiency of Minimizing Compositions of Convex Functions and Smooth Maps*, Mathematical Programming, 2019. [DOI](https://doi.org/10.1007/s10107-018-1311-3)

## 2. Nonconvex-Concave Minimax Optimization

Boț and Böhm consider

\[
\min_x\max_y\;p(x)+\Phi(x,y)-q(y),
\]

where \(\Phi\) is weakly convex in \(x\) and concave in \(y\). They analyze single-loop alternating proximal gradient descent-ascent in deterministic and stochastic settings. Their guarantees concern stationarity of the max function \(p(x)+\max_y\{\Phi(x,y)-q(y)\}\), with complexities \(O(\varepsilon^{-6})\) and \(O(\varepsilon^{-8})\) in the merely concave deterministic and stochastic cases, respectively. Taking \(\Phi(x,y)=\langle A(x),y\rangle\) and \(q=r^*\) gives the closest general framework to our method.

Their alternating proximal GDA iteration is

\[
x_{k+1}=\operatorname{prox}_{\eta_x p}
\bigl(x_k-\eta_x G_x(x_k,y_k)\bigr),
\]

\[
y_{k+1}=\operatorname{prox}_{\eta_y q}
\bigl(y_k+\eta_y G_y(x_{k+1},y_k)\bigr).
\]

> R. I. Boț and A. Böhm, *Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex-Concave Minimax Problems*, SIAM Journal on Optimization, 2023. [DOI](https://doi.org/10.1137/21M1465470)

## 3. Weakly Convex Primal-Dual Methods

Bednarczuk, Syga, and Tran study

\[
\min_x\max_y\;f(x)+\langle Lx,y\rangle-g^*(y),
\]

where \(f\) is weakly convex and \(L\) is linear. Under an inf-sharpness condition and sufficiently close initialization, their PDHG-type method converges linearly to a global saddle point. The result gives whole-sequence convergence, but it does not cover nonlinear \(A(x)\).

The dual-first version is

\[
y_{k+1}=\operatorname{prox}_{\tau g^*}(y_k+\tau Lx_k),
\qquad
\bar y_{k+1}=y_{k+1}+\theta(y_{k+1}-y_k),
\]

\[
x_{k+1}=\operatorname{prox}_{\sigma f}
\bigl(x_k-\sigma L^*\bar y_{k+1}\bigr).
\]

> E. M. Bednarczuk, M. Syga, and T. H. Tran, *Primal-Dual Algorithm for Weakly Convex Functions under Sharpness Conditions*, European Journal of Operational Research, 2026. [DOI](https://doi.org/10.1016/j.ejor.2026.01.053)

## 4. Full Splitting for Structured DC Programs

Boț, Nenov, and Tao consider

\[
\min_{x\in S}\;g(Ax)+\phi(x)-f(Kx),
\]

with convex nonsmooth \(f,g\), smooth \(\phi\), and linear \(A,K\). Their adaptive double-proximal method fully separates the nonsmooth functions and linear operators and uses a moving proximal center. Accumulation points are approximate KKT points, and the whole sequence converges under a KL assumption. The analysis provides a useful full-splitting template, but the operators remain linear.

The core DPFS iteration is

\[
x^{k+1}=\operatorname{Proj}_S\left[
x^k-\frac{1}{\rho_k}
\bigl(A^*z^k-K^*y^k+\nabla\phi(x^k)\bigr)
\right],
\]

\[
y^{k+1}=\arg\min_y\left\{
f^*(y)-\langle Kx^{k+1},y\rangle
+\frac{\beta_k}{2}\|y-y^k\|^2
\right\},
\]

\[
z^{k+1}=\arg\min_z\left\{
g^*(z)-\langle Ax^{k+1},z\rangle
+\frac{\alpha_k}{2}\|z-\delta_k z^k\|^2
\right\}.
\]

> R. I. Boț, R. Nenov, and M. Tao, *A Full Splitting Algorithm for Structured Difference-of-Convex Programs*, Applied Numerical Mathematics, 2026. [DOI](https://doi.org/10.1016/j.apnum.2026.02.019)

## 5. Full Splitting for Structured Fractional Programs

Boț, Li, and Tao consider

\[
\min_{x\in S}\;F(x):=\frac{g(Ax)+h(x)}{f(Kx)},
\]

where \(f,g\) are convex and nonsmooth, \(h\) is smooth and possibly nonconvex, and \(A,K\) are linear. Their single-loop FSPS framework avoids solving a full Dinkelbach subproblem at every iteration.

A simplified S-FSPS iteration is

\[
y^{k+1}\in\partial f(Kx^k),
\]

\[
x^{k+1}=\operatorname{Proj}_S\left[
x^k+\frac{\theta_k}{\delta_k}K^*y^{k+1}
-\frac{1}{\delta_k}\nabla h(x^k)
-\frac{1}{\delta_k}A^*z^k
\right],
\]

\[
z^{k+1}=\operatorname{prox}_{g^*/\gamma_k}
\left(\frac{Ax^{k+1}}{\gamma_k}\right),
\qquad
\theta_{k+1}=
\frac{\Psi(x^{k+1},z^{k+1};\gamma_k)}{f(Kx^{k+1})},
\]

where

\[
\Psi(x,z;\gamma)
=\langle z,Ax\rangle-g^*(z)+h(x)+\iota_S(x)
-\frac{\gamma}{2}\|z\|^2.
\]

S-FSPS converges subsequentially to an exact lifted stationary point. Adaptive FSPS adds extrapolation and backtracking and converges globally to an approximate lifted stationary point under a KL assumption. The composite operators remain linear.

> R. I. Boț, G. Li, and M. Tao, *Full Splitting Algorithms for Fractional Programs with Structured Numerators and Denominators*, SIAM Journal on Optimization, 2025. [DOI](https://doi.org/10.1137/23M1626591)

# II. Current Progress


## 5. Fenchel Min-Max Reformulation


Fenchel duality gives

\[
r(z)=\sup_y\{\langle z,y\rangle-r^*(y)\}.
\]

Hence,

\[
\min_x P(x)=\min_x\sup_y\mathcal L(x,y),
\qquad
\mathcal L(x,y)
=f(x)+\langle A(x),y\rangle-r^*(y).
\]

The first-order system is

\[
0=\nabla f(x)+JA(x)^*y,
\qquad
A(x)\in\partial r^*(y)
\]

## 6. Direct Primal-Dual Method

Our current DDLALM performs one primal descent step and one dual proximal ascent step on Perturbed smoothing method.

<!-- \[
x_{k+1}
=
x_k-	au_k
\bigl(\nabla f(x_k)+JA(x_k)^*y_k\bigr),
\]

\[
y_{k+1}
=
\operatorname{prox}_{\sigma_k r^*}
\bigl(y_k+\sigma_k A(x_{k+1})\bigr).
\] -->

<!-- With an additional proximable term \(p(x)\), the primal step becomes

\[
x_{k+1}
=
\operatorname{prox}_{\tau_k p}
\left(
x_k-	au_k\bigl(\nabla f(x_k)+JA(x_k)^*y_k\bigr)
\right).
\] -->

Key properties:

- The method is single-loop and has no inner stopping criterion.
- It is a nonlinear primal-dual splitting method of the Boț–Böhm type.


## 8. Research Target

minmax （应用场景);

stochastic Nesterov 加速与 ODE 是对方关注的视角;  nonsmooth analysis ( weakly convex);  error bound；  
Known results leave the following gap:

- Drusvyatskiy–Paquette use prox-linear subproblems and inner solves.
- Boț–Böhm analyze max-function stationarity, not KL whole-sequence convergence.
- The 2026 EJOR method assumes a linear coupling.
- Boț–Nenov–Tao also use linear composite operators.
- Boț–Li–Tao treat a structured ratio with linear composite operators.

Our target is a **single-loop primal-dual splitting method for nonlinear \(A(x)\)** with:

- merely convex dual regularization;
- controlled dual tracking error;
- whole-sequence convergence to a critical/KKT point under a KL or error-bound condition./ last iteration. 
- subgradient methods.

**Two main difficulties remain: ？**

## References

1. Drusvyatskiy, D., and Paquette, C. *Efficiency of Minimizing Compositions of Convex Functions and Smooth Maps*. Mathematical Programming 178, 503–558, 2019.
2. Boț, R. I., and Böhm, A. *Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex-Concave Minimax Problems*. SIAM Journal on Optimization 33(3), 1884–1913, 2023.
3. Bednarczuk, E. M., Syga, M., and Tran, T. H. *Primal-Dual Algorithm for Weakly Convex Functions under Sharpness Conditions*. European Journal of Operational Research 334(3), 735–750, 2026.
4. Boț, R. I., Nenov, R., and Tao, M. *A Full Splitting Algorithm for Structured Difference-of-Convex Programs*. Applied Numerical Mathematics 225, 203–225, 2026.
5. Boț, R. I., Li, G., and Tao, M. *Full Splitting Algorithms for Fractional Programs with Structured Numerators and Denominators*. SIAM Journal on Optimization 35(4), 2623–2653, 2025.
