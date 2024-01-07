---
title: 'SVD: Singular Value Decomposition(특이값 분해)'
date: 2023-03-30-00:19:00 +0900
categories: [AI Math, 선형대수]
tags: [Collaborative Filtering, Matrix Decomposition, Singular Value Decomposition]
math: true
---
> 간단 요약  
> 2차원 행렬을 두 개의 잠재요인 행렬과 하나의 대각행렬로 분해하는 기법
{: .prompt-info }
> eigen vector, eigen value
- **2차원 행렬 분해 기법**
    - 유저 잠재요인 행렬 ⇒ 유저 임베딩
    - 잠재요인 대각행렬  ⇒ 임베딩의 중요도
    - 아이템 잠재요인 행렬 ⇒ 아이템 임베딩
- **차원축소 기법**
- **행렬을 대각화하는 방법**
- **모든 m x n 행렬에 대해 적용 가능**

Rating Matrix $R$ 에 대해 유저와 아이템의 잠재 요인을 포함할 수 있는 행렬로 분해한다.

### **Full SVD**

기존 행렬을 온전하게 3개의 행렬로 분해한다.

$$
\tt Full\ \ SVD :R = U\Sigma V^T
$$

- $U$: 유저와 Latent Factor의 관계
    
    $U$의 열벡터는 $R$의 left singular vector
    
- $V$: 아이템과 Latent Factor의 관계
    
    $V$의 열벡터는 $R$의 right singular vector
    
- $\Sigma$: Latent Factor의 중요도
    
    $RR^T$을 고유값 분해해서 얻은 직사각 대각 행렬
    
    대각 원소들은 $R$의 singular value(특이치)
    

### **Truncated SVD**

$\Sigma$를 일부만 사용한다.

$$
\tt Truncated \ \  SVD: R \approx \widehat{U} \Sigma_k \widehat{V^T}=\hat{R}
$$

$\Sigma$는 중요도로 정렬되어 있기 때문에, 상위 k개만 활용하여 기존의 행렬을 거의 유사하게 나타낼 수 있다.

즉, 몇 개의 특이치만을 가지고도 유용한 정보를 유지한다.

분해된 행렬이 부분 복원되면서 가장 중요한 정보로 요약된다.

$\widehat R$은 축소된 $\widehat U, \widehat {V^T}, \Sigma_k$에 의해 계산된다.

각각의 K개의 Latent Factor는 유추할 수 있을 뿐, 정확히 무엇을 의미하는지 알 수 없다.

### **SVD의 한계**

- **분해(Decomposition)하려는 행렬에 결측치가 없어야 한다.**
    
    User-Item 행렬의 경우 모든 값이 채워져야 한다.
    
    Sparsity가 높은 데이터의 경우 결측치가 매우 많다.
    
    실제 데이터는 대부분 Sparse Matrix
    
- **Imputation 후 SVD를 수행 → Computation 비용 증가**
    
    Imputation은 데이터의 양을 상당히 증가시키기 때문
    
    Imputation에 의해 데이터 왜곡 발생 시 성능 저하
    
    행렬의 entry가 매우 적을 때 SVD를 적용하면 과적합 되기 쉽다.


[참고하면 좋은 자료 -- SVD의 의미](https://angeloyeo.github.io/2019/08/01/SVD.html)