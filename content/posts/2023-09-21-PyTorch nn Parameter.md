---
title: PyTorch에서 weight를 저장하는 객체 - nn.Parameter
date: 2023-03-13-22:09:00 +0900
categories: [DL Framework, PyTorch]
tags: [PyTorch, Parameter, weight]
math: true
# img_path: /assets/post_imgs/
# image:lqip: image_filename
---
> 간단 요약  
> **학습의 대상이 되는 Weight를 정의한다.**  
> Tensor 객체의 상속 객체
{: .prompt-info }

Tensor 객체와 매우 비슷하다.

**nn.Module의 attribute가 될 때는 `required_grad = True`로 자동으로 지정되어 AutoGrad의 대상이 된다.**

대부분의 Layer에는 weights 값들이 지정되어 있기 때문에, 직접 지정할 일은 드물다. 그래도 직접 지정하는 법을 알아보자.

nn.Module로 만든 $\tt xw +b$라는 선형 모델을 살펴본다.

### $\tt xw +b$

```python
class MyLinear(nn.Module):
		def __init__ (self, in_features, out_features, bias=True):
				super(). init ()
				**self.in_features = in_features
				self.out_features = out_features**
				**self.weights = nn.Parameter(torch.randn(in_features, out_features))
				self.bias = nn.Parameter(torch.randn(out_features))**

		def forward(self, x : Tensor):
				return x @ self.weights + self.bias
				# xw + b의 형태로 output이 나온다.
```

**ex —  Feature가 7개 있고, 배치가 3인 경우**

데이터는 $3 \times 7$의 형태가 된다.

1. 7개의 feature를 넣어서
    
    `in_features = 7`
    
2. 5개의 클래스 중 하나로 예측하고자 한다면
    
    `out_features = 5`
    
3. $7 \times 5$ 형태의 weight 값이 필요하다.
    
    `nn.Parameter(torch.randn(7, 5)`
    
4. 이후,  bias 값도 선언해준다.
    
    `nn.Parameter(torch.randn(5))`
    
5. 이후, `forward`에서 $\tt xw +b$을 return해준다.
    
    `def forward(self, x : Tensor):
         return x @ self.weights + self.bias`
    
    즉, 모델의 예측 값($\hat y$)을 뱉어낸다.
    

이후, `backward()`에서 실제 값과 예측 값의 차이(loss)에 대해 미분을 수행한다.