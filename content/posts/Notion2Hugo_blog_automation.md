---
title: Notion2Hugo blog 자동화
date: 2024-03-18T05:59:00+09:00
categories: [Code, Review]
tags: [Github Blog, Hugo, Latex, Notion]
type: post
---
나는 노션을 꽤 오래 전부터 사용해왔다.

공부하며 노션에 기록하는 것이 습관화되어 있는데, 이렇게 정리해 둔 게시글만 500개가 넘는다.

애초부터 노션에 정리해 둔 글을 보다 쉽게 블로그에 업로드하고자 호환성이 좋은 깃허브 블로그를 사용하고 있으나, 학습 내용을 기록하는 공간이 두 개로 구분되었을 때 둘 모두를 관리하는 건 생각보다 쉽지 않다는 것을 깨달았다.

아무튼, 이번에는 Hugo 블로그에 Notion에서 작성한 게시글을 보다 쉽게 업로드하기 위해 자동화를 시도해보았다.

- 기존에는 post 작성을 끝낸 후 build하고 push하는 과정을 쉘 커맨드로 간편하게 구성해두었다.
    
    ```bash
    #!/bin/bash
    echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"
    
    # Build the project.
    hugo -t gokarna
    
    # Go To Public folder
    cd public
    # Add changes to git.
    git add .
    
    # Commit changes.
    msg="rebuilding site `date`"
    if [ $# -eq 1 ]
      then msg="$1"
    fi
    git commit -m "$msg"
    
    # Push source and build repos.
    git push origin main
    
    # Come Back up to the Project Root
    cd ..
    
    # blog 저장소 Commit & Push
    git add .
    
    msg="rebuilding site `date`"
    if [ $# -eq 1 ]
      then msg="$1"
    fi
    git commit -m "$msg"
    git push origin main
    ```
    

이조차도 번거로워 이제는 노션 게시글 압축 파일을 압축 풀고 페이지를 적절하게 수정하여 업로드하는 과정을 자동화하고자 한다.

…

처음에는 간단하게 구상했으나 동작을 구현할수록 점점 더 욕심이 생겨서 차라리 개선 사항에 대해 버저닝을 하더라도 먼저 업로드 하기로 결심했다.

## 구현 과정

나의 목표는 노션에서 `내보내기` 버튼을 클릭한 후, 이외의 모든 작업을 딸깍 한 번으로 자동화하는 것이었다.

이를 자동화하기 위해서는 다음과 같은 작업들을 코드로 수행해야 한다.

1. download 폴더에 저장된 노션 페이지 압축 파일을 압축 해제하기
2. 파일 명과 이미지 파일의 이름을 수정하기
3. frontmatter 추가하기
4. latex 문법 수정하기
5. notion image 링크 블로그 디렉토리에 알맞게 갱신하기
6. 처리된 파일들을 블로그의 각 디렉토리에 적절히 이동시키기.

대략 나열했는데 노션과 깃허브 블로그를 함께 운영해본 사람이라면 공감할 반복 작업들이다.

위의 작업 단위를 그대로 함수로 구현했다.

## 코드

### 1. 노션 압축 파일 목록 생성하기

```python
def getZipList(downloadPath):
    dwPathFiles = listdir(downloadPath)
    zips_ = []

    for f in dwPathFiles:
        filePath = path.join(downloadPath,f)
        fname, ext = path.splitext(f)
        if ext == '.zip' and 'Export' in fname:
            zips_.append(filePath)
    return zips_
```

코드에서 보이는 것처럼 노션에서 내보내기를 통해 저장하면 기본적으로 Export가 압축 파일 명에 포함된다는 사실을 이용했다.

따라서 현재 코드에서는 압축 파일 명을 바꾸거나 노션에서 해당 부분의 default 설정이 바뀌게 되는 경우 제대로 동작하지 않는다.

### 2. 압축 풀기

```python
def extractZip(path_ = downloadPath):
    if not path.isdir(sourcePath): 
        makedirs(sourcePath)
    for zf in getZipList(path_):
        with zipfile.ZipFile(zf, 'r') as zipRef:
            zipRef.extractall(sourcePath)
```

압축 풀기 함수에서 `getZipList` 함수를 호출한다.

키워드 파라미터로 download를 default로 설정해두었다.

### 3. 압축 푼 파일 이름, 다른 형식(ex. pdf) 파일 제거하기

```python
def organizeNotionExportFile(path_):
    for file in listdir(path_):
        fname, ext = path.splitext(file)
        if ext not in ['.md', '']:
            remove(path.join(path_, file))
            continue
        if not ext and fname + '.md' not in listdir(path_):
            shutil.rmtree(path.join(path_, fname))
            continue
        fname = ' '.join(fname.split()[:-1])
        new_file = fname + ext
        rename(path.join(path_,file), path.join(path_, new_file))
    return listdir(path_)
```

노션으로 내보내기를 수행해 본 사람은 알겠지만 파일 명에 default로 page id가 붙어있다.

그래서 파일명이 `Entropy(엔트로피) 8c9f84e2a61d4bedb289546cd9f2e782.md` 처럼 매우 지저분하기 때문에, 공백을 기준으로 구분하여 이 부분을 제거해주었다.

이외에도 pdf 파일이나 html 파일로 잘못 내보내기가 된 경우 (혹은 다른 목적으로 내보내기 한 압축 파일의 경우) 제외했다.

디렉토리를 제거하기 위해서는 `os.remove`가 아닌, `shutil`이라는 모듈의 `rmtree`를 활용해야 했다.

### 4. 파일명 기분 좋게(?) 수정하기

```python
def cleanFileNames(path_):
    pattern = re.compile(r'[^\w\d_]+')
    renameCount = 0
    for file in listdir(path_):
        fname, ext = path.splitext(file)
        fname = re.sub(pattern, '_', fname)
        if fname.endswith('_'):
            fname = fname.rstrip('_')
        rename(path.join(path_, file), path.join(path_, fname + ext))
        renameCount += 1
    logging.info(f'[{renameCount} files name successfully changed]')
    return renameCount
```

파일명에서 page id를 제거했지만, 여전히 띄어쓰기, 대괄호 등이 파일명에 존재하기 때문에 파일명으로는 불안하다.

사실 위의 함수에서 한 번에 처리할까 고민하다가 따로 구분했다.

안정감을 위해 공백과 괄호를 언더바로 바꾸고, 파일 끝에 오는 언더바는 또 마음이 불편하니 제거해주었다.

### 5. 이미지 파일 이름 수정하기

```python
def updateImageFileName(path_):
    def _updateImageFileName(path_, folder_name):
        path_ = path.join(path_, folder_name)
        for i, img in enumerate(listdir(path_)):
            rename(path.join(path_, img), path.join(path_, folder_name + str(i) + '.png'))
        logging.info(f'[{i+1} Images Name Changed] {img} -> {folder_name + '.png'}')
    
    for file in listdir(path_):
        if path.isdir(path.join(path_, file)):
            _updateImageFileName(path_, file)
```

노션 페이지에 포함된 이미지 파일들은 따로 폴더에 저장되는데, 모두 Untitled라는 성의없는 이름으로 저장된다.

이는 나중에 페이지 내에서 해당 이미지를 링크할 때에도 불편해지기 때문에 이미지 파일명을 예뻐진 파일명으로 갱신해주는 작업이다.

코드 가독성을 위해 핵심 기능은 중첩 함수로 따로 구분했다.

logging 모듈을 이용하여 동작 과정에서의 이슈를 추적하도록 구성했다.

### 6. 페이지 내부 작업

- **md 파일 내의 이미지 경로를 수정하기 위한 image 파일 경로 기록**
    
    ```python
    if path.isdir(path.join(path_,fname)):
        imgList = [imgFile for imgFile in listdir(path.join(path_,fname))]
        imgIdx = 0
    ```
    
- **이미지 경로 갱신하기**
    
    ```python
    elif '![Untitled](' in line:
        indent_ = line.split('![Untitled]')[0]
        line = f'{indent_}![{fname}](/imgs/{imgList[imgIdx]})\n'
        imgIdx += 1
    ```
    
    파일 명이 길어지는 경우 해당 부분에서 예외 케이스가 발생하는 것을 확인했다.
    
    처음에는 re 문법으로 `![~~](~~)` 형태를 탐색하여 해당 문자열을 재구성했었다.
    
    하지만 `![~~](~~(~~~)~)` 처럼 소괄호가 중첩으로 발생하는 경우가 있어 위의 방식으로 간단하게 구현했다.
    
- **블로그 포스팅 md 파일에 필요한 Frontmatter을 추가하는 동작**
    
    ```python
    if f.isfirstline():
        title = line.lstrip('#')
        titleParam = 'title:' + title
        print('---')
        line = titleParam
    if not FrontMatterClosed:
        if line == '\n':
            continue
        elif f.lineno() > 2 and ':' not in line:
            FrontMatterClosed = True
            print('type: post')
            print('---')
            for p in paramCheck:
                if not paramCheck[p]:
                    logging.warning(f'[{file}] The [{p}] parameter does not exist in the frontmatter of the post.')
        
        # 노션 DB에 존재하는 column들
        elif line.startswith(('마지막 학습일:', 'status:', '갱신:', 
                              'summary:', '생성일:', '생성일0:', 
                              '하위 항목:', '상위 항목:', '이웃 항목:')):
            continue
    
        # 나는 편의를 위해 노션 DB에 categories, tags column을 만들어두었다.
        elif line.startswith(('categories:', 'tags:')):
            param, values = line.split(':')
            values = values.lstrip().rstrip('\n')
            line = f'{param}: [{values}]\n'
    ```
    
    노션 페이지를 내보내기하면 페이지 속성이 `attr:value` 형식으로 md 파일 상단에 적히게 되는데, 해당 값을 재활용하여 Frontmatter로 작성한다.
    
    즉, 나는 편의를 위해 노션 페이지에 date, categories, tags 등의 속성을 추가해두었다.
    
    Frontmatter에서의 이슈는 Frontmatter를 언제 닫아야 할 지 결정하는 것이었다.
    
    단순히 시작 이후 공백 발생 시 Frontmatter를 닫도록 했더니 예외 케이스가 발생하여 결국 
    
    `elif f.lineno() > 2 and ':' not in line` , 즉 3 번째 줄 이상이고 :가 처음으로 포함되지 않을 때 Frontmatter을 닫도록 구성했다.
    
    닫기 전에 categories나 tags 등 노션 페이지에서 넘어오는 파라미터가 없는 경우에 대한 로깅을 추가했다.
    
- **latex 수식 오류 로그 발생시키기**
    
    ```python
    if '⁍' in line:
        logging.error(f'[{file}] {f.lineno()-2}th line latex syntax error occured.')
    ```
    
    가끔씩 latex 문법에서 오류가 발생하여 $⁍$ 기호로 변경되는 경우가 종종 있다.
    
    기호를 검색해보니 `Black Rightwards Bullet`이라고 부르던데, 이상하게도 수식 오류 발생 시 항상 해당 기호로 변경되기 때문에 조건문에서 활용한다.
    
    아마 유니코드와 관련된 문제가 아닐까 짐작된다. 굳이 찾아보진 않았다.
    
- **latex 수식 블로그 문법에 맞게 수정하기**
    
    ```python
    elif '$$' in line and len(line.lstrip()) <= 3: # 블럭 수식
        indent_ = line.split('$$')[0]
        if not insideOfLatexBlock:
            line = indent_ + '`$$\n'
            insideOfLatexBlock = True
        else:
            line = indent_ + '$$`\n'
            insideOfLatexBlock = False
    elif '$' in line and '`$' not in line and '$`' not in line: # 인라인 수식
        tokens = line.split('$')
        insideOfLatexInline = False
        while len(tokens) > 1: # token들이 하나의 문장으로 합쳐질 때까지 반복.
            right_, left_ = tokens.pop(), tokens.pop()
            if not insideOfLatexInline:
                tokens.append(f'{left_}$`{right_}')
                insideOfLatexInline = True
            else:
                tokens.append(f'{left_}`${right_}')
                insideOfLatexInline = False
        line = tokens.pop()
    ```
    
    사실 이 부분은 내 블로그에 한정된 이야기인데, 나는 블로그의 latex 문법 변환 과정을 최적화하기 위해 latex 수식을 코드 블럭으로 감싼다.
    
    굳이 설명을 하자면 블럭 수식의 경우
    
    ```latex
    $$
    H(X)=\sum_{i=1}^n p_i\left(\log \frac{1}{p_i}\right)=-\sum_{i=1}^n p_i \log p_i
    $$
    ```
    
    이렇게 생겼고, 인라인 수식의 경우 
    
    ```latex
    왈왈공자왈$(p_i)$왈아무말왈$(-\log_2(p_i))$말말말
    ```
    
    이렇게 생겼다.
    
    블럭 수식의 경우 latex 식별 기호가 줄바꿈이 반드시 따라온다는 점을 이용해 기호 포함 여부와 문장 길이로 구분했다.
    
    기호 포함 여부만 활용하는 경우 인라인 수식 두 개가 연달아 적히는 경우 블럭 수식으로 인식해버리기 때문에 길이에 대한 조건이 추가로 필요하다.
    
    인라인 수식의 경우 구분자를 기준으로 split한 다음, 하나씩 새로운 구분자로 이어붙이는 코드를 구현했다.
    
    최종적으로 모든 토큰이 하나의 문장으로 이어지면 동작이 종료하도록 구현했다.
    

사실 생각한 것보다 해당 함수가 너무 묵직해져서 작은 작업 단위로 구분하기 위해 호시탐탐 노려보고 있다.

다만 함수 내에서 파일 포인터를 활용하고 있어 이 부분을 함수로 빼냈을 때 어떻게 동작할 지 알아보기 위해 일단 보류해두었다.

해당 부분을 학습한 이후 포스팅을 할까 고민도 했으나, 포스팅이 또 밀릴 것 같아 차후에 따로 업데이트된 코드를 업로드하기로 했다.

최근에 밥 아저씨의 클린 코드 책을 감명 깊게 읽어 주석을 최소화하자는 생각을 가지고 있으나, 아직은 코드의 깔끔함이 그 정도는 아니라고 생각해 변명을 적는 마음으로 코드에 주석을 달았다.

특히 인라인 latex를 처리하는 구문은 코드 직관성이 매우 떨어진다고 생각한다. 조금 더 고민할 필요가 있다.

### 7. 파일 이동시키기

```python
def move_md_(fname, path_, src_path = sourcePath):
    src = path.join(src_path, fname)
    dest = path.join(path_, fname)
    rename(src, dest)

def fileDistribute(path_):
    fname_md, fname_dir = set(), set()
    def _fileDistribute(path_):
        for file in listdir(path_):
            fname, ext = path.splitext(file)
            if ext == '.md':
                fname_md.add(fname)
                move_md_(file, contentPath)
            elif ext == '.png':
                move_md_(file, imgPath, path_)
            elif ext == '':
                fname_dir.add(fname)
            else:
                remove(path.join(path_, file))
    _fileDistribute(path_)
    

    mdImgDir = fname_dir & fname_md

    for fname_md in mdImgDir:
        _fileDistribute(path.join(path_, fname_md))

    shutil.rmtree(sourcePath)
```

마찬가지로 코드의 중복을 최소화하기 위해 중첩 함수 구조를 활용했다.

실제 스크립트에서는 파라미터를 통해 distribute 동작이 실행되기 전에 draft 폴더에서 업로드 할 파일들을 한 눈에 볼 수 있도록 구성했다.

### 전체 코드

결론적으로 전체 코드는 다음과 같다.

```python
from os import path, listdir, makedirs, rename, remove, getenv
import zipfile
import shutil
import fileinput
import re
import logging
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-a', help=' : Running whole functions include fileDistribute when executing the script.', default=False)
parser.add_argument('-d', help=' : Running the distribute function only.', default=False)
args = parser.parse_args()

logging.basicConfig(filename="post_upload.log", encoding='utf-8', level=logging.INFO)

userName = getenv('username')
downloadPath = path.join('\\Users',userName,'Downloads')
# 본인의 post 경로
contentPath = '\\Users\\Ohseungmin\\workspace\\blog\\frontend\\content\\posts'
# 본인의 image 저장 경로
imgPath = '\\Users\\Ohseungmin\\workspace\\blog\\frontend\\static\\imgs' 
currentPath = path.curdir
sourcePath = path.join(currentPath, 'draft_files')

def getZipList(downloadPath):
    dwPathFiles = listdir(downloadPath)
    zips_ = []

    for f in dwPathFiles:
        filePath = path.join(downloadPath,f)
        fname, ext = path.splitext(f)
        if ext == '.zip' and 'Export' in fname:
            zips_.append(filePath)
    return zips_

def extractZip(path_ = downloadPath):
    if not path.isdir(sourcePath): 
        makedirs(sourcePath)
    for zf in getZipList(path_):
        with zipfile.ZipFile(zf, 'r') as zipRef:
            zipRef.extractall(sourcePath)

def move_md_(fname, path_, src_path = sourcePath):
    src = path.join(src_path, fname)
    dest = path.join(path_, fname)
    rename(src, dest)

def fileDistribute(path_):
    fname_md, fname_dir = set(), set()
    def _fileDistribute(path_):
        for file in listdir(path_):
            fname, ext = path.splitext(file)
            if ext == '.md':
                fname_md.add(fname)
                move_md_(file, contentPath)
            elif ext == '.png':
                move_md_(file, imgPath, path_)
            elif ext == '':
                fname_dir.add(fname)
            else:
                remove(path.join(path_, file))
    _fileDistribute(path_)
    

    mdImgDir = fname_dir & fname_md

    for fname_md in mdImgDir:
        _fileDistribute(path.join(path_, fname_md))

    shutil.rmtree(sourcePath)

def organizeNotionExportFile(path_):
    for file in listdir(path_):
        fname, ext = path.splitext(file)
        if ext not in ['.md', '']:
            remove(path.join(path_, file))
            continue
        if not ext and fname + '.md' not in listdir(path_):
            shutil.rmtree(path.join(path_, fname))
            continue
        fname = ' '.join(fname.split()[:-1])
        new_file = fname + ext
        rename(path.join(path_,file), path.join(path_, new_file))
    return listdir(path_)

def updateImageFileName(path_):
    def _updateImageFileName(path_, folder_name):
        path_ = path.join(path_, folder_name)
        for i, img in enumerate(listdir(path_)):
            rename(path.join(path_, img), path.join(path_, folder_name + str(i) + '.png'))
        logging.info(f'[{i+1} Images Name Changed] {img} -> {folder_name + '.png'}')
    
    for file in listdir(path_):
        if path.isdir(path.join(path_, file)):
            _updateImageFileName(path_, file)

def cleanFileNames(path_):
    pattern = re.compile(r'[^\w\d_]+')
    renameCount = 0
    for file in listdir(path_):
        fname, ext = path.splitext(file)
        fname = re.sub(pattern, '_', fname)
        if fname.endswith('_'):
            fname = fname.rstrip('_')
        rename(path.join(path_, file), path.join(path_, fname + ext))
        renameCount += 1
    logging.info(f'[{renameCount} files name successfully changed]')
    return renameCount

def updatePostContent(path_):
    mdList = [mdFile for mdFile in listdir(path_) if mdFile.endswith('.md')]

    for file in mdList:
        fname, _ = path.splitext(file)
        
        if path.isdir(path.join(path_,fname)):
            imgList = [imgFile for imgFile in listdir(path.join(path_,fname))]
            print(imgList)
            imgIdx = 0
        
        FrontMatterClosed = False
        with fileinput.FileInput(path.join(path_,file),inplace=True, encoding='utf-8') as f:
            insideOfLatexBlock = False
            paramCheck = {'categories':False, 'tags':False}
            for line in f:
                # frontmatter 생성
                if f.isfirstline():
                    title = line.lstrip('#')
                    titleParam = 'title:' + title
                    print('---')
                    line = titleParam
                if not FrontMatterClosed:
                    if line == '\n':
                        continue
                    elif f.lineno() > 2 and ':' not in line:
                        FrontMatterClosed = True
                        print('type: post')
                        print('---')
                        for p in paramCheck:
                            if not paramCheck[p]:
                                logging.warning(f'[{file}] The [{p}] parameter does not exist in the frontmatter of the post.')
                    
                    # 노션 DB에 존재하는 column들
                    elif line.startswith(('마지막 학습일:', 'status:', '갱신:', 
                                          'summary:', '생성일:', '생성일0:', 
                                          '하위 항목:', '상위 항목:', '이웃 항목:')):
                        continue

                    # 나는 편의를 위해 노션 DB에 categories, tags column을 만들어두었다.
                    elif line.startswith(('categories:', 'tags:')):
                        param, values = line.split(':')
                        values = values.lstrip().rstrip('\n')
                        line = f'{param}: [{values}]\n'
                
                # 수식 오류 발생 시 로깅하기
                if '⁍' in line:
                    logging.error(f'[{file}] {f.lineno()-2}th line latex syntax error occured.')
                
                # image path 재설정하기
                elif '![Untitled](' in line:
                    indent_ = line.split('![Untitled]')[0]
                    line = f'{indent_}![{fname}](/imgs/{imgList[imgIdx]})\n'
                    imgIdx += 1
                
                # hugo에서 latex 인식 가능하도록 latex 구문 변경하기
                # 들여쓰기때문에 line 길이로 인식하면 안됨.
                elif '$$' in line and len(line.lstrip()) <= 3: # 블럭 수식
                    indent_ = line.split('$$')[0]
                    if not insideOfLatexBlock:
                        line = indent_ + '`$$\n'
                        insideOfLatexBlock = True
                    else:
                        line = indent_ + '$$`\n'
                        insideOfLatexBlock = False
                
                # 수식이 끝나자마자 시작하는 경우 때문에 `$$`가 없다를 예외 조건으로 추가하면 안됨.
                elif '$' in line and '`$' not in line and '$`' not in line: # 인라인 수식
                    tokens = line.split('$')
                    insideOfLatexInline = False
                    while len(tokens) > 1: # token들이 하나의 문장으로 합쳐질 때까지 반복.
                        right_, left_ = tokens.pop(), tokens.pop()
                        if not insideOfLatexInline:
                            tokens.append(f'{left_}$`{right_}')
                            insideOfLatexInline = True
                        else:
                            tokens.append(f'{left_}`${right_}')
                            insideOfLatexInline = False
                    line = tokens.pop()
                print(line, end='')

if __name__ == '__main__':
    if args.a or not args.d:
        extractZip(downloadPath)
        organizeNotionExportFile(sourcePath)
        cleanFileNames(sourcePath)
        updateImageFileName(sourcePath)
        updatePostContent(sourcePath)
    if args.a or args.d:
        fileDistribute(sourcePath)

```

사용 방법은 다음과 같다.

### 사용 방법

1. 블로그로 옮기고자 하는 노션 페이지에서 우측 상단의  `$\cdots$`을 누른다.
    
    ![자동화](/imgs/Notion2Hugo_blog_자동화0.png)
    
2. 내보내기를 누르고, 아래 이미지처럼 설정한 후 내보내기 버튼을 클릭한다.
    
    ![자동화](/imgs/Notion2Hugo_blog_자동화1.png)
    
3. default로 download 폴더에 저장되기 때문에, 경로나 파일명을 변경할 필요 없이 그대로 저장한다.
4. post_upload코드를 동작시킨다.
5. 다운로드 폴더의 압축 파일을 정리한다.

---

### 남은 할 일

- 파일 이동시키기 예외 처리 — 기존에 동일한 이름의 포스팅이 존재하는 경우
- updatePostContent 함수 기능 단위로 구분하기
- 다양한 예외 처리하기

### 글을 마무리하며

나는 사실 단축키를 정말 좋아하고, 단순 반복 작업을 싫어하기 때문에 이때까지 이런 작업을 종종 했다. 이런 작업들은 취미에 가깝다고 생각하여 굳이 정리해두진 않았다만…

노션 자동화의 경우 나름 필요한 사람이 꽤 있을 것 같아 블로그에 업로드한다.

나는 사실 이 글 또한 자동화 코드로 올릴 예정이었는데, 동작 코드 자체를 설명하다 보니 예외적인 latex 수식이 너무 많아 제대로 동작할 것이라는 자신이 없다. 그래도 시도해보겠다.

일단 임시로 첫 버전을 업로드했다. 다음 번에는 기능도 추가하고, 코드도 다듬은 다음 버저닝 방법을 좀 더 공부하여 새롭게 공유하겠다.