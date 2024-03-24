---
title: Kullback-Leibler (KL) Divergence
date: 2022-12-12T12:34:00+09:00
categories: [AI Math, Statistics]
tags: [Cross Entropy, Entropy, KL Divergence]
type: post
---
> **간단 요약**
> 
> 
> **Cross Entropy - Entropy**
> 
> 두 분포의 차이, 정보량을 의미한다.
> 
> metric이 아니다.
> 

엔트로피의 상대성에 대해 이야기한다.

**유도 과정**

`$$
\begin{aligned}H(p, q) & =-\sum_i p_i \log q_i \\& =-\sum_i p_i \log q_i-\sum_i p_i \log p_i+\sum_i p_i \log p_i \\& =H(p)+\sum_i p_i \log p_i-\sum_i p_i \log q_i \\& =H(p)+\sum_i p_i \log \frac{p_i}{q_i}\end{aligned}
$$`

이 때, `$H(p,q) - H(p)$`로 정리되는 다음 수식을 KL-Divergence 혹은 Relative Entropy라고 부른다.

`$$
\sum_i p_i \log \frac{p_i}{q_i}=H(p, q)-H(p)
$$`

`$$
KL(p|q) = \sum_xp_i\log{p_i\over q_i} = E_p[\log{\left({p_i\over q_i}\right)}]
$$`

두 분포 간의 차이를 측정한다.

`$P(X)$`를 기준으로 두 분포의 차이를 의미한다.

**Metric이 아니다.**

- `$K L(p \mid q) \geq 0$`을 만족한다.
- 모든 x에 대해 `$Q(X) =0\rightarrow P(X) =0$`가 성립한다.
- **Symmetry가 성립하지 않는다.**
    
    `$K L(p \mid q) \neq K L(q \mid p)$`
    
- **Triangle inequality를 만족하지 않는다.**

연속 변수의 KL 발산은 Entropy와 마찬가지로 합을 적분으로 대체하여 정의할 수 있다.

- **예제 — Relative Entropy 계산**
    
    ![kullback_leibler_kl_divergence](/imgs/kullback_leibler_kl_divergence0.png)
    
    `$$
    H(p) = -\left( \frac{1}{2}\log\frac{1}{2} + \frac{1}{4}\log\frac{1}{4} + \frac{1}{4}\log\frac{1}{4} \right)\\
     = \frac{3}{2}\log 2 = 0.45154499349
    $$`
    
    `$$
    H(q) = -\left( \frac{1}{3}\log\frac{1}{3} + \frac{1}{3}\log\frac{1}{3} + \frac{1}{3}\log\frac{1}{3} \right)\\
     = \log 3 = 0.47712125472
    $$`
    
    `$$
    H(p,q) = -\left( \frac{1}{2}\log\frac{1}{3} + \frac{1}{4}\log\frac{1}{3} + \frac{1}{4}\log\frac{1}{3} \right)\\
     = \log 3 = 0.47712125472
    $$`
    
    `$$
    H(q,p) = -\left( \frac{1}{3}\log\frac{1}{2} + \frac{1}{3}\log\frac{1}{4} + \frac{1}{3}\log\frac{1}{4} \right)\\
     = \frac{5}{3}\log 2 = 0.50171665944
    $$`
    
    - `$D_{KL}(p||q) = H(p,q) - H(p)$`
        
        `$$
        H(p,q) - H(p) = \log 3 - \frac{3}{2}\log 2 = 0.02557626122
        $$`
        
    - `$D_{KL}(q||p) = H(q,p) - H(q)$`
    
    `$$
    H(q,p) - H(q) = \frac{5}{3}\log 2 - \log 3 = 0.02459540472
    $$`
    

### 참조

[초보를 위한 정보이론 안내서 - KL divergence 쉽게 보기](https://hyunw.kim/blog/2017/10/27/KL_divergence.html)

**연관 개념? 알아보기**

elbo, variational inference

MLE