import streamlit as st
import random
import time

# --- Streamlit page setup ---
st.set_page_config(page_title="Spy Game", page_icon="🕵️", layout="centered")

st.title("🕵️ Spy Game")

# --- Word list (~1000 basic words) ---
LOCAL_WORDS = [
    "Beach","Library","Hospital","Museum","Restaurant","Airport","University","Park","Cinema","Stadium",
    "Zoo","Cafe","Supermarket","Office","Factory","School","Market","Bank","Garden","Bridge","River",
    "Forest","Hotel","Temple","Mountain","Valley","Desert","Village","Town","City","Farm","Field",
    "Harbour","Ocean","Sea","Lake","Stream","Hill","Island","Church","Mosque","Palace","Castle",
    "Tower","Tunnel","Highway","Road","Street","Bakery","Pharmacy","Clinic","Shop","Mall","Garage",
    "Warehouse","Workshop","Studio","Theatre","Court","Embassy","Station","Busstop","Subway","Train",
    "Harbour","Pier","Dock","Factory","Plant","Farm","Mill","Refinery","House","Apartment","Flat",
    "Kitchen","Bathroom","Bedroom","Livingroom","Balcony","Garage","Garden","Roof","Door","Window",
    "Chair","Table","Sofa","Bed","Lamp","Television","Computer","Phone","Tablet","Laptop","Keyboard",
    "Mouse","Printer","Camera","Clock","Watch","Wallet","Bag","Umbrella","Key","Pen","Pencil",
    "Notebook","Paper","Book","Magazine","Bottle","Glass","Cup","Plate","Fork","Spoon","Knife",
    "Bowl","Pan","Pot","Oven","Stove","Microwave","Fridge","Freezer","Fan","Light","Switch","Plug",
    "Battery","Radio","Speaker","Headphones","Mirror","Curtain","Carpet","Pillow","Blanket","Towel",
    "Shirt","Trousers","Dress","Skirt","Shoes","Socks","Hat","Jacket","Coat","Scarf","Gloves",
    "Belt","Tie","Suit","Ring","Necklace","Earring","Bracelet","Sunglasses","Wallet","Purse",
    "Ticket","Passport","Bag","Backpack","Suitcase","Map","Compass","Car","Bus","Train","Truck",
    "Bicycle","Motorbike","Boat","Plane","Helicopter","Taxi","Tram","Ship","Scooter","Van",
    "Ambulance","Firetruck","Policecar","Rocket","Ball","Bat","Racket","Goal","Net","Helmet",
    "Stick","Skate","Board","Swimsuit","Whistle","Trophy","Game","Match","Team","Coach","Player",
    "Referee","Audience","Field","Court","Doctor","Nurse","Teacher","Engineer","Scientist","Artist",
    "Singer","Actor","Writer","Pilot","Chef","Waiter","Driver","Police","Soldier","Firefighter",
    "Lawyer","Judge","Mechanic","Farmer","Plumber","Electrician","Carpenter","Builder","Athlete",
    "Dentist","Vet","Student","Professor","Mayor","President","Secretary","Cleaner","Guard","Cashier",
    "Designer","Photographer","Reporter","Architect","Pharmacist","Therapist","Barber","Baker",
    "Tailor","Dancer","Musician","Painter","Translator","Programmer","Technician","Cook","Courier",
    "Captain","Astronaut","Explorer","Inventor","Researcher","Banker","Shopkeeper","Farmer","Gardener",
    "Fisherman","Miner","Cleaner","Porter","Guard","Coach","Athlete","Player","Referee","Champion",
    "Fan","Spectator","Hospital","Clinic","School","College","University","Library","Museum","Gallery",
    "Restaurant","Cafe","Shop","Supermarket","Market","Hotel","Theatre","Cinema","Stadium","Court",
    "Station","Airport","Bridge","Tunnel","Road","Street","Highway","Park","Playground","Garden",
    "Farm","Factory","Warehouse","Building","House","Apartment","Room","Kitchen","Bathroom","Bedroom",
    "Livingroom","Garage","Balcony","Roof","Chair","Table","Bed","Sofa","Lamp","Clock","Mirror",
    "Curtain","Carpet","Pillow","Blanket","Shelf","Desk","Cupboard","Wardrobe","Fridge","Stove",
    "Oven","Fan","Light","Switch","Plug","Socket","Cable","Battery","Radio","Speaker","Television",
    "Computer","Phone","Tablet","Laptop","Camera","Printer","Scanner","Keyboard","Mouse","Monitor",
    "Headphones","Book","Pen","Pencil","Paper","Notebook","Folder","Envelope","Stamp","Card","Ticket",
    "Pass","Passport","Wallet","Bag","Umbrella","Hat","Coat","Scarf","Gloves","Shoes","Socks",
    "Trousers","Shirt","Dress","Skirt","Belt","Tie","Suit","Watch","Ring","Necklace","Earrings",
    "Bracelet","Sunglasses","Towel","Toothbrush","Soap","Shampoo","Comb","Brush","Mirror","Cream",
    "Lotion","Perfume","Deodorant","Toothpaste","Razor","Camera","Photo","Picture","Toy","Ball",
    "Puzzle","Chess","Dice","Kite","Balloon","Fireworks","Gift","Flower","Tree","Plant","Grass",
    "Leaf","Seed","Fruit","Vegetable","Animal","Bird","Fish","Cat","Dog","Horse","Cow","Sheep",
    "Pig","Goat","Chicken","Duck","Rabbit","Tiger","Lion","Elephant","Bear","Deer","Monkey","Fox",
    "Wolf","Snake","Frog","Spider","Bee","Ant","Butterfly"
]

# --- Session state setup ---
if "started" not in st.session_state:
    st.session_state.started = False
if "word_seen" not in st.session_state:
    st.session_state.word_seen = False
if "reveal_start" not in st.session_state:
    st.session_state.reveal_start = None

# --- Game setup inputs ---
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
        st.session_state.reveal_start = None
        st.session_state.word_seen = False
        st.rerun()

# --- Main Game ---
if st.session_state.started:
    player = st.session_state.current
    total = st.session_state.players

    # PLAYER VIEW LOOP
    if player <= total:
        st.subheader(f"Player {player}")

        col1, col2 = st.columns(2)

        # "Show word" button
        with col1:
            if st.button("Show your word"):
                st.session_state.word_seen = True
                if player in st.session_state.spies:
                    st.warning("🤫 You are the **SPY!**")
                else:
                    st.success(f"Your word is: **{st.session_state.word}**")

        # "Next Player" or "Start Discussion"
        with col2:
            last_player = (player == total)
            label = "Start Discussion" if last_player else "Next Player"
            st.button(
                label,
                disabled=not st.session_state.word_seen,
                on_click=lambda: (
                    next_player(last_player)
                ),
                key=f"next_{player}"
            )

    # AFTER ALL PLAYERS FINISH
    else:
        if st.session_state.reveal_start is None:
            st.session_state.reveal_start = time.time()

        # Live auto-refresh every second
        st.experimental_rerun = getattr(st, "rerun", None)
        st_autorefresh = getattr(st, "autorefresh", None)
        if st_autorefresh:
            st_autorefresh(interval=1000, key="refresh")

        elapsed = time.time() - st.session_state.reveal_start
        remaining = max(0, 240 - int(elapsed))  # 4 min countdown

        starter = random.randint(1, total)
        st.info(f"All players have seen their words! 🎯\n\n**Player {starter}** starts the discussion 🗣️")

        if remaining > 0:
            minutes = remaining // 60
            seconds = remaining % 60
            st.warning(f"⏱️ Word will be revealed in **{minutes} min {seconds} sec**...")
        else:
            st.success(f"⏰ Time’s up! The secret word was: **{st.session_state.word}**")

        if st.button("Restart Game"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

# --- Helper Function ---
def next_player(last_player):
    """Moves to next player or starts discussion"""
    st.session_state.word_seen = False
    if last_player:
        st.session_state.current += 1
        st.session_state.reveal_start = time.time()  # start countdown
    else:
        st.session_state.current += 1
    st.rerun()
