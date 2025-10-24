import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh  # live countdown

# --- Streamlit setup ---
st.set_page_config(page_title="Spy Game", page_icon="🕵️", layout="centered")
st.title("🕵️ Spy Game")

# --- Local word list (short version for clarity) ---
# --- Word list (shortened for clarity, use your 1000-word list here) ---
LOCAL_WORDS = [
 "Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", "Nikola Tesla",
        "Galileo Galilei", "Stephen Hawking", "Niels Bohr", "Rosalind Franklin", "Ada Lovelace",
        "Dmitri Mendeleev", "Richard Feynman", "James Clerk Maxwell", "Michael Faraday",
        "Gregor Mendel", "Alan Turing", "Louis Pasteur", "Enrico Fermi", "Carl Sagan",
        "Erwin Schrödinger", "Max Planck", "Johannes Kepler", "Jane Goodall", "Neil deGrasse Tyson",
"Physics", "Chemistry", "Biology", "Astronomy", "Geology", "Mathematics", "Ecology",
        "Genetics", "Thermodynamics", "Quantum Mechanics", "Electromagnetism", "Relativity",
        "Evolution", "Botany", "Zoology", "Anatomy", "Neuroscience", "Meteorology",
        "Oceanography", "Paleontology", "Biochemistry", "Microbiology", "Astrophysics",
 "Artificial Intelligence", "Machine Learning", "3D Printing", "Robotics", "Drones",
        "Smartphones", "Virtual Reality", "Augmented Reality", "Quantum Computing",
        "Blockchain", "5G Network", "Internet of Things", "Autonomous Vehicles",
        "Wearable Devices", "Cloud Computing", "Cybersecurity", "Social Media", "Biotechnology",
        "Nanotechnology", "SpaceX Rockets", "Electric Cars", "ChatGPT", "Facial Recognition",
"Steam Engine", "Printing Press", "Telegraph", "Typewriter", "Rotary Phone",
        "Phonograph", "Radio", "Television", "VHS", "Cassette Tape", "Slide Projector",
        "Film Camera", "Gramophone", "Pocket Watch", "Abacus", "Mechanical Clock",
        "Horse Carriage", "Sewing Machine", "Record Player", "Analog Computer",

# double meaning
 
    "Bat", "Bank", "Bark", "Book", "Bow", "Box", "Can", "Cell", "Change", "Charge",
    "Check", "Coach", "Cold", "Current", "Date", "Deck", "Drill", "Duck", "Fair", "Fall",
    "File", "Fly", "Found", "Glass", "Jam", "Kind", "Left", "Letter", "Light", "Match",
    "Mine", "Nail", "Note", "Orange", "Park", "Pen", "Pitch", "Plane", "Point", "Post",
    "Ring", "Rock", "Roll", "Seal", "Slip", "Spring", "Square", "Star", "Stick", "Suit",
    "Tear", "Tie", "Train", "Watch", "Well", "Wave", "Right", "Sink", "Duck", "Bear",
    "Yard", "Fair", "Fly", "Palm", "File", "Bowl", "Sink", "Trip", "Toast", "Break",
    "Match", "Wave", "Light", "Can", "Seal", "Iron", "Ball", "Book", "Ring", "Suit",
    "Scale", "Club", "Drill", "Letter", "Spring", "Nail", "Coach", "Fan", "Race", "Pitch",
    "Crane", "Chest", "Jam", "Trip", "Duck", "Bat", "Page", "Ship", "Stage", "Play",
    "Charge", "Store", "Well", "Roll", "Saw", "Clip", "Net", "Pen", "Bill", "Plane",
    "Park", "Rock", "Date", "Line", "Tap", "Watch", "Note", "Ball", "Seal", "Light",
    "Tie", "Ring", "Fair", "Fly", "Mine", "Match", "Bark", "Kind", "Bank", "Spring",
    "File", "Coach", "Post", "Suit", "Wave", "Crane", "Race", "Bat", "Stage", "Trip",
    "Toast", "Pitch", "Duck", "Palm", "Bear", "Can", "Well", "Book", "Right", "Chest",
    "Play", "Drill", "Bill", "Point", "Glass", "Slip", "Jam", "Letter", "Star", "Roll",
    "Trip", "Light", "Ring", "Page", "Seal", "Plane", "Note", "Tie", "Wave", "Mine",
   
    
    
    
    # --- Places ---
"Airport","Bakery","Bank","Bar","Beach","Bridge","Bus Station","Cafe","Castle","Church",
"Cinema","Classroom","Cliff","Concert Hall","Courtroom","Desert","Farm","Fire Station","Forest","Garage",
"Garden","Harbour","Hospital","Hotel","Island","Jungle","Laboratory","Library","Lighthouse","Market",
"Museum","Office","Palace","Park","Petrol Station","Pharmacy","Playground","Police Station","Port","Post Office",
"Prison","Restaurant","School","Shopping Mall","Space Station","Sports Centre","Stadium","Subway","Supermarket","Swimming Pool",
"Temple","Theatre","Town Hall","Train Station","University","Zoo",

# --- Occupations ---
"Actor","Architect","Artist","Athlete","Baker","Banker","Barber","Bartender","Builder","Bus Driver",
"Butcher","Carpenter","Chef","Cleaner","Clerk","Coach","Dentist","Designer","Doctor","Driver",
"Electrician","Engineer","Farmer","Firefighter","Fisherman","Gardener","Hairdresser","Judge","Lawyer","Librarian",
"Mechanic","Miner","Musician","Nurse","Painter","Photographer","Pilot","Plumber","Police Officer","Politician",
"Postman","Professor","Receptionist","Scientist","Secretary","Shopkeeper","Singer","Soldier","Teacher","Waiter",
"Waitress","Writer",

# --- Food & Drink ---
"Apple","Avocado","Bacon","Bagel","Banana","Barbecue","Beans","Beef","Beer","Biscuit",
"Bread","Burger","Butter","Cake","Candy","Carrot","Cereal","Cheese","Chicken","Chips",
"Chocolate","Coffee","Cookie","Corn","Croissant","Cucumber","Curry","Donut","Egg","Fish",
"Fries","Fruit","Garlic","Grapes","Hotdog","Ice Cream","Juice","Lemon","Lettuce","Meat",
"Milk","Noodles","Onion","Orange","Pancake","Pasta","Peach","Pear","Pizza","Popcorn",
"Potato","Rice","Salad","Salt","Sandwich","Soup","Steak","Strawberry","Sushi","Tea",
"Tomato","Water","Wine","Yoghurt",

# --- Sports & Games ---
"Archery","Badminton","Baseball","Basketball","Bowling","Boxing","Chess","Cricket","Cycling","Darts",
"Fencing","Fishing","Football","Golf","Gymnastics","Hiking","Hockey","Judo","Karate","Running",
"Rugby","Sailing","Shooting","Skateboarding","Skiing","Snowboarding","Surfing","Swimming","Table Tennis","Tennis",
"Volleyball","Weightlifting","Wrestling",

# --- Objects & Items ---
"Alarm Clock","Anchor","Backpack","Ball","Balloon","Battery","Bed","Bell","Binoculars","Blanket",
"Book","Bottle","Broom","Brush","Bucket","Camera","Candle","Car","Chair","Clock",
"Computer","Cup","Desk","Door","Drum","Envelope","Fan","Flag","Fork","Glasses",
"Hammer","Helmet","Key","Knife","Lamp","Laptop","Map","Mirror","Mug","Notebook",
"Oven","Paintbrush","Pen","Pencil","Phone","Picture","Pillow","Plate","Radio","Razor",
"Remote","Rope","Ruler","Scissors","Shoe","Spade","Spoon","Suitcase","Table","Television",
"Toothbrush","Torch","Towel","Umbrella","Wallet","Watch","Window",

# --- Animals ---
"Ant","Bat","Bear","Bee","Bird","Butterfly","Camel","Cat","Cheetah","Chicken",
"Cow","Crab","Crocodile","Deer","Dog","Dolphin","Donkey","Duck","Eagle","Elephant",
"Fish","Flamingo","Frog","Fox","Giraffe","Goat","Goose","Hamster","Hedgehog","Horse",
"Kangaroo","Koala","Lion","Lizard","Monkey","Mouse","Octopus","Owl","Panda","Parrot",
"Penguin","Pig","Rabbit","Rat","Seal","Shark","Sheep","Snake","Spider","Squirrel",
"Tiger","Turtle","Whale","Wolf","Zebra",

# --- Transport ---
"Airplane","Ambulance","Bicycle","Boat","Bus","Cable Car","Car","Caravan","Ferry","Helicopter",
"Jet","Lorry","Metro","Minibus","Motorbike","Plane","Sailboat","Scooter","Ship","Submarine",
"Taxi","Train","Tram","Truck","Van",

# --- Nature ---
"Beach","Cave","Cliff","Cloud","Desert","Field","Flower","Forest","Grass","Hill",
"Island","Lake","Leaf","Lightning","Mountain","Ocean","Rain","Rainbow","River","Rock",
"Sand","Sea","Sky","Snow","Soil","Star","Storm","Sun","Tree","Valley",
"Volcano","Waterfall","Wind",

# --- Fantasy / Fun ---
"Alien","Angel","Castle","Cave","Crown","Dragon","Fairy","Ghost","Giant","Knight",
"Mermaid","Monster","Pirate","Prince","Princess","Robot","Superhero","Treasure","Vampire","Wizard",

# --- Everyday Actions / Verbs ---
"Run","Walk","Jump","Eat","Drink","Sleep","Read","Write","Sing","Dance",
"Cook","Play","Drive","Swim","Climb","Watch","Talk","Draw","Clean","Work",
"Study","Teach","Build","Fly","Catch","Throw","Laugh","Cry","Think","Smile",

# --- Technology & Modern Life ---
"App","Battery","Bluetooth","Calculator","Camera","Charger","Computer","Drone","Email","Headphones",
"Internet","Keyboard","Laptop","Microphone","Monitor","Mouse","Phone","Printer","Robot","Screen",
"Smartwatch","Speaker","Tablet","Television","USB","Website","WiFi",

# --- Household ---
"Bed","Chair","Table","Sofa","Lamp","Cupboard","Curtain","Mirror","Carpet","Fridge",
"Oven","Microwave","Sink","Toaster","Washing Machine","Dishwasher","Shower","Bathtub","Towel","Toothbrush",

# --- Countries & Cities ---
"Bangladesh","India","Pakistan","Nepal","China","Japan","South Korea","Singapore","Malaysia","Thailand",
"France","Germany","Italy","Spain","Portugal","Switzerland","England","Scotland","Ireland","Wales",
"USA","Canada","Mexico","Brazil","Argentina","Egypt","Kenya","Nigeria","South Africa","Australia",
"New Zealand","Iceland","Norway","Sweden","Denmark","Netherlands","Belgium","Greece","Turkey","Saudi Arabia",
"Qatar","UAE","Iran","Iraq","Israel","Jordan","Lebanon","Syria","Afghanistan","Sri Lanka",
"Dhaka","London","Paris","Rome","Madrid","Lisbon","Berlin","Tokyo","Seoul","Singapore","Sydney","New York","Dubai",

# --- Movies / Entertainment ---
"Avengers","Batman","Superman","Spider-Man","Iron Man","Hulk","Captain America","Doctor Strange","Thor","Black Panther",
"Harry Potter","Hogwarts","Star Wars","Darth Vader","Luke Skywalker","Yoda","Lightsaber","Jedi","Sith","Death Star",
"Jurassic Park","Dinosaur","Titanic","Avatar","Matrix","Neo","Morpheus","Trinity","Inception","Joker",

# --- Random & Fun ---
"Coffee Shop","Elevator","Beach Ball","Board Game","Laptop","Magic Trick","Haunted House","Time Machine",
"Amusement Park","Camping","Cooking Class","Treasure Map","Space Rocket","Hot Air Balloon","Detective","Spy","Secret Mission",
"Lost Island","Underwater City","Hidden Cave","Deserted Village","Ancient Temple","Golden Crown","Mystery Box","Secret Code",
"Birthday Party","Concert","Festival","Carnival","Picnic","Rainy Day","Sunny Afternoon","Midnight Train","Ocean Cruise","Winter Cabin",

    "Beach","Library","Hospital","Museum","Restaurant","Airport","University","Park","Cinema","Stadium",
    "Zoo","Cafe","Supermarket","Office","Factory","School","Market","Bank","Garden","Bridge","River",
    "Forest","Hotel","Temple","Mountain","Valley","Desert","Village","Town","City","Farm","Field",
    "Harbour","Ocean","Sea","Lake","Stream","Hill","Island","Church","Mosque","Palace","Castle",
    "Tower","Tunnel","Highway","Road","Street","Market","Bakery","Pharmacy","Clinic","Shop","Mall",
    "Garage","Warehouse","Workshop","Studio","Office","Theatre","Court","Embassy","Station","Busstop",
    "Subway","Train","Airport","Harbour","Pier","Dock","Factory","Plant","Farm","Mill","Refinery",
    "House","Apartment","Flat","Room","Kitchen","Bathroom","Bedroom","Livingroom","Balcony","Garage",
    "Garden","Roof","Door","Window","Wall","Ceiling","Floor","Chair","Table","Sofa","Bed","Lamp",
    "Television","Computer","Phone","Tablet","Laptop","Keyboard","Mouse","Printer","Camera","Clock",
    "Watch","Wallet","Bag","Umbrella","Key","Pen","Pencil","Notebook","Paper","Book","Magazine",
    "Newspaper","Bottle","Glass","Cup","Plate","Fork","Spoon","Knife","Bowl","Tray","Pan","Pot",
    "Oven","Stove","Microwave","Fridge","Freezer","Fan","Light","Switch","Plug","Socket","Cable",
    "Battery","Radio","Speaker","Headphones","Mirror","Curtain","Carpet","Pillow","Blanket","Towel",
    "Shirt","Trousers","Dress","Skirt","Shoes","Socks","Hat","Jacket","Coat","Scarf","Gloves",
    "Belt","Tie","Suit","Watch","Ring","Necklace","Earring","Bracelet","Sunglasses","Wallet","Purse",
    "Phone","Charger","Ticket","Passport","Bag","Backpack","Suitcase","Map","Compass","Camera",
    "Car","Bus","Train","Truck","Bicycle","Motorbike","Boat","Plane","Helicopter","Taxi","Subway",
    "Tram","Ship","Scooter","Van","Ambulance","Firetruck","Policecar","Rocket","Ball","Bat","Racket",
    "Goal","Net","Glove","Helmet","Stick","Skate","Board","Swimsuit","Towel","Whistle","Trophy",
    "Game","Match","Score","Team","Coach","Player","Referee","Audience","Stadium","Field","Court",
    "Doctor","Nurse","Teacher","Engineer","Scientist","Artist","Singer","Actor","Writer","Pilot",
    "Chef","Waiter","Driver","Police","Soldier","Firefighter","Lawyer","Judge","Mechanic","Farmer",
    "Plumber","Electrician","Carpenter","Builder","Coach","Athlete","Librarian","Dentist","Vet",
    "Student","Professor","Mayor","Minister","President","Secretary","Cleaner","Guard","Cashier",
    "Manager","Designer","Photographer","Reporter","Editor","Architect","Pharmacist","Therapist",
    "Barber","Hairdresser","Baker","Butcher","Tailor","Dancer","Musician","Painter","Translator",
    "Programmer","Technician","Cook","Shopkeeper","Courier","Pilot","Steward","Captain","Scientist",
    "Astronaut","Explorer","Inventor","Driver","Judge","Nurse","Doctor","Teacher","Librarian",
    "Book","Story","Poem","Novel","Dictionary","Magazine","Newspaper","Menu","Map","Sign","Poster",
    "Painting","Drawing","Sculpture","Photograph","Film","Music","Song","Dance","Concert","Show",
    "Festival","Party","Wedding","Meeting","Class","Lecture","Seminar","Workshop","Conference",
    "Competition","Race","Exam","Test","Holiday","Vacation","Picnic","Trip","Journey","Tour",
    "Adventure","Discovery","Experiment","Research","Game","Battle","War","Peace","Love","Friend",
    "Family","Child","Parent","Brother","Sister","Uncle","Aunt","Cousin","Grandfather","Grandmother",
    "Neighbour","Teacher","Student","Boss","Colleague","Partner","Customer","Doctor","Nurse",
    "Police","Fireman","Soldier","Lawyer","Judge","Artist","Singer","Actor","Writer","Pilot","Chef",
    "Farmer","Driver","Scientist","Engineer","Teacher","Doctor","Nurse","Artist","Singer","Actor",
    "Writer","Painter","Photographer","Dancer","Musician","Builder","Mechanic","Electrician","Plumber",
    "Tailor","Baker","Butcher","Cook","Manager","Clerk","Cashier","Waiter","Waitress","Designer",
    "Programmer","Technician","Librarian","Vet","Dentist","Lawyer","Judge","Politician","Mayor",
    "President","Minister","Soldier","Firefighter","Police","Driver","Pilot","Steward","Captain",
    "Scientist","Astronaut","Explorer","Inventor","Engineer","Researcher","Student","Professor",
    "Banker","Shopkeeper","Farmer","Gardener","Fisherman","Miner","Cleaner","Porter","Guard",
    "Coach","Athlete","Player","Referee","Champion","Captain","Fan","Audience","Spectator",
    "Team","Opponent","Score","Win","Lose","Draw","Goal","Point","Round","Match","Game","Set",
    "Hospital","Clinic","School","College","University","Library","Museum","Gallery","Office",
    "Restaurant","Cafe","Shop","Supermarket","Market","Bank","Hotel","Theatre","Cinema","Stadium",
    "Court","Station","Airport","Harbour","Bridge","Tunnel","Road","Street","Highway","Park",
    "Playground","Garden","Farm","Factory","Warehouse","Building","House","Apartment","Room",
    "Kitchen","Bathroom","Bedroom","Livingroom","Garage","Balcony","Roof","Door","Window",
    "Wall","Floor","Ceiling","Chair","Table","Bed","Sofa","Lamp","Clock","Mirror","Curtain",
    "Carpet","Pillow","Blanket","Shelf","Desk","Cupboard","Wardrobe","Fridge","Stove","Oven",
    "Microwave","Fan","Light","Switch","Plug","Socket","Cable","Battery","Radio","Speaker",
    "Television","Computer","Phone","Tablet","Laptop","Camera","Printer","Scanner","Keyboard",
    "Mouse","Monitor","Headphones","Book","Pen","Pencil","Paper","Notebook","Folder","Envelope",
    "Stamp","Card","Ticket","Pass","Passport","Wallet","Bag","Umbrella","Hat","Coat","Scarf",
    "Gloves","Shoes","Socks","Trousers","Shirt","Dress","Skirt","Belt","Tie","Suit","Watch",
    "Ring","Necklace","Earrings","Bracelet","Sunglasses","Towel","Toothbrush","Soap","Shampoo",
    "Comb","Brush","Mirror","Cream","Lotion","Perfume","Deodorant","Toothpaste","Razor",
    "Camera","Photo","Picture","Art","Music","Dance","Film","Video","Radio","Game","Toy","Ball",
    "Doll","Puzzle","Card","Chess","Lego","Dice","Kite","Balloon","Fireworks","Gift","Flower",
    "Tree","Plant","Grass","Leaf","Flower","Seed","Fruit","Vegetable","Animal","Bird","Fish",
    "Cat","Dog","Horse","Cow","Sheep","Pig","Goat","Chicken","Duck","Rabbit","Tiger","Lion",
    "Elephant","Bear","Deer","Monkey","Fox","Wolf","Snake","Frog","Spider","Bee","Ant","Butterfly"
]
# --- Initialise session state ---
defaults = {
    "started": False,
    "word_seen": False,
    "reveal_start": None,
    "current": 1,
    "players": 0,
    "word": "",
    "spies": [],
    "starter": None,  # ✅ to store who starts
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- Game setup inputs ---
num_players = st.number_input("Number of players", min_value=3, step=1)
num_spies = st.number_input("Number of spies", min_value=1, max_value=num_players - 1, step=1)

if st.button("Start Game"):
    if num_spies >= num_players:
        st.error("Number of spies must be less than players.")
    else:
        st.session_state.word = random.choice(LOCAL_WORDS)
        st.session_state.spies = random.sample(range(1, num_players + 1), num_spies)
        st.session_state.current = 1
        st.session_state.players = num_players
        st.session_state.started = True
        st.session_state.reveal_start = None
        st.session_state.word_seen = False
        st.session_state.starter = None  # reset starter
        st.rerun()

# --- Main Game ---
if st.session_state.started:
    player = st.session_state.current
    total = st.session_state.players

    if player <= total:
        st.subheader(f"Player {player}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Show your word"):
                st.session_state.word_seen = True
                if player in st.session_state.spies:
                    st.warning("🤫 You are the **SPY!**")
                else:
                    st.success(f"Your word is: **{st.session_state.word}**")

        with col2:
            last_player = (player == total)
            label = "Start Discussion" if last_player else "Next Player"
            disabled = not st.session_state.word_seen

            if st.button(label, disabled=disabled):
                st.session_state.word_seen = False
                st.session_state.current += 1
                if last_player:
                    st.session_state.reveal_start = time.time()
                    st.session_state.starter = random.randint(1, total)  # ✅ pick once
                st.rerun()

    else:
        # Countdown only after last player
        if st.session_state.reveal_start is None:
            st.session_state.reveal_start = time.time()

        # auto-refresh every second
        st_autorefresh(interval=1000, key="timer_refresh")

        elapsed = time.time() - st.session_state.reveal_start
        remaining = max(0, 240 - int(elapsed))  # 4 minutes

        # ✅ Use stored starter instead of random every rerun
        starter = st.session_state.starter or 1
        st.info(f"All players have seen their words! 🎯\n\n**Player {starter}** starts the discussion 🗣️")

        if remaining > 0:
            minutes = remaining // 60
            seconds = remaining % 60
            progress = (240 - remaining) / 240
            st.progress(progress)
            st.warning(f"⏱️ Word will be revealed in **{minutes} min {seconds} sec**...")
        else:
            st.success(f"⏰ Time’s up! The secret word was: **{st.session_state.word}**")

        if st.button("Restart Game"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
