import streamlit as st
import random
import time

st.set_page_config(page_title="Spy Game", page_icon="🕵️", layout="centered")

st.title("🕵️ Spy Game")

# --- Local list of ~1000 words ---
LOCAL_WORDS = [
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

# --- Session setup ---
if "started" not in st.session_state:
    st.session_state.started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# --- Inputs ---
num_players = st.number_input("Number of players", min_value=3, step=1)
num_spies = st.number_input("Number of spies", min_value=1, max_value=num_players-1, step=1)

if st.button("Start Game"):
    if num_spies >= num_players:
        st.error("Number of spies must be less than players.")
    else:
        st.session_state.word = random.choice(LOCAL_WORDS)
        st.session_state.spies = random.sample(range(1, num_players + 1), num_spies)
        st.session_state.current = 1
        st.session_state.players = num_players
        st.session_state.started = True
        st.session_state.start_time = time.time()
        st.rerun()

# --- Game Loop ---
if st.session_state.started:
    player = st.session_state.current
    total = st.session_state.players
    elapsed = time.time() - st.session_state.start_time

    st.write(f"⏱️ Time since game started: **{int(elapsed // 60)} min {int(elapsed % 60)} sec**")

    if player <= total:
        st.subheader(f"Player {player}")

        if st.button("Show your word"):
            if player in st.session_state.spies:
                st.warning("🤫 You are the **SPY!**")
            else:
                st.success(f"Your word is: **{st.session_state.word}**")

        if st.button("Next Player"):
            st.session_state.current += 1
            st.rerun()

    else:
        starter = random.randint(1, total)
        st.info(f"All players have seen their words! 🎯\n\n**Player {starter}** starts the discussion 🗣️")

        # Reveal word automatically after 4 minutes (240 seconds)
        if elapsed >= 240:
            st.success(f"⏰ Time’s up! The word was: **{st.session_state.word}**")
        else:
            remaining = 240 - int(elapsed)
            st.warning(f"The secret word will be revealed in {remaining} seconds...")

        if st.button("Restart Game"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
