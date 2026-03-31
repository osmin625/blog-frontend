import os
import re
import shutil
import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def process_markdown(content: str, filename: str) -> str:
    """
    Replaces Obsidian wikilinks with standard markdown links and ensures frontmatter exists.
    """
    # 1. Replace image wikilinks ![[image.png]] or ![[image.png|alias]]
    # to ![image.png](/images/image.png)
    def img_replacer(match):
        inner = match.group(1).split('|')[0]
        return f"![{inner}](/images/{inner})"
    content = re.sub(r'!\[\[(.*?)\]\]', img_replacer, content)

    # 2. Replace regular wikilinks [[Page Name]] or [[Page Name|Alias]]
    # to [Alias](Page_Name.md)
    def link_replacer(match):
        inner = match.group(1)
        if '|' in inner:
            page, alias = inner.split('|', 1)
        else:
            page, alias = inner, inner
        
        # Standardize page name to valid markdown filename
        link = page.replace(' ', '_') + ".md"
        return f"[{alias}]({link})"
        
    content = re.sub(r'\[\[(.*?)\]\]', link_replacer, content)
    
    # Ensure YAML frontmatter exists
    if not content.strip().startswith('---'):
        from datetime import datetime
        title = filename.replace('.md', '').replace('_', ' ')
        date_str = datetime.now().strftime('%Y-%m-%d')
        frontmatter = f"---\ntitle: \"{title}\"\ndate: {date_str}\ndraft: false\n---\n\n"
        content = frontmatter + content

    return content

def main():
    parser = argparse.ArgumentParser(description="Preprocess Obsidian markdown to Hugo")
    parser.add_argument("--src-dir", default="source_knowledge_base", help="Source directory containing Obsidian markdown")
    parser.add_argument("--dest-dir", default="frontend/content/posts", help="Destination directory for Hugo markdown")
    parser.add_argument("--assets-src", default="source_knowledge_base/images", help="Source directory for Obsidian assets")
    parser.add_argument("--assets-dest", default="frontend/static/images", help="Destination directory for Hugo static assets")
    args = parser.parse_args()

    src_dir = Path(args.src_dir)
    dest_dir = Path(args.dest_dir)
    assets_src = Path(args.assets_src)
    assets_dest = Path(args.assets_dest)

    # Copy and process Markdown files
    if src_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
        for filepath in src_dir.rglob('*.md'):
            try:
                content = filepath.read_text(encoding='utf-8')
                new_content = process_markdown(content, filepath.name)
                
                # Copy to destination, preserving name or converting spaces to underscores
                filename = filepath.name.replace(' ', '_')
                dest_path = dest_dir / filename
                dest_path.write_text(new_content, encoding='utf-8')
                logging.info(f"Processed {filepath.name} -> {dest_path}")
            except Exception as e:
                logging.error(f"Error processing {filepath}: {e}")
    else:
        logging.warning(f"Source directory '{src_dir}' does not exist. Skipping markdown processing.")

    # Copy assets
    if assets_src.exists():
        assets_dest.mkdir(parents=True, exist_ok=True)
        for filepath in assets_src.rglob('*'):
            if filepath.is_file():
                dest_path = assets_dest / filepath.name
                shutil.copy2(filepath, dest_path)
                logging.info(f"Copied asset {filepath.name} -> {dest_path}")
    else:
        logging.warning(f"Assets source directory '{assets_src}' does not exist. Skipping asset copying.")

if __name__ == "__main__":
    main()
