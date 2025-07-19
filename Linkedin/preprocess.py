import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_file, process_file="data/processed_posts.json"):
    enriched_posts = []

    with open(raw_file, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            try:
                metadata = extract(post['text'])
                post_meta = post | metadata  # Merge dictionaries
                enriched_posts.append(post_meta)
            except Exception as e:
                print(f"Error processing post: {e}")

    # Save enriched data
    with open(process_file, 'w', encoding='utf-8') as f:
        json.dump(enriched_posts, f, indent=2, ensure_ascii=False)




def extract(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post, and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language, and tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means Hindi + English)

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    json_parser = JsonOutputParser()

    chain = pt | llm | json_parser

    try:
        result = chain.invoke({"post": post})
        return result
    except OutputParserException as e:
        print("Output parsing error:", e)
        # Optional fallback
        return {
            "line_count": post.count("\n") + 1,
            "language": "Unknown",
            "tags": []
        }


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
