# EC601 Project 2 Twitter API

## Overview
This project aims to collect tweets based on user from Twitter API v2 from accessing endpoints and saving tweets collected in CSV format. More specifically, 100 most recent tweets from Elon Musk was collected through the User Lookup endpoint to receive up-to-date details on a given user. Below, there are detailed steps on how the API was used and result collected.

## How to use
### Prerequisites to Start
1) Go to the developer portal dashboard https://developer.twitter.com/en/portal/dashboard 
2) Sign in with your developer account or create one if you don't already have one
3) Create a new project, give it a name and a description
Using jupyter notebook to code in python
4) In your terminal, type "brew install jupyter"
5) Upon installation, type "jupyter notebook" which a new browser would pop up 

### Code Implementation in Jupyter Notebook
1) Follow the folder twitter_api.ipynb step by step 
2) Prior to step 2, type export 'BEARER_TOKEN'='<Your_bearer_token>' in your terminal. Your bearer token can be found in your developer account from creating a new project
3) In step 3, url can be changed to any users you want to analyze. 
"https://api.twitter.com/2/users/'<user account id you want to explore>'/tweets"
Change '<user account id you want to explore>' into a user account id that you want to explore using https://codeofaninja.com/tools/find-twitter-id/ to search for the id
4) Hit Run for each cell and your result should display

## Results
Results can also be seen in tweets.csv
,conversation_id,created_at,lang,text,id
0,1442142105132953600,2021-09-26T18:41:48.000Z,en,@wadeanderson Noted. You should be able to press mic button &amp; say “bug report …”,1442197732882632707
1,1442160267283075074,2021-09-26T18:39:25.000Z,und,@coffeetabletsla @kimpaquette Ok,1442197132103061508
2,1442160267283075074,2021-09-26T18:30:03.000Z,en,"@kimpaquette A helpful case to consider, as the roads intersect at unusual angles",1442194774501462017
3,1442058753700810757,2021-09-26T09:31:38.000Z,en,@pcgamer True,1442059275157843971
4,1441855697973620736,2021-09-26T08:47:22.000Z,en,@bluemoondance74 @NASASpaceflight @SpaceX “Comes in discreet packaging”,1442048135434539009
5,1441926415201579011,2021-09-26T08:38:51.000Z,en,@cnunezimages @SpaceX Well ya see we need to reach around the rocket to uhh …,1442045993684324352
6,1441527389419311104,2021-09-26T00:06:35.000Z,und,@omespino 🤣,1441917078894751746
7,1441801120406454272,2021-09-25T20:54:10.000Z,en,@SawyerMerritt @Tesla Absolutely! Tesla team rocks 💕,1441868653578711040
8,1441569570825801729,2021-09-25T19:47:33.000Z,en,"@Sushihunter2 @pitt_geoff @rajz06 @Tesla @Everman We use no cobalt at all in most of our cars &amp; tiny amounts in others (going to zero soon), whereas phones &amp; laptops primarily use cobalt",1441851891000889350
9,1441843442099769352,2021-09-25T19:44:54.000Z,en,"@RenataKonkoly @Erdayastronaut And booster used to be 70m, but this required an awkward half barrel width of steel, so now it’s 69m",1441851222537879556
10,1441793752075472900,2021-09-25T19:24:28.000Z,en,@Nick_Stevens_Gr Haha so true of rocket engine development,1441846082556792838
11,1441810056358477828,2021-09-25T18:52:21.000Z,und,@Teslarati @KlenderJoey https://t.co/lN4RH9u99a,1441837997645729794
12,1441673474011975681,2021-09-25T08:13:30.000Z,en,@WholeMarsBlog Very much a beta calculation. It will evolve over time to more accurately predict crash probability.,1441677227565850628
13,1441560961593262081,2021-09-25T00:38:07.000Z,und,@AaronS5_ Yes,1441562625662464000
14,1441560961593262081,2021-09-25T00:31:30.000Z,en,"FSD Beta request button goes live tonight, but FSD 10.1 needs another 24 hours of testing, so out tomorrow night",1441560961593262081
15,1441439342472437762,2021-09-24T18:54:43.000Z,en,"@thesheetztweetz Chris was an early employee of SpaceX, and made a significant contribution, but was not a cofounder",1441476204901638148
16,1441243705705254917,2021-09-24T03:30:51.000Z,en,RT @SpaceX: More pics from @inspiration4x return → https://t.co/095WHX44BX https://t.co/Rxb49W4arV,1441243705705254917
17,1441202383732699141,2021-09-24T00:46:39.000Z,und,https://t.co/2jsF5hTWCP,1441202383732699141
18,1441201947785121794,2021-09-24T00:44:55.000Z,und,https://t.co/4QNllqZ75o,1441201947785121794
19,1441177680683024389,2021-09-24T00:44:38.000Z,en,@SpaceXMR Maybe reality is a Rick &amp; Morty episode,1441201877715128320
20,1440421014291173380,2021-09-23T07:27:01.000Z,en,@RenataKonkoly @FelixSchlang @KathyLueders @SpaceX @BoeingSpace I didn’t think so at the time,1440940751718948866
21,1440751226094686214,2021-09-22T20:53:54.000Z,en,@thesheetztweetz So pointy! https://t.co/XMRQKpmy0t,1440781421665161223
22,1440771185231294470,2021-09-22T20:50:08.000Z,en,@BillyM2k Super important for Doge fees to drop to make things like buying movie tix viable,1440780474662543370
23,1440608913754181634,2021-09-22T20:43:05.000Z,en,@EvaFoxU @ChesterNoBS @truth_tesla Giga Berlin will help a lot,1440778702476832778
24,1440693417260957702,2021-09-22T18:40:46.000Z,en,@SueOrigin @SciGuySpace That would break the NASA budget!,1440747919108296708
25,1440740197071671297,2021-09-22T18:26:45.000Z,en,"@PPathole @simongerman600 @waitbutwhy @SeppalaVilleEN AI used to be #1, until last year https://t.co/KSuaheBLLg",1440744391069425666
26,1440740197071671297,2021-09-22T18:18:26.000Z,en,@simongerman600 @waitbutwhy @SeppalaVilleEN Birth rate collapse is the biggest threat to human civilization,1440742298518577156
27,1440714711356432392,2021-09-22T17:54:22.000Z,en,@wapodavenport We always do flight readiness reviews! This argument makes no sense.,1440736242195329028
28,1440608913754181634,2021-09-22T17:40:20.000Z,en,@EvaFoxU @ChesterNoBS @truth_tesla Logistics is underrated,1440732712289984519
29,1440608913754181634,2021-09-22T17:27:46.000Z,en,"@EvaFoxU @ChesterNoBS @truth_tesla Exactly. Giga Shanghai makes cars for export in first half of quarter, then cars for far away parts of China, then cars for nearby parts of China. 

Net result is a crazy wave of deliveries end of quarter. It is tough on our team, so we’re hoping to reduce the wave in Q4 &amp; Q1.",1440729549239558148
30,1440485977059827712,2021-09-22T06:44:29.000Z,en,@rookisaacman @ArceneauxHayley @DrSianProctor @ChrisSembroski @inspiration4x @StJude Great view of Earth!,1440567662258442247
31,1440483489996959754,2021-09-22T02:20:40.000Z,en,@HistoryInPics Tesla is the king of car farts!,1440501267944513537
32,1440419465242439681,2021-09-22T01:05:45.000Z,en,"@ro_ma_vive @cybrtrkguy Hopefully worldwide long-term, but insurance is a regulatory labyrinth/escape room!",1440482413973409802
33,1440419465242439681,2021-09-22T01:01:46.000Z,en,"@cybrtrkguy The regulatory process for approval to offer insurance is extremely slow &amp; complex, varying considerably by state. 

Tesla is hoping to offer real-time (based on actual driving history) insurance in Texas next month.

Probably next year before we get approval in New York.",1440481412835016705
34,1440416990204624900,2021-09-21T20:45:46.000Z,en,"RT @DrSianProctor: The moment when me and my amazing crew, @rookisaacman, @ArceneauxHayley, @ChrisSembroski opened up the @SpaceX cupola fo…",1440416990204624900
35,1440281601485664267,2021-09-21T17:06:09.000Z,en,"@ElectricRaph @28delayslater @KounisTou Good point, we could enable visualization before control. Will enable that option hopefully next month.",1440361722473156611
36,1440281601485664267,2021-09-21T17:01:06.000Z,en,@28delayslater @KounisTou 10.1 should solve that last cone issue,1440360450177204230
37,1440358962432339983,2021-09-21T16:55:11.000Z,en,RT @Tesla: Solar Roof powers Buffalo Heritage Carousel in NY 🌞 https://t.co/cxFFwmuQ2e,1440358962432339983
38,1440159176685088774,2021-09-21T04:22:37.000Z,en,@TeslaOwnersEBay @TeslaGong @inspiration4x Definitely upgraded toilets :) We had some challenges with it this flight.,1440169571466371073
39,1439990574203826181,2021-09-21T04:01:31.000Z,en,"@carsonight Not super surprising, given that internal combustion engine cars literally have “combustion” in the name",1440164262761021448
40,1440159176685088774,2021-09-21T03:48:20.000Z,en,"@TeslaGong @inspiration4x Yeah, a little oven for heating food &amp; Starlink wifi",1440160941505585159
41,1440159176685088774,2021-09-21T03:41:19.000Z,en,Just met with the @Inspiration4x crew in Florida to congratulate them in person. Such great people!,1440159176685088774
42,1439990273346465796,2021-09-20T18:19:37.000Z,en,@ray4tesla Tesla has not yet decided on a fourth Gigafactory location,1440017820167938054
43,1439563373256093698,2021-09-20T06:36:33.000Z,en,"@AustinTeslaClub To be precise, completely &amp; immediately reusable orbital rockets are the fundamental breakthrough needed to make life multiplanetary",1439840888537194496
44,1439828784216039424,2021-09-20T06:34:07.000Z,en,@teslaownersSV @Tesla Which games did they like most?,1439840278362329094
45,1439804882958041088,2021-09-20T04:31:53.000Z,en,@tegmark Nice work!,1439809514308620293
46,1439455901962801158,2021-09-20T03:07:51.000Z,en,@teslaownersSV @TeslaGong @WholeMarsBlog Good,1439788369257639939
47,1439455901962801158,2021-09-20T03:06:19.000Z,en,"@TeslaGong @teslaownersSV @WholeMarsBlog No, has to be turned on by car owner",1439787982475743241
48,1439455901962801158,2021-09-20T03:05:31.000Z,und,@Jason_Hess_ @WholeMarsBlog Yes,1439787780180221954
49,1439455901962801158,2021-09-20T03:05:01.000Z,en,@teslaownersSV @WholeMarsBlog Tesla insurance calculator will show status in real-time &amp; tell you what actions are needed to be rated “good driver”,1439787653394747395
50,1439455901962801158,2021-09-20T03:04:00.000Z,en,@BLKMDL3 @WholeMarsBlog 7 days after approval to log driving style,1439787397022199812
51,1439720509420285953,2021-09-20T03:02:56.000Z,en,@starbasergv Not a tiny engine,1439787129253597184
52,1439455901962801158,2021-09-20T03:02:02.000Z,en,"@WholeMarsBlog Remarkable how few people realize this capability exists. Many think it is 5 years away! With public beta rollout in coming weeks, awareness should improve dramatically.",1439786904443146240
53,1439693847827820545,2021-09-19T21:15:25.000Z,en,@FiveTweetTSLA @tesla_lion @archillect Seems that way,1439699675494461440
54,1439693847827820545,2021-09-19T21:08:37.000Z,en,"@archillect Looks fine. Take 2 aspirin, call me in the morning.",1439697964369317888
55,1439676763873976321,2021-09-19T20:27:41.000Z,en,@TheMarsSociety @NASA Some amount of cooperation would be good,1439687664547115011
56,1439551459763314692,2021-09-19T19:07:05.000Z,en,@RenataKonkoly @rhensing @johnkrausphotos Absolutely,1439667378120499201
57,1439551459763314692,2021-09-19T19:00:07.000Z,en,@rhensing He’s still sleeping,1439665626914635783
58,1439458059449999364,2021-09-19T18:58:51.000Z,en,@stats_feed Needs a little warming up,1439665308101402643
59,1439424186724851721,2021-09-19T14:39:45.000Z,en,@AustinTeslaClub @Tesla @TeslaOwnersEBay @TeslaOwnersUAE @EvaFoxU @leastImAlive @teslaownersSV @gailalfa1 @live_munro @OwenSparks_ I wish there were more,1439600100490334220
60,1439424186724851721,2021-09-19T14:38:33.000Z,en,@AustinTeslaClub @Tesla @TeslaOwnersEBay @TeslaOwnersUAE @EvaFoxU @leastImAlive @teslaownersSV @gailalfa1 @live_munro @OwenSparks_ So few products that you truly love 💕,1439599799049801728
61,1439408853515386880,2021-09-19T02:15:27.000Z,en,@inspiration4x @ArceneauxHayley @rookisaacman @DrSianProctor @ChrisSembroski @StJude Count me in for $50M,1439412791815950336
62,1439366880310046721,2021-09-18T23:13:01.000Z,en,Congratulations @Inspiration4x!!!,1439366880310046721
63,1439366720079204357,2021-09-18T23:12:22.000Z,en,"RT @SpaceX: Splashdown! Welcome back to planet Earth, @Inspiration4x! https://t.co/94yLjMBqWt",1439366720079204357
64,1439350960527134722,2021-09-18T22:16:22.000Z,en,@OwenSparks_ @ChrisSembroski One of my favorite movies,1439352625573605378
65,1439289629983879180,2021-09-18T21:54:27.000Z,en,"@TeslaGong @BryceSpaceTech Yes

No, but it will get refilled &amp; maybe cargo transfer",1439347109099184138
66,1439289629983879180,2021-09-18T21:43:12.000Z,en,"@enn_nafnlaus @BryceSpaceTech Making life multiplanetary is an extremely hard, but not impossible, problem",1439344277063192581
67,1439343752460574726,2021-09-18T21:41:06.000Z,en,RT @SpaceX: Dragon has entered its last orbit before reentry and splashdown → https://t.co/bJFjLCzWdK https://t.co/rAeaXJLLIb,1439343752460574726
68,1439289629983879180,2021-09-18T19:21:57.000Z,en,@BryceSpaceTech Still basically nothing compared to the orbital mass flux needed for a base on moon or Mars,1439308731913748488
69,1439303626565038087,2021-09-18T19:01:40.000Z,ro,RT @SpaceX: Orbital moonrise https://t.co/vrx8Jzeu1t,1439303626565038087
70,1438837949349646336,2021-09-18T19:01:05.000Z,en,"@kittynouveau Probably will trap a Tesla with the production Autopilot build, but won’t work with FSD. Using a ring of cones would stop FSD though.",1439303480330571780
71,1439188261419855872,2021-09-18T13:51:56.000Z,en,@NevanRead @A11electric It will be there,1439225680693186571
72,1414203506186100736,2021-09-18T13:48:32.000Z,en,"@vincent13031925 This engine needs to be 10X lower cost. Order of magnitude change is good reason for a new name. 

What really matters is not yet another “advanced” rocket engine, as there are many such devices, but there has never been a cheap (&lt;$1000/Ton-force) rocket engine. Not even close",1439224823549411329
73,1439167494107787265,2021-09-18T13:34:30.000Z,en,@slashdot Sigh,1439221294738903040
74,1414203506186100736,2021-09-18T12:38:20.000Z,en,"@SamTwits @Erdayastronaut @PPathole @vincent13031925 Long chain hydrocarbons, like kerosene, have excellent volumetric energy density, but what you really want for rockets is best way to bind hydrogen, which is CH4. 

Also, easy to make &amp; store CH4+O2 from CO2+H2O, which are abundant on Mars.",1439207158588088320
75,1439056137572085761,2021-09-18T12:26:46.000Z,und,@SpaceX ♥️ 🌍 🌎 🌏 ♥️,1439204246382125059
76,1414203506186100736,2021-09-18T12:14:57.000Z,en,"@Erdayastronaut @PPathole @vincent13031925 Fully reusable rockets want high T/W to minimize $/ton to orbit, because propellant cost actually matters",1439201272503144451
77,1439167980634402824,2021-09-18T12:00:59.000Z,en,@WholeMarsBlog Automatically drive to most obvious location unless occupant says otherwise,1439197760478134273
78,1439180414757875714,2021-09-18T11:47:37.000Z,en,"@WatchersTank @SpaceX With that, Ship is basically begging for an extra 3 engines",1439194394649837568
79,1439180414757875714,2021-09-18T11:46:33.000Z,und,@WatchersTank @SpaceX 33,1439194125908299777
80,1439083556626567169,2021-09-18T08:26:30.000Z,en,@Aristot21520213 @ray4tesla Exactly,1439143782478450692
81,1439078509872234497,2021-09-18T07:01:59.000Z,en,@ignaciobelieres @oza_shiv @lrocket “Ignition!”,1439122512856731648
82,1439078509872234497,2021-09-18T06:54:13.000Z,en,@oza_shiv @lrocket Throw in some hydrogen &amp; lithium for a real party,1439120557287563265
83,1439078509872234497,2021-09-18T06:52:58.000Z,und,@oza_shiv @lrocket 🔥,1439120245831131136
84,1439078509872234497,2021-09-18T06:11:05.000Z,en,@lrocket What propellant?,1439109703162814468
85,1439090465698041861,2021-09-18T04:54:38.000Z,en,"Moving at ~23 times speed of sound, circling Earth every ~90 minutes https://t.co/AncsjFpirC",1439090465698041861
86,1439037002951708677,2021-09-18T01:43:23.000Z,en,"@hiromichimizuno Ironically, yes at this time. FSD beta system at times can seem so good that vigilance isn’t necessary, but it is. Also, any beta user who isn’t super careful will get booted. 

2000 beta users operating for almost a year with no accidents. Needs to stay that way.",1439042334155497474
87,1438997247903952898,2021-09-18T01:16:17.000Z,en,"@Erdayastronaut @inspiration4x Yeah. We’d use our Ka parabolics or laser links for Dragon, Starship or other spacecraft as soon as they got above cloud level.",1439035515517509636
88,1438997247903952898,2021-09-17T23:17:36.000Z,en,@inspiration4x Sorry it was cold! Dragon will have a food warmer &amp; free wifi next time :),1439005647610290183
89,1438982407487643651,2021-09-17T21:45:15.000Z,en,"RT @SpaceX: The @inspiration4x crew is set to return to Earth on Saturday, September 18 with a targeted splashdown at 7:06 p.m. EDT in the…",1438982407487643651
90,1438982388491689985,2021-09-17T21:45:11.000Z,en,"RT @inspiration4x: Our crew chatted from space with the patients of @StJude! Watch the event here: https://t.co/LP6ZHOO8cq

Support St. Jud…",1438982388491689985
91,1438686351197622277,2021-09-17T21:36:21.000Z,en,@TeslaNY Jay is right,1438980165942620166
92,1438928760846290948,2021-09-17T18:12:05.000Z,en,"Please add your voice to the public comments. Support is greatly appreciated! 

Humanity’s future on the moon, Mars &amp; beyond depends upon it.

Thanks, 
Elon https://t.co/5K6Wda57EP",1438928760846290948
93,1438919113859010562,2021-09-17T17:33:45.000Z,en,RT @SpaceX: The @Inspiration4x crew will share a live on-orbit update about their multi-day journey aboard the Dragon spacecraft at ~5:00 p…,1438919113859010562
94,1416416608990294017,2021-09-17T08:21:58.000Z,en,"@TrungTPhan The lesson from “tortoise &amp; hare” is not that tortoises are faster, but rather that hares should not be complacent",1438780252474560513
95,1438684370785783808,2021-09-17T07:48:30.000Z,en,@cleantechnica September will be interesting,1438771833516564482
96,1438747500010168322,2021-09-17T06:34:35.000Z,en,"@StianWalgermo Technology probably ready in a few months, thereafter limited by regulatory approval",1438753228234047490
97,1438747500010168322,2021-09-17T06:25:59.000Z,en,"@IvanEscobosa Beta button will request permission to assess driving behavior using Tesla insurance calculator. If driving behavior is good for 7 days, beta access will be granted.",1438751064765906945
98,1438747500010168322,2021-09-17T06:15:07.000Z,und,@Gf4Tesla Yes,1438748333250592771
99,1438747500010168322,2021-09-17T06:14:03.000Z,en,@OvershieId Next month,1438748063527575555  
