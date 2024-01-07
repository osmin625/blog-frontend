---
title: Taylor polynomials
date: 2023-11-11-18:04:00 +0900
categories: [AI Math, Numerical Analysis]
tags: [Taylor Approximation, Polynomial Form]
img_path: /assets/post_imgs/
math: true
---

## **테일러 근사**

복잡한 형태의 미분 가능한 함수 $f(x)$를 다항식의 합으로 근사하는 것

$a$를 포함하는 구간에서 함수 $f$가 무한 미분이 가능 할 때

$$
\begin{aligned}f(x) & =\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n !}(x-a)^n \\& =f(a)+\frac{f^{\prime}(a)}{1 !}(x-a)+\frac{f^{\prime \prime}(a)}{2 !}(x-a)^2+\frac{f^{\prime \prime \prime}(a)}{3 !}(x-a)^3+\ldots\end{aligned}
$$

를 테일러 급수라고 한다.

**$f(x)$를 임의의 수 $a$에 대해 정리하는 과정**이라 이해하면 편하다.

- 수식이 이렇게 생긴 이유
    
    $f(x)$를 $a$에 대해 정리하고 싶어 식을 $f(x) = t_n(x-a)^n + t_{n-1}(x-a)^{n-1 }+\dots + t_1(x-a)^1$와 같이 정의했을 때,
    
    $f^{(n)}$은 $f(x)$를 n번 미분하면서 나머지 모든 항이 날아가고 n차항만 남게 된다.
    
    또한, 미분 과정에서 차수는 계수에 곱해진다.
    
    $f^{(n)}(1) = t_1 \times n!$
    
    우리는 원래 식의 계수인 $t_n,...,t_1$을 원하기 때문에, $n!$으로 다시 나눠준다.
    
    - 예제를 통해 다시 한 번 살펴보자.
        
        $f(x) = 7x^3 - 18x^2 + 20x - 1$라고 할 때, $x=1$에 대해 테일러 급수를 적용해보자.
        
        $x=1$에서의 함수값, 미분값, 이차 미분 값 등을 구해보면
        
        - $f(1) = 8$
        - $f'(1) = 5$
        - $f''(1) = 6$
        - $f'''(1) = 42$
        
        과 같다.
        
        각 미분값에 $\tt(미분 차수)!$으로 나눠주면 우리가 원하는 계수를 구할 수 있다.
        
        $$
        f(x) = 7(x-1)^3 + 3(x-1)^2 + 5(x-1) + 8
        $$
        
        $f(x)$는 위처럼 생겼는데, 해당 식에 다시 미분을 해보면 그대로 일치하는 것을 확인할 수 있다.
        

곡선은 무엇에 의해 정의될까?

탄젠트(미분), 곡률(2차 미분), torsion(비틀림, 3차 미분)

즉, 곡선을 제대로 근사하기 위해선 적어도 3차 미분까지 근사를 해야 한다.

수학적으로는 무한하게 미분 가능하다고 정의하지만, 수치 해석에서는 절단 오차 개념을 도입하여 적정 수준까지만 항을 정의한다.

테일러 급수를 활용하여 특수한 값 $a$의 $f(a), f'(a), f''(a), \dots$를 활용하여 $**a$ 주변의 값을 근사**한다.

테일러 급수는 $x$가 $a$에서 멀어질수록 오차가 커진다.

이렇게, $a$지점에서 근사한 $n$차 테일러 다항식을 $p_n(x ; a)$로 표기한다.

## 테일러 근사의 오차

$f(x)$에 대한 테일러 근사를 효율적으로 사용하려면 정확도를 계산하는 과정이 필요하다.

테일러 급수로 $n$차까지 근사한 식 $p_n(x)$과 원본 식$f(x)$의 오차를 구해보자.

$$
R_n(x) = f(x) - p_n(x)
$$

원본 식은 무한대로 미분이 가능할 수도 있지만, 만약 $n+1$차까지만 미분이 가능하다면?

원본 식과 근사식의 오차는 

$$
R_n(x) = {f^{(n+1)}(a)\over(n+1)!}(x-a)^{n+1}
$$

가 되고, $R_n(x)$는 

코시의 평균값 정리에 의해

$$
{f^{(n+1)}(a)\over(n+1)!}(x-a)^{n+1}<R_n(cx) < {f^{(n+1)}(x)\over(n+1)!}(x-a)^{n+1}
$$

을 만족한다.

## Polynomial form

### **Power form**

선형 결합 형태

$$
p_n=a_0+a_1 x+a_2 x^2+\cdots+a_n x^n=\sum_{k=0}^n a_k x^k
$$

### Shifted Power form

$c$가 중심이 되는 다항식

$$
p_n=b_0+b_1(x-c)+b_2(x-c)^2+\cdots+b_n(x-c)^n
$$

### Taylor form(Taylor Polynomial)

shifted power form에서의 계수가 $b_k=\frac{p_n^{(k)}(c)}{k !}$인 경우

$$
p_n(x)=p_n(c)+(x-c) p_n^{\prime}(c)+\frac{(x-c)^2}{2 !} p_n^{\prime \prime}(c)+\cdots+\frac{(x-c)^n}{n!} p_n^{(n)}(c)
$$

### Newton form

중심이 $c_1,c_2,...,c_n$인 경우

$$
\begin{matrix}p_n&=&d_0+d_1\left(x-c_1\right)+d_2\left(x-c_1\right)\left(x-c_2\right)\\&&+\cdots+d_n\left(x-c_1\right) \ldots\left(x-c_n\right)\\\\
&=&d_0+\sum_{k=1}^n d_k \prod_{j=1}^k\left(x-c_j\right)
\end{matrix}
$$

newton form에서 $c_1=\cdots=c_n=c$로 설정하면 shifted power form이 되고, $c_1=\cdots=c_n=0$이면 power form이 된다.

### Nested form(Honer’s method)

$$
\begin{aligned}p(x) & =a_0+a_1 x+a_2 x^2+a_3 x^3+\cdots+a_n x^n \\& =a_0+x\left(a_1+x\left(a_2+x\left(a_3+\cdots+x\left(a_{n-1}+x a_n\right) \cdots\right)\right)\right)\end{aligned}
$$

## Polynomial evaluation

수치 해석은 함수를 정확하게 근사해내는 목적이 있다.

이를 위해 테일러 급수를 활용한다.

테일러 급수를 통해 함수의 모양을 비슷하게 따르더라도, 값이 동일한지를 체크하기 위해 반드시 오차값을 구해야 한다.

우리가 사용하는 대부분의 기계는 Taylor 분석을 통한 근사로 만들어진다.

근사의 속도를 측정하는 방법

- 나머지 정리
- 조립 제법

프로그래머 관점으로 다항식을 평가하자.

수식 계산에서 곱셈 연산이 꽤 무겁기 때문에, 곱셈 횟수를 최대한 줄여야 한다.

$p(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n$에서 $a_0,a_1,...,a_n$과 $x$가 주어지는 경우 다항식을 계산하기 위해 몇 번의 곱셈이 필요한가?

### ex) $p(x) = 3 - 4x -5x^2 - 6x^3 + 7x^4 - 8x^5$

위의 5차 다항식을 직관적으로 계산하면 총 15번의 곱셈이 필요하다.

$4\times x$ ⇒ 1

$5\times x\times x$ ⇒ 2

$\cdots$

**총 곱셈의 개수: ${n(n+1)\over 2}$ ⇒ $O(n^2)$**

어떻게 다항식을 더 효율적으로 평가할 수 있을까? ⇒ 중복 계산을 최소화하자.

$x^3$을 계산할 때, $x\times x\times x$로 계산하는 것이 아니라, 기존에 계산된 $x^2$를 활용하여 $x\times x^2$를 계산하게 되면 곱셈 개수를 줄일 수 있다.

$4 \times x$ ⇒ 1

$5\times x\times x$ ⇒ 2

$6 \times x \times x^2$ ⇒ 2

$\cdots$

**총 곱셈의 개수: $2n -1$ ⇒ $O(n)$**

메모이제이션을 적용하면 $O(N)$이 된다.

메모이제이션을 적용했을 때의 단점으로는, 순서가 발생하기 때문에 병렬 계산이 안된다.

load balancing을 없애며 병렬 계산을 하는 것이 가장 중요하다.

호너의 법칙을 활용하면 **총 곱셈의 개수**가 **$n$**으로 줄어든다.