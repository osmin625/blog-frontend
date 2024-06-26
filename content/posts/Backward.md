---
title: PyTorch의 Backward에 대해 알아보자.
date: 2023-03-13T22:13:00+09:00
categories: [Framework & Library, PyTorch]
tags: [PyTorch, Backward, Autograd]
type: post
---

> ✔️ 간단 요약  
> `forward`함수를 정의하면 자동으로 정의된다.  
> **동작 과정**  
> 1. tensor(loss에 해당)가 포함된 식을 미분한다.  
> 2. 미분 값을 tensor에 저장한다.  

> Autograd, loss, optimizer, nn.Module  

1. **tensor(loss에 해당)가 포함된 식을 미분한다.**
    
    Tensor 객체의 backward 함수에는 default로 Autograd 설정이 되어 있기 때문에, 미분 수식을 따로 작성하지 않아도 자동으로 미분이 가능하다.
    
    **기본 예제**
    
    ```python
    w = torch.tensor(2.0, requires_grad=True)
    y = w**2
    z = 10*y + 25
    z.backward()
    w.grad()
    # output : tensor(40.)
    ```
    
    `$$
    w = 2\\
    y = w^2\\
    z = 10\times y  + 25\\
    z = 10 \times w^2 + 25\\
    {dz\over dw} = 20 \times w = 40
    $$`
    
    **미분 값이 여러 개인 경우**
    
    ```python
    a = torch.tensor([2.,3.], requires_grad=True)
    b = torch.tensor([6.,4.], requires_grad=True)
    Q = 3 * a ** 3 - b ** 2
    # 미분값이 두 개가 나와야하기 때문에, 
    # gradient 값의 크기를 잡아준다.
    external_grad = torch.tensor([1., 1.])
    Q.backward(gradient=external_grad)
    
    a.grad
    b.grad
    # output: tensor([36.,81.])
    # output: tensor([-12.,-8.])
    ```
    
    `$$
    \begin{aligned}
    &Q = 3a^3 - b^2\\
    & \frac{\partial Q}{\partial a}=9 a^2 \\
    & \frac{\partial Q}{\partial b}=-2 b
    \end{aligned}
    $$`
    
2. **미분 값을 tensor에 저장한다.**
    
    tensor를 선언할 때 require_grad=True로 설정하면 tensor에 grad_fn 정보가 저장된다.
    
    e.g. `tensor(6.2564e-05, grad_fn=<MseLossBackward0>)`
    
    또한, `tensor.grad()`를 통해 미분 값을 확인할 수 있다.
    
    grad_fn에는 텐서가 어떤 연산을 했는 연산 정보를 담고 있고, 이 정보는 역전파에 사용된다.
    

[PyTorch Gradient 관련 설명 (Autograd)](https://gaussian37.github.io/dl-pytorch-gradient/)

실제 backward는 Module 단계에서 직접 지정이 가능하다.

Module에서 backward와 optimizer를 오버라이딩 해주면 된다.

사용자가 직접 미분 수식을 써야 하는 부담이 있다.

쓸 일은 없지만, 순서를 이해할 필요는 있다.

### 예제 — Logistic Regression

```python
class LR(nn.Module):
	def init (self, dim, lr=torch.scalar_tensor(0.01)):
		super(LR, self). init () 
		# intialize parameters
		self.w = torch.zeros(dim, 1, dtype=torch.float).to(device)
		self.b = torch.scalar_tensor(0).to(device)
		self.grads = {"dw": torch.zeros(dim, 1, dtype=torch.float).to(device), 
					  "db": torch.scalar_tensor(0).to(device)}
		self.lr = lr.to(device)
```

`$$
h_\theta(x)=\frac{1}{1+e^{-\theta^T \mathbf{x}}}
$$`

```python

def forward(self, x): 
	## compute forward
	z = torch.mm(self.w.T, x) 
	a = self.sigmoid(z) 
	return a

def sigmoid(self, z):
	return 1/ (1 + torch.exp(-z))
```

```python

def backward(self, x, yhat, y): 
	## compute backward
	self.grads["dw"] = (1/x.shape[1]) * torch.mm(x, (yhat - y).T) 
	self.grads["db"] = (1/x.shape[1]) * torch.sum(yhat - y)

```

`$$
\begin{aligned}&\frac{\partial}{\partial \theta_j} J(\theta)=\frac{1}{m} \sum_{i=1}^m\left(h_\theta\left(x^i\right)-y^i\right) x_j^i\end{aligned}
$$`

```python

def optimize(self):
	## optimization step
	self.w = self.w - self.lr * self.grads["dw"]
	self.b = self.b - self.lr * self.grads["db"]
```

기존의 `$\theta$`, 즉, `$\tt w$` 값에 미분값 만큼의 업데이트를 수행해주는 함수. 

`$$
\begin{aligned}\theta_j & :=\theta_j-\alpha \frac{\partial}{\partial \theta_j} J(\theta) \\& :=\theta_j-\alpha \sum_{i=1}^m\left(h_\theta\left(x^i\right)-y^i\right) x_j^i\end{aligned}
$$`

- 전체 코드
    
    ```python
    class LR(nn.Module):
		def init (self, dim, lr=torch.scalar_tensor(0.01)):
			super(LR, self). init () 
			# intialize parameters
			self.w = torch.zeros(dim, 1, dtype=torch.float).to(device)
			self.b = torch.scalar_tensor(0).to(device)
			self.grads = {"dw": torch.zeros(dim, 1, dtype=torch.float).to(device), 
						  "db": torch.scalar_tensor(0).to(device)}
			self.lr = lr.to(device)

		def forward(self, x): 
			## compute forward
			z = torch.mm(self.w.T, x) 
			a = self.sigmoid(z) 
			return a
		
		def sigmoid(self, z):
			return 1/ (1 + torch.exp(-z))

		def backward(self, x, yhat, y): 
			## compute backward
			self.grads["dw"] = (1/x.shape[1]) * torch.mm(x, (yhat - y).T) 
			self.grads["db"] = (1/x.shape[1]) * torch.sum(yhat - y)

		def optimize(self):
			## optimization step
			self.w = self.w - self.lr * self.grads["dw"]
			self.b = self.b - self.lr * self.grads["db"]
    ```