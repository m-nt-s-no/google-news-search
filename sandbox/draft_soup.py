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
# author info in <div class="article-hero__authors">, date in <div class="article-hero__date">

# TO-DO: check other publishers' HTML structures for article content, headline:
# SiliconANGLE, USA Today, The New York Times, The Wall Street Journal, Washington Post, BBC, CNN, Reuters, Bloomberg, NBC News, ABC News, 
# The Guardian, AP, Bloomberg, Forbes

"""
CNN 
headline: 
  <h1 data-editable="headlineText" class="headline__text inline-placeholder vossi-headline-text" id="maincontent">
    China warns US of countermeasures if Trump doesn’t walk back 100% tariff threat
  </h1>
content:
  <p class="paragraph-elevate inline-placeholder vossi-paragraph" data-uri="cms.cnn.com/_components/paragraph/instances/cmgn9p81u00063b6qnajnxwgz@published" data-editable="text" data-component-name="paragraph" data-article-gutter="true">
            Beijing has vowed countermeasures against Washington if US President Donald Trump makes good on his threat to <a href="https://www.cnn.com/2025/10/10/politics/rare-earths-china-trump-threats">impose new 100% tariffs</a> on Chinese imports.
    </p>

  CNN content wrapped inside <main class="article__main"></main>, <div class="article__content-container"></div>, 
  and <div class="article__content" data-editable="content" itemprop="articleBody" data-reorderable="content"></div>
author: 
  <span class="byline__name">
date: 
  published: 
    <div class="timestamp__published"> then <time datetime="sometime">, 
  updated: <div class="updated"> then <time datetime="sometime">
"""

"""
SiliconANGLE
headline:
  <h3 class="sa-post-title">
    AI embraces and extends enterprise software as funding keeps pouring in – but is all this a bubble?
  </h3>
content: <div class="col-md-12 col-xs-12 sa-post-content">, then <div class="single-post-content">, then each paragraph in a bare <p> tag
  "single-post-content" uniquely identifies article content
author: <span class="author"> (first one, subsequent tags are authors of related articles)
date: <p class="text-uppercase post-updated-date">, then <span class="meta-dt">
"""

"""
USA Today
headline: 
  <h1 class="gnt_ar_hl" elementtiming="ar-headline">
  'Keep your mouth shut.’ Tempers flare over shutdown with no end in sight
  </h1>
content: <div class="gnt_ar_b">, then each paragraph in <p class="gnt_ar_b_p">
author:
  <a href="/staff/8391697001/zachary-schermele/" data-t-l=":byline with photo|o|c|text" class="gnt_ar_by_a gnt_ar_by_a__fi"><img class="gnt_ar_by_i" src="/gcdn/authoring/authoring-images/2024/07/08/USAT/74332447007-xxx-usat-886362-021560.JPG?crop=3999,4000,x0,y0&amp;width=48&amp;height=48&amp;format=pjpg&amp;auto=webp" srcset="/gcdn/authoring/authoring-images/2024/07/08/USAT/74332447007-xxx-usat-886362-021560.JPG?crop=3999,4000,x0,y0&amp;width=96&amp;height=96&amp;format=pjpg&amp;auto=webp 2x" decoding="async" loading="eager" alt="Portrait of Zachary Schermele" fetchpriority="high" data-t-l=":byline with photo|o|c|photo"> Zachary Schermele</a>
date:
  <div class="gnt_ar_dt">::after</div>
"""

"""
NYTimes
headline:
  <h1 id="link-767900ef" class="css-4um83n e1h9rw200" data-testid="headline">
    How a Las Vegas Casino Mogul Helped Bring N.B.A. Games Back to China
  </h1>
content (only partial bc paywall):
  <section name="articleBody" class="meteredContent css-ar1ez3">
    <div class="css-s99gbd StoryBodyCompanionColumn" data-testid="companionColumn-0">
      <div class="css-53u6y8">
        <p class="css-ac37hb evys1bk0">
          In 2021, the casino mogul Patrick Dumont approached the N.B.A. commissioner with a brazen idea: Bring American professional basketball 
          back to China.
        </p>
        <p class="css-ac37hb evys1bk0">The N.B.A.’s relationship with Beijing had been in tatters for two years, after a team
          executive’s tweet in support of pro-democracy protests in Hong Kong. The resulting controversy cost the league hundreds of millions of 
          dollars. Partners pulled their sponsorships. China’s state broadcaster CCTV stopped airing games.
        </p>
        <p class="css-ac37hb evys1bk0">
          Western companies that clash so publicly with Beijing rarely get second chances. But Mr. Dumont, an executive with one of the world’s 
          most profitable casino operators, believed that the National Basketball Association could get back into China through Macau, the 
          semiautonomous city where his company ran several highly lucrative casinos.
        </p>
        <p class="css-zry96z" aria-live="polite" role="note">
          <a class="css-1081t4c" href="https://www.nytimes.com/subscription?campaignId=8WXW7">
            Subscribe to The Times</a> to read as many articles as you like.
        </p>
      </div>
      <aside class="css-ew4tgv" aria-label="companion column"></aside>
    </div>
  </section>
author:
  <p class="css-4anu6l e1jsehar1">
    <span class="byline-prefix">By </span>
    <a href="https://www.nytimes.com/by/tania-ganguli" class="css-ojhyzr e1jsehar0" itemprop="name">
      Tania Ganguli
    </a> 
    and 
    <a href="https://www.nytimes.com/by/mara-hvistendahl" class="last-byline css-ojhyzr e1jsehar0" itemprop="name">
      Mara Hvistendahl
    </a>
  </p>
date:
  <ul class="css-1cgskve epjyd6m4">
    <li class="css-ccw2r3 epjyd6m3">
      <time class="css-1uc6ajg e16638kd0" datetime="2025-10-11T05:01:11-04:00">
        Oct. 11, 2025
      </time>
    </li>
  </ul>
"""

"""
WSJ
headline:
  <h1 class="css-1vi6b05-StyledHeadline-Styled-Styled-Styled emwm06f0">
    How China and the U.S. Are Racing to De-Escalate the Trade War
  </h1>

content:
  <p data-type="paragraph" data="[object Object]" class="css-1akm6h5-Paragraph e1e4oisd0">
    President Trump is trying to publicly de-escalate tensions with China to soothe markets while privately 
    keeping up pressure on Beijing—a difficult balancing act that is being closely watched by Wall Street.
  </p>

author:
  <div data-testid="byline" class="epvx9354 css-1iwob86-BylineContainer"> 
    <p class="epvx9352 css-1s90smj-AuthorPlaintext">By </p>
    <a data-testid="author-link" href="https://www.wsj.com/news/author/brian-schwartz" target="_self" aria-label="Author page for Brian Schwartz" class="epvx9353 css-jv4qg1-AuthorLink">
      <span class="css-17x5lw">
        <span class="css-1wc2zh5">
          Brian Schwartz
        </span>
      </span>
    </a>
  </div>
  + 2 more authors

date:
  <p data-testid="timestamp-text" class="es486sg1 css-119j68f-TimeTag">
    <time datetime="2025-10-14T01:00:00.000Z">
      Oct. 13, 2025 9:00 pm
    </time>
    <span> 
      ET
    </span>
  </p>
"""

"""
Washington Post
headline:
  <h1 id="main-content" data-qa="headline" data-testid="headline" class="wpds-c-eRlesA wpds-c-eRlesA-dHdMuz-isOnSplitTopper-false wpds-c-eRlesA-bAbYzz-isStyle-false wpds-c-eRlesA-iPJLV-css">
    Hundreds of CDC layoffs reversed, but biodefense preparedness staff hit
  </h1>

content:
  <div class="wpds-c-PJLV article-body type-text" data-qa="article-body">
    <p data-apitype="text" data-contentid="UDBYJ7RUMH5AT098CK9RXDB3J8" data-el="text" class="wpds-c-heFNVF wpds-c-heFNVF-iPJLV-css overrideStyles font-copy" dir="null">
      Officials have reversed more than half of the about 1,300<a href="https://www.washingtonpost.com/health/2025/10/11/cdc-layoffs-public-health-shutdown/" class="js-itid-click"> layoff notices</a> 
      sent to staff members at the Centers for Disease Control and Prevention, sparing personnel who were leading the response to measles outbreaks in the United States and an Ebola outbreak abroad. 
      But details emerged about the other health officials who lost their jobs, including analysts responsible for monitoring and protecting the United States from biological, chemical and nuclear 
      threats, according to current and former officials.
    </p>
  </div>

author:
  <div data-qa="author-byline" data-testid="article-byline" class="wpds-c-cNdzuP wpds-c-cNdzuP-hSmMVC-isLive-false wpds-c-cNdzuP-igKRIQW-css">
    <div class="wpds-c-PJLV wpds-c-PJLV-kxYKtF-isLive-false wpds-c-PJLV-iPJLV-css overrideStyles">
      <div class="wpds-c-PJLV wpds-c-PJLV-AsWAM-isMultiple-true">
        <span class="PJLV">
          <div data-testid="author-name-with-optional-link" class="wpds-c-byuVAJ wpds-c-byuVAJ-iPJLV-css">
            <span data-testid="byline-attribution" class="PJLV">By <!-- --> </span>
            <a class="wpds-c-PJLV wpds-c-PJLV-ktcktv-isLink-true overrideStyles js-itid-click" href="https://www.washingtonpost.com/people/lena-h-sun/" rel="author">
              Lena H. Sun
            </a>
          </div>
          <span class="wpds-c-kpjDGe wpds-c-kpjDGe-fSGdIc-isSmall-false wpds-c-kpjDGe-iPJLV-css"> and<!-- -->&nbsp;</span>
          </span>
        </div>
        <div class="wpds-c-PJLV wpds-c-PJLV-AsWAM-isMultiple-true">
          <span class="PJLV">
            <div data-testid="author-name-with-optional-link" class="wpds-c-byuVAJ wpds-c-byuVAJ-iPJLV-css">
              <a class="wpds-c-PJLV wpds-c-PJLV-ktcktv-isLink-true overrideStyles js-itid-click" href="https://www.washingtonpost.com/people/paige-winfield-cunningham/" rel="author">
                Paige Winfield Cunningham
              </a>
            </div>
          </span>
        </div>
      </div>
    </div>

date:
  <div data-testid="timestamp" class="wpds-c-bEimne wpds-c-bEimne-dyECYW-theme-default">
    <time datetime="2025-10-13T22:45:15.869Z" class="wpds-c-gRBhEF wpds-c-gRBhEF-idbzzBd-css overrideStyles">
      <div class="wpds-c-eUMOSL">
        <span data-testid="published-date" class="wpds-c-bASIGw wpds-c-bASIGw-inNKvU-css overrideStyles">
          October 13, 2025 at 6:45 p.m. EDT
        </span>
        <span data-testid="relative-date" class="wpds-c-bASIGw wpds-c-bASIGw-ikIXjjZ-css overrideStyles">
          Today at 6:45 p.m. EDT
        </span>
      </div>
    </time>
  </div>
"""

"""
BBC
headline:
  <div data-component="headline-block" class="sc-3b6b161a-0 bPbmDW">
    <h1 class="sc-f98b1ad2-0 jRDKjj">
      Madagascar president hiding in 'safe place' as he warns of coup attempt
    </h1>
  </div>

content:
  <div data-component="text-block" class="sc-3b6b161a-0 jdlrvG">
    <p class="sc-9a00e533-0 bJoRPJ">
      Madagascar's embattled President Andry Rajoelina has said he is sheltering in a "safe place" after an attempt on his life,
      following weeks of protests calling for him to quit.
    </p>
    <p class="sc-9a00e533-0 bJoRPJ">
      In a live broadcast to the nation on Facebook, Rajoelina, 51, said "a group of military personnel and politicians planned 
      to assassinate me".
    </p>
    <p class="sc-9a00e533-0 bJoRPJ">
      He did not reveal his location, but unconfirmed reports earlier suggested that he had fled the country on a French military aircraft.
    </p>
    <p class="sc-9a00e533-0 bJoRPJ">
      It follows a fortnight of nationwide protests, mainly led by young demonstrators, aimed at kicking him out of power.
    </p>
  </div>
  + subsequent paragraphs in additional divs with data-component="text-block"

author:
  <span data-testid="byline-new-contributors" class="sc-c4820dd1-11 bxdaHR">
    <div class="sc-c4820dd1-5 iYeVyy">
      <span class="sc-c4820dd1-7 dbQBRo">
        Natasha Booty
      </span>
      <span data-testid="undefined-role-location" class="sc-c4820dd1-8 evcqcz"></span><span class="sc-c4820dd1-9 iEEPlu"> 
        and
      </span>
    </div>
    <div class="sc-c4820dd1-5 iYeVyy">
      <span class="sc-c4820dd1-7 dbQBRo">
        Sammy Awami
      </span>
      <span data-testid="undefined-role-location" class="sc-c4820dd1-8 evcqcz">
        BBC Africa, Antananarivo
      </span>
    </div>
  </span>

date:
  <time datetime="2025-10-13T18:37:34.650Z" class="sc-c4820dd1-2 IVdPK">
    8 hours ago
  </time>
"""