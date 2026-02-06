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
# The Guardian, AP, Forbes, Fox News, Axios, The Hill, Politico, The Daily Mail

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

content: 
  <div class="col-md-12 col-xs-12 sa-post-content">
    <div class="single-post-content">
      <p>
        Artificial intelligence is changing the world of software even faster than its many proponents predicted.
      </p>
      <p>
        This week we saw several big moves by major companies to leverage AI to transform — let’s call it 
        embrace and extend, as one software giant used to put it — the 
          <a href="https://www.gartner.com/en/documents/6372011#:~:text=Summary,with%20a%20320.4%25%20growth%20rate.">
            $900 billion
          </a> 
        enterprise software market.
      </p>
    </div>
  </div>

author: 
  <div>
	  <p class="text-muted post-author-name text-uppercase">
	      <span class="standing-head" style="color:#dd3333;">
          THIS WEEK IN ENTERPRISE
        </span>					        	                        
        by 
          <a href="https://siliconangle.com/author/roberthof/">
	          <span class="author">
              Robert Hof
            </span>
	        </a>
    </p>
	</div>
    
date: 
  <p class="text-uppercase post-updated-date">
    <span class="meta-dt">
      UPDATED 12:13 EDT
      <span>
        / 
      </span>
      OCTOBER 10 2025
    </span>
    <span class="meta-vr"></span>
  </p>
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

"""
Reuters:
headline:

  <h1 data-testid="Heading" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__medium__2Rl30 text-module__heading_article__2yUro heading-module__base__p-zaD heading-module__heading_article__h3IXH headline-module__headline__L8lWb">
    Voting Rights Act faces a near-death experience at US Supreme Court
  </h1>

content:

  <div class="article-body-module__content__bnXL1">
    <div data-testid="ContextWidget" class="context-widget-module__container__b9mKr article-body-module__context_widget__sq1EI">
      <div data-testid="TabContainer" class="context-widget-module__tabcontainer__O1B-s">
        <ul role="tablist" class="context-widget-module__tabs__AIjL0">
          <li data-testid="Body" role="tab" aria-selected="true" tabindex="0" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__medium__2Rl30 text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf context-widget-module__tab__lRw-D context-widget-module__selected__Et295">
            Summary
          </li>
          <li data-testid="Body" role="tab" aria-selected="false" tabindex="-1" class="text-module__text__0GDob text-module__medium-grey__yZtlg text-module__medium__2Rl30 text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf context-widget-module__tab__lRw-D">
            Companies
          </li>
        </ul>
      </div>
      <div class="context-widget-module__content__lI1uo">
        <ul data-testid="Summary" class="summary-module__summary__QjADA">
          <li data-testid="Body" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf summary-module__point__UgXPz">
            Supreme Court has a muscular 6-3 conservative majority
          </li>
          <li data-testid="Body" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf summary-module__point__UgXPz">
            Landmark law was passed in 1965 during civil rights era
          </li>
          <li data-testid="Body" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf summary-module__point__UgXPz">
            Having gutted one provision, court targets a second
          </li>
          <li data-testid="Body" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__base__o--Cl body-module__small_body__gOmDf summary-module__point__UgXPz">
            Trump administration backed Voting Rights Act challenge
          </li>
        </ul>
      </div>
      <div class="news-assistant-button-module__button-wrapper__APSUF news-assistant-button-module__inline__4CICR news-assistant-button-module__news-ax__aofyo" data-testid="news-assistant"><button text="test" class="button-module__button__Pqh0q button-module__primary__gnCmu button-module__round__QDFgq button-module__w_auto__Sem-F news-assistant-button-module__nx-button__ehQ4l" type="button" data-testid="news-assistant-button" fdprocessedid="e5bhhu">
        <span class="button-module__container__7hKTY news-assistant-button-module__button__OvyzU news-assistant-button-module__small__XCPki news-assistant-button-module__slide-in__V9hqJ">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" aria-hidden="true" focusable="false" role="presentation" data-testid="NewsAssistant" class="news-assistant-button-module__na-icon__YbG-6">
            <path d="M12.7734 3.35938L15 2.5L15.8203 0.3125C15.8594 0.117188 16.0547 0 16.25 0C16.4062 0 16.6016 0.117188 16.6406 0.3125L17.5 2.5L19.6875 3.35938C19.8828 3.39844 20 3.59375 20 3.75C20 3.94531 19.8828 4.14062 19.6875 4.17969L17.5 5L16.6406 7.22656C16.6016 7.38281 16.4062 7.5 16.25 7.5C16.0547 7.5 15.8594 7.38281 15.8203 7.22656L15 5L12.7734 4.17969C12.6172 4.14062 12.5 3.94531 12.5 3.75C12.5 3.59375 12.6172 3.39844 12.7734 3.35938ZM8.00781 2.89062L10.0391 7.34375L14.4922 9.375C14.7266 9.49219 14.8828 9.72656 14.8828 9.96094C14.8828 10.1953 14.7266 10.4297 14.4922 10.5078L10.0391 12.5781L8.00781 17.0312C7.89062 17.2656 7.65625 17.4219 7.42188 17.4219C7.1875 17.4219 6.95312 17.2656 6.875 17.0312L4.80469 12.5781L0.351562 10.5469C0.117188 10.4297 0 10.1953 0 9.96094C0 9.72656 0.117188 9.49219 0.351562 9.375L4.80469 7.34375L6.875 2.89062C6.95312 2.65625 7.1875 2.5 7.42188 2.5C7.65625 2.5 7.89062 2.65625 8.00781 2.89062ZM15 15L15.8203 12.8125C15.8594 12.6172 16.0547 12.5 16.25 12.5C16.4062 12.5 16.6016 12.6172 16.6406 12.8125L17.5 15L19.6875 15.8594C19.8828 15.8984 20 16.0938 20 16.25C20 16.4453 19.8828 16.6406 19.6875 16.6797L17.5 17.5L16.6406 19.7266C16.6016 19.8828 16.4062 20 16.25 20C16.0547 20 15.8594 19.8828 15.8203 19.7266L15 17.5L12.7734 16.6797C12.6172 16.6406 12.5 16.4453 12.5 16.25C12.5 16.0938 12.6172 15.8984 12.7734 15.8594L15 15Z"></path>
          </svg>
          <span data-testid="Text" class="text-module__text__0GDob text-module__white__kE5Pf text-module__medium__2Rl30 text-module__button_label__4BCvX news-assistant-button-module__text__AgZEg">
            Key Points
          </span>
        </span>
        </button>
      </div>
    </div>
  <div data-testid="paragraph-0" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__full_width__kCIGb body-module__small_body__gOmDf article-body-module__paragraph__Ts-yF">
    WASHINGTON, Oct 18 (Reuters) - The Voting Rights Act, a landmark law barring discrimination in voting, was a product of the U.S. civil rights era, sought by 
      <a data-testid="Link" referrerpolicy="no-referrer-when-downgrade" href="/world/nobel-peace-prize-winner-be-announced-year-overshadowed-by-trump-2025-10-10/" class="text-module__text__0GDob text-module__inherit-color__PhuPF text-module__inherit-font__1P1hv text-module__inherit-size__EyiQW link-module__link__INqxZ link-module__underline_default__-okuC">
        Nobel Peace Prize
      </a> 
    recipient Martin Luther King, passed by Congress and signed by Democratic President Lyndon Johnson in 1965.
  </div>
  next div is 
  <div data-testid="paragraph-1" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__small__sph8i body-module__full_width__kCIGb body-module__small_body__gOmDf article-body-module__paragraph__Ts-yF">
  subsequent divs numbered sequentially in data-testid attribute
author:

  <div data-testid="AuthorName" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__medium__2Rl30 text-module__tag_label__4kwMu">
    <span data-testid="Text" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__tag_label__4kwMu">
      By 
    </span>
    <a data-testid="Link" referrerpolicy="no-referrer-when-downgrade" href="/authors/jan-wolfe/" rel="author" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__medium__2Rl30 text-module__tag_label__4kwMu link-module__link__INqxZ link-module__underline_on_hover__YTwYC author-name-module__author__09Ri8">
      Jan Wolfe
    </a>
  </div>

date:

<time data-testid="Body" datetime="2025-10-18T20:01:29Z" class="text-module__text__0GDob text-module__dark-grey__UFC18 text-module__regular__qJJtA text-module__extra_small__8Buss body-module__base__o--Cl body-module__extra_small_body__Bfz20">
  <span class="date-line-module__date__Q468B">
    October 18, 2025
  </span>
  <span class="date-line-module__date__Q468B">
    3:01 PM CDT
  </span>
  <span class="date-line-module__date__Q468B">
    Updated 5 hours ago
  </span>
</time>

"""

"""
Bloomberg
headline:

  <div class="gridLayout_topContent__zu2nl">
    <header class="BasicHeader_header__t6U07">
      <h1 class="ArticleHeadline_headline__Lqhre ArticleHeadline_headlineDefaultLocale__H5pZb" data-component="headline">
        Traders ‘Spooked’ as Bank Lending Risk Puts Stock Market on Edge
      </h1>
    </header>
  </div>

content (partial bc paywall):

  <div class="styles_articleBlur__G34p_ body-content">
    <p class="ArticleBodyText_articleBodyContent__17wqE typography_articleBody__3UcBa" data-component="paragraph">
      The start of earnings season is exposing a potential crack in the stock market’s frothy foundation: risky lending by 
      some regional banks.
    </p>
    <p class="ArticleBodyText_articleBodyContent__17wqE typography_articleBody__3UcBa" data-component="paragraph">
      Shares of 
        <a href="https://www.bloomberg.com/quote/ZION:US" target="_blank" rel="noopener" class="media-ui-Link_link-tVkXhPLPofs-" data-component="link">
          Zions Bancorp
        </a> 
      and 
        <a href="https://www.bloomberg.com/quote/WAL:US" target="_blank" rel="noopener" class="media-ui-Link_link-tVkXhPLPofs-" data-component="link">
          Western Alliance Bancorp
        </a> 
      plunged Thursday after the companies said they were 
        <a href="https://www.bloomberg.com/news/articles/2025-10-16/zions-western-alliance-disclose-bad-loans-tied-to-alleged-fraud" target="_blank" rel="noopener" class="media-ui-Link_link-tVkXhPLPofs-" data-component="link">
          victims of fraud
        </a> 
      on loans to funds that invest in distressed commercial mortgages. The disclosures sent the 
        <a href="https://www.bloomberg.com/quote/BKX:Ind" target="_blank" rel="noopener" class="media-ui-Link_link-tVkXhPLPofs-" data-component="link">
          KBW Bank Index
        </a> to its <!-- -->worst day<!-- --> since April’s tariff tantrum. 
    </p>
  </div>

author:

<div class="ArticleByline_articleBylineAuthors__Y0EHu">
  By 
  <a class="ArticleByline_author__2tHRg ArticleByline_hasProfile__7yEbD" href="/authors/AViW1ik20h8/geoffrey-morgan" rel="author">
    Geoffrey Morgan
  </a> 
  and 
  <a class="ArticleByline_author__2tHRg ArticleByline_hasProfile__7yEbD" href="/authors/AVG2b3ry3O4/georgie-mckay" rel="author">
    Georgie McKay
  </a>
</div>

date:

<div class="BasicByline_timestamp__cSkw_">
  <div class="ArticleTimestamp_articleTimestamp__zlcvt" data-component="timestamp">
    <time datetime="2025-10-18T13:00:00.000Z" data-locale="en-US">
      October 18, 2025 at 8:00 AM CDT
    </time>
  </div>
</div>

"""

"""
NBC News
headline: (with dek)

  <div class="article-hero-headline layout-grid-item grid-col-10-l">
    <h1 class="article-hero-headline__htag lh-none-print black-print">
      Israel and Hamas trade accusations of ceasefire violations
    </h1>
    <div class="styles_articleDek__Y1jmL styles_withImage__tTh_v" data-testid="article-dek">
      Israel said that Hamas had carried out "a blatant violation of the ceasefire agreement" with attacks on its forces in the Rafah area. 
      Hamas restated its commitment to the truce and said it had no knowledge of any clashes.
    </div>
  </div>

content:
  
  <div class="article-body__content">
    <p id="anchor-5a1613" class="body-graf">
      Israel launched airstrikes on 
        <a href="https://www.nbcnews.com/world/middle-east/hamas-gangs-gaza-violence-ceasefire-israel-trump-disarm-rcna237928" target="_blank">
          southern Gaza early Sunday 
        </a>
      in the first major test of its ceasefire with Hamas, as the two sides traded accusations of significant breaches of the deal brokered by 
      President Donald Trump.
    </p>
    <p id="anchor-90c20e" class="body-graf">
      Israel said that Hamas had carried out “a blatant violation of the ceasefire agreement” with attacks on its forces in the Rafah area.
    </p>
    (subsequent <p>s with class="body-graf" and id="anchor-xxxxxx")
  </div>


author:

  <div class="article-inline-byline" data-testid="article-byline-inline" data-activity-map="inline-byline-article-top">
    By 
      <span class="byline-name" data-testid="byline-name">
        <a href="https://www.nbcnews.com/author/nick-duffy-ncpn1308472">
          Nick Duffy
        </a>
      </span>
    and 
      <span class="byline-name" data-testid="byline-name">
        Matt Bradley
      </span>
  </div>

date:

  <div class="styles_contentTimestampWithSource__FIhli" data-testid="article-body-timestamp">
    <time class="relative z-1" datetime="2025-10-19T15:20:37.859Z" data-testid="article-body-timestamp__timestamp" content="2025-10-19T15:20:37.859Z">
      Oct. 19, 2025, 5:23 AM CDT
        <span>
          &nbsp;/&nbsp;
        </span>
      Updated&nbsp;Oct. 19, 2025, 10:20 AM CDT
    </time>
  </div>

"""

"""
ABC News
headline: (with dek)

<div class="kCTVx qtHut lqtkC HkWF HfYhe kGyAC " data-testid="prism-headline">
  <h1 class="vMjAx gjbzK tntuS eHrJ mTgUP ">
    <span class="gtOSm FbbUW tUtYa vOCwz EQwFq yCufu eEak Qmvg nyTIa SRXVc vzLa jgBfc WXDas CiUCW kqbG zrdEG txGfn ygKVe BbezD UOtxr CVfpq xijV soGRS XgdC sEIlf daWqJ ">
      Thieves steal jewels with 'inestimable' value from Louvre museum
    </span>
  </h1>
  <p class="jxTEW Poyse uieav lqtkC HkWF HfYhe kGyAC ">
    <span class="gtOSm FbbUW tUtYa vOCwz EQwFq yCufu eEak Qmvg nyTIa SRXVc vzLa jgBfc WXDas CiUCW kqbG zrdEG txGfn ygKVe BbezD UOtxr CVfpq xijV soGRS XgdC sEIlf daWqJ ">
      The Paris museum said the jewels belonged to Napoleon and his wife.
    </span>
  </p>
</div>

content: (first few <p>s only)

  <div class="xvlfx ZRifP TKoO eaKKC EcdEg bOdfO qXhdi NFNeu UyHES " data-testid="prism-article-body">
    <p class="EkqkG IGXmU nlgHS yuUao MvWXB TjIXL aGjvy ebVHC ">
      PARIS and LONDON -- Several people disguised as construction workers broke into the world-famous Louvre Museum in Paris on Sunday,
      cracking open display cases and stealing jewelry that once belonged to Emperor Napoleon and his wife, officials said.
    </p>
    <p class="EkqkG IGXmU nlgHS yuUao lqtkC TjIXL aGjvy ">
      At least nine pieces of jewelry of "inestimable heritage and historical value" were taken in the brazen heist before the thieves made 
      their getaway on motorcycles, two ministers said.
    </p>
    <p class="EkqkG IGXmU nlgHS yuUao lqtkC TjIXL aGjvy ">
      "Investigations have begun, and a precise list of the stolen items is underway," the museum said in a statement.
    </p>
    <p class="EkqkG IGXmU nlgHS yuUao lqtkC TjIXL aGjvy ">
      Four thieves pulled off the apparently well-planned heist, according to authorities.
    </p>
  </div>
author: (with date)

  <div class="QHblV nkdHX mHUQ kvZxL hTosT whbOj " data-testid="prism-byline">
    <div class="VZTD mLASH BQWr OcxMG oJce ">
      <div class="kKfXc ubAkB VZTD rEPuv ">
        <div class="TQPvQ fVlAg HUcap kxY REjk UamUc WxHIR HhZOB yaUf VOJBn KMpjV XSbaH Umfib ukdDD ">
          <span class="tChGB zbFav ">
            By
          </span>
          <span>
            <a class="zZygg UbGlr iFzkS qdXbA WCDhQ DbOXS tqUtK GpWVU iJYzE " data-testid="prism-linkbase" href="https://abcnews.go.com/author/kevin_shalvey" target="_self">
              Kevin Shalvey
            </a>
            <span class="EpNlu ">
              , 
            </span>
          </span>
          <span>
            <a class="zZygg UbGlr iFzkS qdXbA WCDhQ DbOXS tqUtK GpWVU iJYzE " data-testid="prism-linkbase" href="https://abcnews.go.com/author/somayeh_malekian" target="_self">
              Somayeh Malekian
            </a>
            <span class="EpNlu ">
              , 
            </span>
          </span>
          <span>
            <a class="zZygg UbGlr iFzkS qdXbA WCDhQ DbOXS tqUtK GpWVU iJYzE " data-testid="prism-linkbase" href="https://abcnews.go.com/author/hugo_leenhardt" target="_self">
              Hugo Leenhardt
            </a>
            <span class="EpNlu ">
            , 
            </span>
          </span>
          <span>
            <a class="zZygg UbGlr iFzkS qdXbA WCDhQ DbOXS tqUtK GpWVU iJYzE " data-testid="prism-linkbase" href="https://abcnews.go.com/author/camilla_alcini" target="_self">
              Camilla Alcini
            </a>
            <span class="EpNlu ">
            , and 
            </span>
          </span>
          <span>
            <a class="zZygg UbGlr iFzkS qdXbA WCDhQ DbOXS tqUtK GpWVU iJYzE " data-testid="prism-linkbase" href="https://abcnews.go.com/author/bill_hutchinson" target="_self">
              Bill Hutchinson
            </a>
          </span>
        </div>
        <div class="VZTD mLASH gpiba "><div class="jTKbV zIIsP ZdbeE xAPpq QtiLO JQYD ">
        October 19, 2025, 12:36 PM
        </div>
      </div>
    </div>
  </div>
"""

"""
The Guardian

headline:

  <div style="--grid-area:headline" data-gu-name="headline" class="dcr-1fnjjtg">
    <div class="dcr-14emo0l">
      <div class="dcr-cohhs3">
        <h1 class="dcr-uc7bn6">
          Israel strikes Gaza and cuts off aid after reported attack by Hamas
        </h1>
      </div
    </div>
  </div>

content: (first two <p>s only)

  <div id="maincontent" class="dcr-1uvtuj9">
    <div class="article-body-commercial-selector article-body-viewer-selector dcr-11jq3zt">
      <p class="dcr-130mj7b">
        Israel launched waves of lethal airstrikes on Sunday and cut off all aid into Gaza “until further notice” 
        after a reported attack by Hamas, in escalations that marked the most serious threat so far to the increasingly 
        fragile ceasefire in the devastated territory.
      </p>
      <p class="dcr-130mj7b">
        <a href="https://www.timesofisrael.com/liveblog-october-19-2025/" data-link-name="in body link">
          Two Israeli soldiers
        </a>
        , including an officer, were killed in the Hamas attack. Palestinian officials said dozens died in the 
        retaliatory airstrikes.
      </p>
    </div>
  </div>

author:

  <address aria-label="Contributor info" data-component="meta-byline" data-link-name="byline" data-gu-name="byline">
    <div class="dcr-16bbvim">
      <a rel="author" data-link-name="auto tag link" href="https://www.theguardian.com/profile/william-christou">
        William Christou
      </a>
      <span>
        in Jerusalem and 
      </span>
      <a rel="author" data-link-name="auto tag link" href="https://www.theguardian.com/profile/jasonburke">
        Jason Burke
      </a>
    </div>
  </address>

date:

  <details style="--mobile-colour:var(--dateline)" data-gu-name="dateline" class="dcr-lp0nif">
    <summary class="dcr-1ybxn6r">
      <span class="dcr-u0h1qy">
        Sun 19 Oct 2025 15.11 EDT
      </span>
    </summary>
    First published on Sun 19 Oct 2025 02.23 EDT
  </details>
"""

"""
AP
headline:

  <div class="StoryPage-lede gtmMainScrollContent">
    <div class="StoryPage-lede-content">
      <div class="Page-breadcrumbs">
        <a class="Link " href="https://apnews.com/politics">
          Politics
        </a>
      </div>
    <h1 class="Page-headline">
      Trump suggests US will buy Argentinian beef to bring down prices for American consumers
    </h1>
    </div>
  </div>

content: (first few <p>s only)

  <div class="RichTextStoryBody RichTextBody">
    <p>
      ABOARD AIR FORCE ONE (AP) — President 
        <span class="LinkEnhancement">
          <a class="Link AnClick-LinkEnhancement" data-gtm-enhancement-style="LinkEnhancementA" href="https://apnews.com/hub/donald-trump">
            Donald Trump
          </a>
        </span> 
      said Sunday that the United States could purchase Argentinian beef in an attempt to bring down prices for American consumers.
    </p>
    <p>
      “We would buy some beef from Argentina,” he told reporters aboard Air Force One during a flight from Florida to Washington. 
      “If we do that, that will bring our beef prices down.”
    </p>
    <p>
      Trump promised earlier this week to address the issue as part of his efforts to keep inflation in check.
    </p>
    <p>
      U.S. beef 
        <span class="LinkEnhancement">
          <a class="Link AnClick-LinkEnhancement" data-gtm-enhancement-style="LinkEnhancementA" href="https://apnews.com/article/beef-prices-record-high-cattle-steak-cows-e9fc33bbaec6a76fb243e277bbbb7c0e">
            prices have been stubbornly high
          </a>
        </span> 
      for a variety of reasons, including drought and reduced imports from Mexico due to a flesh-eating pest in cattle herds there.
    </p>
  </div>

author: (with date)

<div class="Page-byline"><div class="Page-byline-info">
  <div class="Page-authors">
    By&nbsp;
    <span class="Link">
      CHRISTOPHER MEGERIAN
    </span>
  </div>
  <div class="Page-dateModified">
    <bsp-timestamp data-timestamp="1760921515000" data-recent-thresholdinhours="1">
      <template data-date-tpl="">
        Updated [hour]:[minute] [AMPM] [timezone], [monthFull] [day], [year]
      </template>
      <span data-date="">
        Updated 7:51 PM CDT, October 19, 2025
      </span>
    </bsp-timestamp>
  </div>
</div>

date:
"""

"""
Forbes
headline:

  <h1 class="speakable-headline font-base font-size color-base aY5Zr">
    Why No One Really Knows How Much Money The Trumps Are Making Right Now
  </h1>

content: (first few <p>s only)

<div class="fs-article fs-premium fs-responsive-text current-article font-body color-body bg-base font-accent article-body premium-container">
  <h2 class="subhead-embed color-accent bg-base font-accent font-size text-align">
    A holding company named DT Marks Defi LLC has taken in more money than almost any other entity in the president’s web of businesses. 
    But thanks to a secretive agreement that surfaced around the time of the inauguration, it remains unclear who is really receiving the cash.
  </h2>
  <hr class="embed-base rule-embed color-accent border-solid weight-light">
  <p>
    <strong>
      <abbr class="drop-cap color-accent font-accent">
        D
      </abbr>
      onald Trump has made a lot of money
    </strong> 
    this year, but no one really knows how much. It’s a mystery not because the president has a private business. Nor because he won’t share 
    his tax returns. Nor even because gains in cryptocurrency can be difficult to track. The main reason no one knows what Trump is making 
    is because of a single, secretive agreement that appeared around the time of the inauguration.
  </p>
  <p>
    At some point, apparently the start of the year, Trump owned 70% of a company named DT Marks Defi LLC, which in turn owned 75% of the 
    crypto project World Liberty Financial. The president’s financial disclosure report listed unnamed family members (presumably World 
    Liberty cofounders Don Jr., Eric and Barron) as the owner of the remaining 30%. But a monitor overseeing the Trump Organization 
    disclosed in a letter to a New York judge that her team learned in January that the first family was selling a stake in an unspecified 
    company that seems all but certain to be DT Marks Defi. That deal presumably changed the ownership structure of DT Marks Defi—though 
    exactly how remains unclear.
  </p>
  <p>
    The agreement came with no public announcement. World Liberty’s website acknowledges that DT Marks Defi holds a stake in the project, 
    but it doesn’t answer the key question—who exactly owns DT Marks Defi. Trump submitted his financial disclosure report in June, but 
    it appears to offer a snapshot of his holdings as of January 1, omitting later developments. The Trump Organization shows no interest 
    in revealing anything about the January agreement—what percentage the first family sold, who bought the stake, how much money was 
    involved, even whether the deal closed.
  </p>
</div>

author:

<p class="ujvJmzbB LfmqX">
  By
  <a class="_4tin10wS _9xFYp YbfXuVMn" aria-label="Dan Alexander" title="https://www.forbes.com/sites/danalexander/" href="https://www.forbes.com/sites/danalexander/" target="_self">
    Dan Alexander
  </a>
  <span class="S7tzPEZ-">
    ,
  </span>
</p>

date:

<div class="v8jKF" data-test-id="timeStamp">
  <time class="ycHdAQ4U UcPtB">
    Oct 15, 2025, 06:30am EDT
  </time>
  <span data-test-id="updatedTimeStamp" class="eJ_uo QCahZ">
    Updated Oct 15, 2025, 12:17pm EDT
  </span>
</div>
"""

"""
Fox News
headline:

<h1 class="headline speakable">
  Trading barbs from light-hearted to vicious, mayoral candidates make final appeal to New Yorkers
</h1>

content: (only first two <p>s)

  <div class="article-content">
    <div class="article-body">
      <p class="speakable">
        <a href="https://www.foxnews.com/category/us/new-york-city" target="_blank" rel="noopener">
          New York City
        </a> 
        mayoral contenders relentlessly criticized their opponents as they made their final pitch to voters Wednesday night 
        in the last debate before early voting starts Saturday.&nbsp;
      </p>
      <p class="speakable">
        Democratic nominee Zohran Mamdani, Independent candidate and former Gov. 
          <a href="https://www.foxnews.com/category/person/andrew-cuomo" target="_blank" rel="noopener">
            Andrew Cuomo
          </a> 
        and Republican nominee Curtis Sliwa once again traded barbs on the debate stage, meeting for the second time in less than a week.
      </p>
    </div>
  </div>

author: 

  <div class="author-byline">
    <span class="author-headshot">
      <img src="https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2025/04/340/340/img_1807.jpeg?ve=1&amp;tl=1" alt="Deirdre Heavey">
    </span> 
    <span>
      By
      <span>
        <a href="https://www.foxnews.com/person/h/deirdre-heavey">
          Deirdre Heavey
        </a> 
        <!---->
      </span>
    </span> 
    <span class="article-source">
      <a href="https://www.foxnews.com/" target="_blank">
        Fox News
      </a>
    </span> 
    <!---->
  </div>

date:

  <div>
    <span class="article-date">
      Published
      <a href="https://www.foxnews.com/html-sitemap/2025/october/23">
        <time datetime="2025-10-22T20:55:17-04:00">
          October 22, 2025 8:55pm EDT
        </time>
      </a>
    </span> 
    <!---->
  </div>

"""

"""
Axios

headline:

  <h1 data-cy="story-headline" class="text-soft-black-core h5 md:h3 font-regular">
    Medicare agency to recall thousands of staff next week
  </h1>

content: (confused by the span)

  <span data-schema="smart-brevity">
    <p>
      The Centers for Medicare and 
        <a class="gtmContentClick" data-vars-link-text="Medicaid" data-vars-click-url="https://www.axios.com/2025/07/08/medicaid-cuts-states" data-vars-content-id="4a6b52d3-72c8-4f57-9630-23bb3e6c0e51" data-vars-headline="Medicare agency to recall thousands of staff next week" data-vars-event-category="story" data-vars-sub-category="story" data-vars-item="in_content_link" href="https://www.axios.com/2025/07/08/medicaid-cuts-states" target="_self">
          Medicaid
        </a> 
      Services plans to recall about 3,000 staff who were furloughed because of the shutdown starting on Monday, officials confirmed to Axios. 
    </p>
    <p>
      <strong>
        The big picture: 
      </strong>
      CMS plans to tap fees it charges outside researchers to access its data to pay staff during 
        <a class="gtmContentClick" data-vars-link-text="the shutdown" data-vars-click-url="https://www.axios.com/2025/10/22/government-shutdown-democracy-failure-defense-leon-panetta" data-vars-content-id="4a6b52d3-72c8-4f57-9630-23bb3e6c0e51" data-vars-headline="Medicare agency to recall thousands of staff next week" data-vars-event-category="story" data-vars-sub-category="story" data-vars-item="in_content_link" href="https://www.axios.com/2025/10/22/government-shutdown-democracy-failure-defense-leon-panetta" target="_self">
          the shutdown
        </a>
      , a spokesperson said. 
    </p>
  </span>

author:

<a data-cy="byline-author" aria-label="Maya Goldman's author page" data-index="0" class="font-regular font-sans leading-none no-underline inline-flex items-center [&amp;&gt;.icon+span]:ml-2 [&amp;&gt;span+.icon]:ml-2 gtmContentClick" data-vars-content-id="4a6b52d3-72c8-4f57-9630-23bb3e6c0e51" data-vars-headline="Medicare agency to recall thousands of staff next week" data-vars-category="story" data-vars-sub-category="story" data-vars-label="Maya Goldman" data-vars-click-url="https://www.axios.com/authors/mgoldman" href="https://www.axios.com/authors/mgoldman">
  <span class="hover:underline focus:underline text-soft-black-core tag hover:text-interactive-secondary hover:underline underline-offset-2 focus:underline">
    Maya Goldman
  </span>
</a>

date:

  <span data-cy="time-rubric" class="flex flex-wrap items-center text-nowrap">
    54 mins ago - 
    <a data-cy="timestamp-section-link" aria-label="Health section" class="font-regular font-sans leading-none no-underline inline-flex items-center [&amp;&gt;.icon+span]:ml-2 [&amp;&gt;span+.icon]:ml-2 gtmContentClick !inline ml-0.5 hover:underline focus:underline" data-vars-content-id="4a6b52d3-72c8-4f57-9630-23bb3e6c0e51" data-vars-headline="Medicare agency to recall thousands of staff next week" data-vars-category="story" data-vars-sub-category="story" data-vars-item="topic" data-vars-label="Health" data-vars-deprecated-params="[object Object]" data-vars-click-url="https://www.axios.com/health" href="https://www.axios.com/health">
      <span>
        Health
      </span>
    </a>
  </span>

  but also had this in the <head>:
    <meta property="article:published_time" content="2025-10-23T01:12:05Z">

"""

"""
The Hill
headline:
  <h1 class="page-title">
		Has America’s economy gone K-shaped? Here’s what to know	
  </h1>

content: (first two <p>s only)
  <div class="article__text | body-copy | flow">
    ...
    <p>
      The U.S. 
        <a href="https://thehill.com/business/5567863-trump-economy-disapproval-poll/">
          economy
        </a> 
      is pulling apart: Booming for some, breaking for many.
    </p>
    <p>
      In other words, it’s looking 
        <a href="https://thehill.com/opinion/finance/5499218-ai-revolution-job-market/" data-type="link" data-id="https://thehill.com/opinion/finance/5499218-ai-revolution-job-market/" target="_blank" rel="noreferrer noopener">
          K-shaped
        </a> 
      — one branch climbs while the other falls. 
    </p>
  </div

author: (and date)

  <section class="article__header">
    ...
    <span>
			  by Andrew Dorn - 10/23/25 8:59 PM ET
        <br>
	  </span>
  </section>

date:

"""

"""
Politico
headline:

<h1 data-testid="title" class="mt-2 text-2xl font-bold leading-[1.12] tracking-[-.02rem] sm:leading-none sm:tracking-[-.05rem] md:text-[1.75rem] lg:text-[2.5rem]" style="">
  <!----> 
  Frustrations boil over as Vance delivers ‘firm’ message to Netanyahu
</h1>

content: (first two <p>s only)

  <p class="is-first-paragraph font-text text-lg leading-[1.6] mt-5 md:mt-[1.875rem]" data-v-47ab9839="">
    The White House is growing increasingly frustrated with Israel just two weeks after President Donald Trump 
    triumphantly announced a deal to end the war in Gaza and bring peace to the Middle East.
  </p>

  <p class="font-text text-lg leading-[1.6] mt-5 md:mt-[1.875rem]" data-v-47ab9839="">
    The mounting frustrations come as a succession of senior officials are passing through Israel this week 
    looking to keep a fragile ceasefire in place. They see some recent developments — the Israeli Defense Force’s 
    counter-attack in Gaza on Sunday, and the Knesset’s vote in favor of West Bank annexation, which Trump has 
    ruled out — as detrimental to the already fragile agreement between Israel and Hamas.
  </p>

author:

  <span class="text-xs leading-normal tracking-[0.1rem] text-gray-vulcan-44">
    <!--[-->
    <!--[-->
    By  
      <a href="https://www.politico.com/staff/eli-stokols" target="_top" class="uppercase hover:text-current font-bold text-gray-vulcan-51 js-tealium-tracking" data-tracking="mpos=center&amp;mid=ar_body&amp;lindex=62&amp;lcol=">
        Eli Stokols
      </a>
    <!--]-->
    <!--[--> 
    and  
      <a href="https://www.politico.com/staff/felicia-schwartz" target="_top" class="uppercase hover:text-current font-bold text-gray-vulcan-51 js-tealium-tracking" data-tracking="mpos=center&amp;mid=ar_body&amp;lindex=63&amp;lcol=">
        Felicia Schwartz
      </a>
    <!--]-->
    <!--]-->
  </span>

date:

  <time datetime="2025-10-23T17:58:21.097-04:00">
    10/23/2025 05:58 PM EDT
  </time>

"""

"""
Daily Mail
headline:

  <h1 class="headline--chWWs">
    <span class="is-paywalled container--EGRAu" data-content-propensity="1">
    </span>
    Chart-topping pop star who fled the US over racism to live in Kenya reveals the downsides of life in Africa
  </h1>

content: (first two <p>s only)
  <div itemprop="articleBody" data-mol-fe--article-body="true">
    <p class="mol-para-with-font">
      Milkshake hitmaker 
      <span data-track-module="internal-body-link">
        <span data-track-module="internal-body-link">
          <a style="font-weight: bold;" target="_self" href="/tvshowbiz/kelis/index.html" id="mol-0e30a010-b02d-11f0-bd8d-13b50ab38914">
            Kelis
          </a>
        </span>
      </span> 
      has ditched the US to begin a new life with her family in Kenya.
    </p>
    <p class="mol-para-with-font">
      The singer, 46, who lost her husband to 
        <span data-track-module="internal-body-link">
          <span data-track-module="internal-body-link">
            <a style="font-weight: bold;" target="_self" href="/news/cancer/index.html" id="mol-0e3f9430-b02d-11f0-bd8d-13b50ab38914">
              cancer
            </a>
          </span>
        </span> 
      in 2022, relocated to the East African country earlier this year to start farming and developing her own luxury resort.
    </p>

author:

  <p class="author-section byline-plain">
    By 
      <a href="/profile-1641/jacques-peterson.html" class="author">
        JACQUES PETERSON, US SENIOR ENTERTAINMENT REPORTER
      </a> 
  </p>

date:

  <p class="byline-section">
    <span class="article-timestamp article-timestamp-published"> 
      <span class="article-timestamp-label">
        Published:
      </span> 
      <time datetime="2025-10-23T21:54:45+0100"> 
        16:54 EDT, 23 October 2025 
      </time> 
    </span>
      | 
    <span class="article-timestamp article-timestamp-updated"> 
      <span class="article-timestamp-label">
        Updated:
      </span> 
      <time datetime="2025-10-23T21:56:42+0100"> 
        16:56 EDT, 23 October 2025 
      </time> 
    </span> 
  </p>

"""