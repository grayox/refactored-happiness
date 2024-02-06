TOPIC_TREE = {
  "Health & Fitness": {
    "Nutrition": {
      "Keto": {},
      "Paleo": {},
      "Intermittent Fasting": {},
      "Clean Eating": {},
      "Vegan": {},
    },
    "Weight Loss": {
      "Weight Loss for Women": {},
      "Weight Loss for Men": {},
    },
    "Aging & Anti-Aging": {},
    "Women's Health": {
      "Fertility": {},
      "Pregnancy": {},
      "Menopause": {},
    }
  },
  "Finance & Investing": {
    "Budgeting & Money Management": {
      "Getting Out of Debt": {},
      "Retirement Planning": {},
    },
    "Investing": {
      "Stocks": {},
      "Real Estate": {},
      "Cryptocurrency": {},
    }
  },
  "Home & Garden": {
    "Decorating on a Budget": {},
    "Landscaping & Outdoor Living": {
      "Backyard Ideas": {},
      "Gardening": {},
    },
    "Interior Design": {},
    "DIY Projects": {
      "Furniture Building": {},
      "Home Improvement": {},
    },
  },
  "Travel": {
    "Budget Travel": {
      "Backpacking": {},
      "Hostels": {},
      "Cheap Flights": {},
    },
    "Luxury Travel": {
      "Hotels": {},
      "Tours": {},
      "Cruises": {},
    },
    "Regional Travel": {
      "Europe": {},
      "Asia": {},
      "USA": {},
    },
  },
  "Entertainment": {
    "Sports": {},
    "Books": {},
    "Movies": {},
    "Television": {},
    "Social Media": {},
  },
  "Parenting & Family": {
    "Pregnancy": {
      "Fertility": {},
    },
    "Babies & Toddlers": {},
    "Child Development & Education": {},
    "Special Needs Children": {},
  },
  "Pets": {
    "Dogs": {},
    "Cats": {},
    "Fish & Aquariums": {},
    "Birds": {},
    "Exotic Pets": {},
    "Pet Health": {
      "Pet Nutrition": {},
      "Veterinary Advice": {},
    },
  },
  "Technology": {
    "Gadgets & Gear": {
      "Smart Home": {},
      "Drones": {},
      "Smart Phones": {},
    },
    "Apps & Software": {},
    "Artificial Intelligence": {},
    "Virtual Reality": {},
  },
  "Automotive": {
    "Car Reviews": {},
    "Auto Repair": {},
    "Customization & Accessories": {},
  },
  "Sports & Outdoors": {
    "Hiking & Camping": {},
    "Hunting & Fishing": {},
    "Extreme Sports": {},
  },
  "Arts & Crafts": {
    "Knitting & Crochet": {},
    "Scrapbooking": {},
    "DIY Crafts": {
      "Candles": {},
      "Jewelry Making": {},
      "Soaps": {},
    }
  },
  "Beauty & Fashion": {
    "Makeup & Cosmetics": {},
    "Skin & Anti-Aging": {},
    "Hair Care": {
      "Hairstyles": {},
      "Hair Loss": {},
    },
    "Plus-size Fashion": {}
  },
  "Food & Cooking": {
    "Recipes": {
      "Desserts": {},
      "Healthy Meals": {},
      "On a Budget": {},
      "Instant Pot": {},
      "Grilling": {},
      "Vegan": {},
      "Keto": {},
    },
    "Restaurants": {}
  },
  "Home Improvement": {
    "Plumbing": {},
    "Electrical": {},
    "HVAC": {},
    "Flooring": {},
    "Bathroom Remodel": {},
    "Kitchen Remodel": {},
    "Roofing": {},
    "Appliance Repair": {
        "Washing Machines & Dryers": {},
        "Dishwashers": {},
        "Refrigerators": {},
    },
  },
  "Education & Learning": {
    "Homeschooling": {},
    "Studying Tips": {
      "Memory": {},
      "Focus": {},
      "Accelerated Learning": {}
    },
    "Writing Help": {
      "Essay Writing": {},
      "Research Papers": {}
    }
  },
  "Lifestyle": {
    "Sustainability & Green Living": {
      "Zero Waste Home": {},
      "Tiny House Living": {},
      "Eco-Friendly Products": {},
    },
    "Minimalism": {
      "Organization": {},
      "Essentialism": {},
      "Living with Less": {},
    },
    "Self-Care & Wellness": {
      "Yoga": {},
      "Meditation": {},
      "Life Coaching": {},
      "Aromatherapy": {
        "Essential Oils": {},
      },
    },
    "Online Business": {
      "Affiliate Marketing": {},
      "Blogging for Profit": {},
      "Side Hustles": {},
    },
    "Art & Culture": {
      "Visual Arts": {
        "Painting": {},
        "Sculpture": {},
        "Photography": {},
      },
      "Performing Arts": {
        "Dance": {},
        "Theater": {},
        "Music": {},
      },
      "Literature": {
        "Fiction Writing": {},
        "Poetry": {},
      },
      "Film & Media": {
        "Movies": {},
        "Television": {},
        "Video Production": {},
      },
      "Culture": {
        "Art History": {},
        "Architecture": {},
      },
    },
  },
}

class Niche:
  def __init__(self, name):
    self.name = name
    self.details = None

def get_random_leaf(tree_node, key_path=None, current_key='',):

  if key_path is None:
    key_path = []

  # Leaf node
  # is_node_a_leaf = is_node_a_niche or is_node_empty_dict

  # case: niche
  is_node_a_niche = isinstance(tree_node, Niche)
  if is_node_a_niche:
    return (tree_node, key_path,)

  # case: {}
  is_dict_empty = not tree_node # assuming it's a dict, which is checked later
  is_node_a_dict = isinstance(tree_node, dict)
  is_node_empty_dict = is_node_a_dict and is_dict_empty
  if is_node_empty_dict:
    return (current_key, key_path,)

  # case: branch
  # continue traversing down branches with random key
  keys = list(tree_node.keys())
  key = random.choice(keys)
  key_path.append(key)
  next_node = tree_node[key]
  return get_random_leaf(tree_node=next_node, key_path=key_path, current_key=key,)

# test_get_random_leaf = get_random_leaf(TOPIC_TREE)
# print(test_get_random_leaf)

import os, requests, json, re, pathlib, textwrap, random, urllib.request
# import generation_types

from google.colab import userdata, files
import google.generativeai as genai

from time import sleep
from IPython.display import display
from IPython.display import Markdown

import praw
from praw.models import InlineGif, InlineImage, InlineVideo

import html2text

def get_pixabay_image_url_from_search(search_query,):
  """
  Gets the URL of an image from Pixabay that matches the given search query.

  Args:
    search_query: The search query to use when searching for images.

  Returns:
    The URL of an image from Pixabay that matches the given search query, or None
    if no images were found.
  """

  FALLBACK_SEARCH_TERM = 'smile'

  base_url = 'https://pixabay.com/api/'
  params = {
    'key': pixabay_api_key,
    'q': search_query,
    'image_type': 'photo',
    'per_page': 200,
    'editors_choice': True,
    'asset_type': 'image',
    'image_type': 'photo',
    'order': 'popular', # 'latest'
    'limit': 200,
    'safesearch': True,
    # 'category': category, # backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
  }

  image_url = False
  response = requests.get(base_url, params=params)

  # Check if the request was successful.
  if response.status_code == 200:
    data = response.json()
    print(data)

    # Check if the "hits" key is present in the response JSON.
    if 'hits' in data:
      # Get random image from results
      try:
        total_hits = data['totalHits']
        if(total_hits == 0):
          return False
        random_hit = random.randint(0, total_hits-1)
        # asset = data['hits'][0]
        asset = data['hits'][random_hit]
        image_url = asset['webformatURL']
      except IndexError:
        if 'hits' not in data or len(data['hits']) == 0:
          print(f"No hits for search query: {search_query}")
          search_query = FALLBACK_SEARCH_TERM # fallback search term
          return get_pixabay_image_url_from_search(search_query)
    else:
      print('No assets found.')
  else:
    print('Request failed with status code:', response.status_code)

  if not image_url:
    image_url = get_pixabay_image_url_from_search(FALLBACK_SEARCH_TERM)

  # Return the assets list.
  return image_url
# get_pixabay_image_url_from_search('flower')

from tenacity import *

MAX_RETRIES = 12
LLM_MODEL_NAME = 'gemini-pro'
WAIT_TIME_IN_SECONDS_BETWEEN_RETRIES = 3

# initialize google gemini
# https://colab.research.google.com/drive/1N3PQgaP9FtaFSMD7jZ0ymGpXlGWyhFmh#scrollTo=2bcfnGEviwTI
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model_name=LLM_MODEL_NAME)
# model

@retry(stop=stop_after_attempt(MAX_RETRIES), wait=wait_fixed(WAIT_TIME_IN_SECONDS_BETWEEN_RETRIES))
def get_completion(prompt):
  response = model.generate_content(prompt)
  # print(f'prompt: {prompt}')
  sleep(1)
  completion = response.text
  # print(f'completion: {completion}')
  return completion

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# def get_random_niche():
#   AFFILIATE_NICHE_CATEGORIES = [ "Health & Fitness", "Finance & Investing", "Home & Garden", "Travel", "Parenting & Family", "Self-Improvement", "Relationships", "Pets", "Arts & Crafts", "Beauty & Fashion", "Food & Cooking", "Technology", "Automotive", "Sports & Outdoors", "Education & Learning", "Home Improvement", "Weddings", "Photography", "Sustainability & Green Living", ]
#   random_niche = random.choice(AFFILIATE_NICHE_CATEGORIES)

# reddit to blog article
def get_blog_article_from_reddit_post(original_reddit_post, article_target_length_in_words,):
  reddit_to_blog_prompt = f"""
    You are an expert at blog writing and SEO optimization. You will be given a post from Reddit.
    The post will contain the original post and some top level comments in JSON format.
    Your task is to write a helpful blog article optimized for SEO using the Reddit post as the basis for the blog article.
    Your article should be {article_target_length_in_words} words in length.
    Format your article with the explicit use of <H1> and <H2> html tags.
    ---
    REDDIT POST: {original_reddit_post}
    ARTICLE:
  """
  blog_article = get_completion(reddit_to_blog_prompt)
  return blog_article

# reddit to keywords
def get_keywords_from_reddit_post(reddit_post):
  reddit_to_keywords_prompt = f"""
    You are an expert at blog writing and SEO optimization. You will be given a post from Reddit.
    The post will contain the original post and some top level comments in JSON format.
    Your task is to extract a set of long tail keywords that a writer will use later to write a blog article based on the Reddit post.
    Separate your list of keywords with a comma.
    ---
    REDDIT POST: {reddit_post}
    KEYWORDS:
  """
  keywords = get_completion(reddit_to_keywords_prompt)
  return keywords

# article to title
def get_article_title_from_text(text):
  article_to_title_prompt = f"""
    You are an expert at blog writing and SEO optimization. You will be given the text of an article.
    Your task is to decide on an appropriate title for the article and ONLY return the title.
    Do not include any extra words or additional language that is not part of the title.
    ---
    ARTICLE TEXT: {text}
    TITLE:
  """
    # Numbers as per the listcicle format are often good for titles. Consider using them.
  article_title = get_completion(article_to_title_prompt).replace('*', '')
  return article_title

# extract excerpt
def get_article_excerpt_from_text(text):
  article_to_excerpt_prompt = f"""
    You are an expert at blog writing and SEO optimization. You will be given the text of an article.
    Your task is to extract an engaging excerpt from the text of the article.
    Do not label the excerpt as such. Do not use any formatting or quotation marks in your response.
    Make the excerpt as brief as possible but in every case, limit the excerpt to no more than 30 words.
    ---
    ARTICLE TEXT: {text}
    EXCERPT:
  """
  article_excerpt = get_completion(article_to_excerpt_prompt)
  return article_excerpt

# keywords to blog
def get_blog_article_from_keywords(keywords, article_target_length_in_words,):
  keywords_to_blog_prompt = f"""
    You are an expert at blog writing and SEO optimization. You will be given a long tailed keyword.
    Your task is write a helpful informational blog article that is SEO optimized to rank for that longtailed keyword.
    Your article should be {article_target_length_in_words} words in length.
    Avoid writing articles that could be considered giving legal, financial, investing, tax or medical advice.
    Format your article in HTML by explicitly using <title>, <h1> and <h2> tags.
    Use <b> and <i> tags where appropriate but DO NOT use markdown like asterisks (* or **).
    Make the <h1> tag either be identical to the keywords or contain the keywords. Also, make the <h1> tag identical to the <title> tag.
    Your goal should be to keep your title to no more than 60 characters or 11 words while still making it descriptive enough so that users know what they are about to click on.
    Avoid the use of generic headings like <h2>Introduction<h2>. Instead, make every heading a very pithy,
    punchy thesis statement that summarizes the content block like <h2>Apps foster toddlers' learning.</h2>
    Do not select any key words dealing with businesses 'near me' as we want the articles to be informational only and not induce hallucinations.
    Cite between 3-5 references using anchor tags and outbound hyperlinks. Use the Vancouver style (a/k/a/ Uniform Requirements Style) for your citations.
    In your citations, only link to the main domain home page. No paths or subdomains. This should mitigate against broken links.
    ---
    NICHE: {keywords}
    ARTICLE:
  """
    # Listcicle formats are often good for articles and titles. Consider using them sometimes when appropriate. But they are not mandatory.
  blog_article = get_completion(keywords_to_blog_prompt)
  return blog_article

# niche to keywords
def get_keywords_from_niche(niche):
  niche_to_keywords_prompt = f"""
    You are an expert at affiliate marketing, blog writing and SEO optimization.
    You will be given the name of a niche for affiliate marketing.
    Your task is to select a low-competition long-tailed keyword in the niche you are given.
    Avoid selecting keywords that might lead to articles that could be considered giving legal, financial, investing, tax or medical advice.
    Do not label the keywords as such. Do not use any formatting like markdown, asterisks (* or **)
    or quotation marks in your response.
    ---
    NICHE: {niche}
    KEYWORD:
  """
  keywords = get_completion(niche_to_keywords_prompt)
  return keywords

# article to image search term
def get_image_search_term_from_title(article_title):
  title_to_search_term_prompt = f"""
    You are an expert at affiliate marketing, blog writing and SEO optimization.
    You will be given an article title. Your job is to produce a search term to enter
    into Pixabay to find a suitable stock image. It is important that your search term only
    include a single word. Some examples include: "nature", "christmas", "background", "sky",
    "winter", "snow", "food", "love", "cat", "forest", "flower"
    ---
    ARTICLE TITLE: {article_title}
    SINGLE-WORD SEARCH TERM:
  """
  search_term = get_completion(title_to_search_term_prompt)
  return search_term

# docs
# https://developer.wordpress.com/docs/oauth2/
# https://developer.wordpress.com/docs/api/1.1/post/sites/%24site/posts/new/ - post params, e.g., meta, tags, etc.
# https://developer.wordpress.org/rest-api/reference/posts # new docs (v2)

# params
# blog
SITE_ID = 'xanadu6'
BLOG_FRIENDLY_NAME = 'Xanadu'
site_url = f'{SITE_ID}.wordpress.com'
BASE_URL = 'https://public-api.wordpress.com/rest/v1/'
# reddit
TARGET_SUBREDDIT = 'Xanadu6'

# settings
TARGET_NUMBER_OF_POSTS = 34
INCLUDE_REDDIT = False
ARTICLE_TARGET_LENGTH_IN_WORDS = 1500
IS_USE_AI_IMAGES = False # True

# get auth header
def get_auth_header(access_token):
  return {'Authorization': f'Bearer {access_token}'}

# get access token
def get_access_token():
  url = 'https://public-api.wordpress.com/oauth2/token'

  credentials = {
    'username': wordpress_username,
    'password': wordpress_password,
    'client_id': wordpress_client_id,
    'client_secret': wordpress_client_secret,
    'grant_type': 'password',
  }

  response = requests.post(url, data=credentials,)

  auth = json.loads(response.text)
  access_token = auth['access_token']
  # print(access_token)
  return access_token

# get user data
def get_user_data(access_token):
  endpoint = f'{BASE_URL}me/'
  headers = get_auth_header(access_token)
  response = requests.get(endpoint, headers=headers,)

  user_data = response.json()
  # print(user_data)
  return user_data

# utility function for kebab case for slug
def get_kebab_case(text):
  text = text.lower()
  text = re.sub(r"[\W_]+", "-", text)
  return text
# print(get_kebab_case("Test String")) # prints "test-string"
# print(get_kebab_case("Random Text Here")) # prints "random-text-here"

# post request
def set_new_post(access_token, article_target_length_in_words, is_set_new_reddit_post=False,):

  endpoint = f'{BASE_URL}sites/{site_url}/posts/new'
  auth_header = get_auth_header(access_token)

  # niche = get_random_niche()
  niche, categories_path, = get_random_leaf(TOPIC_TREE)

  # keywords = 'best nutritional supplements'
  print(f'niche: {niche}')
  print(f'categories_path: {categories_path}')
  keywords = get_keywords_from_niche(niche=niche)
  print(f'keywords: {keywords}')
  sleep(1)
  slug = get_kebab_case(keywords)
  sleep(1)
  blog_article = get_blog_article_from_keywords(
      keywords=keywords,
      article_target_length_in_words=article_target_length_in_words,
    )
  sleep(1)
  article_title = get_article_title_from_text(text=blog_article)
  sleep(1)
  article_excerpt = get_article_excerpt_from_text(text=blog_article)
  sleep(1)

  files = {}
  if IS_USE_AI_IMAGES:
    # encoded image from stable diffusion
    encoded_image = getStableDiffusionText2Image(article_title,) # base64 encoded string

    # image
    files = {
    # 'media[]': (image_path, open(image_path, 'rb',),),
    # 'media[]': ('image.jpg', encoded_image, 'image/jpeg',)
    # 'media[]': ('image.jpg', encoded_image.getvalue(), 'image/jpeg')
      'media[]': (TEMP_IMAGE_PATH, open(TEMP_IMAGE_PATH, 'rb',),),
    }
    # # image_data = {
    # #   'title': 'Image Post',
    # #   'media_attrs[0][caption]': 'My Great Photo'
    # # }
  else:
    # image url from pixabay api
    # image_url = image_path
    # image_url = random.choice(placeholder_images)
    # image_url = get_pixabay_image_url_from_search(search_query=keywords,)
    image_search_term = get_image_search_term_from_title(article_title)
    print(f'image search term: {image_search_term}')
    image_url = get_pixabay_image_url_from_search(image_search_term)

  # tags = ['python', 'api']
  data = {
    # 'title': 'My test title',
    'title': article_title,
    # 'content': 'Testing test',
    'content': blog_article,
    # 'slug': 'testing-test-only-test-this-is-a-test-only',
    'slug': slug,
    'status': 'publish',
    # 'categories': [ 'testing', 'tests', 'tested', ],
    # 'categories': niche,
    'categories': categories_path,
    # 'featured_image': image_url, # moved to conditional below
    # 'tags': (None, tags,),
    'tags': keywords,
    'excerpt': article_excerpt,
    'publicize': True,

    # 'media[0]': open(image_url, 'rb',),
    'media_attrs[0][caption]': keywords,
  }
  if(image_url):
    data['featured_image'] = image_url

  # # handle error
  # if response.status_code != 200:
  #   print('Error: Post failed at `response = requests.post()`')
  #   print(error)
  #   return None
  try:
    response = requests.post(
      endpoint, json=data, headers=auth_header, files=files, # data=image_data,
    )
    response.raise_for_status()
  except requests.exceptions.RequestException as my_error:
    print(f'Error: {my_error}')
    return None

  result = response.json()

  # send post to reddit
  blog_article_url = result["URL"]
  print(f'blog article url: {blog_article_url}')

  blog_article_in_markdown = html2text.html2text(blog_article)
  blog_article_plus_link_to_source = f'Source: [{BLOG_FRIENDLY_NAME} blog]({blog_article_url})\n\n\n{blog_article_in_markdown}'
  print(f'image url: {image_url}')
  # urllib.request.urlretrieve(image_url, TEMP_IMAGE_PATH) # save image to local file

  if is_set_new_reddit_post:
    reddit_post = set_post_to_reddit(
      subreddit=TARGET_SUBREDDIT,
      title=article_title,
      selftext=blog_article_plus_link_to_source,
      # image_path=TEMP_IMAGE_PATH,
      # image_caption=article_excerpt,
    )

  # print(result)
  return result

def set_new_posts(access_token, target_number_of_posts, article_target_length_in_words, is_set_new_reddit_post=False,):
  for i in range(target_number_of_posts):
    new_post = set_new_post(
        access_token=access_token,
        article_target_length_in_words=article_target_length_in_words,
        is_set_new_reddit_post=is_set_new_reddit_post,
      )
    print(f'new post: {new_post}')
    sleep(8)

def main():
  access_token = get_access_token()
  print(f'access token: {access_token}')
  user_data = get_user_data(access_token)
  print(f'user data: {user_data}')
  set_new_posts(
      access_token=access_token,
      target_number_of_posts=TARGET_NUMBER_OF_POSTS,
      article_target_length_in_words=ARTICLE_TARGET_LENGTH_IN_WORDS,
      is_set_new_reddit_post=INCLUDE_REDDIT,
    )

if __name__ == "__main__":
    main()
