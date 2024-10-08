

keys = ['category', 'color', 'article_type', 'brand_name', 'occasion', 'text_description']
categories_array = ["topwear", "bottomwear", "footwear", "accessories"]
brand_name_array= [
        "nike",
        "locomotive",
        "reebok",
        "puma",
        "adidas",
        "fastrack",
        "rockport",
        "esprit",
        "carrera",
        "united_colors_of_benetton",
        "indigo_nation",
        "murcia",
        "john_miller",
        "clarks",
        "jealous_21",
        "flying_machine",
        "new_balance",
        "carlton_london",
        "wildcraft",
        "wrangler",
        "crocs",
        "inkfruit",
        "scullers",
        "urban_yoga",
        "lee",
        "catwalk",
        "w",
        "vishudh",
        "playboy",
        "franco_leone",
        "skechers",
        "ganuchi",
        "newfeel",
        "batman",
        "fila",
        "classic_polo",
        "mark_taylor",
        "spykar",
        "aurelia",
        "basics",
        "genesis",
        "reid_&_taylor",
        "xoxo",
        "roadster",
        "test",
        "timberland",
        "red_tape",
        "tantra",
        "ed_hardy",
        "probase",
        "mother_earth",
        "lotto",
        "lee_cooper",
        "provogue",
        "converse",
        "hush_puppies",
        "id",
        "inc_5",
        "numero_uno",
        "asics",
        "rocia",
        "fifa",
        "chimp",
        "scullers_for_her",
        "hanes",
        "proline",
        "belmonte",
        "and",
        "enroute_women",
        "vans",
        "arrow",
        "mr._men",
        "status_quo",
        "new_hide",
        "adidas_originals",
        "arrow_sport",
        "hidekraft",
        "quechua",
        "belkin",
        "artengo",
        "highlander",
        "black_coffee",
        "kalenji",
        "kipsta",
        "facit",
        "inesis",
        "domyos",
        "decathlon",
        "nabaiji",
        "regent_polo_club",
        "turtle",
        "geonaute",
        "mayhem",
        "mtv",
        "tokyo_talkies",
        "enroute_men",
        "levis",
        "free_authority",
        "pink_floyd",
        "beatles",
        "superman",
        "peter_england",
        "spice_art",
        "little_miss",
        "i_dee",
        "police",
        "image",
        "gas",
        "lino_perros",
        "u.s._polo_assn.",
        "pepe_jeans",
        "casio",
        "beyouty",
        "speedo",
        "cat",
        "buckaroo",
        "crusoe",
        "deni_yo",
        "manchester_united",
        "aneri",
        "wills_lifestyle",
        "undercolors_of_benetton",
        "vital_gear",
        "guess",
        "nautica",
        "david_beckham",
        "c_vox",
        "arrow_woman",
        "campbell",
        "myntra",
        "quiksilver",
        "ice_watch",
        "diva",
        "mr._men_little_miss",
        "baggit",
        "s.oliver",
        "tabac",
        "4711",
        "footloose",
        "skybags",
        "allen_solly",
        "celine_dion",
        "louis_philippe",
        "pal_zileri",
        "van_heusen",
        "roxy",
        "kiara",
        "enamor",
        "fossil",
        "spalding",
        "biba",
        "john_players",
        "global_desi",
        "woodland",
        "2go_active_gear_usa",
        "maxima",
        "satya_paul",
        "hugo_boss",
        "aramis",
        "dkny",
        "dunhill",
        "nautilus",
        "baldessarini",
        "boss",
        "nike_fragrances",
        "dc_comics",
        "music",
        "disney",
        "marvel",
        "ray_ban",
        "oakley",
        "la_emotio",
        "folklore",
        "pacific_gold",
        "mumbai_slang",
        "american_tourister",
        "femella",
        "j._del_pozo",
        "jaguar",
        "paris_hilton",
        "tous",
        "slazenger",
        "formula_1",
        "perry_ellis",
        "calvin_klein",
        "davidoff",
        "yelloe",
        "miss_t",
        "jovan",
        "pierre_cardin",
        "miss_sixty",
        "kylie_minogue",
        "jockey",
        "che_guevara",
        "bulchee",
        "ediots",
        "yardley",
        "secret_temptation",
        "park_avenue",
        "wild_stone",
        "fogg",
        "18+",
        "gatsby",
        "old_spice",
        "denizen",
        "cabarelli",
        "vogue",
        "do_u_speak_green",
        "giordano",
        "aspen",
        "kenneth_cole",
        "skagen",
        "lovable",
        "opium",
        "fabindia",
        "azzaro",
        "cartier",
        "dolce_&_gabbana",
        "ferrari",
        "issey_miyake",
        "versace",
        "arrow_new_york",
        "titan",
        "heart_2_heart",
        "q&q",
        "tonino_lamborghini",
        "only",
        "guerrilla",
        "levitate",
        "ipanema",
        "grendha",
        "allen_solly_woman",
        "van_heusen_woman",
        "angry_birds",
        "u.s._polo_assn._denim_co.",
        "sepia",
        "jack_&_jones",
        "homme",
        "cobblerz",
        "timex",
        "pieces",
        "vero_moda",
        "citizen",
        "tonga",
        "be_for_bag",
        "envirosax",
        "windsor",
        "coolers",
        "fortune",
        "suunto",
        "senorita",
        "stens_by_enroute",
        "bata",
        "gliders",
        "force_10",
        "kelme",
        "peperone",
        "salomon",
        "otls",
        "sdl_by_sweet_dreams",
        "strapless",
        "spinn",
        "paridhan",
        "nina_ricci",
        "yves_saint_laurent",
        "burberry",
        "salvatore_ferragamo",
        "bulgari",
        "mont_blanc",
        "estee_lauder",
        "valentino_perfumes",
        "giorgio_armani",
        "ralph_lauren",
        "carolina_herrera",
        "happy_socks",
        "24",
        "rnc",
        "mineral",
        "miami_blues",
        "polaroid",
        "joker",
        "mickey",
        "latin_quarters",
        "red_chief",
        "helix",
        "bwitch",
        "tortoise",
        "span",
        "swayam",
        "remanika",
        "estd._1977",
        "prafful",
        "estelle",
        "alma",
        "little_miss_intimates",
        "french_connection",
        "amante",
        "fcuk_underwear",
        "calvin_klein_innerwear",
        "calvin_klein_underwear",
        "swiss_army",
        "wilson",
        "smashing_pumpkins",
        "royal_diadem",
        "aerosmith",
        "jimi_hendrix",
        "billy_idol",
        "hugo",
        "rolling_stone",
        "nirvana",
        "john_lenon",
        "carlos_moya",
        "indian_terrain",
        "spinz",
        "globalite",
        "kama_sutra",
        "casio_baby_g",
        "lomani",
        "adrika",
        "fusion_beats",
        "109f",
        "jacques_m",
        "rasasi",
        "giorgio_beverly_hills",
        "paco_rabanne",
        "euroluxe",
        "rising_wave",
        "love_passport",
        "saint_james",
        "f5",
        "umbro",
        "york",
        "shree",
        "tiptopp",
        "portia",
        "pitaraa",
        "sher_singh",
        "revv",
        "lucera",
        "miki_pearl",
        "deborah",
        "calzini",
        "parx",
        "stoln",
        "chromozome",
        "being_human",
        "raymond",
        "kraus_jeans",
        "hidedge",
        "dark_knight",
        "linkin_park",
        "nyk",
        "queen",
        "inaya",
        "just_natural",
        "lencia",
        "toniq",
        "red_rose",
        "mod_acc",
        "morellato",
        "just_cavalli",
        "fiorelli",
        "jag",
        "fnf",
        "smugglerz",
        "ayaany",
        "garfield",
        "avon",
        "f_sports",
        "sushilas",
        "ivory_tag",
        "lakme",
        "ponds",
        "smartoe",
        "revlon",
        "colorbar",
        "biara",
        "tommy_hilfiger",
        "streetwear",
        "olay",
        "horsefly",
        "hm",
        "forever_new",
        "elle",
        "the_amazing_spiderman",
        "lotus_herbals",
        "biotique",
        "fruit_of_the_loom",
        "rreverie",
        "rocky_s",
        "alayna",
        "fcuk",
        "hakashi",
        "taylor_of_london",
        "denim",
        "colour_me",
        "cavallini",
        "brut",
        "peri_peri",
        "avirate",
        "valley_of_flowers",
        "megadeth",
        "scholl"
    ]
article_type_array = [
        "tshirts",
        "shorts",
        "track_pants",
        "caps",
        "jackets",
        "sweatshirts",
        "sports_shoes",
        "shirts",
        "tracksuits",
        "sandals",
        "flip_flops",
        "watches",
        "sports_sandals",
        "casual_shoes",
        "formal_shoes",
        "handbags",
        "trousers",
        "flats",
        "heels",
        "tops",
        "belts",
        "skirts",
        "dresses",
        "jeans",
        "tunics",
        "sweaters",
        "free_gifts",
        "capris",
        "bra",
        "backpacks",
        "leggings",
        "laptop_bag",
        "scarves",
        "ties",
        "churidar",
        "kurtas",
        "kurtis",
        "dupatta",
        "sarees",
        "suits",
        "socks",
        "wallets",
        "hat",
        "shoe_accessories",
        "waistcoat",
        "stoles",
        "messenger_bag",
        "kurta_sets",
        "waist_pouch",
        "rucksacks",
        "mufflers",
        "innerwear_vests",
        "lounge_shorts",
        "lounge_pants",
        "footballs",
        "cufflinks",
        "stockings",
        "sunglasses",
        "necklace_and_chains",
        "bracelet",
        "umbrellas",
        "travel_accessory",
        "duffel_bag",
        "water_bottle",
        "briefs",
        "swimwear",
        "basketballs",
        "clutches",
        "accessory_gift_set",
        "headband",
        "trunk",
        "tights",
        "fragrance_gift_set",
        "perfume_and_body_mist",
        "deodorant",
        "gloves",
        "boxers",
        "mobile_pouch",
        "shrug",
        "suspenders",
        "camisoles",
        "jeggings",
        "night_suits",
        "blazers",
        "nehru_jackets",
        "patiala",
        "salwar",
        "earrings",
        "pendant",
        "bangle",
        "jumpsuit",
        "ties_and_cufflinks",
        "tablet_sleeve",
        "nightdress",
        "trolley_bag",
        "cushion_covers",
        "key_chain",
        "jewellery_set",
        "wristbands",
        "body_wash_and_scrub",
        "robe",
        "shapewear",
        "ipad",
        "ring",
        "nail_polish",
        "eyeshadow",
        "lipstick",
        "compact",
        "kajal_and_eyeliner",
        "lip_liner",
        "foundation_and_primer",
        "lip_plumper",
        "concealer",
        "lip_gloss",
        "highlighter_and_blush",
        "salwar_and_dupatta",
        "baby_dolls",
        "rain_jacket",
        "rain_trousers",
        "lounge_tshirts",
        "bath_robe",
        "mascara",
        "face_wash_and_cleanser",
        "face_moisturisers",
        "eye_cream",
        "beauty_accessory",
        "nail_essentials",
        "makeup_remover",
        "lip_care",
        "sunscreen",
        "hair_colour",
        "toner",
        "mens_grooming_kit",
        "body_lotion",
        "face_scrub_and_exfoliator",
        "mask_and_peel",
        "face_serum_and_gel",
        "hair_accessory",
        "lehenga_choli",
        "shoe_laces"
    ]
text_description_array=['chandler1234']
color_array = [
        "white",
        "grey",
        "blue",
        "black",
        "navy_blue",
        "red",
        "grey_melange",
        "yellow",
        "pink",
        "brown",
        "silver",
        "green",
        "purple",
        "steel",
        "gold",
        "beige",
        "orange",
        "copper",
        "maroon",
        "magenta",
        "cream",
        "tan",
        "olive",
        "teal",
        "multi",
        "khaki",
        "na",
        "peach",
        "mauve",
        "lavender",
        "burgundy",
        "coffee_brown",
        "turquoise_blue",
        "taupe",
        "off_white",
        "charcoal",
        "nude",
        "bronze",
        "fluorescent_green",
        "rust",
        "mustard",
        "skin",
        "sea_green",
        "metallic",
        "lime_green",
        "mushroom_brown",
        "rose"
    ]

occasion_array = [
        "sports",
        "casual",
        "semiformal",
        "formal",
        "party",
        "smart_casual",
        "everyday",
        "daily",
        "work",
        "ethnic",
        "general",
        "maternity",
        "western",
        "evening"
    ]
