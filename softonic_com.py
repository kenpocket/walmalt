import re
import threading
from pymongo import MongoClient
import atexit
from sshtunnel import SSHTunnelForwarder
import requests
from parsel import Selector
from copy import deepcopy
import pymongo

brand = '''1.1.1.1: Faster & Safer Internet
100 Mystery Buttons
10X Fire GFX Sensitivity Tool
10bii Financial Calculator
1945 Air Force: Airplane games
2 Player games : the Challenge
2112TD: Tower Defense Survival
2248: Number Games 2048 Puzzle
3D Anatomy
60 Seconds! Atomic Adventure
60 Seconds! Reatomized
75 Hard
88 Fortunes Slots Casino Games
911 Operator
@Voice Premium License
A Dance of Fire and Ice
A Dark Room ®
ABCmouse.com
ADP Mobile Solutions
AFK Arena
AMC+
APRSdroid - APRS Client
ARC Launcher® Pro Themes DIY
ASA's Sailing Challenge
ASCCP Management Guidelines
AT&T Call Protect
AVG AntiVirus & Security
Abi: A Robot's Tale
Acode - code editor | FOSS
Adobe Acrobat Reader: Edit PDF
Adobe Express: Graphic Design
Affirm: Buy now, pay over time
Afterpay - Buy Now. Pay Later
Age of Apes
Age of Frostfall
Age of History II
Age of Magic: RPG & Strategy
Age of Origins
AirMirror Receiver Pro
AirPlayMirror
Airbnb
Akinator
Alchemy Stars: Aurora Blast
AlfaOBD
AlfredCamera Home Security app
AliExpress
Alibaba.com - B2B marketplace
Alien: Blackout
AllTrails: Hike, Bike & Run
Amazing Slow Downer
Amazon Fire TV
Amazon Freevee
Amazon Music: Discover Songs
Amazon Photos
American Airlines
Ancestry: Family History & DNA
Angry Birds Dream Blast
Angry Birds Journey
Angry Neighbor
Animal Crossing: Pocket Camp
Animation Throwdown: Epic CCG
Ant Legion: For The Swarm
Antistress - relaxation toys
Apex Legends Mobile
Apex News: Breaking & Local
Apple Music
Aquarium Land
Archer Forest : Idle Defence
Archero
Ark of War: Aim for the cosmos
Arknights
Army Men Strike: Toy Wars
ArriveCAN
Art Puzzle - jigsaw art games
Art of War: Legions
Artery Gear: Fusion
Ashley Madison
Asphalt 8 - Car Racing Game
Atlas Earth - Buy Virtual Land
Attack the Light
Audible: audiobooks & podcasts
Audiomack: Music Downloader
Auric Icon Pack
Automatic Call Recorder Pro
Avakin Life - 3D Virtual World
Awaken: Chaos Era
Awf Pixel - watch face
Azur Lane
BALLOZI Vero Watch Face
BATTLESHIP - Multiplayer Game
BJA: Card Counting Trainer Pro
BLK Dating: Meet Black Singles
BRIO World - Railway
BTS Island: In the SEOM
BURGER KING® App
Baba Is You
Baba Wild Slots - Casino Games
Babbel - Learn Languages
Backgammon - Lord of the Board
BaconReader Premium for Reddit
Bad North: Jotunn Edition
Badoo - Dating. Chat. Meet.
Baldur's Gate Enhanced Edition
Ball Bounce
Ball Sort - Color Puzzle Game
Ballistic X
Balls Go High
Bank of America Mobile Banking
Basket Battle
Battle Chasers: Nightwar
Battle Warship: State War.io
Bazooka Boy
Be The King: Judge Destiny
BeReal. Your friends for real.
Beat Maker Pro - DJ Drum Pad
Beatstar - Touch Your Music
Beauty Sporty Fit Watch Face
Ben 10: Up to Speed
Bendy and the Ink Machine
Bermuda Adventures Farm Island
Best Buy
Best Fiends - Match 3 Games
Bible Home - Daily Bible Study
Bible Offline-KJV Holy Bible
Big Farm: Mobile Harvest
Big Fish Casino - Social Slots
Bigo Live - Live Streaming App
Bike Race Pro by T. F. Games
Billionaire Casino Slots 777
Bingo Aloha-Live Bingo Story
Bingo Bash: Live Bingo Games
Bingo Blitz™️ - Bingo Games
Bingo Frenzy-Live Bingo Games
Bingo Journey - Lucky Casino
Bingo Party - Lucky Bingo Game
Bingo Pop: Play Live Online
Bingo Showdown - Bingo Games
Bingo Story – Bingo Games
Bingo Wild - BINGO Game Online
Black Desert Mobile
Black Magic Horoscope
Black Pie - Icon Pack
Blade Idle
Blaze Backless Icon Pack
Blaze Dark Icon Pack
Bleach: Brave Souls Anime Game
Blink Home Monitor — Smart Home Security App
Block Box Skyland Sword
Block Craft 3D：Building Game
Block Crazy Robo World
Blood Pressure App Pro
Blood Pressure Monitor & Info
Blood Pressure Pro
Bloodline: Heroes of Lithas
Blue Archive
Blue Iris
Board Kings: Board dice games
Bob's World - Super Run Game
Booking.com: Hotels and more
Borealis - Icon Pack
Bored Ape Creator - NFT Art
Boris and the Dark Survival
Bottle Jump 3D
Bowling Crew — 3D bowling game
Bowmasters
Bra Maker
Brain Test: Tricky Puzzles
Brave Private Web Browser
Bravo Booster: One-tap Cleaner
Bravo Cleaner: Speed Booster
Brawl Stars
Breaker Fun - Rescue Adventure
Brick Out - Shoot the ball
Bridge Constructor Portal
Bridge Race
Brigit: Borrow & Build Credit
Broadcastify Police Scanner Pro
Bubble Pop Origin! Puzzle Game
Bubble Shooter Star
Bubble Shooter: Panda Pop!
Bucket Crusher
Bud Farm: Idle Tycoon
Buenovela - Novel, Book, Story
Bully: Anniversary Edition
Bumble - Dating. Friends. Bizz
Burner: 2nd Phone Number Line
Button Fever
BuzzCast - Live Video Chat App
BuzzKill - Phone Superpowers
CBS
CC Booster
CC Cleaner
CC FileManager
CCW – Concealed Carry 50 State
CDisplayEx Comic Reader
CE5 Contact
CHRONO TRIGGER (Upgrade Ver.)
CHUCHEL
CRUMB
CSR 2 - Drag Racing Car Games
Caesars Slots: Casino games
Cafe - Live video chat
Call Mirabel Encanto Fake Chat
Call of Antia: Match 3 RPG
Call of Duty Mobile Season 7
CallApp: Caller ID & Recording
Calm - Sleep, Meditate, Relax
Calorie Counter by Lose It!
CamScanner - PDF Scanner App
Cancel Tyranny
Candy Crush Friends Saga
Candy Crush Jelly Saga
Candy Manor - Home Design
Canva: Design, Photo & Video
CapCut - Video Editor
Capital One Mobile
Car Cops
Car Launcher Pro
Car Race 3D: Car Racing
Car Stunts Master - Car Racing
Carcassonne: Official Board Game -Tiles & Tactics
Card Master
Cards, Universe & Everything
Cargo Truck Parking
Cars Arena: Fast Race 3D
Cartoon Photo PRO
Cash Bash Casino - Vegas Slots
Cash Burst - Lucky Vegas Slots
Cash Carnival Coin Pusher Game
Cash Frenzy™ - Casino Slots
Cash Tornado™ Slots - Casino
Cashman Casino Las Vegas Slots
Cast for Chromecast & TV Cast
Castle of Illusion
Castlevania: SotN
Cat Escape
Cat Fishing Simulator
Catan Classic
Central for DayZ - Pro Unlocker
Chamet - Live Video Chat&Meet
Chapters: Interactive Stories
Charm King
Chase Mobile
Chess - Play and Learn
Chess Pro
Chester inform LCD
Chick-fil-A®
Chief Almighty
Chime – Mobile Banking
Chispa: Dating App for Latinos
Chronicle of Infinity
Citizen: Local Safety Alerts
City of Crime: Gang Wars
Civilization Revolution 2
Clapper: Video, Live, Chat
Clash of Empire: Empire Age
Classic Slots™ - Casino Games
Clawee - Real Claw Machines
Clean Phone: Booster, Master
Clime: NOAA Weather Radar Live
Clockmaker: Match 3 Games!
Club Vegas Slots: Casino Games
Clue: The Classic Mystery Game
Cocktail Party: Drink Recipes & Ingredient Library
Coco - Live Video Chat coconut
Coffee Meets Bagel Dating App
Coffee Stack
Coin Master
Collect Em All! Clear the Dots
Conflict of Nations: WW3 Game
Construction Master 5
Construction Master Pro
Construction Simulator 2
Construction Simulator 2014
Construction Simulator 3
Contacts
Contractor Estimate & Invoice
Cookie Jam Blast™ Match 3 Game
Cookie Jam™ Match 3 Games
Cookie Run: Kingdom
Cooking Diary® Restaurant Game
Cooking Fever: Restaurant Game
Cooking Madness -A Chef's Game
Copy My Data: Transfer Content
Costco Wholesale
Couch to 5K®
Count Masters: Stickman Games
Counterside
Covet Fashion - Dress Up Game
Craft Loki Sword Diamond
Craft Playtime: Hide and Seek
Craft Robo Clever Rainbow
Craft Sword Mini Fun
Craftman Go
Craftsman: Building Craft
Crayon Icon Pack
Crazy Drop
Crazy Fox - Big win
Crazy Plane Landing
Crowd Evolution!
Crumbl Cookies
Crunchyroll
Crying Suns
CryptoTab Browser Pro Level
Cube Card
Cubes Empire Champions
Cultist Simulator
Cut the Rope GOLD
Cyber Surfer: Beat&Skateboard
Cytus II
D&D Beyond
D&D Lords of Waterdeep
DAVx⁵ – CalDAV CardDAV WebDAV
DAZN: Stream Live Sports
DHgate-online wholesale stores
DISSIDIA FINAL FANTASY OO
DIY Makeup
DNA Altering
DOOM
DOOM II
DOP Love Story: Delete Stories
DRAGON BALL LEGENDS
DRAGON BALL Z DOKKAN BATTLE
DRAGON QUEST
DROPOUT by CollegeHumor
Da Vinci Eye: AR Art Projector
Daily Bible Trivia Bible Games
Daily Diary:Journal with Lock
Daily Yoga: Fitness+Meditation
Dancing Hair - Music Race 3D
Daniel Tiger's Day & Night
Daniel Tiger's Stop & Go Potty
Dark MODE Watch Face
Dave - Banking & Cash Advance
Dawncaster: Deckbuilding RPG
Day R Premium
Dead Cells
Decor Life - Home Design Game
Deep Clean Inc. 3D
Deep Cleaner-Phone Faster
Deliver It 3D
Delta Touch [7 x Doom engines]
Design Home: Real Home Decor
Design Space: DIY with Cricut
Despotism 3k
Dessert DIY
Destiny Run
Device Info: View phone info
Diablo Immortal
Dice Dreams™️
Dice With Buddies™ Social Game
Dicey Dungeons
Dig Deep
Digital Mod Black watchface
Digital Red Watch Face
Dirt Trackin 2
Discord: Talk, Chat & Hang Out
Dislyte
Disney Collect! by Topps
Disney Emoji Blitz Game
Disney Magic Kingdoms
Disney+
Dog Life Simulator
Dollar General
Domino's Pizza USA
Don't Starve: Pocket Edition
Don't Starve: Shipwrecked
Donut County
Doodle God™
Doom & Destiny Worlds
Doomsday: Last Survivors
Door Kickers
Door Kickers: Action Squad
DoorDash - Dasher
DoorDash - Food Delivery
Double Win Slots- Vegas Casino
DoubleDown Casino Vegas Slots
DoubleU Casino™ - Vegas Slots
Downwell
Dozer Mania
DraStic DS Emulator
Drag Fight
Dragon Farm Adventure-Fun Game
Dragon Raja
Dragon Trail: Hunter World
Dragonscapes Adventure
Dream Wedding
Dreame
Drive Safe & Save™
DroidCamX - HD Webcam for PC
Dropbox: Secure Cloud Storage
Duck Life: Battle
Duck Life: Retro Pack
Dude Theft Wars: Offline games
Duet Display
Dungeon Defense
Dungeon Maker
Dungeon Village 2
Dunkin’
Duo Mobile
Duolingo: language lessons
ESPN
ESPN Fantasy Sports
EVE Echoes
Earn to Die
East Front
Easy Booster
Easy Scanner
Easy Voice Recorder Pro
Eatventure
Elevate - Brain Training Games
ElkNut
Email Home - Email Homescreen
Empire Takeover: Rush & Crush
Empire: Four Kingdoms
Empires & Puzzles: Match-3 RPG
Epic Heroes - Dinosaur Control
Epic Seven
Epic: Kids' Books & Reading
Episode - Choose Your Story
Etsy: Buy & Sell Unique Items
Eventbrite - Discover popular events & nearby fun
EverMerge: Merge 3 Puzzle
Evernote - Note Organizer
Everskies: Virtual Dress up
Evertale
EvoCreo - Pocket Monster Game
Evoland
Evony: The King's Return
Exiled Kingdoms - Full
Expedia: Hotels, Flights & Car
Experian
Exploding Kittens® - Official
Explore Daniel's Neighborhood
ExpressVPN: VPN Fast & Secure
Extreme Car Driving Simulator
F1 TV
FIFA Soccer
FINAL FANTASY
FINAL FANTASY  BRAVE EXVIUS
FINAL FANTASY BE:WOTV
FINAL FANTASY III (3D REMAKE)
FINAL FANTASY IV (3D REMAKE)
FINAL FANTASY IX for Android
FINAL FANTASY TACTICS : WotL
FINAL FANTASY V
FINAL FANTASY VI
FINAL FANTASY VII
FINAL FANTASY VIII Remastered
FL Studio Mobile
FNF Music Battle Full Mod
FNaF 6: Pizzeria Simulator
FORScan Lite
Fabulous Booster-Phone Cleaner
Fabulous Cleaner-Boost&Speedup
Fabulous Files - Clean&Booster
Fabulous Security-Virus&Clean
Face Dance: AI Photo Animator
FaceApp: Face Editor
Facebook
Facemoji Emoji Keyboard&Fonts
Fairy Rush: Genetic Fusion
Fake GPS Joystick & Routes Go
Falling Art Ragdoll Simulator
Falling Fruit
Family Farm Adventure
Family Island™ — Farming game
Fancy Battery: Booster Cleaner
Fantasy Football Draft Wizard
FarmVille 2: Country Escape
FarmVille 3 – Farm Animals
Farming Simulator 18
Farming Simulator 20
Farming USA 2
Fashion Battle - Dress up game
Faster Cleaner
Fate of an Empire - Age of War
Fate of the Empress
Fate/Grand Order (English)
Feeld: Meet Couples & Singles
Feelsy: Stress Anxiety Relief
Fetch Rewards: Earn Gift Cards
FiLMiC Pro: Mobile Cine Camera
Figgerits - Word Puzzle Game
Files by Google
Fill The Fridge
Filto: Video Filter Editor
Find 3D - Match 3D Items
Find My Kids: location tracker
Find the Alien
Find the Difference
Fire Emblem Heroes
Firefox Fast & Private Browser
First To Life
Fish GROW GROW
Fishbrain - Fishing App
Fishdom
Fishing Clash
FitCoach: Fitness Coach & Diet
FitGift: more health more earn
FitNotes Supporter
Fitbit
Five Nights at Freddy's
Five Nights at Freddy's 2
Five Nights at Freddy's 3
Five Nights at Freddy's 4
Five Nights at Freddy's: HW
Five Nights at Freddy's: SL
Flat Earth Sun, Moon & Zodiac Clock
Flex Run 3D
Flex Utility Premium
Flo Ovulation & Period Tracker
Floof - My Pet House
Flora Elegant Multicolor NXV84
Flora Ladies Watch Face NXV01
Florence
Flud (Ad free)
Fly Delta
Football Manager 2022 Mobile
Forager
Forge of Empires: Build a City
Fork N Sausage
Forks Plant-Based Recipes
Foundations Memory Work Cycle2
Fox Nation: Celebrate America
FoxFi Key (supports PdaNet)
Fran Bow Chapter 2
Fran Bow Chapter 3
Fran Bow Chapter 4
Fran Bow Chapter 5
Freeways
Front Armies [RTS]
Frost & Flame: King of Avalon
Frozen Honey ASMR
Fruit Ninja Classic
Fruitsies - Pet Friends
Fun Feud Trivia: Play Offline!
Funimation
Future You: Face Aging&AI Palm
GALATEA: Audiobooks & Novels
GENKI Vocab for 3rd Ed.
GIF Maker, GIF Editor Pro
GIMP
GPS Speedometer and Odometer (Pro)
GPS, Maps, Voice Navigation & Directions
GRID™ Autosport
GSN Casino: Slot Machine Games
GTA: Chinatown Wars
GTA: Liberty City Stories
GUNS UP! Mobile
Galaxiga Arcade Shooting Game
Galaxy Attack: Alien Shooting
Galaxy Genome [Space Sim]
Gallery Pro - Photos & Videos
Game Booster 4x Faster Pro
Game Dev Story
Game Dev Tycoon
Game of Khans
Game of Kings:The Blood Throne
Game of Sultans
Game of Thrones Slots Casino
Game of Thrones: Conquest ™
GameChanger
GameChanger Classic
Garden Affairs
Gardenscapes
Garena Free Fire: 5th Anniv.
Gem Stack
Genies & Gems - Match 3 Game
Genshin Impact - Sumeru Debut
Geocaching®
Geometry Dash
Get Color - Water Sort Puzzle
Get Lucky: Run To The Pool
Getting Over It with Bennett Foddy
Ghost Radar®: LEGACY
Giant Wanted
Gin Rummy Plus
Gin Rummy Stars - Card Game
Goat Simulator MMO Simulator
Goddess Era
Going Balls
Gold & Goblins: Idle Merger
Gold Fish Casino Slot Games
Golden Floral Watch
Golden HoYeah- Casino Slots
Golf Clash
Golf Rival
GoodNovel - Web Novel, Fiction
Goods Match 3D - Triple Master
Google Authenticator
Google Calendar
Google Chat
Google Classroom
Google Docs
Google Drive
Google Earth
Google Family Link
Google Find My Device
Google Home
Google Lens
Google One
Google Pay: Save, Pay, Manage
Google Photos
Google Sheets
Google Translate
Google Voice
Google Wallet
Gossip Harbor: Merge Game
Governor of Poker 3 - Texas
Grand Cash Casino Slots Games
Grand Hotel Mania: Hotel games
Grand Summoners - Anime RPG
Grand Theft Auto III
Grand Theft Auto: Vice City
Graphing Calculator Plus (X84)
Graveyard Keeper
Grindr - Gay chat
Growing Up: Life of the ’90s
Grubhub: Food Delivery
Gummy Drop! Match 3 to Build
Gun Head Run
Guns of Glory: The Iron Mask
Gunship Battle Total Warfare
H310 Watch Face - YOSASH
HATSUNE MIKU: COLORFUL STAGE!
HBO Max: Stream TV & Movies
HMKWatch Analog 264
HMKWatch Digi 134 Re
HOOK 2
HP Smart
Hair Clipper Prank, Fart Sound
Hair Dye
Haircut prank, air horn & fart
Halloween Animated WatchFace
HamStudy.org
Handy Art Reference Tool
Happy Clinic
Happy Color® – Color by Number
Harry Potter: Hogwarts Mystery
Harry Potter: Puzzles & Spells
Haunt the House: Terrortown
Headspace: Mindful Meditation
Headway: Fun & Easy Growth
Hearthstone
HelloFresh: Meal Kit Delivery
Hero Wars – Fantasy Battles
Heroes of Crown
Heroic Expedition
Hidden Camera Detector Gold
Hidden City: Hidden Object
Hidden Through Time
Hide 'N Seek!
High 5 Casino Vegas Slot Games
Highrise: Virtual Metaverse
Hill Climb Racing 2
Hily - Dating. Make Friends.
Hinge - Dating & Relationships
Hit it Rich! Casino Slots Game
Hitman Sniper
Hoard Master
Holdem or Foldem - Texas Poker
Hole.io
Home Design Makeover
Home Workout - No Equipment
Homescapes
Honeycam Chat-Live Video Chat
Honkai Impact 3rd
Hopper: Hotels, Flights & Cars
Hopping Heads: Scream & Shout
Hot Shot Casino Slot Games
Hotels.com: Travel Booking
House of Fun™ - Casino Slots
Huge Win Slots - Casino Game
Hulu: Watch TV shows & movies
Human: Fall Flat
Hungry Shark Evolution
Hunt Royale: Action RPG Battle
Hunting Clash: Hunter Games
Hustle Castle: Medieval games
Huuuge Casino Slots Vegas 777
Hybrid Dark Watch Face
IMVU: online 3D metaverse game
INKredible PRO
IP Cam Viewer Pro
IPTV Extreme Pro
IPTV Pro
ISEKAI: Demon Waifu
Iconic KWGT
Identity V
Idle Angels
Idle Billionaire Tycoon
Idle Heroes
Idle Huntress：Adventure
Idle Lumber Empire
Idle Mafia - Tycoon Manager
Idle Miner Tycoon: Gold & Cash
Immortal Diaries
Immortal Taoists - Idle Manga
InCar - CarPlay for Android PRO
Incoquito
Incredibox
Indeed Job Search
Infinite Galaxy
Infinity 8 Ball
Infinity Kingdom
InkLine IconPack
Inspire 07 - Analog Watch-Face
Inspire X - Analog Watch Face
Instacart Market Food Delivery
Instagram
Internet Browser (TV)
Invasion: Aerial Warefare
Invoice Maker: Easy & Simple
Iron Marines: RTS offline Game
Island Questaway - Jungle Farm
Island War
JB4 Mobile
JCheater: San Andreas Edition
Jackpot Crush - Slots Games
Jackpot Magic Slots
Jackpot Master™ Slots
Jackpot Party Casino Slots
Jackpot Spin
Jackpot World™ - Slots Casino
Jawaker Tarneeb, Hand & Trix
Jigsawscapes - Jigsaw Puzzles
John GBA
Joi - Live Video Chat
Joyread
June's Journey: Hidden Objects
Junkyard Keeper
Jurassic World Alive
Jurassic World™: The Game
JustPlay - Earn or Donate
KFC US - Ordering App
KLWP Live Wallpaper Pro Key
KOF 2002 ACA NEOGEO
KWGT Kustom Widget Pro Key
KeepClean: Cleaner, Antivirus
Keeper Password Manager
Kick The Buddy: Second Kick
Kick the Buddy
Kik — Messaging & Chat App
Kim Kardashian: Hollywood
King James Bible - Verse+Audio
King of Steaks
King's Choice
King's Throne: Royal Delights
Kingdom Guard:Tower Defense TD
Kingdom Maker
Kingdom Rush Frontiers TD
Kingdom Rush Origins - TD
Kingdom Rush Vengeance TD Game
Kingdom Two Crowns
Kiss of War
Kitten Match
Kittens Game
Klarna | Shop now. Pay later.
Klondike Adventures
Knots 3D
Koala Sampler
KonoSuba: Fantastic Days
Kroger
Kungfu Ragdoll
LADB — Local ADB Shell
LAST CLOUDIA
LEGO ® Batman: Beyond Gotham
LEGO ® Marvel Super Heroes
LEGO® Jurassic World™
LEGO® Ninjago: Shadow of Ronin
LEGO® Star Wars™:  TCS
LIMBO
Land Nav Assistant
Land of Empires: Immortal
LandGlide
Last Day on Earth: Survival
Last Empire - War Z: Strategy
Last Fortress: Underground
Last Shelter: Survival
Layton: Curious Village in HD
League of Legends: Wild Rift
League of Pantheons
Legacy 2 - The Ancient Curse
Legacy 3 - The Hidden Relic
Legend City
Legend of Slime: Idle RPG
Legend of the Phoenix
Legendary: Game of Heroes
Let's Play a Game: Horror Game
Libby, by OverDrive
Life360: Find Family & Friends
LifeAfter - Sea of Zombie
LifeUp: Gamify To-Do & Habit
Lightning Link Casino Slots
Lightroom Photo & Video Editor
Like a Pizza
Likee - Community of Interests
Lily’s Garden - Design & Relax
LineX Icon Pack
Lineage2M
Linelight
Lines Pro - Icon Pack
LinkedIn: Jobs & Business News
Litchi for DJI Drones
Little Caesars
Little League Rulebook
LiveATC for Android
Local News - Latest & Smart
Looney Tunes™ World of Mayhem
Lords Mobile: Tower Defense
Lotsa Slots - Casino Games
Love & Pies - Merge
Love Nikki-Dress UP Queen
Lowe's
Lowriders Comeback 2: Cruising
LuX IconPack
Lucky Buddies
Lyft
M64Plus FZ Pro Emulator
MARVEL Future Fight
MARVEL Future Revolution
MARVEL Puzzle Quest: Hero RPG
MARVEL Strike Force: Squad RPG
MD.emu
MD111: Digital watch face
MD112: Digital watch face
MD170B: Digital watch face
MD242: Hybrid watch face
MD289: Digital watch face
MD290: Digital watch face
MD295: Hybrid watch face
MD300: Digital watch face
MEGA
MEGA MAN X DiVE - MOBILE
METAL SLUG 3
MGM Slots Live - Vegas Casino
MHA: The Strongest Hero
MICO: Go Live streaming & Chat
MISTPLAY: Play to earn rewards
MLB
MLB 9 Innings 22
MLB Ballpark
MLB Tap Sports Baseball 2022
MONOPOLY - Classic Board Game
MONOPOLY Slots - Casino Games
MORTAL KOMBAT: A Fighting Game
MTV
MU ORIGIN 3
MX Player Pro
Macy's
Madden NFL 23 Mobile Football
Mafia City
Magic DosBox
Magic Fluids
Magic Hop: EDM & Dancing
Magic Tiles 3
Magic: The Gathering Arena
Makeup Kit - Color Mixing
Makeup Stylist:DIY Makeup Game
Manor Cafe
Manor Matters
Manta: Comics & Graphic Novels
Manual Camera: DSLR Camera Pro
MapleStory M - Fantasy MMORPG
Marble ASMR
Marco Polo - Stay In Touch
Mario Kart Tour
Marsaction: Infinite Ambition
Marvel Contest of Champions
Marvel Unlimited
Master Doctor 3D
Match 3D -Matching Puzzle Game
Max Cleaner
Max Payne Mobile
MeChat - Love secrets
Mech Arena: Robot Showdown
MediaMonkey Pro
MeetMe: Chat & Meet New People
Mega Hit Poker: Texas Holdem
Melon Playground
Melvor Idle - Full Version
Mercari: Your Marketplace
Merge Archers: Castle Defense
Merge Blast
Merge County®
Merge Dragons!
Merge Fables®
Merge Gardens
Merge Grabber
Merge Magic!
Merge Mansion
Merge Master: Rainbow Friends
Merge Super - Monster Fight
Mergeland-Alice's Adventure
Messenger
Messenger - Texting App
Messenger Home - SMS Launcher
Messenger Lite
Messenger for All Message Apps
Messenger: Text Messages, SMS
MiXplorer Silver File Manager
Microsoft Authenticator
Microsoft Edge: Web Browser
Microsoft OneDrive
Microsoft Outlook
Microsoft Teams
Mighty Party
Mileage Tracker by MileIQ
Minecraft: Education Edition
Mini Metro
Minimal Black v17 Watch Face
Minion Rush: Running Game
Misty Continent: Cursed Island
Mob Control
Mobile Antivirus: Norton 360
Mobile Legends: Adventure
Mobile Legends: Bang Bang
Mobile Security - Lookout
MobileSheets
MoboReader - Webnovels Romance
Modern Combat 4: Zero Hour
Mommy Maze
Monash University FODMAP diet
Money Rush
Monsters Gang 3D: beast fights
Monument Valley
Monument Valley 2
Mood Meter
Moon+ Reader Pro
MotorTrend+: Watch Car Shows
Motorsport Manager Mobile 3
Move Animals
Move People
MudRunner
Muscle Booster Workout Planner
Muse Dash
Music Downloader & Mp3 Songs
Music Downloader - Mp3 music
Music Downloader MP3 Download
Music Player & MP3 Player
My Bath & Body Works
My Boy! - GBA Emulator
My Budget Book
My Cafe — Restaurant Game
My Child Lebensborn
My City : Newborn baby
My City: Star Horse Stable
My Face Shape Meter and frames
My Home My World: Coin Jackpot
My Lightning Tracker Pro
My Little Universe
My Macros+
My OldBoy! - GBC Emulator
My Perfect Hotel
My Romance: puzzle & episode
My Singing Monsters Composer
My Spectrum
My Talking Angela 2
MyFitnessPal: Calorie Counter
MyRadar Weather Radar Pro
MySecurityPal
MyWF_GraySteel
MythWars & Puzzles: RPG Match3
Mythic Heroes: Idle RPG
Myths of Moonrise
NBA 2K20
NBA JAM  by EA SPORTS™
NFC Tools - Pro Edition
NFL
NFL Fantasy Football
NOAA Weather Unofficial (Pro)
Navigation Pro: Google Maps Navi on Samsung Watch
Necro Dice
Necrophonic
Need for Speed Most Wanted
Need for Speed™ No Limits
Neo Monsters
Netflix
Network Analyzer Pro
Network Cell Info & Wifi
Neverland Casino: Vegas Slots
NewsBreak: Local News & Alerts
Nextdoor: Neighborhood network
Ni no Kuni: Cross Worlds
Nike: Shop Shoes & Apparel
Noggin Preschool Learning App
NordVPN – fast VPN for privacy
Norton Secure VPN: Wi-Fi Proxy
Nostalgia.NES Pro (NES Emulator)
Notepad – Notes and Checklists
Noteshelf - Notes, Annotations
Nothing Iconpack
Nova Launcher Prime
Novelenders-Read&Write Novels
Nox Security, Antivirus, Clean
Numberblocks: Hide and Seek
OBD Fusion (Car Diagnostics)
OBSIDIAN Gold Class watch face
OCTOPATH TRAVELER: CotC
OK Golf
ONE PIECE Bounty Rush
ONE PIECE TREASURE CRUISE
OTTTD : Over The Top TD
Obey Me! Anime Otome Sim Game
Oddworld: New 'n' Tasty
OfferUp: Buy. Sell. Letgo.
Office Building - Idle Tycoon
Office Fever
OkCupid: Online Dating App
Old School RuneScape
Omega - Live Random Video Chat
OnStar Guardian: Safety App
One Night at Flumpty's
One Night at Flumpty's 2
One Night at Flumpty's 3
One Punch - LIMITED EDITION
One Way: The Elevator
Opera News: Breaking Local & US Headlines
Order please! -Draw&Story game
Organ Trail: Director's Cut
OruxMaps GP
Our Empire Pro
Outline Icons - Icon Pack
Overdrive 2.6 Relaunched by Digital Dream Labs
Overstock - Easy Home Savings
PAW Patrol: A Day in Adventure Bay
PCH+
PER002 - Laila Watch Face
PER007 - Storm Watch Face
PER008 - Soho Watch Face
PER015 - Luna Watch Face
PK XD - Explore Universes!
POCKET COMICS: Premium Webtoon
POP! Slots™ Vegas Casino Games
PPSSPP Gold - PSP emulator
PSPlay: PS5 & PS4 Remote Play
PURE Hookup - anonymous dating
Package Inc - Cargo Simulator
Paint by Number Coloring Games
Paired: Couples & Relationship
Panda Gamepad Pro (BETA)
Panda Mouse Pro(BETA)
Pandora - Music & Podcasts
Pantaya - Streaming in Spanish
Papa's Bakeria To Go!
Papa's Burgeria To Go!
Papa's Cheeseria To Go!
Papa's Cluckeria To Go!
Papa's Cupcakeria To Go!
Papa's Donuteria To Go!
Papa's Freezeria To Go!
Papa's Hot Doggeria To Go!
Papa's Mocharia To Go!
Papa's Pancakeria To Go!
Papa's Pastaria To Go!
Papa's Pizzeria To Go!
Papa's Scooperia To Go!
Papa's Sushiria To Go!
Papa's Taco Mia To Go!
Papa's Wingeria To Go!
Papers Grade Please!
Papers, Please
Paragon Pioneers
Paramount+ | Peak Streaming
Parking Jam 3D
Parking Jam 3D: Drive Out
Party in my Dorm: College Game
Pascal's Wager
PayPal - Send, Shop, Manage
Peace, Death!
Peace, Death! 2
Peacock TV: Stream TV & Movies
PeakFinder
Pedi STAT
Peloton - Fitness & Workouts
Penly: Digital Planner & Notes
Penny & Flo: Finding Home
Peppa Pig: Party Time
Peppa Pig: Sports Day
Perfect Cream
Pet Rescue Saga
Phase 10: World Tour
Phone Case DIY
Phone Clean - Super Cleaner, Booster & Antivirus
Phone Cleaner
Phone Guardian VPN: Safe WiFi
Phone Launcher Apps
Phonograms
PhotoPills
PhotoSync Bundle Add-On
Piano Fire: Edm Music & Piano
Picsart Photo & Video Editor
PictureThis - Plant Identifier
Piggy GO - Clash of Coin
PinPal
Pinterest
Pip-Boy Watchface  [+Bonus]
Pipe Trades Pro Calculator
Pirate Kings™️
Pirates Outlaws
Pirates of the Caribbean: ToW
PixBit - Pixel Icon Pack
Pixelup - AI Photo Enhancer
Pizza Boy GBA Pro
Pizza Boy GBC Emulator Pro
Pizza Hut - Food Delivery & Takeout
Plague Inc: Scenario Creator
Planet Fitness Workouts
Plants vs. Zombies™
PlaySpot - Make Money Playing Games
PlayStation App
PlayWell - Play & Earn Rewards
Plenty of Fish Dating App
Plex: Stream Movies & TV
Pluto TV - Live TV and Movies
Pocket Academy 3
Pocket Champs: 3D Racing Games
Pocket City
Pocket FM: Audiobook & Podcast
Pocket Rogues: Ultimate
Pococha - Live Streaming App
Poker Face: Texas Holdem Live
Poker Live: Texas Holdem Poker
Pokémon GO
Pokémon Masters EX
Police Scanner - Scanner Radio
Poly Bridge
Poly Bridge 2
Poppo live
Poppy Playtime Chapter 1
Poppy Playtime Chapter 2
Poshmark - Buy & Sell Fashion
Pouring Master
PowerDirector - Video Editor
PowerSchool Mobile
Poweramp Full Version Unlocker
Prank Master 3D
Precept Bible
Prepware Airframe
Prepware General
Prepware Powerplant
Prepware Remote Pilot
Private Photo Vault - Keepsafe
Pro Emulator for Game Consoles
ProCam X ( HD Camera Pro )
Progressive
Project Highrise
Project Makeover
Property Brothers Home Design
Providers: EBT, debit, & more
Puff Up
Pull the Pin
Pulling USA
PunBall
Punishing: Gray Raven
Pupil Distance PD Glasses & VR
Puzzle & Dragons
Puzzle Combat: Match-3 RPG
Puzzles & Conquest
Puzzles & Survival
Pyramid Solitaire Saga
QR & Barcode Reader
QR & Barcode Scanner
QR Scanner - Barcode Scanner
QRScanner - Super QR Code Tool
Quick Hit Casino Slot Games
QuickBend: Conduit Bending
QuickBooks Online Accounting, Invoicing & Expenses
QuickBooks Self-Employed:Mileage Tracker and Taxes
RAID: Shadow Legends
RAR
RESET Collection
RFS - Real Flight Simulator
ROLEX Day Date  (unofficial)
ROLEX Submariner (Unofficial)
ROME: Total War
RPG Scribe Pathfinder & 3.5e
Race Master 3D - Car Racing
RadarOmega
RadarScope
Radish Fiction
Ragnarok Origin
Railroad Ink Challenge
Rainbow Brainskull Oracle Deck
Rainpaper
Rarevision VHS Camcorder 📼📹 Retro 80s Cam
ReadEra Premium – ebook reader
Real Drift Car Racing
Real Steel
RealCalc Plus
Realistic Clock - Watch Face
Rebuild
Rebuild 3: Gangs of Deadsville
Redbox: Rent. Stream. Buy.
Reddit
Redecor - Home Design Game
Reface: Funny face swap videos
Refantasia: Charm and Conquer
Regarder Minimal 64 Watch Face
Reigns
Reigns: Her Majesty
Relay for reddit (Pro)
Remind: School Communication
Remote for RokuTV
Rent. Apartments & Homes
Replika: My AI Friend
Reporter - Scary Horror Game
Revive: Face Photo Animator
Rewarded Play: Earn Gift Cards
Ring - Always Home
Rise of Empires: Ice and Fire
Rise of Kingdoms: Lost Crusade
Rise of the Kings
Road of Kings - Endless Glory
Roblox
RoboKiller - Robocall Blocker
Rock N' Cash Vegas Slot Casino
Rocket Booster
Rocket Money - Bills & Budgets
Roku - Official Remote Control
Rolex Daytona WatchFace WearOS
Rolex Royal Watch (unofficial)
Rolex Royal WatchFace WearOS
RollerCoaster Tycoon® Classic
Romance Fate: Story & Chapters
Root Board Game
Root Explorer
Rope and Demolish
Rotation Control Pro
Rovio Classics: AB
Royal Coin Box
Royal Match
RuneScape - Fantasy MMORPG
Rush Royale: Tower Defense TD
Rusted Warfare - RTS Strategy
Rusty Lake Hotel
Rusty Lake Paradise
Rusty Lake: Roots
SCRUFF
SD Maid Pro - Unlocker
SG-100
SHEIN-Fashion Shopping Online
SHOWTIME
SLIME - ISEKAI Memories
SLING: Live TV, Shows & Movies
SMS Backup & Restore Pro
SMZ 'Integrity 7'
SONIC Drive-In - Order Online - Delivery or Pickup
SPACEPLAN
STAR WARS™: KOTOR II
STARZ
Sakura Stories Live Wallpaper
Sam's Club
Sandwich Runner
Save Balls: Brain teaser games
Save Editor for Stardew Valley
Save The Dog Bee - Draw Game
Save the Doge
Scanner Radio Pro - Fire and Police Scanner
Scatter Slots - Slot Machines
Scavenger Hunt
School Party Craft
Schumann Resonance
Screen Mirroring - TV Miracast
Screen Mirroring Pro App
Screen Mirroring Pro for Fire TV
Screen Mirroring Pro for Roku
Screen Recorder - Vidma Record
Screen Recorder - XRecorder
Scribblenauts Remix
Scribblenauts Unlimited
Secure VPN－Safer Internet
Seekers Notes: Hidden Mystery
Seeking
Seesaw
Shadow Division - watch face
Shadow Fight 2 Special Edition
Shazam: Music Discovery
Sheer  KWGT
Sheet Music Scanner & Reader
ShellShock Live
Sherlock・Hidden Object Mystery
Shonen Jump Manga & Comics
Shop Titans: Idle Tycoon RPG
Shop: All your favorite brands
Shudder: Horror & Thrillers
Sideline - 2nd Line for Work
Signal Private Messenger
Silent Castle
SimCity BuildIt
Simple Calendar Pro
Simple Contacts Pro
Simple File Manager Pro
Simple Gallery Pro
Simple Thank You
SimplePlanes - Flight Simulator
SimpleRockets 2
SiriusXM: Music, Sports & News
Six Pack in 30 Days
Sketchbook
Skip-Bo
Skull Wear Watch Face
SkyView® Explore the Universe
Slay the Spire
Slotomania™ Slots Casino Games
Slots Era - Jackpot Slots Game
Slots: Heart of Vegas Casino
SlotsCashHunt: Vegas Casino
Smule: Karaoke Songs & Videos
Snake.io: Fun Snake .io Games
Snap VPN: Super Fast VPN Proxy
Snapchat
Sniper 3D：Gun Shooting Games
Snow Race!!
Soda Sort: Water Color Puzzle
Solar Smash
Solitaire
Solitaire Classic
Solitaire Collection
Solitaire Dragons
Solitaire Grand Harvest
Solitaire Journey
Solitaire TriPeaks Journey
Solitaire Verse
Solitaire, Classic Card Games
Solocator - GPS Field Camera
Sonic 4™ Episode I
Sonic Dash - Endless Running
Sonic Forces - Running Battle
Sonic Jump Pro
Sonic Runners Adventure game
Sonic at the Olympic Games.
SoundCloud: Play Music & Songs
Southwest Airlines
Space Leaper: Cocoon
Space shooter - Galaxy attack
Spades Plus - Card Game
Spades Royale Card Games
Spectrum TV
Speed Master VPN
Spirit Talker
SpongeBob SquarePants BfBB
SpongeBob's Game Frenzy
Sporcle
Spotify: Music and Podcasts
Square Home Key
Stack the States®
Stacky Dash
Star Traders: Frontiers
Star Trek™ Fleet Command
Star Walk 2 - Night Sky View
Star Wars™: Galaxy of Heroes
Star Wars™: KOTOR
StarMaker: Sing and Play
Starbucks
Starbuilder
Stardew Valley
State Railroad: Train Game
State of Survival: Zombie War
Station Manager
StbEmu (Pro)
Steam
Steering Wheel Evolution
Stellarium Plus - Star Map
Stick Hero: Mighty Tower Wars
Stick Nodes Pro - Animator
Stickman Warriors - Super Dragon Shadow Fight
Stop Motion Studio Pro
Strava: Run, Ride, Hike
Strelok Pro
Stumble Guys
Style IV
Subway®
Sudoku - Classic Sudoku Puzzle
Sudoku Ultimate Offline puzzle
Super Hedgehog Rope Hero
Super Slime Simulator: DIY Art
Super VPN Pro
SuperLive
Supremacy 1914 - WW1 Strategy
Supreme Duelist Stickman
Survivor.io
Sweatcoin
Sync for Reddit (Pro)
T-Mobile Internet
TAG Heuer Carrera
THE GAME OF LIFE Vacations
THE KING OF FIGHTERS '98
TL Pro
TMNT Portal Power
TRANSFORMERS: Earth Wars
TRIVIA STAR Quiz Games Offline
TV Cast Pro for Android TV
TV Cast Pro for Fire TV
TV Cast Pro for LG webOS
TV Cast Pro for Roku
TV Cast Pro for Samsung TV
Taco Bell – Order Fast Food
Tactical NAV: MGRS Navigation
Tagged - Meet, Chat & Dating
Taimi - LGBTQ+ Dating and Chat
Talisman
Talking Ben the Dog
Tall Man Run
Talon for Twitter
Tancha 58 Hybrid Watch Face
Tangle Master 3D
Tantan
Tap Away
Tap Color Pro: Color By Number
Tapas – Comics and Novels
Tapchamps
Tappytoon Comics & Novels
Target
Tasker
Tattoo Evolution
Tattoo Stencil
Teach Your Monster to Read
TeamSpeak 3 - Voice Chat Software
Teen Titans GO Figure!
Teeny Titans - Teen Titans Go!
Telekinesis Quest 3D
Tello FPV - Control the Ryze Tello drone FPV + RTH
Tennis Clash: Multiplayer Game
Terabox: Cloud Storage Space
Terraforming Mars
Terraria
Tetris®
Texas Hold'em Poker: Pokerist
Text Free: Call & Texting App
Text or Die
TextNow: Call + Text Unlimited
The Ants: Underground Kingdom
The Blood Type Diet®
The Escapists 2: Pocket Breakout
The Escapists: Prison Escape
The Game of Life
The Game of Life 2
The Grand Mafia
The Home Depot
The House of Da Vinci
The House of Da Vinci 2
The Impossible Game
The King of Fighters ALLSTAR
The Lonely Hacker
The Lord of the Rings: War
The New York Times
The New York Times Crossword
The President
The Room
The Room Three
The Room Two
The Room: Old Sins
The Seven Deadly Sins
The Sims™ FreePlay
The Sun: Origin
The Viridian Obelisk
The Walking Dead No Man's Land
The Walking Dead: Survivors
The Wall Street Journal: Business & Market News
The Weather Channel - Radar
The Wizard of Oz Magic Match 3
The Wonder Weeks
Theme Park Fun 3D!
Themepack - App Icons, Widgets
There Is No Game: WD
Thief Puzzle: to pass a level
Threema
Threes!
TickTock-TikTok Live Wallpaper
Ticket to Earth
Ticket to Ride
Ticketmaster－Buy, Sell Tickets to Concerts, Sports
Tiki Solitaire TriPeaks
Tile Garden:Match 3 Puzzle
Tile Link - Match & Connect
Tiles Hop: EDM Rush!
Time Princess: Story Traveler
Time Warp Scan - Face Scanner
Timeless KWGT
Tinder: Dating app. Meet. Chat
Toca Blocks
Toca Boo
Toca Builders
Toca Hair Salon 3
Toca Hair Salon Me
Toca Kitchen 2
Toca Kitchen Sushi Restaurant
Toca Lab: Elements
Toca Lab: Plants
Toca Life World: Build stories
Toca Life: After School
Toca Life: City
Toca Life: Farm
Toca Life: Hospital
Toca Life: Neighborhood
Toca Life: Office
Toca Life: Pets
Toca Life: School
Toca Life: Stable
Toca Life: Town
Toca Life: Vacation
Toca Mini
Toca Mystery House
Toca Pet Doctor
Tomb of the Mask
TonalEnergy Tuner & Metronome
ToonMe - Cartoon Face Maker
Top Drives – Car Cards Racing
Top Eleven Be a Soccer Manager
Top War: Battle Game
Topps® BUNT® MLB Card Trader
Torque Pro (OBD 2 & Car)
Total Battle: War Strategy
Total War: MEDIEVAL II
TouchRetouch
Tower of Fantasy
Townscaper
Township
Tracker Detect Pro for AirTag
Trading Legend
Traffic Puzzle - Match 3 Game
Traffix: Traffic Simulator
Trailer Park Boys:Greasy Money
Train Station 2: Train Games
Travel Center Tycoon
Travel Town - Merge Adventure
Treasure Master
Triple Match 3D
Triple Tile: Match Puzzle Game
Trivia Crack Premium
Tropical Resort Story
Trucker Path: Truck GPS & Maps
Tubi - Movies & TV Shows
TuneIn Radio: News, Music & FM
Turbo VPN - Secure VPN Proxy
TurboScan: scan documents and receipts in PDF
Twerk Race 3D — Running Game
Twitch: Live Game Streaming
Twitter
Two Dots
US Public Lands
USB Audio Player PRO
USB Camera Pro
Uber - Driver: Drive & Deliver
Uber - Request a ride
Uber Eats: Food Delivery
Udemy - Online Courses
Ugly's 2020
Ulala: Idle Adventure
Ultimate Car Audio App
Ultimate Custom Night
Ultimate Ghost Detector Real
Ultimate Golf!
Ultimate Guitar: Chords & Tabs
Unified Remote Full
Universal Paperclips
Universe in a Nutshell
Univision Now: Univision y UniMás sin cable
Uplive-Live Stream, Go Live
Upside-Cash back on gas & food
Upward: Christian Dating App
UsA Bigger Watch Face - USA122
UsA Chalk - USA126
UsA Exposed - USA110
UsA Florencia - USA111
VPN - Super Unlimited Proxy
VPN Proxy Master - Safer Vpn
VeVe
Vector Full
Vegas Friends - Slots Casino
Vegas Live Slots: Casino Games
Venmo
Vera Icon Pack: shapeless icon
Verticons Icon Pack
Very Little Nightmares
ViX: Cine y TV en Español
Video Editor & Maker - InShot
Video Player Phone
Viki: Asian Dramas & Movies
Vikingard
Vikings: War of Clans – empire
Voice Recorder
Vrbo Vacation Rentals
Vudu- Buy, Rent & Watch Movies
WFP 160 Luxury Mod2 Watch Face
WFP 160 Luxury Watch Face
WFP 237 Allure Watch Face
WFP 241 Exact time Watch Face
WFP 300 Tomcat PRO
WGT Golf
WIN  Dgt Super 22 MOD
WSOP - Poker Games Online
WWE Champions
WWE SuperCard - Battle Cards
Walgreens
Walking Dead: Road to Survival
Walkout Song DJ
Wall of insanity
WallO Wallpapers Cool Themes
Walmart Shopping & Grocery
War Dragons
War Machines：Tanks Battle Game
War Robots Multiplayer Battles
War and Order
War and Peace: Civil War Clash
Warhammer 40,000: Lost Crusade
Warhammer 40,000: Tacticus
Warpath: Ace Shooter
Watch Face - Minimal & Elegant for Android Wear OS
Watch Face -WatchMaker Premium for Android Wear OS
Watch Faces - Pujie - Wear OS
Water Sort - Color Puzzle Game
Watt Time — For your Tesla
Wattpad - Read & Write Stories
Wave Live Wallpaper
Wave Live Wallpapers Maker 3D
Waze Navigation & Live Traffic
Wear for Tesla
Weather Home - Live Radar
Weather Home: Local Forecast
Web Swing Hero
Webnovel
Wehear - Audiobooks & Stories
WeightWatchers
Wells Fargo Mobile
West Game
Western Sniper: Wild West FPS
Western Union: Transfer Money
WhatsApp Business
WhatsApp Messenger
Whatsflirt – Chat and Flirt
Wheel of Fortune: TV Game
Where's George? Official App
Where's My Water?
White Noise
Who - Live Video Chat
Wholee - Online Shopping App
WiFi Analyzer Premium
Wide Clean: Cleaner & Booster
Wild Classic Slots Casino Game
Wild Kratts Rescue Run: Animal Runner Game
Willy Wonka Vegas Casino Slots
Win Money – Play Game for Cash
Wingspan: The Board Game
Wish: Shop And Save
Wizard of Oz Slots Games
Wolf Game: The Wild Kingdom
WolframAlpha
Wonder - AI Art Generator
Word Collect - Word Games Fun
Word Cookies! ®
Word Maker Search: Word Puzzle
Word Office - PDF, Docx, Excel
Word Trip
Wordle!
Words of Wonders: Crossword
Words with Friends 2 Classic
Work Log Pro
Working Scale
World of Goo
World of Tanks Blitz - PVP MMO
Wuhoo Proxy
Wynn Slots - Online Las Vegas Casino Games
Wyze - Make Your Home Smarter
XCOM®: Enemy Within
Xbox
Xfinity
XtraMath
YAHTZEE With Buddies Dice Game
YOYO Doll: School life
Yahoo Fantasy Sports & Daily
Yahoo Mail – Organized Email
Yalla Ludo - Ludo&Domino
Yellow Rope Game
Yelp: Food, Delivery & Reviews
Yes or No?! - Food Pranks
YouTube
YouTube Kids
YouTube Music
YouTube Studio
YouTube TV: Live TV & more
YouVersion Bible App + Audio
Youtubers Life: Gaming Channel
Yu-Gi-Oh! Duel Links
Yu-Gi-Oh! Master Duel
Z Day: Hearts of Heroes | MMO Strategy War
ZEDGE™ Wallpapers & Ringtones
ZEPETO: 3D avatar, chat & meet
Zelle
Zen Match
Zen Tiles
Zeus
Zillow: Homes For Sale & Rent
Zombie Defense
Zombieville USA 2
Zoo - Happy Animals
Zooba: Zoo Battle Royale Game
Zoombinis
Zoosk - Social Dating App
Zynga Poker- Texas Holdem Game
[DW] Minimalistic Magic
aquapark.io
cake live stream video chat
craigslist
dfndr security: antivirus
discovery+ | Stream TV Shows
e-Sword: Bible Study to Go
eBay: The shopping marketplace
ePSXe for Android
fuboTV: Watch Live Sports & TV
iBend Pipe
iFunny - cool memes & videos
iHeart: Music, Radio, Podcasts
iReal Pro
ibis Paint
ibis Paint X
inCarDoc Pro | ELM327 OBD2
myKONAMI® Casino Slot Machines
myVEGAS Slots: Casino Slots
onX Hunt: GPS Hunting Maps
realMyst
rif is fun golden platinum
tango-Live Stream & Video Chat
tinyCam Monitor PRO for IP Cam
uDates - Online Dating & Chat
vDS - NDS Emulator
µTorrent® Pro - Torrent App
新三國志手機版-光榮特庫摩授權
Calculator
Calculator
Calculator
Calculator
Calculator
Dominoes
Dominoes
Dominoes
Dominoes
Dominoes
Hulu
Hulu
Hulu
Hulu
Hulu
United Airlines
United Airlines
United Airlines
United Airlines
United Airlines
Great Clips
Great Clips
Great Clips
Great Clips
Great Clips
Turbotax
Turbotax
Turbotax
Turbotax
Turbotax
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Weather Radar
Weather Radar
Weather Radar
Weather Radar
Weather Radar
Wikipedia
Wikipedia
Wikipedia
Wikipedia
Wikipedia
ABC News
ABC News
ABC News
ABC News
ABC News
Cracker Barrel
Cracker Barrel
Cracker Barrel
Cracker Barrel
Cracker Barrel
Offerup
Offerup
Offerup
Offerup
Offerup
Beats
Beats
Beats
Beats
Beats
News Break
News Break
News Break
News Break
News Break
Overstock
Overstock
Overstock
Overstock
Overstock
Cashapp
Cashapp
Cashapp
Cashapp
Cashapp
Google Play Store
Google Play Store
Google Play Store
Google Play Store
Google Play Store
Poshmark
Poshmark
Poshmark
Poshmark
Poshmark
Siriusxm
Siriusxm
Siriusxm
Siriusxm
Siriusxm
Google Meet
Google Meet
Google Meet
Google Meet
Google Meet
Hotschedules
Hotschedules
Hotschedules
Hotschedules
Hotschedules
Joann
Joann
Joann
Joann
Joann
Mercari
Mercari
Mercari
Mercari
Mercari
Minesweeper
Minesweeper
Minesweeper
Minesweeper
Minesweeper
Monkey
Monkey
Monkey
Monkey
Monkey
Suicide Squad
Suicide Squad
Suicide Squad
Suicide Squad
Suicide Squad
Chess
Chess
Chess
Chess
Chess
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Pac Man
Pac Man
Pac Man
Pac Man
Pac Man
Rumble
Rumble
Rumble
Rumble
Rumble
Watched
Watched
Watched
Watched
Watched
Duolingo
Duolingo
Duolingo
Duolingo
Duolingo
Gasbuddy
Gasbuddy
Gasbuddy
Gasbuddy
Gasbuddy
Groupme
Groupme
Groupme
Groupme
Groupme
Jersey Mikes
Jersey Mikes
Jersey Mikes
Jersey Mikes
Jersey Mikes
Pandora Music
Pandora Music
Pandora Music
Pandora Music
Pandora Music
Spider Solitaire
Spider Solitaire
Spider Solitaire
Spider Solitaire
Spider Solitaire
Yahoo Sports
Yahoo Sports
Yahoo Sports
Yahoo Sports
Yahoo Sports
Amazon Shopping
Amazon Shopping
Amazon Shopping
Amazon Shopping
Amazon Shopping
Doxcy
Doxcy
Doxcy
Doxcy
Doxcy
Grindr
Grindr
Grindr
Grindr
Grindr
Peacock Tv
Peacock Tv
Peacock Tv
Peacock Tv
Peacock Tv
Pluto Tv
Pluto Tv
Pluto Tv
Pluto Tv
Pluto Tv
Wheel Of Fortune
Wheel Of Fortune
Wheel Of Fortune
Wheel Of Fortune
Wheel Of Fortune
Flashlight
Flashlight
Flashlight
Flashlight
Flashlight
Mp3juice
Mp3juice
Mp3juice
Mp3juice
Mp3juice
Tiktok
Tiktok
Tiktok
Tiktok
Tiktok
Credit Karma
Credit Karma
Credit Karma
Credit Karma
Credit Karma
Minecraft
Minecraft
Minecraft
Minecraft
Minecraft
Accuweather
Accuweather
Accuweather
Accuweather
Accuweather
Mathway
Mathway
Mathway
Mathway
Mathway
Nbc News
Nbc News
Nbc News
Nbc News
Nbc News
Gacha Life
Gacha Life
Gacha Life
Gacha Life
Gacha Life
Schoology
Schoology
Schoology
Schoology
Schoology
Textnow
Textnow
Textnow
Textnow
Textnow
Wish
Wish
Wish
Wish
Wish
Gopro
Gopro
Gopro
Gopro
Gopro
Slitherio
Slitherio
Slitherio
Slitherio
Slitherio
The Weather Channel
The Weather Channel
The Weather Channel
The Weather Channel
The Weather Channel
Among Us
Among Us
Among Us
Among Us
Among Us
Genshin Impact
Genshin Impact
Genshin Impact
Genshin Impact
Genshin Impact
Mychart
Mychart
Mychart
Mychart
Mychart
Ring
Ring
Ring
Ring
Ring
Blackboard
Blackboard
Blackboard
Blackboard
Blackboard
Nextdoor
Nextdoor
Nextdoor
Nextdoor
Nextdoor
Tagged
Tagged
Tagged
Tagged
Tagged
Webtoon
Webtoon
Webtoon
Webtoon
Webtoon
Telegram
Telegram
Telegram
Telegram
Telegram
Clash Royale
Clash Royale
Clash Royale
Clash Royale
Clash Royale
Pokemon Unite
Pokemon Unite
Pokemon Unite
Pokemon Unite
Pokemon Unite
Starlink
Starlink
Starlink
Starlink
Starlink
Telemundo
Telemundo
Telemundo
Telemundo
Telemundo
Bible
Bible
Bible
Bible
Bible
Classdojo
Classdojo
Classdojo
Classdojo
Classdojo
Daily Horoscope
Daily Horoscope
Daily Horoscope
Daily Horoscope
Daily Horoscope
Hangouts
Hangouts
Hangouts
Hangouts
Hangouts
Lifetime
Lifetime
Lifetime
Lifetime
Lifetime
Microsoft Word
Microsoft Word
Microsoft Word
Microsoft Word
Microsoft Word
My Talking Tom
My Talking Tom
My Talking Tom
My Talking Tom
My Talking Tom
Pokemon Go
Pokemon Go
Pokemon Go
Pokemon Go
Pokemon Go
Shazam
Shazam
Shazam
Shazam
Shazam
Skype
Skype
Skype
Skype
Skype
Subway Surfers
Subway Surfers
Subway Surfers
Subway Surfers
Subway Surfers
Angry Birds
Angry Birds
Angry Birds
Angry Birds
Angry Birds
Auto Clicker
Auto Clicker
Auto Clicker
Auto Clicker
Auto Clicker
Green Dot
Green Dot
Green Dot
Green Dot
Green Dot
Snow
Snow
Snow
Snow
Snow
Terraria
Terraria
Terraria
Terraria
Terraria
Toca Life World
Toca Life World
Toca Life World
Toca Life World
Toca Life World
Facebook Lite
Facebook Lite
Facebook Lite
Facebook Lite
Facebook Lite
Kodi
Kodi
Kodi
Kodi
Kodi
Amazon Alexa
Amazon Alexa
Amazon Alexa
Amazon Alexa
Amazon Alexa
Uc Browser
Uc Browser
Uc Browser
Uc Browser
Uc Browser
Shareit
Shareit
Shareit
Shareit
Shareit
Cocomelon
Cocomelon
Cocomelon
Cocomelon
Cocomelon
Fox News
Fox News
Fox News
Fox News
Fox News
Mcdonalds
Mcdonalds
Mcdonalds
Mcdonalds
Mcdonalds
NBA
NBA
NBA
NBA
NBA
Fox News
Fox News
Fox News
Fox News
Fox News
Mcdonalds
Mcdonalds
Mcdonalds
Mcdonalds
Mcdonalds
Calculator
Calculator
Calculator
Calculator
Calculator
Dominoes
Dominoes
Dominoes
Dominoes
Dominoes
Tiktok
Tiktok
Tiktok
Tiktok
Tiktok
Fortnite
Fortnite
Fortnite
Fortnite
Fortnite
Hulu
Hulu
Hulu
Hulu
Hulu
Minecraft
Minecraft
Minecraft
Minecraft
Minecraft
United Airlines
United Airlines
United Airlines
United Airlines
United Airlines
The Weather Channel
The Weather Channel
The Weather Channel
The Weather Channel
The Weather Channel
Great Clips
Great Clips
Great Clips
Great Clips
Great Clips
Accuweather
Accuweather
Accuweather
Accuweather
Accuweather
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Amazon Prime Video
Wikipedia
Wikipedia
Wikipedia
Wikipedia
Wikipedia
Among Us
Among Us
Among Us
Among Us
Among Us
Cracker Barrel
Cracker Barrel
Cracker Barrel
Cracker Barrel
Cracker Barrel
Genshin Impact
Genshin Impact
Genshin Impact
Genshin Impact
Genshin Impact
Mathway
Mathway
Mathway
Mathway
Mathway
Mychart
Mychart
Mychart
Mychart
Mychart
Offerup
Offerup
Offerup
Offerup
Offerup
Overstock
Overstock
Overstock
Overstock
Overstock
Cashapp
Cashapp
Cashapp
Cashapp
Cashapp
Google Play Store
Google Play Store
Google Play Store
Google Play Store
Google Play Store
Poshmark
Poshmark
Poshmark
Poshmark
Poshmark
Siriusxm
Siriusxm
Siriusxm
Siriusxm
Siriusxm
Gacha Life
Gacha Life
Gacha Life
Gacha Life
Gacha Life
Google Meet
Google Meet
Google Meet
Google Meet
Google Meet
Hotschedules
Hotschedules
Hotschedules
Hotschedules
Hotschedules
Joann
Joann
Joann
Joann
Joann
Mercari
Mercari
Mercari
Mercari
Mercari
Minesweeper
Minesweeper
Minesweeper
Minesweeper
Minesweeper
Monkey
Monkey
Monkey
Monkey
Monkey
Ring
Ring
Ring
Ring
Ring
Schoology
Schoology
Schoology
Schoology
Schoology
Textnow
Textnow
Textnow
Textnow
Textnow
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Cool Wallpaper
Pac Man
Pac Man
Pac Man
Pac Man
Pac Man
Rumble
Rumble
Rumble
Rumble
Rumble
Watched
Watched
Watched
Watched
Watched
Blackboard
Blackboard
Blackboard
Blackboard
Blackboard
Duolingo
Duolingo
Duolingo
Duolingo
Duolingo
Gasbuddy
Gasbuddy
Gasbuddy
Gasbuddy
Gasbuddy
Groupme
Groupme
Groupme
Groupme
Groupme'''
brands = brand.split('\n')
client = MongoClient(host='127.0.0.1', port=27017)
db = client.get_database('crawlab_test')
mycol = db.AFC_appurse_copy1  # type: pymongo.collection.Collection

proxies = {"https": "http://127.0.0.1:7890"}
headers = {'Host': 'en.softonic.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-CN,zh;q=0.9'}


def demo(df):
    url = 'https://en.softonic.com/s/{}:android'
    for d in brands:
        name = d.split(':')[0]
        request_url = url.format(name)
        response = requests.get(url=request_url, headers=headers)
        x = Selector(response.text)
        search_title = x.xpath('''//li[@class="search-results-list__item"][1]//h2/text()''').get().strip()
        n = re.findall(r'[a-zA-Z0-9]+', name)
        t = re.findall(r'[a-zA-Z0-9]+', search_title)
        if len(n) == 0 or len(t) == 0:
            continue
        count = 0
        for k in t:
            if k in n:
                count += 1
        rate = count / len(n)
        if rate <= 0.4:
            continue
        s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
        next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
        h = deepcopy(headers)
        h['Host'] = next_url.split('/')[2]
        response = requests.get(url=next_url, headers=h)
        x = Selector(response.text)
        articles = x.xpath('//article[@class="editor-review"]').get()
        try:
            articles = re.sub('<article(.*?)>', '', articles, count=0, flags=0)
        except:
            continue
        articles = articles.replace("</article>", "")
        length = len(articles.split('<h3>'))
        detail = []
        big_art = ""
        for i in range(length):
            if i < 2:
                if i == 0:
                    string = f'<div class="detailinfo">{articles.split("<h3>")[i]}</div>'
                else:
                    string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
                detail.append(string)
            else:
                string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
                big_art += string
        detail.append(big_art)
        dt = {}
        for j in range(len(detail)):
            if j == 0:
                k = 1
            else:
                k = j + 1
            dt[f"detailinfo_{k}"] = detail[j]
        dt['brand'] = d
        mycol.insert_one(dt)
        print('update', dt.keys())


def get_sth(keywords: str = None):
    url = 'https://en.softonic.com/s/{}:android'
    data = brands[0:1217]
    df = data[1217:-1]
    threading.Thread(target=demo, args=(df,)).start()
    for d in data:
        print(d)
        name = d.split(':')[0]
        request_url = url.format(name)
        response = requests.get(url=request_url, headers=headers)
        x = Selector(response.text)
        search_title = x.xpath('''//li[@class="search-results-list__item"][1]//h2/text()''').get().strip()
        n = re.findall(r'[a-zA-Z0-9]+', name)
        t = re.findall(r'[a-zA-Z0-9]+', search_title)
        if len(n) == 0 or len(t) == 0:
            continue
        count = 0
        for k in t:
            if k in n:
                count += 1
        rate = count / len(n)
        if rate <= 0.4:
            continue
        s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
        next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
        h = deepcopy(headers)
        h['Host'] = next_url.split('/')[2]
        response = requests.get(url=next_url, headers=h)
        x = Selector(response.text)
        articles = x.xpath('//article[@class="editor-review"]').get()
        try:
            articles = re.sub('<article(.*?)>', '', articles, count=0, flags=0)
        except:
            continue
        articles = articles.replace("</article>", "")
        length = len(articles.split('<h3>'))
        detail = []
        big_art = ""
        for i in range(length):
            if i < 2:
                if i == 0:
                    string = f'<div class="detailinfo">{articles.split("<h3>")[i]}</div>'
                else:
                    string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
                detail.append(string)
            else:
                string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
                big_art += string
        detail.append(big_art)
        dt = {}
        for j in range(len(detail)):
            if j == 0:
                k = 1
            else:
                k = j + 1
            dt[f"detailinfo_{k}"] = detail[j]
        dt['brand'] = d
        mycol.insert_one(dt)
        print('update', dt.keys())


if __name__ == '__main__':
    get_sth()
