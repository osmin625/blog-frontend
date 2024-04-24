from os import path, listdir
import logging

logging.basicConfig(filename="category_gen.log", encoding='utf-8', level=logging.INFO)

contentPath = '\\Users\\Ohseungmin\\workspace\\blog\\frontend\\content\\posts'
hugoDataPath = '\\Users\\Ohseungmin\\workspace\\blog\\frontend\\data'
categoryFile = path.join(hugoDataPath, 'category_hierarchy.yaml')


def getCategories(path_):
    mdList = [mdFile for mdFile in listdir(path_) if mdFile.endswith('.md')]
    for file in mdList:
        categories = []
        with open(path.join(path_,file), encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith('categories:'):
                    _, values = line.split(':')
                    values = values.lstrip().rstrip('\n')
                    categories.extend(values[1:-1].split(','))
        if categories:
            for i in range(2):
                categories[i] = categories[i].strip().strip("\'")
            lines = []
            firstCategory = f'{categories[0]}:\n'
            secondCategory = f'- {categories[1]}\n'
            with open(categoryFile, 'r', encoding='utf-8') as f:
                lines.extend(f.readlines())
                if firstCategory in lines:
                    if secondCategory not in lines:
                        lines.insert(lines.index(firstCategory) + 1,secondCategory)
                        logging.info(f'[H2 Category] {categories[1]} Generated.')
                else:
                    lines.append(firstCategory)
                    lines.append(secondCategory)
                    logging.info(f'[H1 Category] {categories[0]} Generated.')
                    logging.info(f'[H2 Category] {categories[1]} Generated.')
            with open(categoryFile, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line)

    
if __name__ == '__main__':
    getCategories(contentPath)

