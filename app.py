import streamlit as st
import os
from PIL import Image
im = Image.open("logo.png")
#CONFIG
st.set_page_config(
    page_title="FinTech Club IIT (ISM)",
    page_icon=im, 
    layout="wide",
    initial_sidebar_state="collapsed"
)

#CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@400;700;900&display=swap');

    /* GLOBAL THEME */
    .stApp {
        background-color: #050505;
        color: #ffffff;
        font-family: 'Space Mono', monospace;
    }
    
    /* HEADER ALIGNMENT */
    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #333;
    }
    .club-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.2rem; 
        font-weight: 900;
        line-height: 1;
        letter-spacing: -1px;
        color: #fff;
        margin: 0;
    }
    .club-subtitle {
        font-family: 'Space Mono', monospace;
        font-size: 1rem;
        color: #888;
        margin-top: 5px;
    }

    /* HERO SECTION */
    .hero-container {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        padding: 40px 0;
    }
    .hero-number {
        font-family: 'Montserrat', sans-serif;
        font-size: 8rem;
        font-weight: 900;
        color: #1a1a1a;
        line-height: 0.8;
        margin-right: 20px;
    }
    .hero-headline {
        font-family: 'Montserrat', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        line-height: 0.9;
        text-transform: uppercase;
        color: #ffffff;
    }

    /* CARDS - MOBILE OPTIMIZED */
    .feature-card {
        background-color: #111;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 0px;
        min-height: 200px; /* Ensures consistent height */
        margin-bottom: 20px; /* Spacing between cards on mobile */
        transition: all 0.2s ease-in-out;
    }
    .feature-card:hover {
        border-color: #fff;
        background-color: #161616;
        transform: translateY(-2px);
    }
    .card-letter {
        font-family: 'Montserrat', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        color: #444; /* Brightened from #333 for better visibility */
        margin-bottom: 10px;
        opacity: 0.8;
    }
    .card-title {
        font-weight: bold;
        color: #fff;
        margin-bottom: 5px;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
    }
    .card-desc { 
        color: #ccc; 
        font-size: 0.9rem; 
        line-height: 1.4; 
    }

    /* RESOURCE LINKS */
    .resource-link {
        text-decoration: none;
        color: white;
        display: block;
    }
    .resource-tag {
        border: 1px solid #444;
        color: #888;
        padding: 2px 8px;
        font-size: 0.7rem;
        margin-bottom: 10px;
        display: inline-block;
        text-transform: uppercase;
    }
    
    /* MOBILE ADJUSTMENTS */
    @media (max-width: 600px) {
        .hero-number { font-size: 5rem; }
        .hero-headline { font-size: 2.5rem; }
        .club-title { font-size: 1.5rem; }
    }
    </style>
""", unsafe_allow_html=True)

c1, c2 = st.columns([1, 8])

with c1:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.info("Logo Missing")

with c2:
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
            <div class="club-title">FINTECH CLUB</div>
            <div class="club-subtitle">IIT (ISM) DHANBAD | NVCTI</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

#NAVIGATION
tab_home, tab_resources = st.tabs(["// MANIFESTO", "// RESOURCES"])

with tab_home:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-number">01</div>
            <div class="hero-headline">ISN'T<br>JUST<br>TRADING</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **FinTech Club** is an organization running under **Naresh Vashisht Centre for Tinkering & Innovation (NVCTI)** at IIT (ISM) Dhanbad. 
    We analyze and develop financial models utilizing software technology to provide optimal financial solutions.
    """)
    
    st.write("---")
    st.subheader("WHAT EXACTLY DO WE DO?")

    w1, w2 = st.columns(2)
    with w1:
        st.info("**WE LEARN**\n\nFinance, Trading, Mathematics, Machine Learning")
        st.info("**WE APPLY**\n\nAlgo Trading, Data Analytics, Quant")
    with w2:
        st.info("**WE GROW**\n\nNetworking, Real Life Fintech PS, Leadership")
        st.info("**WE COMPETE**\n\nQuant Analysis, Inter IIT, Hackathons")

    st.write("---")
    
    st.subheader("WHY FINTECH??")
    
    def card(letter, title, desc):
        st.markdown(f"""
        <div class="feature-card">
            <div class="card-letter">{letter}</div>
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    # Grid Layout
    col_left, col_right = st.columns(2)

    with col_left:
        card("A", "Deep Dive into Fintech", "Understand the intersection of finance, technology, and innovation.")
        card("B", "Real-World Experience", "Work on impactful projects and live simulations.")
        card("C", "Skill Enhancement", "Master quantitative finance, trading strategies, and AI tools.")
        
    with col_right:
        card("D", "Exclusive Networking", "Engage with industry leaders, mentors, and talented peers.")
        card("E", "Global Perspective", "Explore international fintech regulations and market opportunities.")
        card("F", "Competitions & Challenges", "Compete in hackathons, ideathons, and tech meets.")

    st.markdown("<br><center><small style='color:#555;'>INVEST &nbsp;|&nbsp; STRATEGISE &nbsp;|&nbsp; INNOVATE</small></center>", unsafe_allow_html=True)


#KNOWLEDGE BASE
with tab_resources:
    st.header("The Repository")
    st.caption("Curated resources for recruitment purposes")

    # 1. CLUB FILES
    st.subheader("Session Files")
    st.warning("⚠️ Session files will be uploaded after the Workshop.")
    sessions = [
        ("Session 1: Induction Session", "session1.pdf"),
        ("Session 2: Workshop 1", "session2.pdf"),
        ("Session 3: Workshop 2", "session3.pdf"),
        ("Workshop Assets (ZIP)", "workshop_assets.zip")
    ]
    f1, f2 = st.columns(2)
    
    for index, (title, filename) in enumerate(sessions):
        col = f1 if index % 2 == 0 else f2
        
        with col:
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    st.download_button(
                        label=f"⬇️ {title}",
                        data=f,
                        file_name=filename,
                        mime="application/octet-stream",
                        use_container_width=True
                    )
            else:
                st.button(
                    f"🔒 {title}", 
                    disabled=True, 
                    use_container_width=True, 
                    key=f"missing_{index}"
                )
    st.subheader("Project Files")
    def resource_card(tag, title, desc, link):
        return f"""
        <div class="feature-card">
            <span class="resource-tag">{tag}</span>
            <a href="{link}" target="_blank" class="resource-link">
                <div class="card-title" style="margin-top:10px;">{title} ↗</div>
            </a>
            <div class="card-desc">{desc}</div>
        </div>
        """
    l1, l2 = st.columns(2)

    with l1:
        st.markdown(resource_card("PYTHON", "Python Project", "🔒 Coming Soon!", ""), unsafe_allow_html=True)
    with l2:
        st.markdown(resource_card("Analysis", "Fundamental Analysis Project", "🔒 Coming Soon!", ""), unsafe_allow_html=True)
    st.divider()
    st.subheader("External Uplinks")
    
    def resource_card(tag, title, desc, link):
        return f"""
        <div class="feature-card">
            <span class="resource-tag">{tag}</span>
            <a href="{link}" target="_blank" class="resource-link">
                <div class="card-title" style="margin-top:10px;">{title} ↗</div>
            </a>
            <div class="card-desc">{desc}</div>
        </div>
        """
    l1, l2 = st.columns(2)
    
    with l1:
        st.markdown(resource_card("PLAYLIST", "Statistics (Krish Naik)", "Complete Statistics playlist for Data Science.", "https://youtube.com/playlist?list=PLZoTAELRMXVMgtxAboeAx-D9qbnY94Yay&si=ZeS_hMxVuiQ--knf"), unsafe_allow_html=True)
        st.markdown(resource_card("RESOURCE", "Basics of Python", "W3Schools Python Course.", "https://www.w3schools.com/python/default.asp"), unsafe_allow_html=True)
        st.markdown(resource_card("PROBABILITY", "Probability - 50 Challenging Problems", "50 Challenging Problems in Probability Solutions.", "https://youtube.com/playlist?list=PL3YfeZZ7Mdjmhucty7I55jX7RwS30pVAN&si=S9ctK3z-zBRkRGxY"), unsafe_allow_html=True)

    with l2:
        st.markdown(resource_card("MODULE 1", "Zerodha: Stock Markets", "Introduction to Stock Markets.", "https://zerodha.com/varsity/module/introduction-to-stock-markets/"), unsafe_allow_html=True)
        st.markdown(resource_card("MODULE 2", "Zerodha: Technical Analysis", "Technical Analysis Guide.", "https://zerodha.com/varsity/module/technical-analysis/"), unsafe_allow_html=True)
        st.markdown(resource_card("MODULE 3", "Zerodha: Fundamental Analysis", "Fundamental Analysis Guide.", "https://zerodha.com/varsity/module/fundamental-analysis/"), unsafe_allow_html=True)
        









