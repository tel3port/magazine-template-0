from django.shortcuts import render
import os
from random import randint
import glob
import traceback


def get_rand_url():
    url_list = [
        'buy now',
        'click here',
        'Act Now',
        'Add to your Bookmarks',
        'Apply today',
        'Be sure to click',
        'Book now',
        'Buy and Save',
        'Buy Now',
        'Call today',
        'Check our discounts',
        'Check out  THIS',
        'Check this out',
        'Choose your Best NOW',
        'Click button NOW',
        'Click for more',
        'Click Here',
        'Come see our prices',
        'Compare prices',
        'Contact us',
        'Contact us today',
        'Discover',
        'Do not buy unless...',
        'Don’t forget to click',
        'Don’t miss out',
        'Don’t wait longer',
        'Download now',
        'Find Items here',
        'Find out more',
        'Find savings ',
        'Find yours',
        'Follow this        ',
        'Get a quote        ',
        'Get Free           ',
        'Get it here        ',
        'Get More Info Here ',
        'Get the Best       ',
        'Get your           ',
        'Give a gift        ',
        'How to GET         ',
        'Hurry              ',
        'Investigate        ',
        'Join today         ',
        'Join us            ',
        'Learn more         ',
        'Learn to  LIVE      ',
        'Look at this        ',
        'Need more          ',
        'No obligation to try',
        'Now you can        ',
        'Order Now          ',
        'Order Your  PET     ',
        'Pay Less           ',
        'Please see         ',
        'Please view our  PAGE',
        'Purchase           ',
        'Read reviews       ',
        'Register           ',
        'Request yours today',
        'Research           ',
        'Respond by CLICKING',
        'Rush today         ',
        'Save Big           ',
        'Save Money         ',
        'Save on            ',
        'Save Today         ',
        'Save up to  1000   ',
        'Save with          ',
        'Search for This    ',
        'Search Now         ',
        'Search our         ',
        'See deals          ',
        'See more           ',
        'See our coupon     ',
        'See our products   ',
        'See pricing        ',
        'Send for  INFO     ',
        'Shop at            ',
        'Shop low prices    ',
        'Shop now           ',
        'Shop online        ',
        'Shop today         ',
        'Show price         ',
        'Sign me up now     ',
        'Sign up            ',
        'Start now          ',
        'Start today        ',
        'Stock up           ',
        'Submit             ',
        'Take a closer look ',
        'Take a look at     ',
        'Take a tour        ',
        'Tour our           ',
        'Try it today       ',
        'View all Products  ',
        'View features      ',
        'Visit our page      ',
        'Visit us here       ',
        'Watch for  FREE     ',
        'You might also try ',
        'You might consider ',
        'Yours for asking'
    ]
    return url_list[randint(0, len(url_list) - 1)]


anchor_list = [
    "https://my7.travel.blog/awesome/",
    "https://my7.travel.blog/awesome/",
    "https://my7.travel.blog/awesome/",
    "https://my7.travel.blog/awesome/",
    "https://my7.travel.blog/awesome/"
]

with open(f"{os.getcwd()}/gallery/dict/kw_list.txt") as kw_file:
    global kws
    kws = [line.strip() for line in kw_file]

random_kw = kws[randint(0, len(kws) - 1)]


# Create your views here.
def home(request):
    image_list = extract_images()

    title = f"{kws[randint(0, len(kws) - 1)]} and {kws[randint(0, len(kws) - 1)]}"
    keywords = f"{kws[randint(0, len(kws) - 1)]}, {kws[randint(0, len(kws) - 1)]}, {kws[randint(0, len(kws) - 1)]}, {kws[randint(0, len(kws) - 1)]}"
    # content = random_content_getter()
    content = ""

    random_anchor = anchor_list[randint(0, len(anchor_list) - 1)]

    # try:
    #     for i in glob.glob("/media/media/*"):
    #         os.remove(i)
    #
    # except Exception as we:
    #     print('image_deleter Error occurred ' + str(we))
    #     print(traceback.format_exc())
    #     pass

    print(f"NUMBER OF IMAGES: {len(image_list)}")

    final_postings = []

    for s_image in image_list:
        final_postings.append((s_image, title, keywords, content, get_rand_url, random_anchor.strip()))

    stuff_for_frontend = {
        'final_postings': final_postings,
    }

    return render(request, template_name="gallery/index.html", context=stuff_for_frontend)


def extract_images():
    path = r"./media/media/"

    final_info = os.listdir(path)

    return final_info
