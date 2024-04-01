---
title: Hugo Blog category 404 해결 방법
date: 2024-01-31T07:50:00+09:00
categories: [Review, Troubleshooting]
tags: [Github Blog, Hugo]
type: post
---
Hugo 블로그를 사용하며 분명이 업로드한 포스팅이 보이지 않는 경우가 가끔 발생한다.

나는 이번에 블로그를 hugo로 이전하며 카테고리 페이지를 직접 구현했는데, 이 때 카테고리가 제대로 동작하지 않는 문제를 마주했다.

이는 카테고리 front matter에 대문자가 포함된 경우 hugo의 urlize의 동작이 jekyll의 urlize와 달라서 발생하는 문제로 보인다.

### category → 404 found

![hugo_blog_category_404_해결_방법](/imgs/hugo_blog_category_404_해결_방법1.png)

기존에 Jekyll에서는 front-matter에 categories로 대문자를 마음껏 사용했었는데, Hugo 블로그로 옮기고 나니 대문자가 인식이 되지 않는다.

### Hugo와 Jekyll의 urlize 차이점

- jekyll에서의 urlize — 대문자는 그대로 유지, 띄어쓰기는 ‘-’로 변경
    
    **`/DL-Algorithm/`** → 정상 동작
    
- hugo에서의 urlize — 대문자는 소문자로, 띄어쓰기는 ‘-’로 변경
    
    **`/dl-algorithm/`** ≠ `/DL-Algorithm/` → 인덱싱 오류 발생
    

### 공식 문서의 지침

공식 문서에서 `preserveTaxonomyNames = true` 옵션을 통해 카테고리의 대문자를 그대로 유지하면 된다고 말하지만… 문제는 또 발생한다.

- `preserveTaxonomyNames = true`옵션을 주면?
    
    **`/DL%20Algorithm/`** ≠ `/DL-Algorithm/` → 인덱싱 오류 발생
    

띄어쓰기가 유니코드 그대로 url에 삽입되기 때문에 여전히 page not found가 발생한다.

### **원하는 것**

url을 생성할 때 대문자만 유지하고, 띄어쓰기는 `-`로 변환하기

ex) [https://osmin625.github.io/categories/DL-Algorithm/](https://osmin625.github.io/categories/DL-Algorithm/)

### **해결 방안 — `disablePathToLower`**

config.toml에 `disablePathToLower = true` 추가하기.

참고로 Site의 Parameter이기 때문에 [Params] 내부가 아닌, 최상단에 추가해주어야 한다.

![hugo_blog_category_404_해결_방법](/imgs/hugo_blog_category_404_해결_방법0.png)

이제 제대로 뜨는 것을 확인할 수 있다.

### 참조

[Upper case urls](https://discourse.gohugo.io/t/upper-case-urls/1525)

[https://github.com/gohugoio/hugo/issues/557](https://github.com/gohugoio/hugo/issues/557)

[https://github.com/coderzh/hugo/commit/8575e5defa57e77771bb94d69e0b01f45b6833d2](https://github.com/coderzh/hugo/commit/8575e5defa57e77771bb94d69e0b01f45b6833d2)

[https://github.com/markotoplak/orange-hugo/commit/6d4fec3149790e6e427b96b488d4e5f93ba0e128](https://github.com/markotoplak/orange-hugo/commit/6d4fec3149790e6e427b96b488d4e5f93ba0e128)