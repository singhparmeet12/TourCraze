"""
TourCraze Deep Itinerary Knowledge Base.
Contains comprehensive, highly detailed multi-day itineraries for all Indian states,
major tourist cities, and world-class attractions.
"""

from typing import Dict, List, Any

# =============================================================================
# COMPREHENSIVE CURATED DESTINATION KNOWLEDGE BASE (2-to-7 Day Deep Itineraries)
# =============================================================================
DEEP_DESTINATION_KNOWLEDGE: Dict[str, Dict[str, Any]] = {
    # -------------------------------------------------------------------------
    # 🏔️ HIMACHAL PRADESH
    # -------------------------------------------------------------------------
    "manali": {
        "city": "Manali",
        "state": "Himachal Pradesh, India",
        "tagline": "Valley of Gods, Rohtang High Passes & Alpine Pine Forests",
        "category": "mountains",
        "best_season": "October to June (Snow in Dec-Feb)",
        "currency": "INR",
        "cost_multiplier": 1.0,
        "aliases": ["kullu manali", "solang", "old manali", "rohtang", "sethan"],
        "daily_templates": [
            {
                "theme": "Arrival, 16th-Century Hadimba Forest & Old Manali Bohemian Cafes",
                "location": "Old Manali & Dhungri Cedar Forest",
                "morning": {
                    "title": "Hadimba Devi Temple & Ancient Deodar Sanctuary",
                    "location": "Hadimba Temple Road, Dhungri Forest",
                    "activity": "Explore the 1553 AD pagoda-style wooden Hadimba Temple dedicated to Bhima's wife. Walk under 400-year-old towering deodars and sip fresh hot spiced apple juice.",
                    "cost": 250
                },
                "afternoon": {
                    "title": "Old Manali Riverside Foodie Walk & Lunch",
                    "location": "Manu Temple Road, Old Manali",
                    "activity": "Stroll bohemian alleyways filled with hand-knitted woolen shops and silver jewellery. Savor wood-fired trout pizza and mint lemonade at Cafe 1947 by the gushing Manalsu river.",
                    "cost": 850
                },
                "evening": {
                    "title": "Mall Road, Tibetan Monastery & Steaming Siddu",
                    "location": "The Mall Road & Gadhan Thekchhokling Gompa",
                    "activity": "Spin the gilded prayer wheels at the Tibetan Monastery. Shop for Kullu pashmina shawls and taste authentic Himachali steamed Siddu stuffed with poppy-seed paste and ghee.",
                    "cost": 550
                },
                "tip": "Walk across the Manalsu river bridge on foot to avoid Old Manali narrow taxi traffic jams."
            },
            {
                "theme": "Solang Valley Snow Glaciers & High-Altitude Paragliding",
                "location": "Solang Valley (14 km from Manali)",
                "morning": {
                    "title": "Solang Valley Ropeway & Mt. Phatru Summit",
                    "location": "Solang Valley Gondola Station",
                    "activity": "Ride the high-speed cable car to 3,200 meters at Mt. Phatru for 360-degree snow peak vistas. Embark on tandem high-altitude paragliding or snow zorbing across the slopes.",
                    "cost": 2400
                },
                "afternoon": {
                    "title": "Anjani Mahadev Waterfall Trek & Pahadi Lunch",
                    "location": "Upper Solang Stream",
                    "activity": "Take an easy 2 km nature trek or pony ride to the sacred Anjani Mahadev waterfall cliff. Enjoy hot maggi, rajma-chawal, and mountain ginger-lemon tea at riverside wooden shacks.",
                    "cost": 600
                },
                "evening": {
                    "title": "Vashisht Natural Thermal Springs & German Bakery",
                    "location": "Vashisht Village",
                    "activity": "Soak in 4,000-year-old natural hot sulphur mineral springs believed to have healing properties. Relax at German Bakery with fresh apple crumble cake.",
                    "cost": 450
                },
                "tip": "Book government-approved paragliding pilots at the official counters in Solang Valley."
            },
            {
                "theme": "Engineering Marvel: Atal Tunnel & Sissu Waterfall, Lahaul",
                "location": "Atal Tunnel (9.02 km) & Sissu, Lahaul Valley",
                "morning": {
                    "title": "Drive Through Atal Tunnel into Lahaul Moonscapes",
                    "location": "South Portal to North Portal (Atal Tunnel)",
                    "activity": "Cross the world's longest highway tunnel above 10,000 feet. Experience the magical transition from lush green Kullu mountains to rugged, snow-capped Trans-Himalayan valleys.",
                    "cost": 1600
                },
                "afternoon": {
                    "title": "Sissu Waterfall Hike & Chandra River Pebble Bank",
                    "location": "Sissu Village, Lahaul",
                    "activity": "Hike right to the foot of the 50-meter thundering Sissu glacial waterfall. Walk on the suspension bridge over the turquoise Chandra River and savor authentic Tibetan Thukpa.",
                    "cost": 750
                },
                "evening": {
                    "title": "Return via Solang & Riverside Bonfire Session",
                    "location": "Beas Riverbed / Aleo",
                    "activity": "Return to Manali valley and unwind beside a crackling riverside bonfire with live acoustic guitar sessions and grilled barbecued paneer/chicken.",
                    "cost": 950
                },
                "tip": "Temperatures drop sharply in Lahaul; wear windproof thermal jackets even during summer."
            }
        ]
    },

    "shimla": {
        "city": "Shimla",
        "state": "Himachal Pradesh, India",
        "tagline": "Queen of Hills, Colonial Heritage & Himalayan Toy Train",
        "category": "mountains",
        "best_season": "Year-Round (Snow in Dec-Feb)",
        "currency": "INR",
        "cost_multiplier": 1.05,
        "aliases": ["kufri", "chail", "narkanda", "mashobra", "himachal shimla"],
        "daily_templates": [
            {
                "theme": "The Ridge, Neo-Gothic Christ Church & Heritage Mall Road",
                "location": "The Ridge & Mall Road Shimla",
                "morning": {
                    "title": "Heritage Walk & 1857 Christ Church",
                    "location": "The Ridge, Shimla",
                    "activity": "Stroll across the iconic pedestrian-only Ridge, photograph the 1857 stained-glass Christ Church, and take in panoramic views of the Pir Panjal range.",
                    "cost": 200
                },
                "afternoon": {
                    "title": "Gaiety Heritage Theatre & Indian Coffee House",
                    "location": "Mall Road Promenade",
                    "activity": "Tour the Victorian Gothic 1887 Gaiety Theatre where Rudyard Kipling performed. Enjoy authentic filter coffee, hot mutton cutlets, and dosas at the historic Indian Coffee House.",
                    "cost": 600
                },
                "evening": {
                    "title": "Jakhoo Hill Ropeway & Giant Hanuman Shrine",
                    "location": "Jakhoo Hill (Highest Peak of Shimla at 8,054 ft)",
                    "activity": "Ride the scenic aerial ropeway cable car up to Jakhoo Temple summit. Gaze at the 108-foot colossal vermillion Hanuman statue as the sun sets over valley lights.",
                    "cost": 750
                },
                "tip": "Keep your eyeglasses and food items tucked inside bags near Jakhoo due to mischievous temple monkeys."
            },
            {
                "theme": "Viceregal Lodge, Himalayan Bird Park & Kufri Alpine Highlands",
                "location": "Observatory Hill & Kufri",
                "morning": {
                    "title": "Viceregal Lodge (Rashtrapati Niwas) Tour",
                    "location": "Observatory Hill (Indian Institute of Advanced Study)",
                    "activity": "Explore the majestic English Renaissance manor where historic Partition conferences took place. Walk through manicured royal botanical lawns and indoor teakwood libraries.",
                    "cost": 450
                },
                "afternoon": {
                    "title": "Kufri Alpine Horseback Trail & Himalayan Nature Park",
                    "location": "Kufri (16 km east at 8,600 ft)",
                    "activity": "Ride horseback through cedar forests to Mahasu Peak. Visit Himalayan Nature Park to see snow leopards, monal pheasants, and Himalayan brown bears.",
                    "cost": 1200
                },
                "evening": {
                    "title": "Lakkar Bazar Woodcraft & Steaming Chana Tikki",
                    "location": "Lakkar Bazar (Adjoining The Ridge)",
                    "activity": "Shop for handcrafted walnut wood keychains, walking sticks, and wooden kitchenware. Savor famous crispy Shimla Chana-Tikki at Sitaram and hot gulab jamun.",
                    "cost": 400
                },
                "tip": "Take the Shimla municipal lift from Cart Road directly up to Mall Road to skip steep stairs."
            }
        ]
    },

    "spiti": {
        "city": "Spiti Valley",
        "state": "Himachal Pradesh, India",
        "tagline": "The Middle Land: Thousand-Year Monasteries & High Desert Stars",
        "category": "mountains",
        "best_season": "May to October",
        "currency": "INR",
        "cost_multiplier": 1.2,
        "aliases": ["kaza", "spiti valley", "chandratal", "tabo", "hikkim", "kibber"],
        "daily_templates": [
            {
                "theme": "Kaza Town, 1000-Year Key Monastery & Kibber High Village",
                "location": "Kaza, Key Gompa & Kibber",
                "morning": {
                    "title": "11th-Century Key Gompa Fortress Monastery",
                    "location": "Key Monastery (4,166m altitude)",
                    "activity": "Climb up the multi-storied fortress monastery overlooking the Spiti river. Receive herbal tea blessings from resident Buddhist monks and view ancient thangkas and murals.",
                    "cost": 300
                },
                "afternoon": {
                    "title": "Kibber Wildlife Sanctuary & Highest Chicham Bridge",
                    "location": "Kibber (4,270m) & Chicham Suspension Bridge",
                    "activity": "Walk through Tibetan white-washed stone homes in Kibber. Cross the 1,000-ft deep canyon on Asia's highest motorable suspension bridge at Chicham. Taste authentic Tibetan momos.",
                    "cost": 650
                },
                "evening": {
                    "title": "Kaza Main Market Walk & Sea-Buckthorn Herbal Tea",
                    "location": "Kaza Market & Riverside Stupa",
                    "activity": "Browse for Spiti organic sea-buckthorn tea, woolens, and prayer flags. Relax at The Himalayan Cafe with butter tea and buckwheat pancakes under clear mountain skies.",
                    "cost": 500
                },
                "tip": "Spend your first 24 hours in Kaza resting and drinking plenty of fluids to acclimatize to 12,000 ft."
            },
            {
                "theme": "World Records Circuit: Highest Post Office & Fossil Village",
                "location": "Hikkim (4,440m), Komic (4,587m) & Langza",
                "morning": {
                    "title": "Send Postcards from World's Highest Post Office",
                    "location": "Hikkim Village Post Office",
                    "activity": "Write and mail handwritten stamped postcards to loved ones from the world's highest operational post office at 14,567 feet.",
                    "cost": 400
                },
                "afternoon": {
                    "title": "World's Highest Motorable Village & Tangyud Gompa",
                    "location": "Komic Village",
                    "activity": "Visit Komic at 15,049 ft and its 14th-century monastery. Have organic seabuckthorn tea and barley thukpa at the Spiti Organic Kitchen run by local women.",
                    "cost": 550
                },
                "evening": {
                    "title": "Langza Golden Buddha & Prehistoric Marine Fossils",
                    "location": "Langza Village (Chau Chau Kang Nilda View)",
                    "activity": "Photograph the 1,000-year-old giant golden Buddha statue gazing over snow-capped Chau Chau Kang Nilda. Search for Tethys sea ammonite marine fossils in the shale rocks.",
                    "cost": 350
                },
                "tip": "Do not extract or buy illegal fossils; take photos to preserve Spiti's geological heritage."
            },
            {
                "theme": "Turquoise Crescent: Chandratal Lake & Kunzum Pass",
                "location": "Kunzum La (4,551m) & Chandratal Lake (4,300m)",
                "morning": {
                    "title": "Kunzum Pass Stupas & Buddhist Circumambulation",
                    "location": "Kunzum Pass (Gateway between Spiti & Lahaul)",
                    "activity": "Cross the 15,000-ft Kunzum Pass, drive around the sacred Kunzum Goddess stupa for good fortune, and marvel at Shigri glacier views.",
                    "cost": 1200
                },
                "afternoon": {
                    "title": "Chandratal 'Moon Lake' Fairy-tale Walk",
                    "location": "Chandratal Lake Sanctuary",
                    "activity": "Hike the gentle 1.5 km trail to the crescent-shaped turquoise Moon Lake. Watch the water magically shift shades from deep aquamarine to sapphire under changing sunlight.",
                    "cost": 600
                },
                "evening": {
                    "title": "Milky Way Galaxy Stargazing at Parasol Camps",
                    "location": "Chandratal Base Campsite (4,000m)",
                    "activity": "Settle into a cozy Swiss canvas camp. Step outside at night to witness the jaw-dropping, naked-eye spectacle of millions of stars and the vivid Milky Way core.",
                    "cost": 1800
                },
                "tip": "Camping within 3 km of Chandratal shoreline is prohibited by law; stay at designated eco-campsites."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 🏖️ GOA
    # -------------------------------------------------------------------------
    "goa": {
        "city": "Goa",
        "state": "Goa, India",
        "tagline": "Golden Beaches, Portuguese Latin Quarters & Coastal Flavors",
        "category": "beach",
        "best_season": "October to April",
        "currency": "INR",
        "cost_multiplier": 1.15,
        "aliases": ["north goa", "south goa", "panjim", "panaji", "calangute", "baga", "anjuna", "palolem", "vagator", "candolim"],
        "daily_templates": [
            {
                "theme": "North Goa Sea Forts, Chapora Sunset & Vagator Cliffside Sundowners",
                "location": "Sinquerim, Candolim & Vagator",
                "morning": {
                    "title": "17th-Century Aguada Fort & Sea Bastion",
                    "location": "Sinquerim Beach / Fort Aguada",
                    "activity": "Explore the massive Portuguese freshwater fort built in 1612 with its iconic four-storey lighthouse overlooking the Arabian Sea.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Authentic Goan Seafood Shack Lunch & Watersports",
                    "location": "Calangute / Candolim Shoreline",
                    "activity": "Feast on Goan butter-garlic calamari, Kingfish rava fry, and chilled coconut beverages right on the soft golden sands.",
                    "cost": 1200
                },
                "evening": {
                    "title": "Chapora Fort 'Dil Chahta Hai' Sunset & Cliff Lounge",
                    "location": "Chapora Fort & Little Vagator Cliffs",
                    "activity": "Climb up the red laterite ramparts of Chapora Fort for an epic sunset over the Ozran coast, followed by Mediterranean mezze and DJ tunes at Thalassa or Antares.",
                    "cost": 1600
                },
                "tip": "Rent a scooter or self-drive car with yellow plates from registered vendors in Calangute."
            },
            {
                "theme": "UNESCO Old Goa Cathedrals & Fontainhas Latin Quarter",
                "location": "Old Goa & Panjim Fontainhas",
                "morning": {
                    "title": "Basilica of Bom Jesus & Se Cathedral Heritage",
                    "location": "Old Goa UNESCO Heritage Complex",
                    "activity": "Marvel at the 1605 Baroque Basilica holding the sacred relics of St. Francis Xavier and the colossal golden bell inside Se Cathedral.",
                    "cost": 300
                },
                "afternoon": {
                    "title": "Fontainhas Latin Quarter Walking Tour & Portuguese Bakery",
                    "location": "Panjim Latin Quarter",
                    "activity": "Wander through cobblestone lanes framed by pastel yellow, indigo, and terracotta Portuguese colonial villas with hanging wrought-iron balconies. Savor warm Bebinca and cashew sweets at Confeitaria 31 de Janeiro.",
                    "cost": 850
                },
                "evening": {
                    "title": "Mandovi River Luxury Sunset Cruise & Goan Folk Dancers",
                    "location": "Santa Monica Jetty, Panaji",
                    "activity": "Board a twilight river cruise gliding past riverfront casinos with live Dekhni and Fugdi folk dance performances on the deck.",
                    "cost": 900
                },
                "tip": "Dress modestly with covered shoulders and knees when visiting the operational churches in Old Goa."
            },
            {
                "theme": "South Goa Secret Lagoons, Cabo de Rama & Palolem Crescent Bay",
                "location": "Cabo de Rama, Cola Beach & Palolem",
                "morning": {
                    "title": "Cabo de Rama Cliff Fort & Untouched Emerald Waters",
                    "location": "Canacona, South Goa",
                    "activity": "Drive through cashew and coconut plantations to the historic Cabo de Rama fortress perched atop sheer ocean cliffs.",
                    "cost": 250
                },
                "afternoon": {
                    "title": "Secret Freshwater Lagoon Kayaking at Cola Beach",
                    "location": "Cola Beach",
                    "activity": "Descend to the hidden golden sandbar separating the emerald freshwater lagoon from the crashing ocean waves. Kayak quietly along palm-lined banks.",
                    "cost": 900
                },
                "evening": {
                    "title": "Palolem Crescent Beach Dolphin Cruise & Candlelit Dinner",
                    "location": "Palolem Beach, South Goa",
                    "activity": "Take a wooden fishing boat out into the bay to spot wild playful dolphins, then dine under glowing fairy-lit canopies on the sand.",
                    "cost": 1300
                },
                "tip": "Cola beach path is an unpaved mud track; take your time while driving two-wheelers."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 👑 RAJASTHAN
    # -------------------------------------------------------------------------
    "jaipur": {
        "city": "Jaipur (The Pink City)",
        "state": "Rajasthan, India",
        "tagline": "Grand Hill Forts, Royal Palaces & World-Renowned Bazaars",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.05,
        "aliases": ["jaipur", "pink city", "amber fort", "hawa mahal", "rajasthan jaipur"],
        "daily_templates": [
            {
                "theme": "Amber Fort Royalty, Sheesh Mahal & Jal Mahal Floating Palace",
                "location": "Amer & Man Sagar Lake",
                "morning": {
                    "title": "Amer Fort Hilltop Citadel & Sheesh Mahal Mirrors",
                    "location": "Devisinghpura, Amer (11 km north)",
                    "activity": "Explore Raja Man Singh's 16th-century fortress, the glittering Sheesh Mahal made of thousands of Belgian convex glass pieces, and the Ganesh Pol royal gateway.",
                    "cost": 550
                },
                "afternoon": {
                    "title": "Panna Meena Ka Kund Stepwell & Royal Rajasthani Thali",
                    "location": "Amer Town & 1135 AD Restaurant",
                    "activity": "Photograph the geometrical 8-storey stepwell at Panna Meena. Feast on authentic Dal Baati Churma, Gatte ki Sabzi, and Ker Sangri in royal brass thalis.",
                    "cost": 1100
                },
                "evening": {
                    "title": "Jal Mahal Palace Lakeview & Nahargarh Sunset",
                    "location": "Man Sagar Lake & Nahargarh Fort",
                    "activity": "Admire the illuminated 18th-century palace floating in the middle of Man Sagar lake, then drive up to Nahargarh Fort's Padao lounge for sunset over the entire Pink City.",
                    "cost": 650
                },
                "tip": "Visit Amer Fort right at 8:00 AM opening to take crowd-free photos in the Mirror Palace."
            },
            {
                "theme": "City Palace, Jantar Mantar UNESCO Observatory & Hawa Mahal",
                "location": "Old Walled Pink City",
                "morning": {
                    "title": "City Palace Royal Courtyards & Peacock Gate",
                    "location": "Jaleb Chowk, Old City",
                    "activity": "Tour the active royal residence of the Jaipur Maharaja, marvel at the four seasonal gates in Pritam Niwas Chowk, and see the world's largest silver urns (Gangajalis).",
                    "cost": 700
                },
                "afternoon": {
                    "title": "Jantar Mantar UNESCO Astronomical Observatory",
                    "location": "Opposite City Palace",
                    "activity": "Discover the 1734 astronomical stone instruments built by Sawai Jai Singh II, including the world's largest stone sundial accurate to 2 seconds.",
                    "cost": 300
                },
                "evening": {
                    "title": "Hawa Mahal (Palace of Winds) & Bapu Bazar Shopping",
                    "location": "Badi Choupad & Bapu Bazar",
                    "activity": "Photograph Hawa Mahal's 953 honeycombed jharokhas from the Tattoo Cafe terrace. Shop for blue pottery, Jaipuri quilts (Razai), and mojari leather juttis.",
                    "cost": 850
                },
                "tip": "Hire an accredited tourist guide inside Jantar Mantar to truly understand how the stone sundials function."
            },
            {
                "theme": "Chokhi Dhani Ethnic Village & Albert Hall Museum",
                "location": "Ram Niwas Garden & Tonk Road",
                "morning": {
                    "title": "Albert Hall Museum (Central Museum)",
                    "location": "Ram Niwas Garden",
                    "activity": "Explore the Indo-Saracenic museum showcasing royal carpets, weaponry, miniature paintings, and an ancient Egyptian mummy.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "LMB (Laxmi Mishtan Bhandar) Street Food Trail",
                    "location": "Johari Bazar, Walled City",
                    "activity": "Taste Jaipur's most famous crispy Pyaaz Kachoris, Ghewar soaked in saffron rabdi, and creamy lassi served in earthen kulhads.",
                    "cost": 550
                },
                "evening": {
                    "title": "Chokhi Dhani Rajasthani Cultural Village Fiesta",
                    "location": "12 Miles, Tonk Road",
                    "activity": "Immerse yourself in Rajasthani folk dances (Ghoomar, Kalbelia), puppet shows, camel rides, acrobatics, and an authentic royal village dinner seated on floor cushions.",
                    "cost": 1600
                },
                "tip": "Chokhi Dhani opens at 5:00 PM; arrive on time to enjoy all cultural performances before dinner."
            }
        ]
    },

    "udaipur": {
        "city": "Udaipur (City of Lakes)",
        "state": "Rajasthan, India",
        "tagline": "Venice of the East, Palaces & Candlelit Lake Pichola",
        "category": "heritage",
        "best_season": "September to March",
        "currency": "INR",
        "cost_multiplier": 1.15,
        "aliases": ["udaipur", "city of lakes", "lake pichola", "fateh sagar", "rajasthan udaipur"],
        "daily_templates": [
            {
                "theme": "City Palace Royalty, Jagdish Temple & Lake Pichola Boat Cruise",
                "location": "City Palace Complex & Pichola",
                "morning": {
                    "title": "City Palace: Rajasthan's Largest Palace Complex",
                    "location": "Lake Pichola East Bank",
                    "activity": "Walk through 400 years of Mewar royal history across the Zenana Mahal, Mor Chowk peacock mosaics, and Sheesh Mahal overlooking Lake Pichola.",
                    "cost": 650
                },
                "afternoon": {
                    "title": "1651 Jagdish Temple & Rooftop Traditional Lunch",
                    "location": "Jagdish Chowk",
                    "activity": "Admire the 3-tiered carved stone pillars of Jagdish Temple. Dine at a lakefront terrace enjoying authentic Mewari Gatta curry and Safed Maas.",
                    "cost": 850
                },
                "evening": {
                    "title": "Sunset Boat Cruise to Jag Mandir Island Palace",
                    "location": "Bansi Ghat, Lake Pichola",
                    "activity": "Board a royal motorboat cruising past the Taj Lake Palace to Jag Mandir island. Watch the white marble courtyards glow as the sun sets over the Aravalli hills.",
                    "cost": 1100
                },
                "tip": "The sunset boat slot (5:00 PM - 6:00 PM) at Bansi Ghat offers the most dramatic golden lighting."
            },
            {
                "theme": "Bagore Ki Haveli Folk Spectacle, Saheliyon Ki Bari & Sajjangarh Monsoon Palace",
                "location": "Gangaur Ghat & Sajjangarh Hill",
                "morning": {
                    "title": "Saheliyon-ki-Bari (Courtyard of Maidens)",
                    "location": "Fateh Sagar Lake Road",
                    "activity": "Stroll through royal landscaped marble fountains, lotus pools, and elephant-shaped water jets built for the princesses and royal maidens.",
                    "cost": 250
                },
                "afternoon": {
                    "title": "Fateh Sagar Lake Drive & Vintage Car Museum",
                    "location": "Fateh Sagar / Gulab Bagh",
                    "activity": "Drive around the scenic promenade of Fateh Sagar Lake. Visit the Maharaja's private collection of classic Rolls Royce, Cadillacs, and Mercedes.",
                    "cost": 600
                },
                "evening": {
                    "title": "Dharohar Folk Dance at Bagore Ki Haveli",
                    "location": "Gangaur Ghat",
                    "activity": "Watch the spellbinding evening Dharohar cultural dance with Kalbelia dancers, fiery brass pot balancings on heads, and traditional Rajasthani puppetry.",
                    "cost": 450
                },
                "tip": "Queue up at Bagore Ki Haveli ticket window by 5:30 PM for the 7:00 PM Dharohar show as seats are first-come-first-serve."
            }
        ]
    },

    "jodhpur": {
        "city": "Jodhpur (The Blue City)",
        "state": "Rajasthan, India",
        "tagline": "Colossal Mehrangarh Fort, Indigo Blue Alleys & Umaid Bhawan",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.0,
        "aliases": ["jodhpur", "blue city", "mehrangarh", "umaid bhawan", "jaswant thada"],
        "daily_templates": [
            {
                "theme": "Mehrangarh Fort Citadel, Flying Fox Zip-line & Blue City Alleys",
                "location": "Mehrangarh Fort & Navchokiya Old City",
                "morning": {
                    "title": "Mehrangarh Fort: The Citadel of the Sun",
                    "location": "Mehrangarh Fort (Perched 400 ft above the city)",
                    "activity": "Explore Rao Jodha's 1459 fortress, the Phool Mahal (Palace of Flowers), Moti Mahal, royal palanquins, and cannons on the battlements.",
                    "cost": 600
                },
                "afternoon": {
                    "title": "Flying Fox Zip-lining over Fort Moats & Jaswant Thada",
                    "location": "Mehrangarh Moat & Jaswant Thada Memorial",
                    "activity": "Glide on 6 exhilarating aerial zip-lines over ancient fort walls and lakes. Visit the delicate white marble cenotaph of Jaswant Thada.",
                    "cost": 1800
                },
                "evening": {
                    "title": "Navchokiya Blue City Walking Trail & Makhaniya Lassi",
                    "location": "Clock Tower (Ghanta Ghar) & Sardar Market",
                    "activity": "Wander through the indigo blue painted alleys of Navchokiya. Savor world-famous saffron Makhaniya Lassi and spicy Mawa Kachoris at Shri Mishrilal.",
                    "cost": 450
                },
                "tip": "Wear comfortable walking shoes for the cobblestone ramps inside Mehrangarh Fort."
            },
            {
                "theme": "Umaid Bhawan Art Deco Palace & Mandore Royal Gardens",
                "location": "Umaid Bhawan & Mandore Heritage Complex",
                "morning": {
                    "title": "Umaid Bhawan Palace Royal Museum",
                    "location": "Circuit House Road, Cantt Area",
                    "activity": "Tour one of the world's largest private royal residences built of golden Chittar sandstone, featuring royal clock collections, classic cars, and crystal.",
                    "cost": 400
                },
                "afternoon": {
                    "title": "Mandore Ancient Capital Cenotaphs & Rock Terraces",
                    "location": "Mandore (9 km north)",
                    "activity": "Explore the multi-tiered red sandstone devals (chhatris) of the Marwar rulers set amidst landscaped botanical gardens and playful langurs.",
                    "cost": 300
                },
                "evening": {
                    "title": "Bishnoi Village Safari & Desert Sunset Feast",
                    "location": "Guda Bishnoiyan / Rohet",
                    "activity": "Visit eco-conscious Bishnoi tribal hamlets, spot wild blackbucks and migratory birds, watch potters and durry weavers, and enjoy authentic millet roti with garlic chutney.",
                    "cost": 1200
                },
                "tip": "Bishnoi communities strictly protect all flora and fauna; respect local customs and dress conservatively."
            }
        ]
    },

    "jaisalmer": {
        "city": "Jaisalmer (The Golden City)",
        "state": "Rajasthan, India",
        "tagline": "Living Golden Fort, Thar Desert Dunes & Camel Safaris",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.05,
        "aliases": ["jaisalmer", "thar desert", "sam sand dunes", "golden city", "sonar qila"],
        "daily_templates": [
            {
                "theme": "Sonar Qila (Living Golden Fort) & 7 Intricate Jain Temples",
                "location": "Jaisalmer Fort Citadel",
                "morning": {
                    "title": "Jaisalmer Golden Fort (Sonar Qila) Walking Tour",
                    "location": "Trikuta Hill Fort",
                    "activity": "Walk through India's only living fortress where 4,000 residents live inside yellow sandstone walls built in 1156 AD. Explore the Maharaja Palace (Raj Mahal).",
                    "cost": 450
                },
                "afternoon": {
                    "title": "12th-Century Carved Yellow Sandstone Jain Temples",
                    "location": "Inside Fort Complex",
                    "activity": "Marvel at the 7 interconnected Jain shrines featuring thousands of delicate human and celestial stone carvings without mortar. Visit the Gyan Bhandar manuscript library.",
                    "cost": 350
                },
                "evening": {
                    "title": "Patwon Ki Haveli & Gadisar Lake Sunset Paddle",
                    "location": "Patwa Complex & Gadisar Lake",
                    "activity": "Tour the 5-mansion Patwon ki Haveli with its 66 filigreed jharokha balconies. Paddle a boat across Gadisar Lake under the carved Tillon Ki Prokhol gateway.",
                    "cost": 750
                },
                "tip": "Enjoy panoramic golden sunset views from the fort cannon bastions at Sunset Point."
            },
            {
                "theme": "Haunted Kuldhara Ghost Village & Sam Sand Dunes Desert Safari",
                "location": "Kuldhara & Sam Sand Dunes (42 km west)",
                "morning": {
                    "title": "Abandoned 13th-Century Kuldhara Ghost Village",
                    "location": "Kuldhara Village, Thar Desert",
                    "activity": "Explore the eerie preserved ruins of 84 Paliwal Brahmin villages abandoned overnight in the 1800s due to a tyrant minister's curse.",
                    "cost": 300
                },
                "afternoon": {
                    "title": "4x4 Thar Dune Bashing & Quad Biking",
                    "location": "Sam Sand Dunes Desert Highway",
                    "activity": "Experience heart-pounding off-road 4x4 dune bashing across golden Thar dunes, followed by quad biking on deep sand waves.",
                    "cost": 1800
                },
                "evening": {
                    "title": "Sunset Camel Safari, Kalbelia Folk Dance & Swiss Desert Camp",
                    "location": "Sam Desert Dune Camps",
                    "activity": "Ride decorated camels into the sunset. Enjoy live Kalbelia snake-dance performances, Rajasthani ghoomar, fireworks, and a lavish desert dinner under the stars.",
                    "cost": 2200
                },
                "tip": "Wear sunglasses and wrap a cotton turban/scarf to protect against blowing sand during the evening camel ride."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 🌴 KERALA
    # -------------------------------------------------------------------------
    "kerala": {
        "city": "Kerala (Munnar, Alleppey & Fort Kochi)",
        "state": "Kerala, India",
        "tagline": "God's Own Country: Tea Mountains, Houseboat Backwaters & Spice Trails",
        "category": "nature",
        "best_season": "September to March",
        "currency": "INR",
        "cost_multiplier": 1.1,
        "aliases": ["kerala", "munnar", "alleppey", "alappuzha", "kochi", "cochin", "thekkady", "wayanad", "varkala"],
        "daily_templates": [
            {
                "theme": "Fort Kochi Colonial Heritage, Chinese Fishing Nets & Kathakali",
                "location": "Fort Kochi & Mattancherry",
                "morning": {
                    "title": "Historic Chinese Fishing Nets & St. Francis Church",
                    "location": "Fort Kochi Beach & Church Road",
                    "activity": "Watch fishermen operate 14th-century cantilevered Chinese fishing nets at sunrise. Visit India's oldest European church where Vasco da Gama was first buried.",
                    "cost": 300
                },
                "afternoon": {
                    "title": "Mattancherry Dutch Palace & Jew Town Antique Street",
                    "location": "Jew Town & Paradesi Synagogue (1568 AD)",
                    "activity": "Admire Ramayana murals at the Dutch Palace. Stroll through Jew Town smelling fresh cardamom and cinnamon, browsing antique shops and 400-year-old Jewish synagogue.",
                    "cost": 650
                },
                "evening": {
                    "title": "Live Kathakali Facial Makeup & Classical Dance Drama",
                    "location": "Kerala Kathakali Centre, Fort Kochi",
                    "activity": "Arrive early to watch actors apply intricate organic herbal face paints, followed by a mesmerizing 1-hour performance of facial expressions (Navarasas) and martial drama.",
                    "cost": 600
                },
                "tip": "Arrive at 5:00 PM at the Kathakali theatre to witness the fascinating traditional green-room makeup process."
            },
            {
                "theme": "Munnar Tea Mountain Valleys & Eravikulam Nilgiri Tahr",
                "location": "Munnar (1,600m altitude)",
                "morning": {
                    "title": "Eravikulam National Park (Home of Nilgiri Tahr)",
                    "location": "Rajamalai Hills, Munnar",
                    "activity": "Take the government safari bus up misty rolling hills to spot the endangered wild mountain goat (Nilgiri Tahr) roaming free under Anamudi (South India's highest peak).",
                    "cost": 550
                },
                "afternoon": {
                    "title": "Tata Tea Museum & Fresh Leaf Factory Processing",
                    "location": "KDHP Nallathanni Estate",
                    "activity": "Learn the art of tea manufacturing from fresh leaf picking to black CTC tea grading. Enjoy a guided tasting of first-flush white and green teas.",
                    "cost": 450
                },
                "evening": {
                    "title": "Mattupetty Dam & Echo Point Shola Forests",
                    "location": "Mattupetty / Echo Point (13 km east)",
                    "activity": "Take a scenic speed-boat ride across Mattupetty reservoir surrounded by tea slopes, and listen to your voice echo across natural green amphitheaters.",
                    "cost": 650
                },
                "tip": "Book Eravikulam National Park passes online to avoid the 2-hour morning ticket queue."
            },
            {
                "theme": "Alleppey Luxury Houseboat Cruise across Vembanad Backwaters",
                "location": "Alleppey (Alappuzha) Backwaters",
                "morning": {
                    "title": "Boarding Traditional Thatched Kettuvallam Houseboat",
                    "location": "Punnamada Jetty, Alleppey",
                    "activity": "Check into your private air-conditioned wooden houseboat constructed using coir knots and jackfruit wood without a single iron nail.",
                    "cost": 4500
                },
                "afternoon": {
                    "title": "Backwater Canal Glide & Traditional Karimeen Lunch",
                    "location": "Vembanad Lake & Kuttanad Waterways",
                    "activity": "Glide through narrow palm-fringed canals below sea level. Savor authentic hot Karimeen Pollichathu (pearl spot fish wrapped in banana leaf) cooked on board.",
                    "cost": 800
                },
                "evening": {
                    "title": "Village Canoe Shikiara Ride & Sunset over Paddy Fields",
                    "location": "Kainakary / Champakulam Village",
                    "activity": "Switch to a small wooden rowing canoe to explore hidden village waterways, duck farms, and paddy fields glowing golden under the sunset sky.",
                    "cost": 650
                },
                "tip": "Houseboats anchor by 5:30 PM near village banks per government fishing net regulations; enjoy the serene night sounds on water."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 🏛️ DELHI, PUNJAB & AGRA
    # -------------------------------------------------------------------------
    "delhi": {
        "city": "New Delhi & Old Delhi",
        "state": "National Capital Territory, India",
        "tagline": "Mughal Monuments, Colonial Lutyens & Food Capital",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.0,
        "aliases": ["delhi", "new delhi", "old delhi", "delhi ncr"],
        "daily_templates": [
            {
                "theme": "Old Delhi Mughal Heartland: Jama Masjid, Chandni Chowk & Red Fort",
                "location": "Shahjahanabad, Old Delhi",
                "morning": {
                    "title": "1656 Jama Masjid & Chandni Chowk Rickshaw Ride",
                    "location": "Jama Masjid / Chandni Chowk",
                    "activity": "Climb the grand red sandstone steps of India's largest Mughal mosque. Hop on a cycle-rickshaw navigating through 400-year-old spice lanes of Khari Baoli.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Paranthe Wali Gali & Karim's Mughal Lunch",
                    "location": "Gali Paranthe Wali & Matia Mahal",
                    "activity": "Taste deep-fried rabri and paneer paranthas, or savor legendary mutton seekh kebabs and butter chicken at 1913 Karim's near Jama Masjid gate 1.",
                    "cost": 750
                },
                "evening": {
                    "title": "Red Fort (Lal Qila) Ramparts & Light Show",
                    "location": "Netaji Subhash Marg, Chandni Chowk",
                    "activity": "Walk through the Diwan-i-Aam and Diwan-i-Khas where the Peacock Throne once stood. Witness the sound and light history narration across the battlements.",
                    "cost": 600
                },
                "tip": "Use the Delhi Metro (Yellow Line - Chandni Chowk Station) to avoid Old Delhi street traffic."
            },
            {
                "theme": "UNESCO Qutub Minar, Humayun's Tomb Garden & India Gate",
                "location": "South Delhi & Central Vista",
                "morning": {
                    "title": "Qutub Minar Complex & 1600-Year Rustless Iron Pillar",
                    "location": "Mehrauli, South Delhi",
                    "activity": "Marvel at the 73-meter fluted red sandstone minaret built in 1192 AD by Qutb-ud-din Aibak and the metallurgical mystery of the rustless Gupta Iron Pillar.",
                    "cost": 450
                },
                "afternoon": {
                    "title": "Humayun's Tomb: The Architectural Precursor to the Taj Mahal",
                    "location": "Nizamuddin East",
                    "activity": "Stroll through the symmetrical Charbagh Persian water gardens and white marble dome mausoleum built in 1570 for Mughal Emperor Humayun.",
                    "cost": 500
                },
                "evening": {
                    "title": "India Gate War Memorial & Kartavya Path Stroll",
                    "location": "Kartavya Path (Central Vista)",
                    "activity": "Pay tribute at the National War Memorial and Amar Jawan Jyoti. Stroll down the illuminated lawns of Kartavya Path enjoying ice cream and cold coffee.",
                    "cost": 300
                },
                "tip": "Monument tickets can be booked online via ASI QR codes on spot for discounted entry."
            }
        ]
    },

    "amritsar": {
        "city": "Amritsar",
        "state": "Punjab, India",
        "tagline": "The Golden Temple, Wagah Border Patriotism & Punjabi Gastronomy",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 0.85,
        "aliases": ["amritsar", "golden temple", "harmandir sahib", "wagah border", "punjab amritsar"],
        "daily_templates": [
            {
                "theme": "The Golden Temple (Harmandir Sahib), Mega Langar & Jallianwala Bagh",
                "location": "Heritage Street, Amritsar",
                "morning": {
                    "title": "Sri Harmandir Sahib (The Golden Temple) Darshan",
                    "location": "Golden Temple Road",
                    "activity": "Circumambulate the sacred Amrit Sarovar pool and bow before the gilded sanctum housing the Guru Granth Sahib. Listen to soothing live Gurbani kirtan.",
                    "cost": 100
                },
                "afternoon": {
                    "title": "World's Largest Free Community Kitchen (Guru Ka Langar)",
                    "location": "Langar Hall Complex",
                    "activity": "Partake in the holy Langar serving 100,000 pilgrims daily with hot rotis, dal, and kheer prepared by devoted volunteers regardless of religion or caste.",
                    "cost": 150
                },
                "evening": {
                    "title": "Jallianwala Bagh Memorial & Partition Museum",
                    "location": "Heritage Street (100 meters away)",
                    "activity": "Pay respects at the 1919 massacre martyrs' well and bullet-riddled brick walls, followed by the emotional Partition Museum at Town Hall.",
                    "cost": 300
                },
                "tip": "Cover your head with a scarf and wash feet in the shallow cleansing pool before entering Golden Temple premises."
            },
            {
                "theme": "Wagah-Attari Border Beating Retreat Ceremony & Kesar Da Dhaba",
                "location": "Attari-Wagah Border (28 km west) & Old Amritsar",
                "morning": {
                    "title": "Gobindgarh Fort & Punjab Martial History Museum",
                    "location": "Old Cantt Road, Gobindgarh",
                    "activity": "Explore Maharaja Ranjit Singh's 18th-century military fortress, the Toshakhana coin treasury, and watch the 7D show on Sikh military victories.",
                    "cost": 450
                },
                "afternoon": {
                    "title": "Authentic Amritsari Kulcha & Lassi Feast",
                    "location": "Bhai Kulwant Singh Kulchian / Maqbool Road",
                    "activity": "Devour world-famous flaky potato-paneer stuffed Amritsari tandoori kulchas drenched in fresh butter with spicy chole and tamarind chutney.",
                    "cost": 400
                },
                "evening": {
                    "title": "Electric Wagah-Attari Border Flag Lowering Ceremony",
                    "location": "India-Pakistan Border (Attari)",
                    "activity": "Join 20,000 cheering spectators in the border stadium watching BSF soldiers perform the high-kicking, chest-thumping patriotic flag-lowering drill at sunset.",
                    "cost": 500
                },
                "tip": "Reach the Wagah Border stadium by 3:30 PM to secure prime viewing seats near the central gates."
            }
        ]
    },

    "agra": {
        "city": "Agra",
        "state": "Uttar Pradesh, India",
        "tagline": "Home of the Taj Mahal, Agra Fort & Mughal Grandeur",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.0,
        "aliases": ["agra", "taj mahal", "agra fort", "fatehpur sikri"],
        "daily_templates": [
            {
                "theme": "Sunrise at the Taj Mahal & UNESCO Agra Fort",
                "location": "Tajganj & Yamuna Riverbank",
                "morning": {
                    "title": "Sunrise Splendor at the Ivory-White Taj Mahal",
                    "location": "Dharmapuri, Forest Colony, Tajganj",
                    "activity": "Enter through the East Gate at dawn to witness Emperor Shah Jahan's 1632 marble wonder glow in soft morning pink and golden hues with zero crowds.",
                    "cost": 650
                },
                "afternoon": {
                    "title": "Mughal Agra Fort: Imperial Seat of Akbar & Shah Jahan",
                    "location": "Rakabganj, Agra",
                    "activity": "Tour the 94-acre red sandstone fortress, the Sheesh Mahal, Diwan-i-Khas, and the Musamman Burj balcony where Shah Jahan gazed at the Taj Mahal in his final days.",
                    "cost": 450
                },
                "evening": {
                    "title": "Mehtab Bagh Moonlit Sunset & Petha Tasting",
                    "location": "Mehtab Bagh (Across the Yamuna)",
                    "activity": "Photograph the reflection of the Taj Mahal across the Yamuna River from the 16th-century Mughal pleasure gardens. Taste authentic Panchhi Petha in saffron, paan, and chocolate flavors.",
                    "cost": 400
                },
                "tip": "The Taj Mahal is closed for general tourists on Fridays for prayers; plan your visit Saturday through Thursday."
            },
            {
                "theme": "Fatehpur Sikri: The Ghost City of Emperor Akbar",
                "location": "Fatehpur Sikri (37 km west of Agra)",
                "morning": {
                    "title": "Buland Darwaza: World's Highest Gateway",
                    "location": "Fatehpur Sikri Citadel",
                    "activity": "Climb the 54-meter Buland Darwaza built in 1573 to commemorate Akbar's Gujarat victory. Tie a sacred thread for blessings at the white marble tomb of Sufi Saint Salim Chishti.",
                    "cost": 500
                },
                "afternoon": {
                    "title": "Panch Mahal & Jodha Bai Palace Complex",
                    "location": "Fatehpur Sikri Royal Enclosure",
                    "activity": "Explore the 5-storey wind pavilion (Panch Mahal), the jewel-box Turkish Sultana's House, and the Diwan-i-Khas with its iconic intricately carved lotus central pillar.",
                    "cost": 400
                },
                "evening": {
                    "title": "Tomb of Itimad-ud-Daulah (Baby Taj) at Twilight",
                    "location": "Moti Bagh, Agra",
                    "activity": "Visit the delicate jewel-box mausoleum built by Queen Nur Jahan for her father, featuring the earliest intricate pietra dura marble inlays in India.",
                    "cost": 350
                },
                "tip": "Use government electric shuttle carts to travel between the parking lot and Fatehpur Sikri gates."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 🐘 KARNATAKA & TAMIL NADU
    # -------------------------------------------------------------------------
    "bangalore": {
        "city": "Bengaluru (Bangalore)",
        "state": "Karnataka, India",
        "tagline": "Garden City of India, Craft Breweries & Palace Heritage",
        "category": "general_city",
        "best_season": "Year-Round",
        "currency": "INR",
        "cost_multiplier": 1.1,
        "aliases": ["bangalore", "bengaluru", "garden city", "karnataka bangalore"],
        "daily_templates": [
            {
                "theme": "Lalbagh Glass House, Tipu Sultan Palace & Church Street Roasters",
                "location": "Central Bengaluru & Church Street",
                "morning": {
                    "title": "Lalbagh Botanical Gardens & 1889 London-style Glass House",
                    "location": "Mavalli, Lalbagh",
                    "activity": "Walk among 240 acres of rare tropical trees, ancient 3-billion-year-old Lalbagh Rock, and the Victorian glass pavilion. Savor crispy Benne Masala Dosa at iconic MTR.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Bangalore Palace (Tudor-style Royal Estate)",
                    "location": "Vasanth Nagar",
                    "activity": "Tour the 1878 wooden palace modeled on Windsor Castle, featuring fortified towers, battlements, Tudor interiors, and Raja Ravi Varma oil paintings.",
                    "cost": 650
                },
                "evening": {
                    "title": "Church Street Microbreweries & Bookshop Cafes",
                    "location": "Church Street & Brigade Road",
                    "activity": "Browse through Blossom Book House, sip single-origin manual pour-over coffees, and taste craft artisanal apple ciders at Toit or Arbor Brewing Company.",
                    "cost": 1200
                },
                "tip": "Use Namma Metro (Purple and Green lines) to effortlessly bypass city peak hour traffic."
            }
        ]
    },

    "coorg": {
        "city": "Coorg (Madikeri / Kodagu)",
        "state": "Karnataka, India",
        "tagline": "Scotland of India, Coffee Plantations & Misty Abbey Falls",
        "category": "mountains",
        "best_season": "September to June",
        "currency": "INR",
        "cost_multiplier": 1.05,
        "aliases": ["coorg", "madikeri", "kodagu", "karnataka coorg"],
        "daily_templates": [
            {
                "theme": "Abbey Falls, Raja's Seat Sunset & Fragrant Coffee Plantation Walk",
                "location": "Madikeri & Abbey Falls Trail",
                "morning": {
                    "title": "Abbey Falls Hanging Bridge Cascade",
                    "location": "Abbey Falls Road (8 km from Madikeri)",
                    "activity": "Walk through private aromatic coffee, pepper, and cardamom plantations leading to the roaring 70-foot water cascade from the hanging suspension bridge.",
                    "cost": 250
                },
                "afternoon": {
                    "title": "Coffee Estate Tour & Authentic Kodava Pandi Curry",
                    "location": "Madikeri Estate / Coorg Cuisine Restaurant",
                    "activity": "Learn about Arabica and Robusta bean harvesting and roasting. Taste signature spicy Kodava pork/mushroom Pandi Curry with soft rice Akki Rotti.",
                    "cost": 850
                },
                "evening": {
                    "title": "Raja's Seat Seasonal Flower Gardens & Valley Sunset",
                    "location": "Raja's Seat, Madikeri",
                    "activity": "Sit in the royal pavilion where the Kings of Kodagu watched sunsets. Admire endless rolling Western Ghats ridges and musical fountains.",
                    "cost": 200
                },
                "tip": "Buy authentic Coorg homemade chocolates, pure wild honey, and green peppercorns from government spice outlets in Madikeri."
            },
            {
                "theme": "Dubare Elephant Camp & Bylakuppe Golden Tibetan Monastery",
                "location": "Kushalnagar & Dubare",
                "morning": {
                    "title": "Dubare Elephant Camp Kaveri River Interaction",
                    "location": "Dubare Forest, River Kaveri",
                    "activity": "Cross the Kaveri river by boat early morning to participate in elephant bathing and feeding alongside forest department mahouts.",
                    "cost": 800
                },
                "afternoon": {
                    "title": "Namdroling Golden Temple (Bylakuppe Tibetan Settlement)",
                    "location": "Bylakuppe (Second Largest Tibetan Settlement)",
                    "activity": "Step into the vibrant Buddhist temple housing 40-foot golden statues of Buddha Shakyamuni, Padmasambhava, and Amitayus. Smell Tibetan incense.",
                    "cost": 300
                },
                "evening": {
                    "title": "Tibetan Momos & Kushalnagar Bamboo Handicrafts",
                    "location": "Kushalnagar Camp",
                    "activity": "Enjoy steaming hot Tibetan momos, Thenthuk noodle soup, and shop for hand-woven carpets and singing prayer bowls.",
                    "cost": 450
                },
                "tip": "Arrive at Dubare Elephant Camp before 9:00 AM for the daily elephant river bath session."
            }
        ]
    },

    "pondicherry": {
        "city": "Puducherry (Pondicherry)",
        "state": "Puducherry Union Territory, India",
        "tagline": "French Colonial White Town, Auroville Matrimandir & Surf Beaches",
        "category": "beach",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.05,
        "aliases": ["pondicherry", "puducherry", "pondy", "auroville", "french quarter"],
        "daily_templates": [
            {
                "theme": "French White Town Heritage Walk, Croissants & Promenade Sunset",
                "location": "White Town (French Quarter) & Rock Beach",
                "morning": {
                    "title": "French Quarter Yellow Villas & Sri Aurobindo Ashram",
                    "location": "Rue Dumas & Rue Romain Rolland, White Town",
                    "activity": "Stroll down French street-named boulevards framed by bougainvillea over yellow colonial mansions. Visit Sri Aurobindo Ashram and the sacred Samadhi shrine.",
                    "cost": 250
                },
                "afternoon": {
                    "title": "Artisan French Bakeries & Wood-fired Sourdough Lunch",
                    "location": "Cafe des Arts / Baker Street",
                    "activity": "Enjoy authentic buttery pain au chocolat, quiches, iced cafe au lait, and artisanal crepes inside a restored 19th-century French courtyard.",
                    "cost": 850
                },
                "evening": {
                    "title": "Rock Beach Promenade Sunset Walk & Gandhi Statue",
                    "location": "Goubert Avenue (Car-Free Promenade)",
                    "activity": "Walk along the 1.5 km oceanfront promenade with waves crashing against volcanic sea boulders. Enjoy evening sea breezes and French gelato.",
                    "cost": 350
                },
                "tip": "Goubert Avenue promenade is strictly closed to vehicular traffic from 6:00 PM to 7:30 AM daily."
            },
            {
                "theme": "Auroville Universal Town, Golden Matrimandir & Serenity Beach",
                "location": "Auroville & Serenity Beach",
                "morning": {
                    "title": "Auroville & The Golden Globe Matrimandir Viewpoint",
                    "location": "Auroville Experimental Township (10 km north)",
                    "activity": "Walk through shaded forest paths to the Golden Sphere Matrimandir, an architectural and spiritual marvel of silence and human unity.",
                    "cost": 300
                },
                "afternoon": {
                    "title": "Auroville Solar Kitchen Organic Buffet & Boutiques",
                    "location": "Auroville Visitor's Centre",
                    "activity": "Dine at the eco-friendly Solar Kitchen. Browse handcrafted aromatherapy candles, handmade marbled paper, and spiral tie-dye apparel.",
                    "cost": 650
                },
                "evening": {
                    "title": "Serenity Beach Surfing Lesson & Beach Shack Dining",
                    "location": "Serenity Beach / Kottakuppam",
                    "activity": "Watch surfers ride Bay of Bengal breaks or take a beginner 1-hour surf lesson. Dine on fresh grilled prawns and woodfired pizzas by the sea.",
                    "cost": 1100
                },
                "tip": "Matrimandir inner meditation chamber passes must be booked at least 3 to 7 days in advance online."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 🏔️ LADAKH & KASHMIR
    # -------------------------------------------------------------------------
    "ladakh": {
        "city": "Leh Ladakh",
        "state": "Ladakh, India",
        "tagline": "Land of High Passes, Turquoise Pangong & Nubra Sand Dunes",
        "category": "mountains",
        "best_season": "May to September",
        "currency": "INR",
        "cost_multiplier": 1.25,
        "aliases": ["leh", "ladakh", "pangong", "nubra", "khardung la", "hunder", "tso moriri"],
        "daily_templates": [
            {
                "theme": "Acclimatization, Leh Palace & Shanti Stupa Golden Sunset",
                "location": "Leh Town (3,500m elevation)",
                "morning": {
                    "title": "Leh Palace (Lhachen Palkhar) & Ancient Heritage Walk",
                    "location": "Namgyal Hill, Old Town Leh",
                    "activity": "Visit the 17th-century 9-storey royal palace modeled after Lhasa's Potala Palace. Walk through the mud-brick corridors of the Old Heritage quarter.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Changspa Garden Cafe Lunch & Apricot Delicacies",
                    "location": "Changspa Lane, Leh",
                    "activity": "Rest under apple trees at a local garden cafe. Taste authentic Ladakhi Skyu (hand-rolled pasta stew), Tingmo steamed buns, and fresh apricot juice.",
                    "cost": 750
                },
                "evening": {
                    "title": "Shanti Stupa Panoramic Sunset & Chanting",
                    "location": "Changspa Hilltop, Shanti Stupa",
                    "activity": "Climb 500 white steps to the Japanese Peace Pagoda. Marvel at the 360-degree panorama of Leh town, Stok Kangri snow peak, and the Indus valley at twilight.",
                    "cost": 250
                },
                "tip": "Strict rest on Day 1 is mandatory for AMS (Acute Mountain Sickness) acclimatization at 11,500 ft."
            },
            {
                "theme": "Khardung La Summit & Nubra Valley Double-Humped Bactrian Camels",
                "location": "Khardung La (17,982 ft) & Diskit / Hunder",
                "morning": {
                    "title": "Conquering Khardung La Pass (Highest Motorable Road)",
                    "location": "Khardung La Top (39 km from Leh)",
                    "activity": "Drive across the iconic snowbound pass at 5,359 meters. Photograph the world-famous yellow milestone and prayer flags fluttering against glaciated peaks.",
                    "cost": 1800
                },
                "afternoon": {
                    "title": "Diskit Monastery Giant Maitreya Buddha",
                    "location": "Diskit, Nubra Valley",
                    "activity": "Visit the 14th-century monastery and gaze in awe at the 106-foot vibrant Maitreya Buddha statue gazing serenely down the Shyok River gorge.",
                    "cost": 400
                },
                "evening": {
                    "title": "Hunder White Sand Dunes & Bactrian Camel Safari",
                    "location": "Hunder Sand Dunes (Cold Desert Oasis)",
                    "activity": "Ride rare double-humped Bactrian camels across white desert sand dunes framed by snow-dusted mountains. Enjoy an authentic Ladakhi folk cultural evening.",
                    "cost": 1200
                },
                "tip": "Limit your stop at the top of Khardung La to 20 minutes to avoid oxygen deprivation headaches."
            },
            {
                "theme": "Shyok River Run to Shimmering Pangong Tso Lake",
                "location": "Shyok River Route to Pangong Tso (4,250m)",
                "morning": {
                    "title": "Scenic Shyok Valley Off-Road River Drive",
                    "location": "Agham - Shyok - Durbuk Route",
                    "activity": "Drive along the dramatic vertical canyon walls and pebble beds of the turquoise Shyok River connecting Nubra to Pangong.",
                    "cost": 2200
                },
                "afternoon": {
                    "title": "Pangong Tso First View & Color-Shifting Waters",
                    "location": "Lukung / Spangmik Shores",
                    "activity": "Witness the dramatic first sight of the 134-km long Pangong Lake spanning India and Tibet. Watch the lake water shift through 7 shades of blue under changing sunlight.",
                    "cost": 500
                },
                "evening": {
                    "title": "Sunset Lake Photography & Starry Swiss Tent Stay",
                    "location": "Spangmik Lakeside Eco-Camps",
                    "activity": "Walk along the crystal-clear saline shoreline. Sit outside your heated canvas tent gazing at the unpolluted Milky Way galaxy under sub-zero night skies.",
                    "cost": 2500
                },
                "tip": "Carry personal power banks as electricity in Pangong camps is powered by solar generators and turns off by 10:30 PM."
            }
        ]
    },

    "kashmir": {
        "city": "Srinagar & Kashmir Valley",
        "state": "Jammu & Kashmir, India",
        "tagline": "Paradise on Earth: Dal Lake Shikaras, Gulmarg Gondola & Saffron Meadows",
        "category": "mountains",
        "best_season": "Year-Round (Chinar Autumn in Oct-Nov, Snow in Dec-Feb)",
        "currency": "INR",
        "cost_multiplier": 1.2,
        "aliases": ["kashmir", "srinagar", "gulmarg", "pahalgam", "sonamarg", "dal lake"],
        "daily_templates": [
            {
                "theme": "Dal Lake Heritage Houseboat, Sunrise Shikara & Floating Vegetable Market",
                "location": "Dal Lake & Boulevard Road, Srinagar",
                "morning": {
                    "title": "Dawn Shikara Row to World's Only Floating Vegetable Market",
                    "location": "Interior Dal Lake Canals",
                    "activity": "Row through mist-covered lotus lagoons at 5:30 AM to witness local Kashmiri farmers bartering fresh vegetables, water chestnuts, and fresh flowers on wooden boats.",
                    "cost": 800
                },
                "afternoon": {
                    "title": "Mughal Terraced Gardens: Shalimar Bagh & Nishat Bagh",
                    "location": "Boulevard Road, Dal Lake Eastern Bank",
                    "activity": "Walk through Emperor Jahangir's 1619 terraced pleasure gardens with cascading central water channels, fountains, and 400-year-old majestic Chinar trees.",
                    "cost": 350
                },
                "evening": {
                    "title": "Carved Cedar Wood Houseboat Stay & Kahwa Tea",
                    "location": "Nigeen / Dal Lake Houseboat",
                    "activity": "Check into a vintage carved deodar wood houseboat with Victorian chandeliers. Sip steaming Kashmiri saffron Kahwa brewed with crushed almonds and cardamom.",
                    "cost": 2800
                },
                "tip": "Bargain politely with floating shikara vendors selling saffron, walnuts, and pashmina shawls."
            },
            {
                "theme": "Gulmarg Meadow of Flowers & World's Highest Gondola Ride",
                "location": "Gulmarg (50 km west at 8,690 ft)",
                "morning": {
                    "title": "Gulmarg Gondola Phase 2: Apharwat Peak Summit",
                    "location": "Gulmarg Gondola Station to Mt. Apharwat (13,780 ft)",
                    "activity": "Ride Asia's longest and highest two-stage cable car to Mt. Apharwat near the LOC. Enjoy panoramic views of Nanga Parbat and year-round powdery snow activities.",
                    "cost": 2200
                },
                "afternoon": {
                    "title": "St. Mary's 1902 Stone Church & Strawberry Valley Hike",
                    "location": "Gulmarg Golf Course & Meadows",
                    "activity": "Walk across lush green golf meadows (world's highest green golf course) to the 120-year-old British stone church and Strawberry Valley pine woods.",
                    "cost": 450
                },
                "evening": {
                    "title": "Traditional Kashmiri Wazwan Feast Dinner",
                    "location": "Ahdoos / Mughal Darbar, Srinagar",
                    "activity": "Indulge in an authentic multi-course royal Wazwan feast: Rogan Josh, succulent Rista meatballs in red gravy, Gushtaba in creamy yogurt broth, and saffron rice.",
                    "cost": 1400
                },
                "tip": "Book Gulmarg Gondola Phase 2 tickets online at least 3 weeks in advance through the official JK Cable Car portal."
            }
        ]
    },

    "rishikesh": {
        "city": "Rishikesh",
        "state": "Uttarakhand, India",
        "tagline": "Yoga Capital of the World, White-Water River Rafting & Ganga Ghats",
        "category": "mountains",
        "best_season": "September to June",
        "currency": "INR",
        "cost_multiplier": 0.95,
        "aliases": ["rishikesh", "laxman jhula", "ram jhula", "triveni ghat", "shivpuri", "uttarakhand rishikesh"],
        "daily_templates": [
            {
                "theme": "River Rafting Rapids, Cliff Jumping & Beatles Ashram",
                "location": "Shivpuri & Swarg Ashram",
                "morning": {
                    "title": "16 km Grade III+ White-Water Rafting from Shivpuri",
                    "location": "Shivpuri to NIM Beach / Ram Jhula",
                    "activity": "Navigate legendary Ganges rapids (Roller Coaster, Golf Course, Club House) with certified river guides. Experience thrilling 20-foot cliff jumping and body surfing.",
                    "cost": 1400
                },
                "afternoon": {
                    "title": "The Beatles Ashram (Chaurasi Kutia) Graffiti Art",
                    "location": "Rajaji Tiger Reserve Edge, Swarg Ashram",
                    "activity": "Explore the 1968 Maharishi Mahesh Yogi meditation retreat where The Beatles wrote 48 songs. Walk through the 84 stone meditation domes covered in vibrant spiritual street murals.",
                    "cost": 400
                },
                "evening": {
                    "title": "Triveni Ghat Maha Aarti & Floating Diya Lamps",
                    "location": "Triveni Ghat Promenade",
                    "activity": "Sit on the holy bathing steps as priests chant Vedic hymns, blow conch shells, and sway massive flaming brass lamps while thousands of leaf diyas float down the river.",
                    "cost": 300
                },
                "tip": "Keep dry clothes and waterproof pouches for phones during white-water rafting."
            }
        ]
    },

    "varanasi": {
        "city": "Varanasi (Kashi / Banaras)",
        "state": "Uttar Pradesh, India",
        "tagline": "World's Oldest Living City, Sacred Ghats & Ganga Aarti",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 0.9,
        "aliases": ["varanasi", "kashi", "banaras", "benaras", "kashi vishwanath", "ganga aarti"],
        "daily_templates": [
            {
                "theme": "Sunrise Boat on Sacred Ganges, Subah-e-Banaras & Kashi Vishwanath Corridor",
                "location": "Assi Ghat & Kashi Vishwanath",
                "morning": {
                    "title": "Sunrise Wooden Boat Row from Assi to Dashashwamedh",
                    "location": "Assi Ghat / Ganges River",
                    "activity": "Row gently past 84 ancient ghats at dawn as temple bells ring and morning aarti (Subah-e-Banaras) echoes across the misty holy waters.",
                    "cost": 600
                },
                "afternoon": {
                    "title": "Kashi Vishwanath Jyotirlinga Temple & Golden Corridor",
                    "location": "Vishwanath Gali, Godowlia",
                    "activity": "Take darshan at the sacred golden spire Kashi Vishwanath Temple, rebuilt by Ahilyabai Holkar in 1780, and walk through the expansive new temple corridor.",
                    "cost": 350
                },
                "evening": {
                    "title": "Grand Ganga Maha Aarti at Dashashwamedh Ghat",
                    "location": "Dashashwamedh Ghat",
                    "activity": "Watch 7 young priests perform the hypnotic multi-tiered brass lamp aarti with synchronized conch shells, incense smoke, and floating diya offerings on the river.",
                    "cost": 500
                },
                "tip": "Phones, leather belts, and bags must be deposited in digital lockers before entering Kashi Vishwanath Temple."
            }
        ]
    },

    "hampi": {
        "city": "Hampi",
        "state": "Karnataka, India",
        "tagline": "UNESCO Boulders, Vijayanagara Empire & Stone Chariot",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 0.9,
        "aliases": ["hampi", "vijayanagara", "hospet", "karnataka hampi"],
        "daily_templates": [
            {
                "theme": "Vittala Temple Musical Pillars, Stone Chariot & Tungabhadra Coracle",
                "location": "Sacred Center & Tungabhadra River",
                "morning": {
                    "title": "Vittala Temple Complex & Iconic Stone Chariot",
                    "location": "Vittala Complex, Hampi",
                    "activity": "Marvel at the 16th-century stone chariot dedicated to Garuda and the 56 monolithic musical pillars that emit musical notes when gently tapped.",
                    "cost": 400
                },
                "afternoon": {
                    "title": "Traditional Round Coracle Boat Ride on Tungabhadra",
                    "location": "Chakratirtha / Purandara Mantapa",
                    "activity": "Spin across swirling river whirlpools in a traditional woven circular coracle boat past boulder cliffs and submerged Shiva lingas.",
                    "cost": 600
                },
                "evening": {
                    "title": "Matanga Hill Sunrise/Sunset 360-Degree Panorama",
                    "location": "Matanga Hill (Highest Point in Hampi)",
                    "activity": "Climb ancient stone steps to Matanga hilltop for the most breathtaking golden sunset across the endless boulder landscape and Achyutaraya Temple.",
                    "cost": 250
                },
                "tip": "Electric battery golf carts are available from the parking lot to Vittala temple gates for elderly travelers."
            }
        ]
    },

    "kolkata": {
        "city": "Kolkata (The City of Joy)",
        "state": "West Bengal, India",
        "tagline": "Victorian Architecture, Intellectual Culture & Street Food",
        "category": "heritage",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 0.85,
        "aliases": ["kolkata", "calcutta", "howrah", "park street", "dakshineswar"],
        "daily_templates": [
            {
                "theme": "Victoria Memorial Marble Palace, St. Paul's & Park Street Culinary Trail",
                "location": "Maidan & Park Street, Central Kolkata",
                "morning": {
                    "title": "Victoria Memorial White Marble Royal Museum",
                    "location": "Queens Way, Maidan",
                    "activity": "Tour Lord Curzon's 1921 British Raj monument built of Makrana marble with 64 acres of landscaped gardens, royal oil paintings, and the bronze Angel of Victory.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Peter Cat Chelo Kebab & Flurys Heritage Tearoom",
                    "location": "Park Street",
                    "activity": "Dine on legendary butter-sizzler Chelo Kebabs at Peter Cat (est. 1975) followed by heritage English tea and rum balls at Flurys (est. 1927).",
                    "cost": 950
                },
                "evening": {
                    "title": "Historic Howrah Bridge, Mallick Ghat Flower Market & Tram Ride",
                    "location": "Hooghly Riverfront / Strand Road",
                    "activity": "Walk across the 1943 cantilevered Howrah Bridge with zero nuts or bolts. Stroll through Asia's largest flower market and ride Asia's oldest operating electric tram.",
                    "cost": 400
                },
                "tip": "Ride the heritage Kolkata tram route from Esplanade to Nonapukur for a nostalgic retro experience."
            }
        ]
    },

    "darjeeling": {
        "city": "Darjeeling",
        "state": "West Bengal, India",
        "tagline": "Queen of the Hills, Kanchenjunga Sunrises & UNESCO Toy Train",
        "category": "mountains",
        "best_season": "March to June / October to December",
        "currency": "INR",
        "cost_multiplier": 1.0,
        "aliases": ["darjeeling", "tiger hill", "batasia loop", "ghoom"],
        "daily_templates": [
            {
                "theme": "4:00 AM Tiger Hill Kanchenjunga Sunrise, Batasia Loop & UNESCO Toy Train",
                "location": "Tiger Hill (8,482 ft) & Ghoom",
                "morning": {
                    "title": "Dawn Golden Sunrise over Mt. Kanchenjunga & Everest",
                    "location": "Tiger Hill Sunrise Pavilion",
                    "activity": "Watch the first morning sun rays turn the snow-white peak of Kanchenjunga (world's 3rd highest peak) into dazzling gold, pink, and orange.",
                    "cost": 650
                },
                "afternoon": {
                    "title": "UNESCO Himalayan Toy Train Steam Joyride to Ghoom",
                    "location": "Darjeeling Railway Station to Batasia Loop",
                    "activity": "Ride the 1881 British heritage narrow-gauge steam engine chugging through spiral 360-degree Batasia Loop war memorial and India's highest railway station at Ghoom.",
                    "cost": 1500
                },
                "evening": {
                    "title": "Glenary's Bakery & Mall Road (Chowrasta) Stroll",
                    "location": "Chowrasta Mall & Nehru Road",
                    "activity": "Sip first-flush Muscatel Darjeeling black tea with hot apple strudel at 100-year-old Glenary's Bakery. Stroll Chowrasta watching local horseback rides.",
                    "cost": 750
                },
                "tip": "Leave your hotel by 3:45 AM for Tiger Hill to beat tourist vehicular traffic jams."
            }
        ]
    },

    "andaman": {
        "city": "Andaman & Nicobar Islands (Havelock & Neil)",
        "state": "Andaman & Nicobar, India",
        "tagline": "Turquoise Lagoons, Asia's Best Radhanagar Beach & Scuba Diving",
        "category": "beach",
        "best_season": "October to May",
        "currency": "INR",
        "cost_multiplier": 1.35,
        "aliases": ["andaman", "havelock", "radhanagar", "port blair", "neil island", "swaraj dweep"],
        "daily_templates": [
            {
                "theme": "Port Blair Cellular Jail (Kala Pani) & Light and Sound History",
                "location": "Port Blair & Corbyn's Cove",
                "morning": {
                    "title": "Cellular Jail National Memorial (Kala Pani)",
                    "location": "Atlanta Point, Port Blair",
                    "activity": "Tour the 1906 7-winged colonial prison where Indian freedom fighters (Vir Savarkar, Batukeshwar Dutt) were imprisoned in solitary confinement.",
                    "cost": 350
                },
                "afternoon": {
                    "title": "Corbyn's Cove Beach Jet Skiing & Coastal Lunch",
                    "location": "Corbyn's Cove (7 km south)",
                    "activity": "Relax on the coconut-fringed crescent beach with speed boating and jet skiing, followed by fresh seafood curries and king coconut water.",
                    "cost": 950
                },
                "evening": {
                    "title": "Cellular Jail Sound & Light Laser Spectacle",
                    "location": "Cellular Jail Courtyard",
                    "activity": "Witness the moving acoustic narration in the voice of the ancient Peepal tree narrating heroic struggles of freedom fighters under evening spotlights.",
                    "cost": 400
                },
                "tip": "Cellular Jail is closed on Mondays; book evening Sound & Light show tickets online in advance."
            }
        ]
    },

    "mumbai": {
        "city": "Mumbai (The City of Dreams)",
        "state": "Maharashtra, India",
        "tagline": "Gateway of India, Marine Drive Queen's Necklace & Bollywood",
        "category": "general_city",
        "best_season": "October to March",
        "currency": "INR",
        "cost_multiplier": 1.25,
        "aliases": ["mumbai", "bombay", "marine drive", "colaba", "bandra"],
        "daily_templates": [
            {
                "theme": "Gateway of India, 1903 Taj Mahal Palace & Elephanta Rock Caves",
                "location": "Colaba & Apollo Bunder",
                "morning": {
                    "title": "Gateway of India & Elephanta Island Ferry",
                    "location": "Apollo Bunder, Colaba",
                    "activity": "Photograph the 1924 basalt ceremonial arch. Board a harbor ferry across Mumbai port to the 5th-century UNESCO Elephanta rock-cut Trimurti Shiva caves.",
                    "cost": 650
                },
                "afternoon": {
                    "title": "Cafe Mondegar Jukebox & Colaba Causeway Shopping",
                    "location": "Colaba Causeway",
                    "activity": "Enjoy draft beer and retro jukebox tunes at 1932 Cafe Mondegar surrounded by Mario Miranda murals. Shop for antique brassware, leather bags, and bohemian jewelry.",
                    "cost": 900
                },
                "evening": {
                    "title": "Marine Drive Queen's Necklace Sunset & Girgaon Chowpatty",
                    "location": "Marine Drive Promenade & Chowpatty",
                    "activity": "Sit on the iconic tetrapod seawall watching the sunset over the Arabian Sea. Savor Mumbai's legendary crunchy Bhel Puri, Sev Puri, and Kulfi at Chowpatty.",
                    "cost": 400
                },
                "tip": "Elephanta Caves are closed on Mondays; boats do not operate during rough monsoon seas."
            }
        ]
    }
}

