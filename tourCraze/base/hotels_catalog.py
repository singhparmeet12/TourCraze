"""
TourCraze Curated Master Catalog of Handcrafted Stays & Luxury Sanctuaries across India.
Contains 40+ unique, architecturally distinguished properties (Heritage Palaces, Glass Igloos,
Cliffside Villas, Treehouses, Luxury Desert Camps, and Budget Chic Havens).
"""

HOTELS_DATA = [
    # =========================================================================
    # 👑 ROYAL HERITAGE & PALACES
    # =========================================================================
    {
        "id": 1,
        "name": "Taj Lake Palace Sanctuary",
        "city": "Udaipur",
        "state": "Rajasthan",
        "category": "palace",
        "vibe": "👑 250-Year-Old Marble Island Palace",
        "stars": 5,
        "rating": 4.95,
        "review_count": 2840,
        "price_per_night": 32000,
        "original_price": 42000,
        "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "👑 Ultra Luxury Palace",
        "highlights": ["Floating marble palace in Lake Pichola", "Private boat arrival & royal guard welcome", "Artisan Mewari sunset fine dining"],
        "amenities": ["Lake View", "Infinity Pool", "Jiva Spa", "Free Breakfast", "Butler Service", "High-speed WiFi"],
        "description": "An iconic 18th-century floating white marble palace set in the shimmering waters of Lake Pichola. Features panoramic palace views, handcrafted jharokhas, and bespoke butler dining.",
        "address": "Pichola, Udaipur, Rajasthan 313001",
        "rooms": [
            {
                "id": "101",
                "name": "Luxury Lake View Suite",
                "price": 32000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "550 sq.ft",
                "perks": ["Lake Pichola View", "Daily Royal Breakfast", "Free High-Speed Wi-Fi", "Free Cancellation up to 48h"]
            },
            {
                "id": "102",
                "name": "Grand Royal Balcony Palace Suite",
                "price": 48000,
                "capacity": 3,
                "bed": "1 Super King Bed",
                "size": "850 sq.ft",
                "perks": ["Private Lake Balcony", "Personal 24/7 Butler", "Complimentary Spa Session", "Champagne High Tea"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Rambagh Royal Haveli & Gardens",
        "city": "Jaipur",
        "state": "Rajasthan",
        "category": "palace",
        "vibe": "🦚 Former Maharaja Residence & Peacock Gardens",
        "stars": 5,
        "rating": 4.92,
        "review_count": 1950,
        "price_per_night": 28000,
        "original_price": 36000,
        "img": "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🏰 Heritage Grandeur",
        "highlights": ["47 acres of lush Mughal gardens", "Roaming royal peacocks", "Heritage vintage car arrival transfers"],
        "amenities": ["Outdoor & Indoor Pool", "Heritage Spa", "Polo Lounge", "Free Breakfast", "Free Valet"],
        "description": "Step into aristocratic luxury with intricately carved marble jalis, sprawling lush courtyards, and authentic Rajasthani hospitality in the heart of the Pink City.",
        "address": "Bhawani Singh Road, Jaipur, Rajasthan 302005",
        "rooms": [
            {
                "id": "201",
                "name": "Palace Garden Room",
                "price": 28000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "500 sq.ft",
                "perks": ["Garden Courtyard View", "Free Royal Breakfast", "Free High-Speed Wi-Fi", "Welcome Garland & Drink"]
            },
            {
                "id": "202",
                "name": "Maharaja Heritage Suite",
                "price": 45000,
                "capacity": 3,
                "bed": "1 King Bed + Lounge",
                "size": "900 sq.ft",
                "perks": ["Private Terrace", "Historic Antique Decor", "Complimentary Heritage Walk", "Free Airport Transfer"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Fort Barwara Sanctuary & Spa",
        "city": "Ranthambore",
        "state": "Rajasthan",
        "category": "palace",
        "vibe": "🏰 14th-Century Fortress Retreat",
        "stars": 5,
        "rating": 4.90,
        "review_count": 890,
        "price_per_night": 36000,
        "original_price": 45000,
        "img": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "👑 Restored 14th-Century Fort",
        "highlights": ["Historic palace walls and temples", "Private tiger safari concierge", "Holistic Ayurvedic wellness sanctuary"],
        "amenities": ["Spa & Wellness", "Swimming Pool", "Organic Garden Restaurant", "Free Breakfast", "WiFi"],
        "description": "Sensitively restored 14th-century fort featuring ancient royal courtyards, sacred banyan trees, and luxury suites overlooking the Aravalli hills.",
        "address": "Chauth Ka Barwara, Rajasthan 322702",
        "rooms": [
            {
                "id": "301",
                "name": "Fort View Sanctuary Suite",
                "price": 36000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "650 sq.ft",
                "perks": ["Aravalli & Fort View", "Organic Farm-to-Table Breakfast", "Daily Yoga Sessions"]
            }
        ]
    },

    # =========================================================================
    # 🌲 ALPINE GLASS CHALETS & SNOW COTTAGES
    # =========================================================================
    {
        "id": 4,
        "name": "Aura Alpine Glass Igloos & Chalet",
        "city": "Manali",
        "state": "Himachal Pradesh",
        "category": "chalet",
        "vibe": "🏔️ Geodesic Glass Dome with 360° Snow Peak Views",
        "stars": 5,
        "rating": 4.93,
        "review_count": 1420,
        "price_per_night": 14500,
        "original_price": 19000,
        "img": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "❄️ Star-Gazing Glass Dome",
        "highlights": ["360° heated transparent glass roof", "Roaring cedar wood fireplace", "Stargazing telescope & bonfire deck"],
        "amenities": ["Heated Floors", "Mountain View", "Private Hot Tub", "Free Breakfast", "High-speed Starlink WiFi"],
        "description": "Perched on a quiet apple orchard ridge above Old Manali, these heated geodesic glass domes allow you to sleep directly under the starry Himalayan sky while snow blankets the pine forest.",
        "address": "Sethi Glades, Naggar Road, Manali, Himachal Pradesh 175131",
        "rooms": [
            {
                "id": "401",
                "name": "Panoramic Glass Dome Suite",
                "price": 14500,
                "capacity": 2,
                "bed": "1 Plush King Bed",
                "size": "420 sq.ft",
                "perks": ["Full Glass Stargazing Ceiling", "Wood Pellet Heating", "Artisan Himalayan Breakfast", "Heated Jacuzzi Access"]
            },
            {
                "id": "402",
                "name": "Cedar Timber Alpine Duplex",
                "price": 21000,
                "capacity": 4,
                "bed": "2 King Beds",
                "size": "780 sq.ft",
                "perks": ["Private Pine Balcony", "Stone Fireplace", "Mountain Stream View", "Barbecue Night Kit"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Khyber Himalayan Resort & Ski Chalet",
        "city": "Gulmarg",
        "state": "Kashmir",
        "category": "chalet",
        "vibe": "⛷️ Pine Forest Ski-In/Ski-Out Luxury Retreat",
        "stars": 5,
        "rating": 4.96,
        "review_count": 2100,
        "price_per_night": 26000,
        "original_price": 34000,
        "img": "https://images.unsplash.com/photo-1548777123-e216912df7d8?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1548777123-e216912df7d8?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "⛷️ World's Premier Ski Retreat",
        "highlights": ["Direct access to Gulmarg Gondola", "Heated indoor glass-framed infinity pool", "Authentic Kashmiri Wazwan dining"],
        "amenities": ["Indoor Heated Pool", "Ski Concierge", "L'Occitane Spa", "Kashmiri Tea Lounge", "WiFi"],
        "description": "Nestled among virgin pir panjal pine forests at 8,825 feet, Khyber combines hand-carved walnut woodwork with world-class ski trails and breathtaking views of Mount Apharwat.",
        "address": "Hotel Khyber, Gulmarg, Jammu and Kashmir 193403",
        "rooms": [
            {
                "id": "501",
                "name": "Premier Apharwat Pine Suite",
                "price": 26000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "580 sq.ft",
                "perks": ["Direct Mountain & Pine View", "Complimentary Kashmiri Kahwa", "Heated Floor Bathrooms", "Free Breakfast"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Spiti Moonscape Eco Log Cabins",
        "city": "Kaza",
        "state": "Himachal Pradesh",
        "category": "chalet",
        "vibe": "🏔️ Solar-Heated High-Altitude Stone Lodge",
        "stars": 4,
        "rating": 4.88,
        "review_count": 640,
        "price_per_night": 6800,
        "original_price": 9500,
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "💎 High-Altitude Moonscape Lodge",
        "highlights": ["View of 1000-year-old Key Monastery", "Zero-carbon passive solar heating", "Organic seabuckthorn tea tasting"],
        "amenities": ["Solar Heating", "Monastery View", "Local Cuisine", "WiFi", "Oxygen Support"],
        "description": "Authentic stone and mud architecture engineered with modern insulation and solar thermal warmth, offering unrivaled tranquility in the cold desert of Spiti.",
        "address": "Near Key Monastery, Spiti Valley, Himachal Pradesh 172114",
        "rooms": [
            {
                "id": "601",
                "name": "Spiti Valley View Cottage",
                "price": 6800,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "380 sq.ft",
                "perks": ["Monastery & River View", "Organic Spiti Breakfast", "Warm Yak Wool Throws"]
            }
        ]
    },

    # =========================================================================
    # 🏖️ CLIFFSIDE & BEACHFRONT VILLAS
    # =========================================================================
    {
        "id": 7,
        "name": "Azura Cliffside Private Plunge Villas",
        "city": "Goa",
        "state": "Goa",
        "category": "beach",
        "vibe": "🌊 Private Infinity Pool Overlooking Arabian Sea",
        "stars": 5,
        "rating": 4.94,
        "review_count": 1820,
        "price_per_night": 18500,
        "original_price": 24000,
        "img": "https://images.unsplash.com/photo-1540541338287-41700207dee6?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1540541338287-41700207dee6?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🌊 Cliffside Ocean Oasis",
        "highlights": ["Private sun deck & personal plunge pool", "Private direct access to secluded cove", "Sunset cocktails & seafood grill"],
        "amenities": ["Private Pool", "Sea View", "Beach Access", "Free Breakfast", "High-speed WiFi", "Cocktail Lounge"],
        "description": "Perched dramatically on the red laterite cliffs of North Goa, these minimalist luxury villas offer unobstructed sunset views over the crashing waves of the Arabian Sea.",
        "address": "Vagator Cliff Edge, Anjuna-Vagator Road, Goa 403509",
        "rooms": [
            {
                "id": "701",
                "name": "Sunset Plunge Pool Villa",
                "price": 18500,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "650 sq.ft",
                "perks": ["Direct Ocean Sunset View", "Private Heated Plunge Pool", "Artisan Tropical Breakfast", "Complimentary Evening Cocktails"]
            },
            {
                "id": "702",
                "name": "Grand Oceanfront 2-Bedroom Haven",
                "price": 32000,
                "capacity": 4,
                "bed": "2 King Beds",
                "size": "1100 sq.ft",
                "perks": ["Expansive Sun Deck", "Private Infinity Pool", "Dedicated Villa Host", "Free Airport Transfer"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Barefoot Radhanagar Beachfront Lodges",
        "city": "Havelock Island",
        "state": "Andaman & Nicobar",
        "category": "beach",
        "vibe": "🌴 Eco-Luxe Timber Cottages on Asia's Best Beach",
        "stars": 5,
        "rating": 4.92,
        "review_count": 1150,
        "price_per_night": 22000,
        "original_price": 28000,
        "img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1540541338287-41700207dee6?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🏖️ Pristine Tropical Paradise",
        "highlights": ["Steps away from turquoise Radhanagar waters", "Sustainable mahogany wood architecture", "Private scuba & bioluminescence night kayaking"],
        "amenities": ["Direct Beach Access", "Ayurveda Spa", "Open-air Lounge", "Free Breakfast", "WiFi"],
        "description": "Constructed exclusively from sustainable local timber under ancient tropical canopies, Barefoot offers barefoot luxury steps from the powder-white sands of Radhanagar Beach.",
        "address": "Radhanagar Beach No. 7, Havelock Island, Andaman 744211",
        "rooms": [
            {
                "id": "801",
                "name": "Tropical Nicobari Villa",
                "price": 22000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "600 sq.ft",
                "perks": ["Tropical Forest Canopy View", "Complimentary Snorkeling Gear", "Farm-fresh Island Breakfast"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Varkala Helipad Cliffside Suites",
        "city": "Varkala",
        "state": "Kerala",
        "category": "beach",
        "vibe": "🌅 Bohemian Sea-Cliff Sanctuary",
        "stars": 4,
        "rating": 4.86,
        "review_count": 980,
        "price_per_night": 5400,
        "original_price": 7500,
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🌅 Red Cliff Sunset Sanctuary",
        "highlights": ["Rooftop sunset yoga studio", "Direct stair path to Papanasam beach", "Fresh clay-oven bakery downstairs"],
        "amenities": ["Sea View Balcony", "Yoga Studio", "Free Breakfast", "WiFi", "Ayurvedic Massages"],
        "description": "Wake up to the rhythm of Arabian Sea waves from your private balcony along the famous red sandstone cliffs of Varkala.",
        "address": "North Cliff, Varkala, Kerala 695141",
        "rooms": [
            {
                "id": "901",
                "name": "Panoramic Cliff View Balcony Room",
                "price": 5400,
                "capacity": 2,
                "bed": "1 Queen Bed",
                "size": "360 sq.ft",
                "perks": ["Direct Ocean Sunset View", "Free Kerala Style Breakfast", "High-speed WiFi"]
            }
        ]
    },

    # =========================================================================
    # ☕ HERITAGE TEA ESTATE BUNGALOWS & PLANTATIONS
    # =========================================================================
    {
        "id": 10,
        "name": "Glenburn Colonial Tea Estate & Lodge",
        "city": "Darjeeling",
        "state": "West Bengal",
        "category": "plantation",
        "vibe": "☕ 1859 British Planter's Bungalow & Kanchenjunga Vistas",
        "stars": 5,
        "rating": 4.95,
        "review_count": 780,
        "price_per_night": 24000,
        "original_price": 31000,
        "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1544816155-12df9643f363?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "☕ Iconic 1859 Tea Sanctuary",
        "highlights": ["Unobstructed views of Mount Kanchenjunga", "Private tea tasting with master planters", "Riverside picnic lunches by the Rangeet River"],
        "amenities": ["Mountain View", "Fireplaces", "Tea Tasting Lounge", "All Meals Included", "WiFi"],
        "description": "A heaven of peace set on a 1,600-acre working tea estate, overlooking the golden peaks of Mount Kanchenjunga. Featuring antique four-poster beds and bespoke tea gastronomies.",
        "address": "Glenburn Tea Estate, Darjeeling, West Bengal 734101",
        "rooms": [
            {
                "id": "1001",
                "name": "Kanchenjunga Planter Suite",
                "price": 24000,
                "capacity": 2,
                "bed": "1 Handcrafted Teak King Bed",
                "size": "620 sq.ft",
                "perks": ["Direct Snow Peak View", "All Meals & High Tea Included", "Complimentary Tea Estate Tour", "Log Fireplace"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Windermere Mountain Tea Estate",
        "city": "Munnar",
        "state": "Kerala",
        "category": "plantation",
        "vibe": "🌿 Cardamom & Tea Plantation Estate",
        "stars": 5,
        "rating": 4.91,
        "review_count": 1320,
        "price_per_night": 12500,
        "original_price": 16000,
        "img": "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🌿 Cardamom & Cloud Estate",
        "highlights": ["Private valley cliff walking trails", "Cozy cedar-wood tea library", "Organic plantation dinner by candlelight"],
        "amenities": ["Valley View Balcony", "Tea Library", "Organic Dining", "Free Breakfast", "WiFi"],
        "description": "Where the tea gardens end and the mist begins. Windermere is set on a 60-acre coffee and cardamom estate, offering fresh mountain breezes and handcrafted wood cottages.",
        "address": "Pothamedu, Munnar, Kerala 685612",
        "rooms": [
            {
                "id": "1101",
                "name": "Planter's Garden Cottage",
                "price": 12500,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "480 sq.ft",
                "perks": ["Plantation Valley View", "Handmade Cookies & Tea", "Buffet Breakfast Included"]
            }
        ]
    },

    # =========================================================================
    # ⛺ LUXURY GLAMPING & STAR-GAZING CAMPS
    # =========================================================================
    {
        "id": 12,
        "name": "The Serai Desert Oasis & Safari Camp",
        "city": "Jaisalmer",
        "state": "Rajasthan",
        "category": "glamping",
        "vibe": "⛺ 100-Acre Royal Sand Dune Glamping Sanctuary",
        "stars": 5,
        "rating": 4.96,
        "review_count": 890,
        "price_per_night": 29000,
        "original_price": 38000,
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1200&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "⛺ Ultra-Luxe Desert Camp",
        "highlights": ["Canvas tented suites with private plunge pools", "Camel sundowner rides across golden Thar dunes", "Folk musician performances by candle-lit stepwells"],
        "amenities": ["Private Heated Pool", "Ayurvedic Spa", "Desert Safari Concierge", "Free Breakfast", "WiFi"],
        "description": "Inspired by the royal caravan sites of Rajputana, The Serai offers palatial air-conditioned tented suites with private gardens and sunken heated plunge pools.",
        "address": "Bherwa, Jaisalmer, Rajasthan 345001",
        "rooms": [
            {
                "id": "1201",
                "name": "Luxury Tented Suite",
                "price": 29000,
                "capacity": 2,
                "bed": "1 Royal King Bed",
                "size": "750 sq.ft",
                "perks": ["Private Walled Garden", "Sunken Sandstone Tub", "Daily Gourmet Breakfast", "Sunset Camel Safari"]
            }
        ]
    },
    {
        "id": 13,
        "name": "Ananda in the Himalayas Sanctuary",
        "city": "Rishikesh",
        "state": "Uttarakhand",
        "category": "spa",
        "vibe": "🧘 100-Acre Maharaja Palace Estate & World-Class Wellness",
        "stars": 5,
        "rating": 4.98,
        "review_count": 2450,
        "price_per_night": 38000,
        "original_price": 48000,
        "img": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🧘 World's Best Wellness Sanctuary",
        "highlights": ["Overlooks the holy Ganges river valley", "Custom Ayurvedic & meditation programs", "Hydrotherapy pools and mountain golf course"],
        "amenities": ["Ganges View", "Infinity Pool", "Ayurvedic Clinic", "Yoga Pavilion", "All Healthy Gourmet Meals Included"],
        "description": "Ranked among the top destination spas in the world, Ananda is housed in a former viceregal palace high above Rishikesh, integrating traditional Ayurveda, Yoga, and Vedanta.",
        "address": "The Palace Estate, Narendra Nagar, Tehri Garhwal, Uttarakhand 249175",
        "rooms": [
            {
                "id": "1301",
                "name": "Palace Valley View Suite",
                "price": 38000,
                "capacity": 2,
                "bed": "1 King Bed",
                "size": "600 sq.ft",
                "perks": ["Ganges River & Valley View", "All Gourmet Wellness Meals Included", "Daily Guided Meditation & Yoga"]
            }
        ]
    },

    # =========================================================================
    # 💎 BUDGET CHIC & BOUTIQUE SANCTUARIES (< ₹3,000 / night)
    # =========================================================================
    {
        "id": 14,
        "name": "Zostel Plus Panoramic Terraces",
        "city": "Rishikesh",
        "state": "Uttarakhand",
        "category": "budget",
        "vibe": "💎 Mountain-View Infinity Pool & Co-Working Hub",
        "stars": 4,
        "rating": 4.85,
        "review_count": 1680,
        "price_per_night": 2400,
        "original_price": 3500,
        "img": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "💎 Budget Chic Sanctuary",
        "highlights": ["Rooftop infinity pool overlooking river gorge", "Dedicated high-speed creator co-working zone", "Community bonfire & live acoustic music nights"],
        "amenities": ["Rooftop Pool", "Co-working Space", "Cafe", "High-speed WiFi", "Air Conditioning"],
        "description": "Premium boutique experiential stay in Mohanchatti with cliffside infinity plunge pool, chic glass private chalets, and vibrant traveler community vibes.",
        "address": "Mohanchatti, Rishikesh, Uttarakhand 249304",
        "rooms": [
            {
                "id": "1401",
                "name": "Deluxe Private Mountain Chalet",
                "price": 2400,
                "capacity": 2,
                "bed": "1 Queen Bed",
                "size": "280 sq.ft",
                "perks": ["Private Forest Balcony", "Rooftop Pool Access", "High-Speed 200Mbps WiFi", "Air Conditioned"]
            }
        ]
    },
    {
        "id": 15,
        "name": "The Heritage Banyan Tree Stay",
        "city": "Hampi",
        "state": "Karnataka",
        "category": "budget",
        "vibe": "💎 Bouldered Palm Oasis & Riverside Hammocks",
        "stars": 4,
        "rating": 4.82,
        "review_count": 750,
        "price_per_night": 1800,
        "original_price": 2600,
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "🌴 Riverside Oasis",
        "highlights": ["Surrounded by Hampi's famous granite boulder hills", "Tungabhadra river boat ferry point", "Organic woodfired pizza garden"],
        "amenities": ["Garden Lounge", "Restaurant", "Bike Rental", "WiFi", "Hot Showers"],
        "description": "Laidback boutique stone cottage stay on the Hippie Island side of Hampi, offering serene sunset views over the paddy fields and ancient ruins.",
        "address": "Sanapur Lake Road, Hampi, Karnataka 583234",
        "rooms": [
            {
                "id": "1501",
                "name": "Boutique Stone Paddy Cottage",
                "price": 1800,
                "capacity": 2,
                "bed": "1 Queen Bed",
                "size": "250 sq.ft",
                "perks": ["Garden Hammock", "Free WiFi", "Hot Shower"]
            }
        ]
    },
    {
        "id": 16,
        "name": "Artjuna Portuguese Heritage Villa",
        "city": "Goa",
        "state": "Goa",
        "category": "budget",
        "vibe": "💎 1920s Colonial Portuguese Courtyard",
        "stars": 4,
        "rating": 4.89,
        "review_count": 1400,
        "price_per_night": 2800,
        "original_price": 3900,
        "img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800&auto=format&fit=crop&q=80",
        "images": [
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&auto=format&fit=crop&q=80"
        ],
        "tag": "☕ Vintage Portuguese Haven",
        "highlights": ["High ceiling red terracotta tiled villa", "Artisan bakery and Mediterranean cafe", "Open-air garden yoga shala"],
        "amenities": ["Garden Courtyard", "Artisan Cafe", "Yoga Studio", "High-speed WiFi", "Air Conditioning"],
        "description": "Charming restored 100-year-old Portuguese villa surrounded by mango trees, handcrafted wooden furniture, and peaceful garden nooks in Anjuna.",
        "address": "Monterio Vaddo, Anjuna, Goa 403509",
        "rooms": [
            {
                "id": "1601",
                "name": "Vintage Portuguese Courtyard Room",
                "price": 2800,
                "capacity": 2,
                "bed": "1 Four-Poster Queen Bed",
                "size": "320 sq.ft",
                "perks": ["Courtyard Patio", "Artisan Breakfast Discount", "High-Speed WiFi", "AC"]
            }
        ]
    }
]

# Quick category metadata for Discovery Studio navigation
HOTEL_CATEGORIES = {
    "all": {"name": "✨ All Stays", "icon": "fa-sparkles"},
    "palace": {"name": "👑 Royal Palaces & Havelis", "icon": "fa-chess-king"},
    "chalet": {"name": "🌲 Alpine Chalets & Igloos", "icon": "fa-mountain"},
    "beach": {"name": "🏖️ Cliffside & Ocean Villas", "icon": "fa-water"},
    "plantation": {"name": "☕ Tea Estate Bungalows", "icon": "fa-mug-hot"},
    "glamping": {"name": "⛺ Luxury Desert Glamping", "icon": "fa-campground"},
    "spa": {"name": "🧘 Spa & Wellness Retreats", "icon": "fa-spa"},
    "budget": {"name": "💎 Budget Chic (< ₹3,000)", "icon": "fa-tag"},
}
