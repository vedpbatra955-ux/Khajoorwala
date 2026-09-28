import streamlit as st
import urllib.parse
import os
import base64

# --- FILE PATHS ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_IMAGE_FILE = os.path.join(CURRENT_DIR, "k2.png")

# Page Config
st.set_page_config(page_title="Khajoorwala Kataria's | Premium Dates", page_icon="🌴", layout="wide", initial_sidebar_state="collapsed")

# --- 1. WORLD-CLASS UI / CSS INJECTION ---
def apply_premium_styles(bg_image_path):
    bg_css = ""
    if os.path.exists(bg_image_path):
        with open(bg_image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        
        bg_css = f"""
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(252,251,249,0.96), rgba(252,251,249,0.96)), url('data:image/png;base64,{encoded}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        """
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@700;900&display=swap');
        
        {bg_css}
        
        #MainMenu {{visibility: hidden;}}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        * {{ font-family: 'Inter', sans-serif; }}
        h1, h2, h3, h4 {{ font-family: 'Playfair Display', serif !important; }}
        
        /* Trust Bar */
        .trust-bar {{
            display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;
            padding: 15px 10px; border-top: 1px solid #EAEAEA; border-bottom: 1px solid #EAEAEA;
            background-color: rgba(255,255,255,0.6); margin-bottom: 3rem;
            font-size: 0.9rem; color: #1E392A; font-weight: 600; text-align: center;
        }}
        
        /* Product Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 16px !important; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04) !important;
            border: 1px solid rgba(0,0,0,0.03) !important; background-color: rgba(255, 255, 255, 0.95);
            transition: all 0.3s ease !important; overflow: hidden;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
            transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08) !important;
            border: 1px solid rgba(212, 175, 55, 0.3) !important;
        }}

        /* Buttons */
        .stButton > button {{
            border-radius: 8px !important; border: 1.5px solid #1E392A !important;
            color: #1E392A !important; background-color: transparent !important;
            font-weight: 700 !important; text-transform: uppercase; font-size: 0.9rem !important;
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{ background-color: #1E392A !important; color: white !important; }}
        
        /* Cart +/- Buttons (Specific targeting) */
        .qty-btn .stButton > button {{
            padding: 0 !important; font-size: 1.2rem !important; border: none !important;
            background-color: #F0F4F1 !important; color: #1E392A !important; border-radius: 50% !important;
            width: 32px !important; height: 32px !important; min-height: 32px !important;
        }}
        .qty-btn .stButton > button:hover {{ background-color: #1E392A !important; color: white !important; }}
        
        /* Badges */
        .badge {{
            display: inline-block; padding: 0.35em 0.85em; font-size: 0.7rem; font-weight: 700;
            border-radius: 4px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px;
        }}
        .badge-gold {{ background-color: #FAF4E8; color: #B8860B; border: 1px solid #E8D3A5; }}
        .badge-green {{ background-color: #E8F5E9; color: #2E7D32; border: 1px solid #C8E6C9; }}
        
        /* Footer */
        .footer-text {{
            text-align: center; color: #666; font-size: 0.85rem; line-height: 1.8;
            margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #DDD;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

apply_premium_styles(BG_IMAGE_FILE)

# --- 2. HERO SECTION & TRUST BAR ---
st.markdown("""
<div style="text-align: center; padding: 3rem 1rem 1.5rem 1rem;">
    <h1 style="font-size: clamp(3rem, 8vw, 5rem); color: #1E392A; font-weight: 900; margin-bottom: 0.2rem; line-height: 1.1;">
        <span style="font-size: clamp(2rem, 6vw, 3.5rem); vertical-align: middle;">🌴</span> Khajoorwala<sup style="font-size: clamp(0.8rem, 2vw, 1.2rem); font-family: 'Inter', sans-serif; font-weight: 700; color: #B8860B; letter-spacing: 1px; margin-left: 8px;">KATARIA'S</sup>
    </h1>
    <p style="font-size: clamp(1rem, 3vw, 1.2rem); color: #555; font-weight: 400; max-width: 600px; margin: 1rem auto 2rem auto; line-height: 1.6;">
        Nature's purest energy. Premium, hand-selected dates delivered fresh to your door in Malviya Nagar & South Delhi.
    </p>
</div>
<div class="trust-bar">
    <span>✨ Hand-Selected Quality</span>
    <span>✈️ Imported from Saudi Arabia</span>
    <span>🚫 100% No Preservatives</span>
</div>
""", unsafe_allow_html=True)


# Initialize shopping cart as a Dictionary to track quantities {product_id: quantity}
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- 3. PRODUCT CATALOG ---
products = [
    {
        "id": 1, "name": "The Marathon Date", "price": 40, "unit": "/ piece",
        "tag": "<span class='badge badge-gold'>🔥 Best Seller</span>",
        "desc": "Nature's Energy Gel. 1 Premium Pitted Date + Sea Salt.",
        "benefits": "🏃‍♂️ **Quick carbs** for instant natural energy.<br><br>🧂 **Sea Salt** replenishes lost electrolytes.<br><br>🚫 **No refined sugar** prevents post-run crashes.",
        "image_file": os.path.join(CURRENT_DIR, "marathon.jpg")
    },
    {
        "id": 2, "name": "Premium Ajwa Dates", "price": 850, "unit": "(500g)",
        "tag": "<span class='badge badge-green'>✈️ Imported</span>",
        "desc": "The 'Holy Date'. Authentic, rich, and deeply healing.",
        "benefits": "❤️ **Heart Health:** Rich in antioxidants and minerals.<br><br>💪 **Immunity:** Known historically for its deep healing properties.<br><br>🩸 **Iron Rich:** Excellent for maintaining healthy blood levels.",
        "image_file": os.path.join(CURRENT_DIR, "ajwa.jpg")
    },
    {
        "id": 3, "name": "Medjool Dates", "price": 950, "unit": "(500g)",
        "tag": "<span class='badge badge-green'>👑 Premium</span>",
        "desc": "The 'King of Dates'. Large, beautifully soft, and caramel-sweet.",
        "benefits": "🌾 **High Fiber:** Excellent for digestive health.<br><br>🔋 **Sustained Energy:** A low glycemic index food.<br><br>🦴 **Bone Health:** Contains potassium, magnesium, and copper.",
        "image_file": os.path.join(CURRENT_DIR, "medjool.jpg")
    }
]

st.markdown("<h2 style='color: #1E392A; text-align: center; margin-bottom: 2rem; font-size: 2.2rem;'>Select Your Fuel</h2>", unsafe_allow_html=True)
cols = st.columns(3, gap="large")

for index, product in enumerate(products):
    with cols[index]:
        with st.container(border=True):
            if os.path.exists(product["image_file"]):
                st.image(product["image_file"], use_container_width=True)
            else:
                st.markdown(
                    """
                    <div style="background-color: #F0F4F1; height: 250px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
                        <span style="color: #9EBAA8; font-size: 0.9rem;">📸 Product Image Missing</span>
                    </div>
                    """, unsafe_allow_html=True
                )
            
            st.markdown(product['tag'], unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: #1E392A; font-size: 1.6rem; margin: 0;'>{product['name']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: #666; height: 45px; font-size: 0.95rem; line-height: 1.4; margin-top: 5px;'>{product['desc']}</p>", unsafe_allow_html=True)
            
            with st.popover("Explore Health Benefits"):
                st.markdown(product['benefits'], unsafe_allow_html=True)
                
            st.markdown("<hr style='margin: 15px 0; border: none; border-top: 1px solid #EEE;'>", unsafe_allow_html=True)
            
            bottom_col1, bottom_col2 = st.columns([1, 1.2])
            with bottom_col1:
                st.markdown(f"""
                <div style="line-height: 1;">
                    <span style='color: #1E392A; font-family: "Playfair Display", serif; font-weight: 900; font-size: 1.5rem;'>₹{product['price']}</span><br>
                    <span style='color: #888; font-size: 0.8rem; font-weight: 600;'>{product['unit']}</span>
                </div>
                """, unsafe_allow_html=True)
            with bottom_col2:
                # Add to Cart updates the dictionary quantity
                if st.button("Add to Cart", key=f"add_{product['id']}", use_container_width=True):
                    pid = product['id']
                    if pid in st.session_state.cart:
                        st.session_state.cart[pid] += 1
                    else:
                        st.session_state.cart[pid] = 1
                    st.toast(f"✅ Added to cart! Scroll down to checkout.")

# --- 4. ADVANCED CHECKOUT & CART (MOBILE OPTIMIZED) ---
st.markdown("<hr style='margin: 4rem 0 2rem 0; border-top: 2px solid #EAEAEA;'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #1E392A; text-align: center; font-size: 2.2rem;'>🛒 Your Cart</h2>", unsafe_allow_html=True)

if not st.session_state.cart:
    st.markdown("<p style='text-align: center; color: #888; font-size: 1.1rem;'>Your cart is currently empty. Add some dates above to fuel up!</p>", unsafe_allow_html=True)
else:
    cart_col1, cart_col2, cart_col3 = st.columns([1, 2, 1])
    
    with cart_col2:
        st.markdown("<div style='background: white; padding: 25px; border-radius: 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border: 1px solid #EAEAEA; margin-bottom: 20px;'>", unsafe_allow_html=True)
        
        total_price = 0
        
        # Build the dynamic cart UI
        for pid, qty in list(st.session_state.cart.items()):
            # Find the product details from the ID
            prod = next((p for p in products if p['id'] == pid), None)
            if prod:
                item_total = prod['price'] * qty
                total_price += item_total
                
                # Visual Layout for each item row
                row_col1, row_col2, row_col3, row_col4, row_col5 = st.columns([4, 1, 1, 1, 2], vertical_alignment="center")
                
                with row_col1:
                    st.markdown(f"<span style='color: #444; font-size: 1.1rem; font-weight: 600;'>{prod['name']}</span>", unsafe_allow_html=True)
                
                with row_col2:
                    st.markdown('<div class="qty-btn">', unsafe_allow_html=True)
                    if st.button("➖", key=f"minus_{pid}"):
                        st.session_state.cart[pid] -= 1
                        if st.session_state.cart[pid] == 0:
                            del st.session_state.cart[pid]
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with row_col3:
                    st.markdown(f"<div style='text-align: center; font-weight: 700; font-size: 1.1rem; color: #1E392A;'>{qty}</div>", unsafe_allow_html=True)
                    
                with row_col4:
                    st.markdown('<div class="qty-btn">', unsafe_allow_html=True)
                    if st.button("➕", key=f"plus_{pid}"):
                        st.session_state.cart[pid] += 1
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                with row_col5:
                    st.markdown(f"<div style='text-align: right; color: #1E392A; font-weight: 700; font-size: 1.1rem;'>₹{item_total}</div>", unsafe_allow_html=True)
                
                st.markdown("<div style='border-bottom: 1px dashed #EEE; margin: 10px 0;'></div>", unsafe_allow_html=True)
        
        # Free Delivery Progress Bar (Gamification)
        FREE_DELIVERY_THRESHOLD = 1000
        if total_price < FREE_DELIVERY_THRESHOLD:
            amount_needed = FREE_DELIVERY_THRESHOLD - total_price
            progress = int((total_price / FREE_DELIVERY_THRESHOLD) * 100)
            st.markdown(f"<p style='text-align: center; color: #B8860B; font-weight: 600; font-size: 0.9rem; margin-bottom: 5px;'>Add ₹{amount_needed} more to unlock FREE Delivery!</p>", unsafe_allow_html=True)
            st.progress(progress)
        else:
            st.markdown("<p style='text-align: center; color: #2E7D32; font-weight: 700; font-size: 1rem; margin-bottom: 5px;'>🎉 You have unlocked FREE Delivery!</p>", unsafe_allow_html=True)
            st.progress(100)

        # Total Amount
        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px; padding-top: 15px; border-top: 2px solid #1E392A;">
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.5rem; color: #1E392A;">Total Amount</span>
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.8rem; color: #B8860B;">₹{total_price}</span>
            </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Pincode Checker
        st.markdown("<p style='color: #1E392A; font-weight: 700; margin-bottom: 5px;'>📍 Delivery Check</p>", unsafe_allow_html=True)
        pincode = st.text_input("Enter your Pincode", placeholder="e.g. 110017", label_visibility="collapsed")
        if pincode:
            if pincode.strip() == "110017":
                st.success("✅ Free Local Delivery in Malviya Nagar!")
            elif pincode.strip().startswith("1100"):
                st.info("✅ We deliver to your area! Standard fees apply.")
            else:
                st.warning("Delivery currently restricted to South Delhi.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Professional WhatsApp Checkout Message Generation
        seller_phone = "919210191930" 
        
        receipt_lines = []
        for pid, qty in st.session_state.cart.items():
            prod = next((p for p in products if p['id'] == pid), None)
            if prod:
                receipt_lines.append(f"▪️ {qty}x {prod['name']} (₹{prod['price'] * qty})")
        order_details = "\n".join(receipt_lines)
        
        message = f"🌴 *New Order for Khajoorwala Kataria's*\n\nHi! I would like to place an order:\n\n{order_details}\n\n*Total: ₹{total_price}*\n\nPlease confirm my order and share payment details!"
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{seller_phone}?text={encoded_message}"
        
        st.markdown(
            f"""
            <a href="{whatsapp_url}" target="_blank" style="
                background-color: #1E392A; color: white; padding: 18px 20px; border-radius: 12px;
                text-decoration: none; display: block; width: 100%; text-align: center;
                font-size: 1.2rem; font-weight: 700; text-transform: uppercase;
                box-shadow: 0 8px 25px rgba(30, 57, 42, 0.3); transition: all 0.3s ease;
            ">
            Secure Checkout via WhatsApp 📲
            </a>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

# --- 5. BRAND STORY & REVIEWS ---
st.markdown("<hr style='margin: 4rem 0 3rem 0; border-top: 1px solid #EAEAEA;'>", unsafe_allow_html=True)
story_col, review_col = st.columns([1, 1.2], gap="large")

with story_col:
    st.markdown("<h2 style='color: #1E392A;'>The Kataria Story</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="color: #555; font-size: 1.05rem; line-height: 1.7;">
    What started as a search for pure, unrefined energy for our own morning runs turned into a passion for sourcing the finest dates in the world. 
    <br><br>
    At Khajoorwala Kataria's, we believe in honest food. We hand-pack every box right here in South Delhi, ensuring that whether you are breaking your fast, gifting a loved one, or fueling a marathon, you are getting nature's absolute best.
    </p>
    """, unsafe_allow_html=True)

with review_col:
    st.markdown("<h2 style='color: #1E392A;'>South Delhi Speaks</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #B8860B; margin-bottom: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
        <p style="margin: 0; font-style: italic; color: #444;">"The Marathon Dates are a game changer for my weekend cycling trips. Completely natural energy without the sugar crash."</p>
        <p style="margin: 5px 0 0 0; font-size: 0.8rem; color: #888; font-weight: 600;">— Rahul S., Hauz Khas</p>
    </div>
    <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #1E392A; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
        <p style="margin: 0; font-style: italic; color: #444;">"The Ajwa dates are incredibly fresh. So much better than what sits on supermarket shelves for months."</p>
        <p style="margin: 5px 0 0 0; font-size: 0.8rem; color: #888; font-weight: 600;">— Priya M., Malviya Nagar</p>
    </div>
    """, unsafe_allow_html=True)


# --- 6. PROFESSIONAL FOOTER ---
st.markdown("""
<div class="footer-text">
    <strong>Khajoorwala Kataria's</strong><br>
    Premium Hand-Selected Dates | Malviya Nagar, New Delhi, 110017<br>
    WhatsApp Support: +91 92101 91930 <br>
    FSSAI Lic No: [Add Your License Here] <br><br>
    <em>Freshness guaranteed. Delivered daily across South Delhi.</em>
</div>
""", unsafe_allow_html=True)
