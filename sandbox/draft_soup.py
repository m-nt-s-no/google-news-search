from bs4 import BeautifulSoup
import requests
import re

 #TechCrunch example 1: author page, no actual article
url_1 = "https://techcrunch.com/author/ronjourn/page/83/?__hstc=259903189.2f3f33a24b44870ec4a577029c49e44b.1726185600094.1726185600095.1726185600096.1&__hssc=259903189.1.1726185600097&__hsfp=451136374"
response_1 = requests.get(url_1)
soup_1 = BeautifulSoup(response_1.text, "html.parser")

p_tags_soup_1 = soup_1.find_all("p", class_=re.compile("paragraph"))
print([item.text for item in p_tags_soup_1])
# only result is copyright notice: ['© 2025 TechCrunch Media LLC.']

# TechCrunch example 2: actual article
url_2 = "https://techcrunch.com/2025/09/30/adobes-video-editing-app-premiere-arrives-on-iphones/"
response_2 = requests.get(url_2)
soup_2 = BeautifulSoup(response_2.text, "html.parser")

# article content is tagged with <p class="wp-block-paragraph">
p_tags_soup_2 = soup_2.find_all("p", class_=re.compile("paragraph"))
print([item.text for item in p_tags_soup_2])
# outputs article content:
"""
['Adobe’s popular video editing app Premiere is available on iPhone starting today, following the company’s announcement 
of its plans to release the app on mobile earlier this month. The Android version of the app is under development, Adobe says.', 

'The Premiere app for mobile is free to use and offers editing features, like multi-track timeline, including videos, sounds, music,
and text; support for 4K HDR editing; auto-generated captions; and the ability to adjust factors like color and shadows for different 
frames, fit for a mobile screen.', 'If you have captured the clip from your mobile device, it is likely to have background noise. 
You can easily reduce the noise and increase the dialog through the slider control. ', 

'Adobe has also added a number of AI-powered features to the app. First, you can create background sounds based on a prompt. 
If you are feeling adventurous, you can perform the sound by humming or singing, and AI will convert that into a sound effect.', 
'Using its Firefly models, the company allows users to create images and stickers and to turn images into videos for transition shots. 
Although the app is free, these AI features will require you to buy credits.', 

'The company is also providing access to its own stock library of photos, clips, and sounds to use in videos without charge.', 

'With this new Premiere app, creators can start a project on the go and transfer it to the desktop app across platforms using Adobe Cloud. 
However, you can’t send the project from desktop to mobile at the moment. ', 

'“We want to empower all types of\xa0creators\xa0to work. We know that the next generation of creators chooses and prefers to edit on mobile. 
And so that’s [the new mobile app] a critical way that we meet them where they’re at,” Mike Folgner, a product director at Adobe, 
told TechCrunch over a call.', 

'Premiere joins a suite of apps the company is bringing to mobile, such as Photoshop for iOS and Android, and Firefly for mobile.', 

'With this launch, the company is positioning itself as a competitor to ByteDance’s CapCut, Meta’s Edits, a16z-backed startup Captions, 
and India-based InVideo.', 

'', '', '', 'Topics', '© 2025 TechCrunch Media LLC.']
"""
# FYI TechCrunch headline HTML is: <h1 class="article-hero__title wp-block-post-title">Adobe’s video editing app Premiere arrives on iPhones</h1>

# TO-DO: check other publishers' HTML structures for article content, headline:
# SiliconANGLE, USA Today, The New York Times, The Wall Street Journal, Washington Post, BBC, CNN, Reuters, Bloomberg, NBC News, ABC News, 
# The Guardian, AP, Bloomberg, Forbes

"""
CNN headline: 
  <h1 data-editable="headlineText" class="headline__text inline-placeholder vossi-headline-text" id="maincontent">
    China warns US of countermeasures if Trump doesn’t walk back 100% tariff threat
  </h1>
  content:
  <p class="paragraph-elevate inline-placeholder vossi-paragraph" data-uri="cms.cnn.com/_components/paragraph/instances/cmgn9p81u00063b6qnajnxwgz@published" data-editable="text" data-component-name="paragraph" data-article-gutter="true">
            Beijing has vowed countermeasures against Washington if US President Donald Trump makes good on his threat to <a href="https://www.cnn.com/2025/10/10/politics/rare-earths-china-trump-threats">impose new 100% tariffs</a> on Chinese imports.
    </p>

  CNN content wrapped inside <main class="article__main"></main>, <div class="article__content-container"></div>, 
  and <div class="article__content" data-editable="content" itemprop="articleBody" data-reorderable="content"></div>
"""