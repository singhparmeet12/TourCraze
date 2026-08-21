"""
TourCraze Intelligent Geo & Destination Decision Engine.
Contains accurate geographical coordinates for Indian hubs and tourist destinations,
distance calculation algorithms, and multi-criteria quiz matching logic.
"""

import math
from typing import Dict, List, Any, Optional

# =============================================================================
# MAJOR DEPARTURE HUBS WITH ACCURATE COORDINATES
# =============================================================================
DEPARTURE_HUBS: List[Dict[str, Any]] = [
    {"name": "Delhi NCR", "state": "Delhi", "lat": 28.6139, "lng": 77.2090, "popular": True},
    {"name": "Mumbai", "state": "Maharashtra", "lat": 19.0760, "lng": 72.8777, "popular": True},
    {"name": "Bengaluru", "state": "Karnataka", "lat": 12.9716, "lng": 77.5946, "popular": True},
    {"name": "Chandigarh", "state": "Punjab/Haryana", "lat": 30.7333, "lng": 76.7794, "popular": True},
    {"name": "Pune", "state": "Maharashtra", "lat": 18.5204, "lng": 73.8567, "popular": True},
    {"name": "Kolkata", "state": "West Bengal", "lat": 22.5726, "lng": 88.3639, "popular": True},
    {"name": "Hyderabad", "state": "Telangana", "lat": 17.3850, "lng": 78.4867, "popular": True},
    {"name": "Chennai", "state": "Tamil Nadu", "lat": 13.0827, "lng": 80.2707, "popular": True},
    {"name": "Jaipur", "state": "Rajasthan", "lat": 26.9124, "lng": 75.7873, "popular": True},
    {"name": "Ahmedabad", "state": "Gujarat", "lat": 23.0225, "lng": 72.5714, "popular": True},
    {"name": "Kochi", "state": "Kerala", "lat": 9.9312, "lng": 76.2673, "popular": True},
    {"name": "Lucknow", "state": "Uttar Pradesh", "lat": 26.8467, "lng": 80.9462, "popular": True},
    {"name": "Dehradun", "state": "Uttarakhand", "lat": 30.3165, "lng": 78.0322, "popular": False},
    {"name": "Goa (Panaji)", "state": "Goa", "lat": 15.4909, "lng": 73.8278, "popular": False},
    {"name": "Guwahati", "state": "Assam", "lat": 26.1445, "lng": 91.7362, "popular": False},
    {"name": "Indore", "state": "Madhya Pradesh", "lat": 22.7196, "lng": 75.8577, "popular": False},
    {"name": "Bhopal", "state": "Madhya Pradesh", "lat": 23.2599, "lng": 77.4126, "popular": False},
    {"name": "Varanasi", "state": "Uttar Pradesh", "lat": 25.3176, "lng": 82.9739, "popular": False},
    {"name": "Amritsar", "state": "Punjab", "lat": 31.6340, "lng": 74.8723, "popular": False},
    {"name": "Shimla", "state": "Himachal Pradesh", "lat": 31.1048, "lng": 77.1734, "popular": False}
]

# =============================================================================
# CURATED TOURIST DESTINATIONS DATABASE (ACCURATE GEO, VIBES, ROADS & SEASONS)
# =============================================================================
GEO_DESTINATIONS: List[Dict[str, Any]] = [
    # --- NORTH INDIA (HIMACHAL, UTTARAKHAND, J&K, LADAKH, PUNJAB, RAJASTHAN) ---
    {
        "id": "manali",
        "name": "Manali & Solang Valley",
        "state": "Himachal Pradesh",
        "lat": 32.2432, "lng": 77.1892,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🏔️ Snow & High Altitude",
        "img": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Jun (Snow Dec–Feb)",
        "ideal_days": 4,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 22000,
        "vibes": ["adventure", "mountains", "snow", "couples", "friends", "relaxed"],
        "highlights": ["Solang Snow Valley", "Atal Tunnel & Sissu", "Old Manali Cafes", "Hadimba Forest"],
        "description": "High-altitude pine forests, snow adventure sports at Solang, and roaring Beas river."
    },
    {
        "id": "shimla",
        "name": "Shimla & Kufri",
        "state": "Himachal Pradesh",
        "lat": 31.1048, "lng": 77.1734,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🌲 Colonial Queen of Hills",
        "img": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?w=800&auto=format&fit=crop&q=80",
        "season": "Year-round (Snow Dec–Feb)",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 16000,
        "vibes": ["family", "couples", "mountains", "relaxed", "heritage"],
        "highlights": ["Mall Road & Ridge", "Kufri Snow Point", "Viceregal Lodge", "Jakhoo Ropeway"],
        "description": "British colonial heritage, vintage UNESCO toy train, and pine-clad hills."
    },
    {
        "id": "rishikesh",
        "name": "Rishikesh & Shivpuri",
        "state": "Uttarakhand",
        "lat": 30.0869, "lng": 78.2676,
        "category": "adventure",
        "is_mountain": False,
        "tag": "🌊 River Rafting & Yoga",
        "img": "https://images.unsplash.com/photo-1596178065887-1198b6148b2b?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – Jun",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "budget",
        "avg_cost": 12000,
        "vibes": ["adventure", "friends", "solo", "relaxed", "nature"],
        "highlights": ["Ganges White Water Rafting", "Triveni Ghat Evening Aarti", "Beatles Ashram", "Cliff Bungee Jump"],
        "description": "Yoga capital of the world, exhilarating Ganga rafting, and riverside luxury camping."
    },
    {
        "id": "mussoorie",
        "name": "Mussoorie & Landour",
        "state": "Uttarakhand",
        "lat": 30.4598, "lng": 78.0644,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🍂 Ruskin Bond Pine Trails",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Mar – Nov",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 18000,
        "vibes": ["couples", "relaxed", "mountains", "family"],
        "highlights": ["Landour Bakehouse", "Lal Tibba Viewpoint", "Kempty Falls", "Camel's Back Road"],
        "description": "Quiet colonial charm in Landour, misty pine pathways, and doon valley night panoramas."
    },
    {
        "id": "nainital",
        "name": "Nainital & Bhimtal",
        "state": "Uttarakhand",
        "lat": 29.3803, "lng": 79.4636,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🛶 Emerald Lake & Hills",
        "img": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=80",
        "season": "Mar – Jul, Oct – Feb",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 15000,
        "vibes": ["family", "couples", "relaxed", "mountains"],
        "highlights": ["Naini Lake Boating", "Snow View Ropeway", "Naina Peak Trek", "Tibetan Market"],
        "description": "Quaint emerald eye-shaped lake surrounded by seven verdant Himalayan peaks."
    },
    {
        "id": "jim_corbett",
        "name": "Jim Corbett National Park",
        "state": "Uttarakhand",
        "lat": 29.5300, "lng": 78.7747,
        "category": "nature",
        "is_mountain": False,
        "tag": "🐅 Royal Bengal Safari",
        "img": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=800&auto=format&fit=crop&q=80",
        "season": "Nov – Jun",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 20000,
        "vibes": ["adventure", "nature", "family", "friends"],
        "highlights": ["Dhikala 4x4 Jeep Safari", "Kosi River Riverside Resorts", "Corbett Falls", "Birdwatching Trails"],
        "description": "India's oldest national park with thrilling open-jeep tiger safaris along the Kosi river."
    },
    {
        "id": "jaipur",
        "name": "Jaipur & Amer",
        "state": "Rajasthan",
        "lat": 26.9124, "lng": 75.7873,
        "category": "heritage",
        "is_mountain": False,
        "tag": "👑 The Pink City & Forts",
        "img": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 3,
        "style": "Luxury",
        "budget_tier": "mid",
        "avg_cost": 22000,
        "vibes": ["heritage", "couples", "family", "luxury", "culture"],
        "highlights": ["Amer Fort Elephant Ridge", "Hawa Mahal Facade", "Nahargarh Sunset Point", "Chokhi Dhani Heritage Village"],
        "description": "Regal forts, vibrant pink bazaar bazaars, and opulent royal Rajputana architecture."
    },
    {
        "id": "udaipur",
        "name": "Udaipur & Lake Pichola",
        "state": "Rajasthan",
        "lat": 24.5854, "lng": 73.7125,
        "category": "heritage",
        "is_mountain": False,
        "tag": "✨ City of Lakes & Palaces",
        "img": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – Mar",
        "ideal_days": 3,
        "style": "Luxury",
        "budget_tier": "luxury",
        "avg_cost": 34000,
        "vibes": ["couples", "luxury", "heritage", "relaxed"],
        "highlights": ["City Palace Museum", "Lake Pichola Sunset Boat Cruise", "Jagmandir Island", "Sajjangarh Monsoon Palace"],
        "description": "Venice of the East with shimmering marble palaces floating on tranquil lake waters."
    },
    {
        "id": "jaisalmer",
        "name": "Jaisalmer & Sam Dunes",
        "state": "Rajasthan",
        "lat": 26.9157, "lng": 70.9083,
        "category": "desert",
        "is_mountain": False,
        "tag": "🏜️ Golden City & Desert Camps",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 20000,
        "vibes": ["adventure", "couples", "friends", "heritage"],
        "highlights": ["Golden Living Fort", "Sam Sand Dunes Camel Safari", "Desert Stargazing Swiss Tents", "Patwon Ki Haveli"],
        "description": "Living sandstone fort, thar desert camel treks, and magical dune folk nights."
    },
    {
        "id": "agra",
        "name": "Agra & Fatehpur Sikri",
        "state": "Uttar Pradesh",
        "lat": 27.1767, "lng": 78.0081,
        "category": "heritage",
        "is_mountain": False,
        "tag": "🤍 Taj Mahal Wonder",
        "img": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 2,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 10000,
        "vibes": ["heritage", "family", "couples", "culture"],
        "highlights": ["Taj Mahal Sunrise Tour", "Agra Fort Red Sandstone Citadel", "Mehtab Bagh Reflection View", "Fatehpur Sikri"],
        "description": "World wonder monument of eternal love and majestic Mughal imperial history."
    },
    {
        "id": "varanasi",
        "name": "Varanasi & Sarnath",
        "state": "Uttar Pradesh",
        "lat": 25.3176, "lng": 82.9739,
        "category": "heritage",
        "is_mountain": False,
        "tag": "🪔 Spiritual Heart of India",
        "img": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "budget",
        "avg_cost": 12000,
        "vibes": ["culture", "solo", "heritage", "relaxed"],
        "highlights": ["Dashashwamedh Maha Ganga Aarti", "Morning Sunrise Boat on Ganges", "Kashi Vishwanath Temple", "Sarnath Buddhist Stupa"],
        "description": "Ancient ghats, hypnotic evening fire aartis, and profound spiritual energy."
    },
    {
        "id": "leh_ladakh",
        "name": "Leh Ladakh & Nubra Valley",
        "state": "Ladakh",
        "lat": 34.1526, "lng": 77.5771,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🏍️ Land of High Passes",
        "img": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?w=800&auto=format&fit=crop&q=80",
        "season": "May – Sep",
        "ideal_days": 7,
        "style": "Adventure",
        "budget_tier": "luxury",
        "avg_cost": 45000,
        "vibes": ["adventure", "solo", "friends", "mountains"],
        "highlights": ["Pangong Tso Color-Changing Lake", "Khardung La Pass (17,982 ft)", "Hunder Sand Dunes & Bactrian Camels", "Thiksey Monastery"],
        "description": "Epic trans-himalayan mountain biking, cobalt lakes, and ancient Tibetan monasteries."
    },
    {
        "id": "gulmarg",
        "name": "Gulmarg & Srinagar",
        "state": "Jammu & Kashmir",
        "lat": 34.0484, "lng": 74.3805,
        "category": "mountains",
        "is_mountain": True,
        "tag": "❄️ Ski Paradise & Dal Lake",
        "img": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=800&auto=format&fit=crop&q=80",
        "season": "Year-round (Snow Nov–Mar)",
        "ideal_days": 5,
        "style": "Luxury",
        "budget_tier": "luxury",
        "avg_cost": 38000,
        "vibes": ["couples", "luxury", "snow", "mountains", "family"],
        "highlights": ["Gulmarg Phase 2 Cable Car Gondola", "Dal Lake Houseboat Stay & Shikara", "Pahalgam Betaab Valley", "Mughal Terraced Gardens"],
        "description": "Asia's highest cable car, powdery ski slopes, and iconic luxury wooden houseboats."
    },

    # --- WEST & CENTRAL INDIA (MAHARASHTRA, GOA, GUJARAT, MADHYA PRADESH) ---
    {
        "id": "goa_north",
        "name": "North Goa (Calangute, Vagator)",
        "state": "Goa",
        "lat": 15.5494, "lng": 73.7535,
        "category": "beach",
        "is_mountain": False,
        "tag": "🎉 Beach Clubs & Sunsets",
        "img": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – May",
        "ideal_days": 4,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 24000,
        "vibes": ["beach", "nightlife", "friends", "adventure", "couples"],
        "highlights": ["Vagator Cliff Sunset Lounges", "Anjuna Flea Market", "Scuba & Watersports", "Chapora Fort"],
        "description": "Vibrant seaside shacks, coastal sunset nightlife, and exhilarating watersports."
    },
    {
        "id": "goa_south",
        "name": "South Goa (Palolem, Agonda)",
        "state": "Goa",
        "lat": 15.0100, "lng": 74.0232,
        "category": "beach",
        "is_mountain": False,
        "tag": "🧘 Peaceful Serene Coastline",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – May",
        "ideal_days": 4,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 25000,
        "vibes": ["beach", "couples", "relaxed", "nature", "luxury"],
        "highlights": ["Palolem Crescent Beach", "Butterfly Beach Boat Safari", "Cabo De Rama Cliff View", "Portuguese Heritage Mansions"],
        "description": "Untouched white sand coves, serene sea-facing wooden cottages, and dolphin cruises."
    },
    {
        "id": "lonavala",
        "name": "Lonavala & Khandala",
        "state": "Maharashtra",
        "lat": 18.7557, "lng": 73.4091,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🌧️ Sahyadri Waterfalls & Forts",
        "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
        "season": "Jun – Feb (Peak in Monsoons)",
        "ideal_days": 2,
        "style": "Relaxed",
        "budget_tier": "budget",
        "avg_cost": 10000,
        "vibes": ["family", "friends", "relaxed", "nature"],
        "highlights": ["Tiger's Leap Cliff", "Bhushi Dam Cascades", "Karla Buddhist Caves", "Lonavala Chikki Street"],
        "description": "Iconic Mumbai-Pune weekend escape with dramatic mist-cloaked Sahyadri cliffs."
    },
    {
        "id": "mahabaleshwar",
        "name": "Mahabaleshwar & Panchgani",
        "state": "Maharashtra",
        "lat": 17.9237, "lng": 73.6586,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🍓 Strawberry Valleys & Viewpoints",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Jun",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 14000,
        "vibes": ["family", "couples", "relaxed", "mountains"],
        "highlights": ["Mapro Strawberry Garden", "Arthur's Seat Valley Point", "Venna Lake Boating", "Table Land Plateau"],
        "description": "Luscious strawberry farms, evergreen western ghat views, and cool mountain breezes."
    },
    {
        "id": "alibaug",
        "name": "Alibaug Coastal Getaway",
        "state": "Maharashtra",
        "lat": 18.6414, "lng": 72.8722,
        "category": "beach",
        "is_mountain": False,
        "tag": "⛵ Speedboat & Beach Villas",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – May",
        "ideal_days": 2,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 15000,
        "vibes": ["couples", "friends", "beach", "relaxed"],
        "highlights": ["Kolaba Sea Fort", "Mandwa Jet Ski Watersports", "Nagaon Beach Shacks", "Luxury Coconut Grove Villas"],
        "description": "Short 20-min catamaran drive from Mumbai with beach resorts and authentic seafood."
    },
    {
        "id": "rann_of_kutch",
        "name": "Rann of Kutch & Bhuj",
        "state": "Gujarat",
        "lat": 23.7337, "lng": 69.8597,
        "category": "desert",
        "is_mountain": False,
        "tag": "🌕 White Salt Desert & Full Moon",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Nov – Feb (Rann Utsav)",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "mid",
        "avg_cost": 22000,
        "vibes": ["culture", "family", "couples", "photography"],
        "highlights": ["White Salt Desert Moonlight Walk", "Rann Utsav Tent City", "Kala Dungar Panoramic Summit", "Kutchi Handicraft Villages"],
        "description": "Vast endless white salt desert glowing under the full moon with vibrant folk dances."
    },

    # --- SOUTH INDIA (KARNATAKA, KERALA, TAMIL NADU, GOA) ---
    {
        "id": "coorg",
        "name": "Coorg (Madikeri)",
        "state": "Karnataka",
        "lat": 12.4244, "lng": 75.7382,
        "category": "nature",
        "is_mountain": True,
        "tag": "☕ Coffee Estates & Waterfalls",
        "img": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – May",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 18000,
        "vibes": ["couples", "nature", "relaxed", "mountains", "family"],
        "highlights": ["Abbey & Iruppu Waterfalls", "Namdroling Golden Monastery (Bylakuppe)", "Coffee Plantation Stays", "Raja's Seat Sunset"],
        "description": "Scotland of India with aromatic coffee plantations, Tibetan settlements, and misty peaks."
    },
    {
        "id": "chikmagalur",
        "name": "Chikmagalur & Mullayanagiri",
        "state": "Karnataka",
        "lat": 13.3161, "lng": 75.7720,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🥾 Peak Treks & Rainforests",
        "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – Apr",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "budget",
        "avg_cost": 14000,
        "vibes": ["adventure", "friends", "nature", "mountains"],
        "highlights": ["Mullayanagiri Karnataka's Highest Peak", "Baba Budangiri Range", "Hebbe Waterfalls 4x4 Trail", "Coffee Tasting"],
        "description": "Birthplace of Indian coffee, offering rugged Western Ghat treks and lush emerald hills."
    },
    {
        "id": "gokarna",
        "name": "Gokarna & Om Beach",
        "state": "Karnataka",
        "lat": 14.5479, "lng": 74.3188,
        "category": "beach",
        "is_mountain": False,
        "tag": "🌊 Bohemian Cliffside Beaches",
        "img": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Apr",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "budget",
        "avg_cost": 13000,
        "vibes": ["beach", "solo", "friends", "couples", "adventure"],
        "highlights": ["5-Beach Cliffside Hike", "Om Beach & Half Moon Bay", "Mahabaleshwar Ancient Temple", "Beach Shack Cafes"],
        "description": "Unspoiled beach trails connecting five pristine golden coves separated by rocky cliffs."
    },
    {
        "id": "hampi",
        "name": "Hampi & Tungabhadra",
        "state": "Karnataka",
        "lat": 15.3350, "lng": 76.4600,
        "category": "heritage",
        "is_mountain": False,
        "tag": "🏛️ Vijayanagara Ruins & Boulders",
        "img": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "budget",
        "avg_cost": 14000,
        "vibes": ["heritage", "solo", "friends", "culture"],
        "highlights": ["Virupaksha 7th-Century Temple", "Stone Chariot at Vittala Temple", "Coracle River Ride across Tungabhadra", "Hippie Island Sunsets"],
        "description": "UNESCO World Heritage surreal boulder-strewn kingdom of the Vijayanagara Empire."
    },
    {
        "id": "munnar",
        "name": "Munnar & Eravikulam",
        "state": "Kerala",
        "lat": 10.0889, "lng": 77.0595,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🍵 Rolling Emerald Tea Carpets",
        "img": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – May",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "mid",
        "avg_cost": 18000,
        "vibes": ["couples", "nature", "mountains", "relaxed", "family"],
        "highlights": ["Kolukkumalai Highest Tea Peak", "Eravikulam Nilgiri Tahr Sanctuary", "Mattupetty Dam", "Spice Plantation Tours"],
        "description": "Endless layers of manicured tea estates, spice plantations, and cool hill weather."
    },
    {
        "id": "alleppey",
        "name": "Alleppey (Alappuzha)",
        "state": "Kerala",
        "lat": 9.4981, "lng": 76.3388,
        "category": "nature",
        "is_mountain": False,
        "tag": "🛶 Venice of the East & Houseboats",
        "img": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – Mar",
        "ideal_days": 2,
        "style": "Luxury",
        "budget_tier": "mid",
        "avg_cost": 22000,
        "vibes": ["couples", "luxury", "relaxed", "nature", "family"],
        "highlights": ["Private Traditional Kettuvallam Houseboat", "Vembanad Lake Backwater Cruise", "Karimeen Fish Fry Dinner", "Marari Quiet Beach"],
        "description": "Gliding through palm-fringed canals on traditional wooden houseboats with fresh Kerala cuisine."
    },
    {
        "id": "wayanad",
        "name": "Wayanad Rainforests",
        "state": "Kerala",
        "lat": 11.6854, "lng": 76.1320,
        "category": "nature",
        "is_mountain": True,
        "tag": "🌿 Treehouses & Caves",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – May",
        "ideal_days": 3,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 16000,
        "vibes": ["nature", "couples", "adventure", "friends"],
        "highlights": ["Edakkal Prehistoric Caves", "Chembra Heart-Shaped Lake Trek", "Banasura Sagar Earth Dam", "Luxury Rainforest Treehouse Resorts"],
        "description": "Lush evergreen biodiversity hotspot with prehistoric rock etchings and canopy treehouses."
    },
    {
        "id": "ooty",
        "name": "Ooty & Coonoor",
        "state": "Tamil Nadu",
        "lat": 11.4102, "lng": 76.6950,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🚂 Nilgiri Heritage Toy Train",
        "img": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=80",
        "season": "Year-round",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 16000,
        "vibes": ["family", "couples", "mountains", "relaxed"],
        "highlights": ["Nilgiri Mountain Railway Steam Train", "Botanical & Rose Gardens", "Dolphin's Nose Coonoor View", "Homemade Chocolate Stores"],
        "description": "Colonial hill station nestled among blue eucalyptus mountains with heritage steam train."
    },
    {
        "id": "kodaikanal",
        "name": "Kodaikanal & Vattakanal",
        "state": "Tamil Nadu",
        "lat": 10.2381, "lng": 77.4892,
        "category": "mountains",
        "is_mountain": True,
        "tag": "☁️ Princess of Hill Stations",
        "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Jun",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "budget",
        "avg_cost": 15000,
        "vibes": ["couples", "solo", "mountains", "nature"],
        "highlights": ["Kodai Star Lake Cycling", "Pillar Rocks Viewpoint", "Vattakanal Dolphin's Nose Hike", "Pine Forest Walks"],
        "description": "Misty pine cliffs, serene star-shaped lake, and bohemian hillside cafes in Vattakanal."
    },
    {
        "id": "pondicherry",
        "name": "Pondicherry & Auroville",
        "state": "Tamil Nadu / Puducherry",
        "lat": 11.9416, "lng": 79.8083,
        "category": "beach",
        "is_mountain": False,
        "tag": "🥐 French Quarter & Promenades",
        "img": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – Mar",
        "ideal_days": 3,
        "style": "Relaxed",
        "budget_tier": "budget",
        "avg_cost": 14000,
        "vibes": ["couples", "relaxed", "culture", "beach", "solo"],
        "highlights": ["White Town French Quarter Walk", "Rock Beach Promenade", "Auroville Matrimandir Dome", "French Cafes & Croissants"],
        "description": "Cobblestone streets lined with pastel French colonial villas, bakeries, and golden beaches."
    },

    # --- EAST & NORTH-EAST INDIA (SIKKIM, MEGHALAYA, WEST BENGAL, ARUNACHAL) ---
    {
        "id": "gangtok",
        "name": "Gangtok & North Sikkim",
        "state": "Sikkim",
        "lat": 27.3389, "lng": 88.6065,
        "category": "mountains",
        "is_mountain": True,
        "tag": "🏔️ Kanchenjunga & Yumthang",
        "img": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=80",
        "season": "Mar – May, Oct – Dec",
        "ideal_days": 5,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 26000,
        "vibes": ["adventure", "mountains", "couples", "family"],
        "highlights": ["Tsomgo Glacial Lake & Nathula Pass", "Yumthang Valley of Flowers", "Rumtek Monastery", "MG Marg Pedestrian Street"],
        "description": "Crystal Himalayan peaks, blooming rhododendron valleys, and vibrant Buddhist monasteries."
    },
    {
        "id": "darjeeling",
        "name": "Darjeeling & Mirik",
        "state": "West Bengal",
        "lat": 27.0410, "lng": 88.2663,
        "category": "mountains",
        "is_mountain": True,
        "tag": "☕ Himalayan Queen & Toy Train",
        "img": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=80",
        "season": "Mar – Jun, Sep – Dec",
        "ideal_days": 4,
        "style": "Family",
        "budget_tier": "budget",
        "avg_cost": 16000,
        "vibes": ["family", "couples", "mountains", "heritage"],
        "highlights": ["Tiger Hill Kanchenjunga Sunrise", "UNESCO DHR Toy Train", "Happy Valley Tea Estate", "Batasia Loop Garden"],
        "description": "World's finest muscatel tea gardens with front-row seats to sunrise over Mt. Kanchenjunga."
    },
    {
        "id": "shillong",
        "name": "Shillong & Cherrapunji",
        "state": "Meghalaya",
        "lat": 25.5788, "lng": 91.8933,
        "category": "nature",
        "is_mountain": True,
        "tag": "🌿 Living Root Bridges & Waterfalls",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
        "season": "Sep – May",
        "ideal_days": 4,
        "style": "Adventure",
        "budget_tier": "mid",
        "avg_cost": 22000,
        "vibes": ["nature", "adventure", "friends", "solo"],
        "highlights": ["Double Decker Living Root Bridge Trek", "Nohkalikai Thundering Waterfall", "Dawki Crystal Clear Umngot River", "Mawlynnong Cleanest Village"],
        "description": "Scotland of the East with 100-year-old bio-engineered root bridges and turquoise rivers."
    },
    {
        "id": "kaziranga",
        "name": "Kaziranga National Park",
        "state": "Assam",
        "lat": 26.5775, "lng": 93.1711,
        "category": "nature",
        "is_mountain": False,
        "tag": "🦏 One-Horned Rhino Sanctuary",
        "img": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=800&auto=format&fit=crop&q=80",
        "season": "Nov – Apr",
        "ideal_days": 3,
        "style": "Family",
        "budget_tier": "mid",
        "avg_cost": 20000,
        "vibes": ["nature", "family", "adventure"],
        "highlights": ["Elephant & Jeep Safari in Central Range", "Tea Garden Walks", "Brahmaputra River Dolphin Sightings", "Assamese Cultural Bihu Evenings"],
        "description": "UNESCO World Heritage wetlands home to two-thirds of the world's great one-horned rhinos."
    },
    {
        "id": "andaman",
        "name": "Andaman & Havelock Island",
        "state": "Andaman & Nicobar Islands",
        "lat": 11.9761, "lng": 92.9876,
        "category": "beach",
        "is_mountain": False,
        "tag": "🤿 Radhanagar & Scuba Diving",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "season": "Oct – May",
        "ideal_days": 5,
        "style": "Luxury",
        "budget_tier": "luxury",
        "avg_cost": 42000,
        "vibes": ["beach", "couples", "luxury", "adventure"],
        "highlights": ["Radhanagar Asia's Best Beach", "Scuba & Sea Walk at Elephant Beach", "Cellular Jail Light & Sound Show", "Night Kayaking Bioluminescence"],
        "description": "Turquoise island paradise with glowing bioluminescent waters and rich coral reefs."
    }
]


# =============================================================================
# GEOGRAPHIC DISTANCE & TRAVEL MODE CALCULATION UTILITIES
# =============================================================================
def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates great-circle distance in kilometers using Haversine formula."""
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def estimate_road_distance_and_transit(dest: Dict[str, Any], origin_lat: float, origin_lng: float) -> Dict[str, Any]:
    """
    Estimates realistic road distance and travel time based on terrain topography.
    Mountain ghat terrain incurs a 1.45x winding multiplier; plains incur ~1.22x.
    """
    aerial_km = calculate_haversine_distance(origin_lat, origin_lng, dest["lat"], dest["lng"])
    
    # Mountain routes vs plains highway winding factor
    multiplier = 1.45 if dest.get("is_mountain") else 1.22
    road_km = round(aerial_km * multiplier)

    # Determine best transit recommendations
    if road_km <= 280:
        mode = "🚗 Road Trip"
        hrs = max(2.5, round(road_km / 50, 1))
        transit_desc = f"{hrs} hrs scenic drive"
    elif road_km <= 550:
        mode = "🛣️ Highway Drive / 🚆 Train"
        hrs = round(road_km / 55, 1)
        transit_desc = f"{hrs} hrs by road / 6-8 hrs train"
    elif road_km <= 900:
        mode = "🚆 Express Train / ✈️ Flight"
        hrs = round(road_km / 65, 1)
        transit_desc = f"Overnight Train / ~1.5 hrs Flight"
    else:
        mode = "✈️ Direct Flight"
        transit_desc = "2 to 3 hrs direct flight"

    return {
        "road_km": road_km,
        "aerial_km": round(aerial_km),
        "transit_mode": mode,
        "transit_desc": transit_desc
    }


def find_destinations_by_radius(origin_name: str, max_km: int, category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Returns list of destinations within max_km from origin hub, enriched with real driving distances.
    """
    hub = next((h for h in DEPARTURE_HUBS if h["name"].lower() == origin_name.lower()), DEPARTURE_HUBS[0])
    results = []

    for d in GEO_DESTINATIONS:
        if category and category != "all" and d["category"] != category:
            continue

        transit_info = estimate_road_distance_and_transit(d, hub["lat"], hub["lng"])
        if transit_info["road_km"] <= max_km:
            item = dict(d)
            item["distance_km"] = transit_info["road_km"]
            item["transit_mode"] = transit_info["transit_mode"]
            item["transit_desc"] = transit_info["transit_desc"]
            item["from_hub"] = hub["name"]
            results.append(item)

    # Sort by closest distance first
    results.sort(key=lambda x: x["distance_km"])
    return results


# =============================================================================
# DESTINATION DECISION QUIZ MATCH ENGINE
# =============================================================================
def match_quiz_destinations(answers: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Evaluates 5 quiz questions and scores all curated destinations to return top 3 best fits.
    Questions:
    1. companion: 'solo', 'couples', 'friends', 'family'
    2. landscape: 'mountains', 'beach', 'heritage', 'nature', 'desert'
    3. vibe: 'adventure', 'relaxed', 'culture', 'nightlife'
    4. days: 2, 4, 7
    5. budget: 'budget', 'mid', 'luxury'
    """
    companion = answers.get("companion", "couples")
    landscape = answers.get("landscape", "mountains")
    vibe = answers.get("vibe", "relaxed")
    pref_days = int(answers.get("days", 4))
    budget_tier = answers.get("budget", "mid")

    scored = []
    for d in GEO_DESTINATIONS:
        score = 50  # base score

        # 1. Landscape Match (Weight: 25)
        if d["category"] == landscape:
            score += 25
        elif landscape in d.get("vibes", []):
            score += 15

        # 2. Companion Match (Weight: 15)
        if companion in d.get("vibes", []):
            score += 15
        elif d.get("style", "").lower() == companion:
            score += 10

        # 3. Vibe / Activity Match (Weight: 15)
        if vibe in d.get("vibes", []):
            score += 15
        elif d.get("style", "").lower() == vibe:
            score += 12

        # 4. Duration Match (Weight: 10)
        day_diff = abs(d.get("ideal_days", 4) - pref_days)
        if day_diff == 0:
            score += 10
        elif day_diff <= 1:
            score += 7
        elif day_diff <= 2:
            score += 4

        # 5. Budget Match (Weight: 10)
        if d.get("budget_tier") == budget_tier:
            score += 10
        else:
            score += 5

        # Normalize score to percentage (max ~100)
        match_pct = min(99, max(68, round(score * 0.9 + 5)))

        # Reason snippet
        why_match = f"Ideal for {companion} trips seeking {landscape} & {vibe} vibes with optimal {d['ideal_days']}-day itineraries."

        item = dict(d)
        item["match_score"] = match_pct
        item["match_reason"] = why_match
        scored.append(item)

    scored.sort(key=lambda x: x["match_score"], reverse=True)
    return scored[:3]
