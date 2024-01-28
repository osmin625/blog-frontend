---
title: PyTorch 모델 정의하기 - nn.Module
date: 2023-03-13T22:09:00+09:00
categories: [DL Framework, PyTorch]
tags: [PyTorch, Module]
type: post
---

> **간단 요약**  
> 반복되는 Layer을 만들기 위한 Torch의 가장 기본적인 신경망 모듈  
> 매개변수를 캡슐화하는 간편한 방법  
> GPU로 이동, 내보내기(exporting), 불러오기(loading) 등의 작업을 위한 헬퍼(helper)를 제공한다.  
{: .prompt-info }

DL 모델은 모두 Layer의 반복이며, 블록 반복의 연속이다.

Module에서 정의하는 것

- **Input**
- **Output**
- **Forward**
- (Backward)
    
    이 때, Backward는 자동 미분이 되기 때문에, 해당되는 weight의 값들을 내보내준다.
    
    즉, weight가 학습의 대상이 되고, 이를 parameter(tensor)로 정의한다.
    
    일반적으로는 직접 지정해줄 필요가 없다.
    

### example

```python
import torch
from torch.autograd import Variable

class LinearRegression(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super(LinearRegression, self).__init__()
        # pytorch에서 제공하는 xw + b 모듈
        self.linear = torch.nn.Linear(inputSize, outputSize)
		

    def forward(self, x):
        out = self.linear(x)
        return out
```

![module](module.png)