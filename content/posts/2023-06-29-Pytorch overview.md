---
title: PyTorch 개요
date: 2023-03-13-09:58:00 +0900
categories: [DL Framework, PyTorch]
tags: [PyTorch, Overview]
pin: true
---
> Naver BoostCamp AI Tech에서 학습한 내용을 재구성했습니다.  
> 해당 게시글은 지속적으로 업데이트할 예정입니다.  
{: .prompt-info }

## 구현 개요(PyTorch)

### 1. 데이터 준비

- [Tensor](https://osmin625.github.io/posts/Tensor/)
- [PyTorch Datasets & DataLoaders](https://osmin625.github.io/posts/PyTorch-Datasets-&-DataLoaders/)

### 2. 모델 정의 ([torch.nn.Module](https://osmin625.github.io/posts/PyTorch-%EB%AA%A8%EB%8D%B8-%EC%A0%95%EC%9D%98%ED%95%98%EA%B8%B0/))

[PyTorch **모델 불러오기**](https://osmin625.github.io/posts/PyTorch-%EB%AA%A8%EB%8D%B8-%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0/)

- Input size, Output size 정의 [nn.Parameter](https://osmin625.github.io/posts/PyTorch-nn-Parameter/)
- Forward 연산 정의
- [Backward](https://osmin625.github.io/posts/Backward/) 연산 정의

### 3. 하이퍼 파라미터 지정 [**Hyperparameter Tuning**](https://osmin625.github.io/posts/Hyperparameter_tuning/)

### 4. 모델 평가 기준 및 Optimizer 설정

1. 모델 평가 기준 : loss를 어떻게 계산할 것인가? [손실 함수(Loss Function)](https://osmin625.github.io/posts/Loss-function/)
2. [Optimizer](https://osmin625.github.io/posts/Optimizer/) 설정

### 5. 모델 학습

- [1 epoch에 일어나는 일](https://osmin625.github.io/posts/1-epoch/)  
- [PyTorch **Multi-GPU 학습**](https://www.notion.so/PyTorch-Multi-GPU-cddece8aedc84060ab5baceb59821da0?pvs=21) 

### 6. 모델 성능 평가

[**Monitoring tools for PyTorch**](https://www.notion.so/Monitoring-tools-for-PyTorch-f9c8625b26ab4dd0aa4d122d4deaac44?pvs=21)

### 7. 추론

- [AutoGrad 튜토리얼](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
- [Tensor와 AutoGrad 튜토리얼](https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_autograd.html)
- [Pytorch로 Linear Regression하기](https://towardsdatascience.com/linear-regression-with-pytorch-eb6dedead817)
- [Pytorch로 Logistic Regression하기](https://medium.com/dair-ai/implementing-a-logistic-regression-model-from-scratch-with-pytorch-24ea062cd856)
- 한 epoch에서 이뤄지는 모델 학습 과정을 정리해보고 성능을 올리기 위해서 어떤 부분을 먼저 고려하면 좋을지 논의해보기
    1. 데이터 개선
    2. 모델 개선
    3. loss 개선
    4. optimizer 개선

[DL 모델 구현 예제](https://www.notion.so/DL-9c7cebfa869b40e0a88d48c071604065?pvs=21)

[**PyTorch Troubleshooting**](https://www.notion.so/PyTorch-Troubleshooting-c45a703ff84e453b87c31bba2311a578?pvs=21)