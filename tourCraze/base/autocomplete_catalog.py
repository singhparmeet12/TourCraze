"""
TourCraze Master Autocomplete Directory.
Dynamically aggregates and compiles every destination across the platform:
- 150 Curated Category Destinations (Mountains, Beach, Road Trips, Waterfalls, Cafes)
- 30 Unique Trending Destinations
- Curated Multi-Day Knowledge Base Hubs
- Top International Escapes
Ensures 100% of destinations are searchable with rich metadata, badges, and keyword matching.
"""

import re
from typing import List, Dict, Any
from .destinations_catalog import DESTINATIONS_DATA, TRENDING_DESTINATIONS
from .itinerary_knowledge_base import DEEP_DESTINATION_KNOWLEDGE


def _clean_budget_number(budget_val: Any) -> int:
    if isinstance(budget_val, int):
        return budget_val
    if isinstance(budget_val, str):
        digits = re.sub(r'[^\d]', '', budget_val)
        if digits:
            return int(digits)
    return 18000


def build_master_autocomplete_list() -> List[Dict[str, Any]]:
    """
    Builds a unified, deduplicated list of all searchable destinations
    across TourCraze with icons, tags, badge classes, recommended days, budget, and search keywords.
    """
    items: List[Dict[str, Any]] = []
    seen_names = set()

    # Category icon & badge mappings
    category_meta = {
        "mountains": {
            "tag": "🏔️ Mountain",
            "badge_class": "badge-gem",
            "icon": "fa-mountain",
            "days": 4,
            "budget": 18000,
            "style": "Adventure"
        },
        "beach": {
            "tag": "🏖️ Beach",
            "badge_class": "badge-top",
            "icon": "fa-umbrella-beach",
            "days": 4,
            "budget": 20000,
            "style": "Relaxed"
        },
        "road-trip": {
            "tag": "🚗 Road Trip",
            "badge_class": "badge-gem",
            "icon": "fa-car",
            "days": 5,
            "budget": 22000,
            "style": "Adventure"
        },
        "waterfall": {
            "tag": "🌊 Waterfall",
            "badge_class": "badge-top",
            "icon": "fa-water",
            "days": 3,
            "budget": 12000,
            "style": "Relaxed"
        },
        "cafe": {
            "tag": "☕ Cafes & Culture",
            "badge_class": "badge-gem",
            "icon": "fa-mug-hot",
            "days": 3,
            "budget": 14000,
            "style": "Relaxed"
        }
    }

    # 1. Add all 30 Trending Destinations
    for dest in TRENDING_DESTINATIONS:
        name = dest["name"]
        norm_key = name.lower().strip()
        if norm_key not in seen_names:
            seen_names.add(norm_key)
            
            # Keywords from name, state, and description
            keywords = [
                k.lower() for k in name.replace('&', ' ').replace('-', ' ').replace(',', ' ').split()
            ] + [k.lower() for k in dest["state"].split()]
            if "tagline" in dest:
                keywords.extend([k.lower() for k in dest["tagline"].split() if len(k) > 3])

            items.append({
                "name": name,
                "state": dest["state"],
                "tag": "🔥 Trending",
                "badge_class": "badge-top",
                "icon": "fa-fire",
                "days": dest.get("days", 4),
                "budget": dest.get("budget", 18000),
                "style": "Relaxed",
                "keywords": list(set(keywords))
            })

    # 2. Add all 150 Categorized Destinations (Mountains, Beach, Road Trips, Waterfalls, Cafes)
    for dest in DESTINATIONS_DATA:
        name = dest["name"]
        norm_key = name.lower().strip()
        if norm_key not in seen_names:
            seen_names.add(norm_key)
            
            cats = dest.get("categories", ["mountains"])
            main_cat = cats[0] if cats else "mountains"
            meta = category_meta.get(main_cat, {
                "tag": "⭐ Featured",
                "badge_class": "badge-top",
                "icon": "fa-location-dot",
                "days": 4,
                "budget": 18000,
                "style": "Relaxed"
            })
            
            keywords = [
                k.lower() for k in name.replace('&', ' ').replace('-', ' ').replace(',', ' ').split()
            ] + [k.lower() for k in dest["state"].split()]
            if "description" in dest:
                keywords.extend([k.lower() for k in dest["description"].split() if len(k) > 3])

            clean_budget = _clean_budget_number(dest.get("budget", meta["budget"]))

            items.append({
                "name": name,
                "state": dest["state"],
                "tag": dest.get("tag", meta["tag"]),
                "badge_class": meta["badge_class"],
                "icon": meta["icon"],
                "days": dest.get("days", meta["days"]),
                "budget": clean_budget,
                "style": dest.get("style", meta["style"]),
                "keywords": list(set(keywords))
            })

    # 3. Add Knowledge Base Curated Destinations
    for key, data in DEEP_DESTINATION_KNOWLEDGE.items():
        city_name = data["city"]
        norm_key = city_name.lower().strip()
        if norm_key not in seen_names and key not in seen_names:
            seen_names.add(norm_key)
            seen_names.add(key)
            
            keywords = [key] + [
                k.lower() for k in city_name.replace('&', ' ').replace('-', ' ').replace(',', ' ').split()
            ] + [k.lower() for k in data["state"].split()]
            keywords.extend(data.get("aliases", []))

            items.append({
                "name": city_name,
                "state": data["state"],
                "tag": "⭐ Top Curated",
                "badge_class": "badge-top",
                "icon": "fa-star",
                "days": len(data.get("daily_templates", [1, 2, 3])),
                "budget": int(20000 * data.get("cost_multiplier", 1.0)),
                "style": "Relaxed",
                "keywords": list(set(keywords))
            })

    # 4. Add Top International Escapes
    international_escapes = [
        {"name": "Bali", "state": "Indonesia", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-umbrella-beach", "days": 6, "budget": 55000, "style": "Relaxed", "keywords": ["bali", "ubud", "seminyak", "canggu", "kuta", "indonesia", "nusapenida"]},
        {"name": "Dubai", "state": "United Arab Emirates", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-building", "days": 5, "budget": 60000, "style": "Luxury", "keywords": ["dubai", "burj khalifa", "desert safari", "uae", "abu dhabi"]},
        {"name": "Paris", "state": "France", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-wine-glass", "days": 5, "budget": 85000, "style": "Luxury", "keywords": ["paris", "eiffel tower", "louvre", "france", "europe"]},
        {"name": "Switzerland (Swiss Alps)", "state": "Switzerland", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-snowflake", "days": 7, "budget": 120000, "style": "Luxury", "keywords": ["switzerland", "swiss", "interlaken", "lucerne", "zurich", "alps", "zermatt"]},
        {"name": "Tokyo", "state": "Japan", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-torii-gate", "days": 7, "budget": 95000, "style": "Relaxed", "keywords": ["tokyo", "kyoto", "japan", "shibuya", "shinjuku", "mount fuji"]},
        {"name": "Singapore", "state": "Singapore", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-tree-city", "days": 4, "budget": 50000, "style": "Family", "keywords": ["singapore", "marina bay", "sentosa", "gardens by the bay"]},
        {"name": "Bangkok & Phuket", "state": "Thailand", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-sun", "days": 6, "budget": 45000, "style": "Relaxed", "keywords": ["thailand", "bangkok", "phuket", "krabi", "pattaya", "phi phi"]},
        {"name": "London", "state": "United Kingdom", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-landmark", "days": 6, "budget": 95000, "style": "Relaxed", "keywords": ["london", "uk", "england", "big ben", "tower bridge", "britain"]},
        {"name": "Rome & Amalfi Coast", "state": "Italy", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-monument", "days": 6, "budget": 90000, "style": "Luxury", "keywords": ["rome", "italy", "colosseum", "amalfi", "vatican", "florence", "venice"]},
        {"name": "Maldives", "state": "Maldives", "tag": "🌴 International", "badge_class": "badge-intl", "icon": "fa-water", "days": 5, "budget": 90000, "style": "Luxury", "keywords": ["maldives", "male", "water villa", "overwater", "snorkeling", "scuba"]}
    ]

    for intl in international_escapes:
        norm_key = intl["name"].lower().strip()
        if norm_key not in seen_names:
            seen_names.add(norm_key)
            items.append(intl)

    return items


# Master cached list instance
MASTER_AUTOCOMPLETE_DESTINATIONS: List[Dict[str, Any]] = build_master_autocomplete_list()
