import os
import random
from random import randint

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Entry


def get_random_cta_image():
    cta_image_list = [
        '/media/media/watch.gif',
        '/media/media/a.gif',
        '/media/media/b.gif',
        '/media/media/c.gif',
        '/media/media/d.gif',
        '/media/media/e.gif',
        '/media/media/f.gif',
        '/media/media/g.gif',
        '/media/media/h.gif',
        '/media/media/i.gif',
    ]
    return cta_image_list[randint(0, len(cta_image_list) - 1)]


def get_random_conj():
    conj_list = [
        'and',
        'A minute later',
        'Accordingly',
        'Actually',
        'After',
        'After a short time',
        'Afterward',
        'Also',
        'And',
        'Another',
        'As an example',
        'As a consequence',
        'As a result',
    ]

    return f' {conj_list[randint(0, len(conj_list) - 1)].lower()} '


def random_name():
    name_list = [
        'Liam',
        'Noah',
        'William',
        'James',
        'Oliver',
        'Benjamin',
        'Elijah',
        'Joshua Lucas',
        'Christopher Mason',
        'Andrew Logan',
        'Theodore Alexander',
        'Caleb Ethan',
        'Ryan Jacob',
        'Asher Michael',
        'Nathan Daniel',
        'Thomas Henry',
        'Leo Jackson',
        'Isaiah Sebastian',
        'Charles Aiden',
        'Josiah Matthew',
        'Hudson Samuel',
        'Christian David',
        'Hunter Joseph',
        'Connor Carter',
        'Owen',
        'Wyatt',
        'John',
    ]
    return f' {name_list[randint(0, len(name_list) - 1)].lower()} '


def random_comment():
    comment_list = [
        "Needed to compose you a very little word to thank you yet again regarding the nice suggestions you’ve contributed here.",
        "It has been simply incredibly generous with you to provide openly what exactly many individuals would’ve marketed for an ebook to end up making some cash for their end, primarily given that you could have tried it in the event you wanted.",
        "Those guidelines additionally worked to become a good way to recognize that other people online have the identical fervor like mine to grasp great deal more around this condition.",
        "I believe there are many more pleasurable opportunities ahead for individuals that looked at your site.",
        "I wish to show thanks to you just for bailing me out of this particular trouble.As a result of checking through the net and meeting techniques that were not productive, I thought my life was done.",
        "Existing without the answers to the difficulties you’ve sorted out through this guide is a critical case, as well as the kind which could have badly affected my entire career if I had not discovered your website.",
        "Your good knowledge and kindness in playing with all the pieces were very useful. I don’t know what I would have done if I had not encountered such a step like this.",
        "Thanks a lot very much for the high quality and results-oriented help. I won’t think twice to endorse your blog post to anybody who wants and needs support about this area.",
        "I simply wanted to write down a quick word to say thanks to you for those wonderful tips and hints you are showing on this site.",
        "My rather long internet look up has at the end of the day been compensated with pleasant insight to talk about with my family and friends.",
        "I ‘d mention that most of us visitors are endowed to exist in a fabulous place with very many wonderful individuals with very helpful things.",
        "I feel really happy to have seen your webpage and look forward to so many more entertaining times reading here. Thanks once more for all the details.",
        "Thank you a lot for providing individuals with a very spectacular possibility to read critical reviews from this site.",
        "It’s always so sweet and also full of a lot of fun for me personally and my office colleagues to search your blog a minimum of thrice in a week to see the new guidance you have got.",
        "And indeed, I’m just always astounded concerning the remarkable things served by you. Some four facts on this page are undeniably the most effective I’ve had.",
        "I have to voice my passion for your kindness giving support to those people that should have guidance on this important matter.",
        "Your very own commitment to getting the message throughout came to be rather powerful and have consistently enabled employees just like me to arrive at their desired goals.",
        "Your new valuable key points imply much a person like me and extremely more to my office workers. With thanks; from everyone of us.",
        "I and my friends were going through the nice, helpful tips from the blog then the sudden came up with an awful suspicion I never expressed respect to the website owner for those secrets.",
        "The young boys ended up stimulated to read through them and now have unquestionably been having fun with these things.",
        "Appreciation for really being thoughtful and also for deciding on certain marvelous guides most people really want to be aware of.",
        "I am commenting to let you know what a terrific experience my daughter enjoyed reading through your web page. She noticed a wide variety of pieces, with the inclusion of what it is like to have an awesome helping style to have the rest without hassle grasp some grueling matters.",
        "You truly did more than visitors’ expectations. Thank you for rendering these helpful, trusted, edifying and also cool thoughts on the topic to Kate.",
        "I simply wanted to thank you so much again. I am not sure the things that I might have gone through without the type of hints revealed by you regarding that situation.",
        "Some us know all relating to the compelling medium you present powerful steps on this blog and therefore strongly encourage contribution from other ones on this subject while our own child is truly discovering a great deal. Have fun with the remaining portion of the year.",
        "Thanks for one marvelous posting! I enjoyed reading it; you are a great author.I will make sure to bookmark your blog and may come back someday. I want to encourage that you continue your great posts, have a nice weekend!",
        "My spouse and I love your blog and find almost all of your post’s to be just what I’m looking for. can you offer guest writers to write content for you? I wouldn’t mind producing a post or elaborating on some the subjects you write concerning here. Again, awesome weblog!",
        "My partner and I stumbled over here different website and thought I might as well check things out. I like what I see so now I’m following you. Look forward to checking out your web page repeatedly.",
        "I enjoy what you guys are usually up too. This sort of clever work and coverage! Keep up the wonderful works guys I’ve added you guys to my blogroll.",
        "Hi there I am so thrilled I found your website, I really found you by mistake, while I was browsing on Yahoo for something else, Anyhow I am here now and would just like to say thanks a lot for a tremendous post and a all round exciting blog (I also love the theme/design), I don’t have time to go through it all at the minute but I have saved it and also added in your RSS feeds, so when I have time I will be back to read more, Please do keep up the awesome job.",
        "Appreciating the persistence you put into your blog and detailed information you provide.",
        "It’s great to come across a blog every once in a while that isn’t the same out of date rehashed material. Fantastic read.",
        "I’ve bookmarked your site, and I’m adding your RSS feeds to my Google account.",
        "I really love the theme/design of your website. Do you ever run into any browser compatibility problems? A small number of my blog audience have complained about my site not working correctly in Explorer but looks great in Safari. Do you have any ideas to help fix this problem?",
        "I am curious to find out what blog system you’re using?",
        "I’m experiencing some small security issues with my latest blog, and I’d like to find something safer. Do you have any suggestions?",
        "Hmm, it seems like your site ate my first comment (it was extremely long) so I guess I’ll just sum it up what I had written and say, I’m thoroughly enjoying your blog. I as well am an aspiring blog writer, but I’m still new to the whole thing. Do you have any recommendations for newbie blog writers? I’d appreciate it.",
        "Woah! I’m enjoying the template/theme of this website. It’s simple, yet effective. A lot of times it’s very hard to get that “perfect balance” between superb usability and visual appeal. I must say you’ve done a very good job with this.",
    ]
    return f' {comment_list[randint(0, len(comment_list) - 1)].lower()} '


with open(f"{os.getcwd()}/blog/dict/kw_list.txt") as kw_file:
    kws = [line.strip() for line in kw_file]

random_kw = kws[randint(0, len(kws) - 1)]

tags = ''

for _ in range(10):
    tags += kws[randint(0, len(kws) - 1)] + ','

desc = "site is about "
for _ in range(10):
    desc += kws[randint(0, len(kws) - 1)] + ' and '


def random_image():
    path = r"./media/media/"
    rand_img = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    return rand_img


url_list = [
    'https://afflat3d1.com/lnk.asp?o=9075&c=918277&a=242672&k=EBF2EDB942180C1F39AC57CE3994F57C&l=8504',
    'https://afflat3d1.com/lnk.asp?o=18084&c=918277&a=242672&k=580FAC50554E1E3F5AACC583D06DE0AD&l=19332',
    'https://afflat3d1.com/lnk.asp?o=18099&c=918277&a=242672&k=89F4A996358DADE546AA2BF166C9A7F9&l=19340',
    'https://afflat3d1.com/lnk.asp?o=18095&c=918277&a=242672&k=C12104E1F23E5C340EAF089395EBD125&l=19345',
    'https://afflat3d1.com/lnk.asp?o=18627&c=918277&a=242672&k=B97D03D349CE4FE1BE27D635A16AD24B&l=19818',
    'https://afflat3d1.com/lnk.asp?o=19322&c=918277&a=242672&k=F5A185D25CB8289CD91DF3803D395C64&l=20323',
    'https://afflat3d1.com/lnk.asp?o=19594&c=918277&a=242672&k=30F2E776196A860C8FE3BBDE6D69D334&l=20556',
    'https://afflat3d1.com/lnk.asp?o=7527&c=918277&a=242672&k=956D04E486409DA8ED5528F3448FB86F&l=6239',
    'https://afflat3d1.com/lnk.asp?o=10721&c=918277&a=242672&k=18DBF0EF0820E9FDB52660B31C464213&l=10603',
    'https://afflat3d1.com/lnk.asp?o=18174&c=918277&a=242672&k=29DA121E59E0456E7F1B9D705D276327&l=19429',
]
headline_list = [
    'Forecasters call for weather on Monday',
    'Amphibious pitcher makes debut',
    'Cows lose their jobs as milk prices drop',
    'Miracle cure kills fifth patient',
    'Man Accused of Killing Lawyer Receives a New Attorney',
    'State population to double by 2040, babies to blame',
    'Missippis literacy program shows improvement',
    'Breathing oxygen linked to staying alive',
    'Police arrest everyone on February 22nd',
    'Thursday is cancelled',
    'Bridge closure date: Thursday or October',
    'Most Earthquake Damage is Caused by Shaking',
    'Federal Agents Raid Gun Shop, Find Weapons',
    'Safety meeting ends in accident',
    'Muddy Creek Problem: Its too muddy',
    'Murderer says detective ruined his reputation',
    'Utah Poison Control Center reminds everyone not to take poison',
    'Bugs flying around with wings are flying bugs',
    'Students Cook & Serve Grandparents',
    'Alton attorney accidentally sues himself',
    'Hospitals resort to hiring doctors',
    'Farmer using cannon to protect watermelons',
    'Voters to vote on whether to vote',
    'Museums full of history',
    'Goat accused of robbery',
]

sidebar_info_list = [
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
]


def divide_string(mystring):
    word_list = mystring.split(" ")
    str_len = len(word_list)
    mid_index = int(str_len / 2)
    str_1 = ""
    str_2 = ""
    for ix in range(mid_index):
        str_1 += word_list[ix] + " "

    for iy in range(mid_index, str_len):
        str_2 += word_list[iy] + " "

    return str_1, str_2


def random_title(titles):
    return f' {titles[randint(0, len(titles) - 1)]} '


def random_texts(texts):
    return f' {texts[randint(0, len(texts) - 1)]} '


def random_tags(m_tags):
    return f' {m_tags[randint(0, len(m_tags) - 1)]} '


post_titles = []
post_texts = []
post_tags = []


class HomeView(ListView):
    posts = Entry.objects.all()
    model = Entry
    template_name = 'blog/home-page.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rand_im'] = random_image

        return context


def single_post(request, slug):
    template = 'blog/post-page.html'
    posts = Entry.objects.all()
    s_post = Entry.objects.get(slug=slug)
    single_author = s_post.entry_author
    single_date = s_post.entry_date
    single_title = s_post.entry_title
    my_string = s_post.entry_text
    my_sub_id = s_post.site_sub_id
    my_sentences = my_string.split('.')
    sentence_num = len(my_sentences)
    kw_str = my_sentences[sentence_num - 1]

    kw_list = kw_str.split(",")
    rand_kws = ""
    for _ in range(8):
        rand_kws += kw_list[randint(0, len(kw_list) - 1)] + ','

    str_1 = divide_string(my_string)[0]
    str_2 = divide_string(my_string)[1]
    stuff_for_single_post = {
        "title": single_title,
        "text_1": str_1,
        "text_2": str_2.replace("from articlesfactory.com", ""),
        "author": single_author,
        "date": single_date,
        "rand_cta_im": get_random_cta_image,
        'rand_im_1': random_image,
        'rand_im_2': random_image,
        'rand_thumb': random_image,
        'rand_url': url_list[randint(0, len(url_list) - 1)],
        "sidebar_things": sidebar_info_list,
        'tags': tags,
        'desc': desc,
        'c_name': random_name,
        'c_text': random_comment,
    }
    return render(request, template, context=stuff_for_single_post)





# # CLASSES NOT IN USE!
# def home(request):
#     global rand_index
#     posts = Entry.objects.all()
#     post_titles = []
#     post_texts = []
#     post_tags = []
#
#     for s_post in posts:
#         post_titles.append(s_post.entry_title)
#         post_texts.append(s_post.entry_text)
#         post_tags.append(s_post.entry_tags)
#         rand_index = randint(0, len(post_titles))
#
#     r_title = random_title(post_titles)
#     r_texts = random_texts(post_texts)
#     r_tags = random_tags(post_tags)
#
#     homepage_data = {
#         "r_title": r_title,
#         'r_text': r_texts,
#         'r_tags': r_tags,
#         'r_author': random_name,
#         'loop_times': len(post_titles),
#
#     }
#     return render(request, template_name='blog/home-page.html', context=homepage_data)

# class HomeView(ListView):
#     model = Entry
#     template_name = 'blog/home-page.html'
#     context_object_name = "blog_entries"
#     ordering = ['-entry_date']
#     paginate_by = 6
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sidebar_things'] = sidebar_info_list
#         context['tags'] = tags
#         context['desc'] = desc
#         context['rand_im'] = random_image
#
#         return context
#
#
# class CreateEntryView(CreateView):
#     model = Entry
#     template_name = 'blog/create_entry.html'
#     fields = ['entry_title', 'entry_text']
#
#     def form_valid(self, form):
#         form.instance.entry_author = self.request.user
#         return super().form_valid(form)
#
#
# class EntryView(DetailView):
#     model = Entry
#     slug_field = 'slug'
#     template_name = 'blog/entry_detail.html'
#     data_set = random_image()
#     stuff_for_post = {
#
#         "info": data_set
#     }
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rand_im'] = random_image()
#         context['tags'] = [kws[randint(0, len(kws) - 1)], kws[randint(0, len(kws) - 1)], kws[randint(0, len(kws) - 1)],
#                            kws[randint(0, len(kws) - 1)], kws[randint(0, len(kws) - 1)]]
#
#         return context
