import streamlit as st
# please type in the line below IN THE TERMINAL to get it to work (at least on mac)
# python3 -m streamlit run app.py

# Page Configuration
st.set_page_config(page_title="CHEM 107 Database", layout="wide")

# site styling
if 'theme' not in st.session_state:
    st.session_state.theme = 'Dark'

with st.sidebar:
    st.title("Settings")
    theme_choice = st.radio("Select Theme:", ["Dark", "Light"])
    st.session_state.theme = theme_choice
    st.divider()
    st.info("Use the toggle above to switch between the Dark and Light layouts.")

# --- Dynamic CSS Injection ---
if st.session_state.theme == "Dark":
    bg_color = "#2f0707"
    text_color = "#ffffff"
    input_bg = "#3E0909"
    card_bg = "rgba(255, 255, 255, 0.1)"
    btn_bg = "#3E0909"
    btn_text = "#690c0c"
else:
    bg_color = "#ffffff"
    text_color = "#270505"
    input_bg = "#A10A0A"
    card_bg = "#f8f9fb"
    btn_bg = "#AE0C0C"
    btn_text = "#ffffff"

st.markdown(f"""
    <style>
    /* Main App Background */
    .stApp {{
        background-color: {bg_color};
    }}
    
    /* Global Text Color */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label, .stApp div {{
        color: {text_color} !important;
    }}
    
    /* Sidebar Text Correction (Streamlit sidebars can be tricky) */
    [data-testid="stSidebar"] {{
        background-color: {bg_color};
        border-right: 1px solid rgba(255,255,255,0.1);
    }}

    /* Input Fields */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
        background-color: {input_bg} !important;
        border-radius: 20px !important;
        color: #31333F !important; /* Keep text inside inputs dark for readability */
    }}

    /* Buttons */
    div.stButton > button {{
        background-color: {btn_bg};
        color: {btn_text};
        border-radius: 10px;
        border: none;
        width: 100%;
        font-weight: bold;
        transition: 0.3s ease;
    }}
    
    div.stButton > button:hover {{
        opacity: 0.8;
        border: 1px solid {text_color};
    }}

    hr {{
        border-color: {text_color};
        opacity: 0.2;
    }}
    </style>
    """, unsafe_allow_html=True)

# video dictionary
content = [
    { 
        "id": 1, 
        "title": "Scientific Notation - Fast Review!", 
        "category": "Measurements", 
        "url": "https://youtu.be/ZtB0vJMGve4?si=XjluxwtoAA59s3W0", 
        "keywords": ["review", "introduction", "conversion"]
    },
    { 
        "id": 2, 
        "title": "How To Round Numbers Using Significant Figures", 
        "category": "Measurements", 
        "url": "https://youtu.be/fxdYta_Olv0?si=F5SqVca2P_eXbDe-",
        "keywords": ["sig figs", "significant figures", "tutorial"]
    },
    { 
        "id": 3, 
        "title": "Homogenous and Heterogeneous Mixtures Examples, Classification of Matter, Chemistry", 
        "category": "Atoms & Molecules", 
        "url": "https://youtu.be/eI-tmv4DLEk?si=TPChawH_HM0IL-Ts",
        "keywords": ["mixtures", "matter", "classification"]
    },
    { 
        "id": 4, 
        "title": "How To Convert Grames To Moles - VERY EASY!", 
        "category": "Stoichiometry", 
        "url": "https://youtu.be/irYPta9G_sw?si=Tr09sGiEZ5eIqLgS",
        "keywords": ["conversion", "moles", "molar mass"]
    },
    {
        "id": 5, 
        "title": "Unit Conversion | Metric System & SI Units", 
        "category": "Measurements", 
        "url": "https://youtu.be/_GB7IhyQt9A?si=h1lGY7LhaLRkPXMQ",
        "keywords": ["metric conversions", "SI units", "density", "temperature"]
    },
    {
        "id": 6, 
        "title": "Stoichiometry - Chemistry for Massive Creatures: Crash Course Chemistry #6", 
        "category": "Stoichiometry", 
        "url": "https://youtu.be/UL1jmJaUkaQ?si=laUOdnn5CKzl6ykc",
        "keywords": ["easy review", "mole ratios", "balancing equations"]
    },
    {
        "id": 7, 
        "title": "Cations and Anions Explained", 
        "category": "Atoms & Molecules", 
        "url": "https://youtu.be/aAV2DMAI5f8?si=yMSZ0W9JbLIxmENX",
        "keywords": ["charges", "introduction", "ions"]
    },
    {
        "id": 8, 
        "title": "How to Memorize The Polyatomic Ions - Formulas, Charges, Naming - Chemistry", 
        "category": "Atoms & Molecules", 
        "url": "https://youtu.be/FXBEh7nd9KQ?si=zbXkU4L6GdSDw9hA",
        "keywords": ["formulas", "charges", "polyatomic ions"]
    },
    {
        "id": 9, 
        "title": "Step by Step Stoichiometry Practice Problems | How to Pass Chemistry", 
        "category": "Stoichiometry", 
        "url": "https://youtu.be/lcnIiC8JZg0?si=DZc2m-bsbyhodz8Q",
        "keywords": ["conversion", "molar mass"]
    },
    {
        "id": 10, 
        "title": "Writing Chemical Formulas For Ionic Compounds", 
        "category": "Moles/Molecules/Chemical Equations", 
        "url": "https://youtu.be/GJ4Mds0CWLE?si=tXMMT7CQ9U5AbJh6",
        "keywords": ["formulas", "transition metals", "polyatomic ions"]
    },
    {
        "id": 11, 
        "title": "Naming Molecular Compounds", 
        "category": "Moles/Molecules/Chemical Equations", 
        "url": "https://youtu.be/eWn5jnJf0h4?si=8afqk21TT9pgiUao",
        "keywords": ["chemical formula", "prefix"]
    },
    {
        "id": 12, 
        "title": "Balancing Chemical Equations", 
        "category": "Moles/Molecules/Chemical Equations", 
        "url": "https://youtu.be/X7ckfeRjjvI?si=G2O1H9OvGbCz6VKH",
        "keywords": ["introduction", "practice problems"]
    },
    {
        "id": 13, 
        "title": "Boyle's Law Practice Problems", 
        "category": "Gas Laws", 
        "url": "https://youtu.be/v8r_AU_TlPg?si=YFidWJGXetxW8IZq",
        "keywords": ["boyle's law", "volume", "pressure"]
    },
    {
        "id": 14, 
        "title": "Ideal Gas Law Practice Problems with Molar Mass", 
        "category": "Gas Laws", 
        "url": "https://youtu.be/0VaupcMr3oQ?si=bgaumSqDSJHBPiEm",
        "keywords": ["ideal gas", "practice problems", "molar mass"]
    },
    {
        "id": 15, 
        "title": "Partial Pressures & Vapor Pressure: Crash Course Chemistry #15", 
        "category": "Gas Laws", 
        "url": "https://youtu.be/JbqtqCunYzA?si=94ba2kr5LjuXqL3R",
        "keywords": ["john dalton's law", "vapor pressure"]
    },
    {
        "id": 16, 
        "title": "Bohr Model of the Hydrogen Atom, Electron Transitions, Atomic Energy Levels, Lyman & Balmer Series", 
        "category": "Periodic Table/Atomic Structure", 
        "url": "https://youtu.be/mXxsT1ut35Q?si=RN3NNESF2HNqz004",
        "keywords": ["electronic transition", "light emission"]
    },
    {
        "id": 17, 
        "title": "Orbital Diagrams and Electron Configuration - Basic Introduction - Chemistry Practice Problems", 
        "category": "Periodic Table/Atomic Structure", 
        "url": "https://youtu.be/6dRdMy9tgzE?si=95int4KHGj-qre9N",
        "keywords": ["electronic configuration", "atomic number"]
    },
    {
        "id": 18, 
        "title": "Valence Electrons and the Periodic Table", 
        "category": "Periodic Table/Atomic Structure", 
        "url": "https://youtu.be/FPk2ziB9iX0?si=recmrKpqiczqa1LN",
        "keywords": ["electronic configuration", "bohr model"]
    },
    {
        "id": 19, 
        "title": "Bond Polarity, Electronegativity and Dipole Moment - Chemistry Practice Problems", 
        "category": "Chemical Bonding/Molecular Structure", 
        "url": "https://youtu.be/ds5HXmBkO0Y?si=oHu4v10q8DyjaygJ",
        "keywords": ["polarity", "bonds"]
    },
    {
        "id": 20, 
        "title": "How to Draw Lewis Structures", 
        "category": "Chemical Bonding/Molecular Structure", 
        "url": "https://youtu.be/NFZtjSeT3XE?si=hqdUUiOwz_8cllY7",
        "keywords": ["lewis structures", "review", "beginner"]
    },
    {
        "id": 21, 
        "title": "Polar and Nonpolar Molecules", 
        "category": "Chemical Bonding/Molecular Structure", 
        "url": "https://youtu.be/4ykSzYl_4vI?si=VECc-ZOfjy6HxMh4",
        "keywords": ["polarity", "introduction"]
    },
    {
        "id": 22, 
        "title": "Internal Energy, Heat, and Work Thermodynamics, Pressure & Volume, Chemistry Problems", 
        "category": "Energy", 
        "url": "https://youtu.be/E7s-hIoyNqY?si=hhp6-QGdXIApyVAd",
        "keywords": ["heat", "introduction"]
    },
    {
        "id": 23, 
        "title": "Energy work and heat", 
        "category": "Energy", 
        "url": "https://youtu.be/lF0AYzsuXo0?si=OQUahjJa9hMSPz0u",
        "keywords": ["heat", "energy"]
    },
    {
        "id": 24, 
        "title": "Calculating Heat and Work", 
        "category": "Energy", 
        "url": "https://youtu.be/Rjid2E8xcew?si=uQIitZxnzoJyj7W6",
        "keywords": ["heat", "work"]
    },
    {
        "id": 25, 
        "title": "Gibbs Free Energy - Entropy, Enthalpy & Equilibrium Constant K", 
        "category": "Entropy/Second Law of Thermodynamics", 
        "url": "https://youtu.be/2KuNzB0cZL4?si=aY5i9F0lJ39nkTD-",
        "keywords": ["entropy", "enthalpy", "energy"]
    },
    {
        "id": 26, 
        "title": "Entropy, Enthalpy, & Gibbs Free Energy - Chemistry Spontaneity Formulas", 
        "category": "Entropy/Second Law of Thermodynamics", 
        "url": "https://youtu.be/bp389WSTplY?si=nTtVAu3gk7HYXmIG",
        "keywords": ["energy", "review", "formulas"]
    },
    {
        "id": 27, 
        "title": "Entropy - 2nd Law of Thermodynamics - Enthalpy & Microstates", 
        "category": "Entropy/Second Law of Thermodynamics", 
        "url": "https://youtu.be/lN66F9V7-_Q?si=PexdBzCKjHxWKFPL",
        "keywords": ["introduction", "practice problems", "entropy"]
    },
    {
        "id": 28, 
        "title": "Integrated Rate Laws and Half Life Formula - Nth Order Reaction - Chemical Kinetics", 
        "category": "Chemical Kinetics", 
        "url": "https://youtu.be/2c8KSAeNQ6Y?si=UVohsgc8MmTljXQN",
        "keywords": ["order reactions", "review", "tutorial"]
    },
    {
        "id": 29, 
        "title": "Intregrated Rate Laws - Zero, First, & Second Order Reactions - Chemical Kinetics", 
        "category": "Chemical Kinetics", 
        "url": "https://youtu.be/7I0Xg92_eA4?si=jK4OXAHWBggW6blC",
        "keywords": ["introduction", "rate constant"]
    },
    {
        "id": 30, 
        "title": "Homoegenous vs Heterogeneous Catalysts - Basic Introduction", 
        "category": "Chemical Kinetics", 
        "url": "https://youtu.be/Tb0nzaj7bSA?si=cNvlFRyfHM3SKH0a",
        "keywords": ["catalysts", "review", "introduction"]
    },
    {
        "id": 31, 
        "title": "How To Write The Equilibrium Expression For a Chemical Reaction - Law of Mass Action", 
        "category": "Chemical Equilibrium", 
        "url": "https://youtu.be/cmVuUFIaLW0?si=10z8G-dhAhWtXMzK",
        "keywords": ["equilibrium", "review"]
    },
    {
        "id": 32, 
        "title": "Chemical Equilibrium Constant K - Ice Tables - Kp and Kc", 
        "category": "Chemical Equilibrium", 
        "url": "https://youtu.be/J4WJCYpTYj8?si=e4BbCNZwQu3HDgtF",
        "keywords": ["ice tables", "review", "practice problems"]
    },
    {
        "id": 33, 
        "title": "Le Chatelier's Principle", 
        "category": "Chemical Equilibrium", 
        "url": "https://youtu.be/bNcTt3l3Q8k?si=P8fXk4J-XkgVQfeh",
        "keywords": ["introduction", "practice problems", "chatelier"]
    },
    {
        "id": 34, 
        "title": "Engineering Chemistry: Review for Exam 1", 
        "category": "All", 
        "url": "https://youtu.be/M17GdOgrdZc?si=nQzBLAPC3PoIbiJa",
        "keywords": ["review"]
    },
    {
        "id": 35, 
        "title": "Engineering Chemistry: Review for Exam 2", 
        "category": "All", 
        "url": "https://youtu.be/szZyxdLXSmU?si=sIixFX7T7fG7WDHZ",
        "keywords": ["review"]
    }
]

# sidebar and header
st.title("CHEM 107 Database")
st.write("Explore CHEM 107 content for your class! Visit the forum to ask questions!")

# Create columns for Search, Forum Button (non working), and Category Filter
# Adjusting ratio to [3, 0.7, 1.3] to keep them on one line nicely
col1, col_forum, col2 = st.columns([3, 0.7, 1.3])

with col1:
    search_query = st.text_input("Search titles and tags...", placeholder="Try 'Dilution' or 'Formal Charge'", label_visibility="collapsed")

with col_forum:
    st.button("Forum") # non functional lol

with col2:
    categories = ["All", "Measurements", "Atoms & Molecules", "Moles/Molecules/Chemical Equations", "Stoichiometry", "Gas Laws", "Periodic Table/Atomic Structure", "Chemical Bonding/Molecular Structure", "Energy", "Entropy/2nd Law of Thermodynamics", "Chemical Kinetics", "Chemical Equilibrium"]
    active_category = st.selectbox("Category", categories, label_visibility="collapsed")

# Filtering Logic
filtered_content = []
for item in content:
    matches_search = (
        search_query.lower() in item["title"].lower() or 
        any(search_query.lower() in kw for kw in item["keywords"])
    )
    matches_category = (active_category == "All" or item["category"] == active_category)
    
    if matches_search and matches_category:
        filtered_content.append(item)

# Main Content Grid
st.divider()
st.subheader(f"Results ({len(filtered_content)})")

if filtered_content:
    cols = st.columns(2)
    for index, item in enumerate(filtered_content):
        with cols[index % 2]:
            st.markdown(f"### {item['title']}")
            st.video(item['url'])
            st.caption(f"Category: {item['category']} | Tags: {', '.join(item['keywords'])}")
            st.button(f"Save to Favorites", key=f"btn_{item['id']}")
            st.write("---")
else:
    st.warning("Sorry, nothing's popping up! Try again with a different search.")

# Footer 
st.markdown("<center style='opacity:0.5'>Built with Streamlit & VS Code • 2026</center>", unsafe_allow_html=True)