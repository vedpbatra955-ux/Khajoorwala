import streamlit as st
import urllib.parse
import os
import base64

# --- FILE PATHS ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_IMAGE_FILE = os.path.join(CURRENT_DIR, "k2.png")

# Page Config
st.set_page_config(page_title="Khajoorwala Kataria's | Premium Dates in South Delhi", page_icon="🌴", layout="wide", initial_sidebar_state="collapsed")

# --- 1. ROYAL OASIS UI / CSS INJECTION ---
def apply_premium_styles(bg_image_path):
    bg_css = ""
    if os.path.exists(bg_image_path):
        with open(bg_image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        
        # Warm Cream (#FAF5EA) overlay on the watermark
        bg_css = f"""
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(250,245,234,0.95), rgba(250,245,234,0.95)), url('data:image/png;base64,{encoded}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: #FAF5EA;
        }}
        """
    else:
        bg_css = """
        [data-testid="stAppViewContainer"] { background-color: #FAF5EA; }
        """
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700;900&display=swap');
        
        {bg_css}
        
        #MainMenu {{visibility: hidden;}}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* Typography */
        * {{ font-family: 'Inter', sans-serif; color: #2B2B2B; }}
        h1, h2, h3, h4 {{ font-family: 'Playfair Display', serif !important; color: #1F3D2B !important; }}
        
        /* Announcement Strip */
        .announcement-bar {{
            background-color: #1F3D2B; color: #FAF5EA; text-align: center; padding: 10px;
            font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;
            margin: -60px -40px 20px -40px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        /* Trust Bar */
        .trust-bar {{
            display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;
            padding: 20px 10px; border-top: 1px solid rgba(184, 137, 43, 0.2); 
            border-bottom: 1px solid rgba(184, 137, 43, 0.2);
            background-color: transparent; margin-bottom: 4rem;
            font-size: 0.95rem; color: #1F3D2B; font-weight: 600; text-align: center;
        }}
        
        /* Product Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 14px !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important;
            border: 1px solid rgba(31, 61, 43, 0.08) !important; background-color: #FFFFFF;
            transition: all 0.3s ease !important; overflow: hidden; padding: 15px;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
            transform: translateY(-6px); box-shadow: 0 15px 35px rgba(31, 61, 43, 0.1) !important;
            border: 1px solid rgba(184, 137, 43, 0.4) !important;
        }}

        /* Solid Green Buttons -> Gold on Hover */
        .stButton > button {{
            border-radius: 8px !important; border: none !important;
            color: #FFFFFF !important; background-color: #1F3D2B !important;
            font-weight: 700 !important; text-transform: uppercase; font-size: 0.9rem !important;
            transition: all 0.3s ease; letter-spacing: 0.5px;
            box-shadow: 0 4px 10px rgba(31,61,43,0.2);
        }}
        .stButton > button:hover {{ 
            background-color: #B8892B !important; color: #FFFFFF !important; 
            box-shadow: 0 6px 15px rgba(184, 137, 43, 0.3);
        }}
        
        /* Cart +/- Buttons (Keep them subtle) */
        .qty-btn .stButton > button {{
            padding: 0 !important; font-size: 1.2rem !important; border: none !important; box-shadow: none !important;
            background-color: #E8EBE9 !important; color: #1F3D2B !important; border-radius: 50% !important;
            width: 32px !important; height: 32px !important; min-height: 32px !important;
        }}
        .qty-btn .stButton > button:hover {{ background-color: #1F3D2B !important; color: white !important; }}
        
        /* Badges */
        .badge {{
            display: inline-block; padding: 0.35em 0.85em; font-size: 0.7rem; font-weight: 700;
            border-radius: 4px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px;
        }}
        .badge-gold {{ background-color: #FDF8EE; color: #B8892B; border: 1px solid rgba(184,137,43,0.3); }}
        .badge-green {{ background-color: #E8ECE9; color: #1F3D2B; border: 1px solid rgba(31,61,43,0.2); }}
        .badge-brown {{ background-color: #F3EBE6; color: #4A2C1A; border: 1px solid rgba(74,44,26,0.2); }}
        
        /* Footer */
        .footer-text {{
            text-align: center; color: #2B2B2B; font-size: 0.85rem; line-height: 1.8;
            margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(31,61,43,0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

apply_premium_styles(BG_IMAGE_FILE)

# --- 2. ANNOUNCEMENT & HERO SECTION ---
st.markdown("<div class='announcement-bar'>✨ Free delivery in Malviya Nagar on orders above ₹500 ✨</div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 3rem 1rem 1.5rem 1rem;">
    <h1 style="font-size: clamp(3.5rem, 8vw, 5.5rem); font-weight: 900; margin-bottom: 0; line-height: 1.1;">
        Khajoorwala<sup style="font-size: clamp(0.8rem, 2vw, 1.2rem); font-family: 'Inter', sans-serif; font-weight: 700; color: #B8892B; letter-spacing: 1px; margin-left: 8px;">KATARIA'S</sup>
    </h1>
    <p style="font-size: clamp(1.1rem, 3vw, 1.3rem); color: #2B2B2B; font-weight: 400; max-width: 600px; margin: 1rem auto 2rem auto; line-height: 1.6;">
        Fresh from the farm to your South Delhi doorstep. Premium, hand-selected dates for pure, natural energy.
    </p>
</div>
<div class="trust-bar">
    <span>🌿 Hand-Selected Quality</span>
    <span>🚫 No Preservatives</span>
    <span>🛵 Fast Local Delivery</span>
    <span>🔄 Easy Replacement</span>
</div>
""", unsafe_allow_html=True)


if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- 3. PRODUCT CATALOG ---
products = [
    {
        "id": 1, "name": "The Marathon Date", "price": 40, "unit": "per piece",
        "tag": "<span class='badge badge-gold'>🔥 Best Seller</span>",
        "desc": "Nature's Energy Gel. 1 Premium Pitted Date + Sea Salt.",
        "image_file": os.path.join(CURRENT_DIR, "marathon.jpg")
    },
    {
        "id": 2, "name": "Premium Ajwa", "price": 850, "unit": "500g box",
        "tag": "<span class='badge badge-green'>✈️ Imported</span>",
        "desc": "The 'Holy Date'. Authentic, rich, and deeply healing.",
        "image_file": os.path.join(CURRENT_DIR, "ajwa.jpg")
    },
    {
        "id": 3, "name": "Medjool Caramel", "price": 950, "unit": "500g box",
        "tag": "<span class='badge badge-brown'>👑 Premium</span>",
        "desc": "The 'King of Dates'. Large, soft, and melt-in-your-mouth sweet.",
        "image_file": os.path.join(CURRENT_DIR, "medjool.jpg")
    }
]

cols = st.columns(3, gap="large")

for index, product in enumerate(products):
    with cols[index]:
        with st.container(border=True):
            if os.path.exists(product["image_file"]):
                st.image(product["image_file"], use_container_width=True)
            else:
                st.markdown(
                    """
                    <div style="background-color: #E8ECE9; height: 250px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
                        <span style="color: #1F3D2B; font-size: 0.9rem; font-weight: 600;">📸 Photo Placeholder</span>
                    </div>
                    """, unsafe_allow_html=True
                )
            
            st.markdown(product['tag'], unsafe_allow_html=True)
            st.markdown(f"<h3 style='font-size: 1.6rem; margin: 0;'>{product['name']}</h3>", unsafe_allow_html=True)
            
            # Star Rating & Freshness Line
            st.markdown("""
            <div style="margin-top: 4px; margin-bottom: 10px;">
                <span style="color: #B8892B; font-size: 0.9rem;">★★★★★</span>
                <span style="color: #2B2B2B; font-size: 0.75rem; margin-left: 5px; opacity: 0.8;">(Fresh stock - packed this week)</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<p style='height: 45px; font-size: 0.95rem; line-height: 1.4;'>{product['desc']}</p>", unsafe_allow_html=True)
                
            st.markdown("<hr style='margin: 15px 0; border: none; border-top: 1px solid rgba(31,61,43,0.1);'>", unsafe_allow_html=True)
            
            bottom_col1, bottom_col2 = st.columns([1, 1.2])
            with bottom_col1:
                st.markdown(f"""
                <div style="line-height: 1;">
                    <span style='font-family: "Playfair Display", serif; font-weight: 900; font-size: 1.5rem;'>₹{product['price']}</span><br>
                    <span style='font-size: 0.8rem; font-weight: 600; opacity: 0.7;'>{product['unit']}</span>
                </div>
                """, unsafe_allow_html=True)
            with bottom_col2:
                if st.button("Add to Cart", key=f"add_{product['id']}", use_container_width=True):
                    pid = product['id']
                    if pid in st.session_state.cart:
                        st.session_state.cart[pid] += 1
                    else:
                        st.session_state.cart[pid] = 1
                    st.toast(f"✅ Added to cart! Scroll down to checkout.")

# --- 4. ADVANCED CHECKOUT & CART ---
st.markdown("<hr style='margin: 4rem 0 2rem 0; border: none;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 2.2rem;'>🛒 Your Cart</h2>", unsafe_allow_html=True)

if not st.session_state.cart:
    st.markdown("<p style='text-align: center; font-size: 1.1rem; opacity: 0.8;'>Your cart is currently empty. Add some dates above to fuel up!</p>", unsafe_allow_html=True)
else:
    cart_col1, cart_col2, cart_col3 = st.columns([1, 2, 1])
    with cart_col2:
        st.markdown("<div style='background: white; padding: 25px; border-radius: 14px; box-shadow: 0 8px 30px rgba(31,61,43,0.08); border: 1px solid rgba(184,137,43,0.2); margin-bottom: 20px;'>", unsafe_allow_html=True)
        
        total_price = 0
        for pid, qty in list(st.session_state.cart.items()):
            prod = next((p for p in products if p['id'] == pid), None)
            if prod:
                item_total = prod['price'] * qty
                total_price += item_total
                
                row_col1, row_col2, row_col3, row_col4, row_col5 = st.columns([4, 1, 1, 1, 2], vertical_alignment="center")
                with row_col1:
                    st.markdown(f"<span style='font-size: 1.1rem; font-weight: 600;'>{prod['name']}</span>", unsafe_allow_html=True)
                with row_col2:
                    st.markdown('<div class="qty-btn">', unsafe_allow_html=True)
                    if st.button("➖", key=f"minus_{pid}"):
                        st.session_state.cart[pid] -= 1
                        if st.session_state.cart[pid] == 0:
                            del st.session_state.cart[pid]
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                with row_col3:
                    st.markdown(f"<div style='text-align: center; font-weight: 700; font-size: 1.1rem;'>{qty}</div>", unsafe_allow_html=True)
                with row_col4:
                    st.markdown('<div class="qty-btn">', unsafe_allow_html=True)
                    if st.button("➕", key=f"plus_{pid}"):
                        st.session_state.cart[pid] += 1
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                with row_col5:
                    st.markdown(f"<div style='text-align: right; font-weight: 700; font-size: 1.1rem;'>₹{item_total}</div>", unsafe_allow_html=True)
                st.markdown("<div style='border-bottom: 1px dashed rgba(31,61,43,0.1); margin: 10px 0;'></div>", unsafe_allow_html=True)
        
        FREE_DELIVERY_THRESHOLD = 500
        if total_price < FREE_DELIVERY_THRESHOLD:
            amount_needed = FREE_DELIVERY_THRESHOLD - total_price
            st.markdown(f"<p style='text-align: center; color: #B8892B; font-weight: 600; font-size: 0.9rem; margin-bottom: 5px;'>Add ₹{amount_needed} more to unlock FREE Delivery!</p>", unsafe_allow_html=True)
            st.progress(int((total_price / FREE_DELIVERY_THRESHOLD) * 100))
        else:
            st.markdown("<p style='text-align: center; color: #1F3D2B; font-weight: 700; font-size: 1rem; margin-bottom: 5px;'>🎉 You have unlocked FREE Delivery!</p>", unsafe_allow_html=True)
            st.progress(100)

        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px; padding-top: 15px; border-top: 2px solid #1F3D2B;">
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.5rem;">Total Amount</span>
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.8rem; color: #B8892B;">₹{total_price}</span>
            </div>
            <div style="text-align: center; margin-top: 10px; font-size: 0.85rem; font-weight: 600; opacity: 0.8;">
                🛡️ Payment Accepted: UPI, Cash on Delivery
            </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        seller_phone = "919210191930" 
        receipt_lines = [f"▪️ {qty}x {next(p['name'] for p in products if p['id'] == pid)} (₹{next(p['price'] for p in products if p['id'] == pid) * qty})" for pid, qty in st.session_state.cart.items()]
        order_details = "\n".join(receipt_lines)
        message = f"🌴 *New Order for Khajoorwala Kataria's*\n\nHi! I would like to place an order:\n\n{order_details}\n\n*Total: ₹{total_price}*\n\nPlease confirm my order!"
        encoded_message = urllib.parse.quote(message)
        
        st.markdown(
            f"""
            <a href="https://wa.me/{seller_phone}?text={encoded_message}" target="_blank" style="
                background-color: #1F3D2B; color: white; padding: 18px 20px; border-radius: 8px;
                text-decoration: none; display: block; width: 100%; text-align: center;
                font-size: 1.2rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
                box-shadow: 0 8px 25px rgba(31, 61, 43, 0.3); transition: all 0.3s ease;
            ">
            Checkout via WhatsApp 📲
            </a>
            """, unsafe_allow_html=True
        )

# --- 5. WHY DATES & BRAND STORY ---
st.markdown("<hr style='margin: 4rem 0 3rem 0; border: none;'>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Why Choose Our Dates?</h2>", unsafe_allow_html=True)
feat1, feat2, feat3 = st.columns(3)
with feat1:
    st.markdown("<div style='text-align: center; padding: 20px; background: white; border-radius: 12px;'><h3 style='font-size:1.4rem;'>⚡ Instant Energy</h3><p style='font-size:0.95rem; opacity:0.8;'>Loaded with fast-absorbing natural carbs. The perfect pre-workout or morning fuel.</p></div>", unsafe_allow_html=True)
with feat2:
    st.markdown("<div style='text-align: center; padding: 20px; background: white; border-radius: 12px;'><h3 style='font-size:1.4rem;'>🩸 Iron Rich</h3><p style='font-size:0.95rem; opacity:0.8;'>A natural powerhouse of iron and essential minerals to support healthy blood levels.</p></div>", unsafe_allow_html=True)
with feat3:
    st.markdown("<div style='text-align: center; padding: 20px; background: white; border-radius: 12px;'><h3 style='font-size:1.4rem;'>🌾 High Fiber</h3><p style='font-size:0.95rem; opacity:0.8;'>Excellent for digestion. A sweet treat that actually keeps your gut healthy.</p></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
story_col, review_col = st.columns([1, 1], gap="large")

with story_col:
    st.markdown("<h2>The Kataria Story</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.05rem; line-height: 1.7; opacity: 0.9;">
    What started as a search for pure, unrefined energy for our own morning runs turned into a passion for sourcing the finest dates in the world. <br><br>
    We hand-pack every box right here in South Delhi. Whether you are breaking your fast, gifting a loved one, or fueling a marathon, you are getting nature's absolute best.
    </p>
    """, unsafe_allow_html=True)

with review_col:
    st.markdown("<h2>South Delhi Speaks</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #B8892B; margin-bottom: 15px;">
        <p style="margin: 0; font-style: italic;">"The Marathon Dates are a game changer for my weekend cycling trips. Completely natural energy without the sugar crash."</p>
        <p style="margin: 5px 0 0 0; font-size: 0.8rem; font-weight: 600; opacity: 0.7;">— Rohit, Malviya Nagar</p>
    </div>
    <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #1F3D2B;">
        <p style="margin: 0; font-style: italic;">"The Ajwa dates are incredibly fresh. So much better than what sits on supermarket shelves for months."</p>
        <p style="margin: 5px 0 0 0; font-size: 0.8rem; font-weight: 600; opacity: 0.7;">— Priya M., Hauz Khas</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. FAQ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 1.5rem;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)
with st.expander("How long do the dates stay fresh?"):
    st.write("Our dates are packed fresh weekly. When stored in a cool, dry place in their airtight container, they will easily stay fresh for 3 to 6 months. For longer storage, you can keep them in the refrigerator.")
with st.expander("What are the payment options?"):
    st.write("For ultimate trust and convenience, we accept UPI payments and Cash on Delivery (COD). We will share the UPI QR code when confirming your order on WhatsApp.")
with st.expander("How long does delivery take?"):
    st.write("Orders placed before 2 PM are typically delivered the same day in Malviya Nagar. Surrounding South Delhi areas are delivered within 24 hours.")

# --- 7. PROFESSIONAL FOOTER ---
st.markdown("""
<div class="footer-text">
    <strong>Khajoorwala Kataria's</strong><br>
    Premium Hand-Selected Dates | Malviya Nagar, New Delhi, 110017<br>
    WhatsApp Support: +91 92101 91930 <br>
    FSSAI Lic No: [Add Your License Here] <br><br>
    <em>Freshness guaranteed. Delivered daily across South Delhi.</em><br>
    <span style="font-size: 0.75rem; margin-top: 10px; display: block;">Follow us on Instagram @KhajoorwalaKatarias</span>
</div>
""", unsafe_allow_html=True)
