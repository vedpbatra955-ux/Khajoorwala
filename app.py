import streamlit as st
import urllib.parse
import os
import base64

# --- FILE PATHS ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_IMAGE_FILE = os.path.join(CURRENT_DIR, "k2.png")
LOGO_FILE = os.path.join(CURRENT_DIR, "KHAJOORWALA.png")

# Page Config
st.set_page_config(page_title="Khajoorwala | Premium Dates in South Delhi", page_icon="🌴", layout="wide", initial_sidebar_state="collapsed")

# --- 1. ROYAL OASIS UI & MICRO-ANIMATIONS ---
def apply_premium_styles(bg_image_path):
    bg_css = ""
    if os.path.exists(bg_image_path):
        with open(bg_image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        
        bg_css = f"""
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(250,245,234,0.96), rgba(250,245,234,0.96)), url('data:image/png;base64,{encoded}');
            background-size: cover; background-position: center; background-repeat: no-repeat;
            background-attachment: fixed; background-color: #FAF5EA;
        }}
        """
    else:
        bg_css = """[data-testid="stAppViewContainer"] { background-color: #FAF5EA; }"""
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700;900&display=swap');
        
        {bg_css}
        
        #MainMenu {{visibility: hidden;}} header {{visibility: hidden;}} footer {{visibility: hidden;}}
        
        /* Smooth Fade-in Animation */
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .animate-fade {{ animation: fadeInUp 0.6s ease-out forwards; }}
        
        /* Typography */
        * {{ font-family: 'Inter', sans-serif; }}
        p, span, div {{ color: #2B2B2B; }}
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
            border-bottom: 1px solid rgba(184, 137, 43, 0.2); background-color: transparent; margin-bottom: 4rem;
            font-size: 0.95rem; color: #1F3D2B; font-weight: 600; text-align: center;
        }}
        
        /* Product Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 14px !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important;
            border: 1px solid rgba(31, 61, 43, 0.08) !important; background-color: #FFFFFF;
            transition: all 0.3s ease !important; overflow: hidden; padding: 15px;
            animation: fadeInUp 0.5s ease-out forwards;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
            transform: translateY(-6px); box-shadow: 0 15px 35px rgba(31, 61, 43, 0.1) !important;
            border: 1px solid rgba(184, 137, 43, 0.4) !important;
        }}

        /* Buttons (Fixed text color) */
        .stButton > button {{
            border-radius: 8px !important; border: none !important;
            background-color: #1F3D2B !important;
            transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(31,61,43,0.2);
        }}
        .stButton > button p, .stButton > button span, .stButton > button div {{
            color: #FFFFFF !important;
            font-weight: 700 !important; text-transform: uppercase; font-size: 0.9rem !important; letter-spacing: 0.5px;
        }}
        .stButton > button:hover {{ background-color: #B8892B !important; box-shadow: 0 6px 15px rgba(184, 137, 43, 0.3); }}
        
        /* Quantity Buttons (Fixed text color) */
        .qty-btn .stButton > button {{
            padding: 0 !important; border: none !important; box-shadow: none !important;
            background-color: #E8EBE9 !important; border-radius: 50% !important;
            width: 32px !important; height: 32px !important; min-height: 32px !important;
        }}
        .qty-btn .stButton > button p, .qty-btn .stButton > button span {{
            color: #1F3D2B !important; font-size: 1.2rem !important; text-transform: none;
        }}
        .qty-btn .stButton > button:hover {{ background-color: #1F3D2B !important; }}
        .qty-btn .stButton > button:hover p, .qty-btn .stButton > button:hover span {{ color: #FFFFFF !important; }}
        
        /* Badges */
        .badge {{
            display: inline-block; padding: 0.35em 0.85em; font-size: 0.7rem; font-weight: 700;
            border-radius: 4px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px;
        }}
        .badge-gold {{ background-color: #FDF8EE; color: #B8892B; border: 1px solid rgba(184,137,43,0.3); }}
        .badge-green {{ background-color: #E8ECE9; color: #1F3D2B; border: 1px solid rgba(31,61,43,0.2); }}
        .badge-brown {{ background-color: #F3EBE6; color: #4A2C1A; border: 1px solid rgba(74,44,26,0.2); }}
        
        /* Comparison Table */
        .compare-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }}
        .compare-table th {{ background-color: #1F3D2B; color: white; padding: 15px; text-align: left; font-family: 'Playfair Display', serif; font-size: 1.1rem; }}
        .compare-table td {{ padding: 15px; border-bottom: 1px solid #EAEAEA; font-size: 0.95rem; color: #444; min-width: 120px; }}
        .compare-table tr:last-child td {{ border-bottom: none; }}
        
        /* 4-Column Footer */
        .premium-footer {{ background-color: #1F3D2B; color: #FAF5EA; padding: 3rem 2rem; margin: 4rem -4rem -4rem -4rem; font-size: 0.9rem; }}
        .premium-footer p, .premium-footer a, .premium-footer span {{ color: #D1D8D3 !important; text-decoration: none; line-height: 1.8; font-size: 0.9rem; }}
        .premium-footer a:hover {{ color: #B8892B !important; text-decoration: underline; }}
        
        /* Mobile Scroll for table */
        .table-responsive {{ overflow-x: auto; -webkit-overflow-scrolling: touch; }}
        </style>
        """, unsafe_allow_html=True
    )

apply_premium_styles(BG_IMAGE_FILE)

# --- 2. ANNOUNCEMENT & HERO SECTION (WITH LOGO) ---
st.markdown("<div class='announcement-bar'>✨ Same-day delivery in Malviya Nagar for orders before 2 PM ✨</div>", unsafe_allow_html=True)

# Encode Logo for Header
logo_base64 = ""
if os.path.exists(LOGO_FILE):
    with open(LOGO_FILE, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()

if logo_base64:
    hero_title_html = f'<img src="data:image/png;base64,{logo_base64}" style="width: 100%; max-width: 450px; height: auto; margin: 0 auto; display: block; margin-bottom: 15px;" alt="Khajoorwala">'
else:
    hero_title_html = '<h1 style="font-size: clamp(3.5rem, 8vw, 5.5rem); font-weight: 900; margin-bottom: 0; line-height: 1.1;">Khajoorwala</h1>'

st.markdown(f"""
<div class="animate-fade" style="text-align: center; padding: 3rem 1rem 1.5rem 1rem;">
    {hero_title_html}
    <p style="font-size: clamp(1.1rem, 3vw, 1.3rem); color: #2B2B2B; font-weight: 400; max-width: 600px; margin: 1rem auto 2rem auto; line-height: 1.6;">
        Fresh from the farm to your South Delhi doorstep. Premium, hand-selected dates for pure, natural energy.
    </p>
</div>
<div class="trust-bar animate-fade">
    <span>🌿 Hand-Selected Quality</span>
    <span>🚫 No Preservatives</span>
    <span>🛵 Fast Local Delivery</span>
    <span>🔄 Easy Replacement</span>
</div>
""", unsafe_allow_html=True)


if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- 3. TRANSPARENT PRODUCT CATALOG (DYNAMIC GRID) ---
products = [
    {
        "id": 1, "name": "The Marathon Date", "price": 40, "unit": "1 piece", "price_per": "₹40 per piece",
        "tag": "<span class='badge badge-gold'>🔥 Best Seller</span>",
        "desc": "Nature's Energy Gel. 1 Premium Pitted Date + Sea Salt.",
        "image_file": os.path.join(CURRENT_DIR, "marathon.jpg")
    },
    {
        "id": 2, "name": "Premium Ajwa", "price": 850, "unit": "500g box", "price_per": "₹170 per 100g",
        "tag": "<span class='badge badge-green'>✈️ Imported</span>",
        "desc": "The 'Holy Date'. Authentic, rich, and deeply healing.",
        "image_file": os.path.join(CURRENT_DIR, "ajwa.jpg")
    },
    {
        "id": 3, "name": "Medjool Caramel", "price": 950, "unit": "500g box", "price_per": "₹190 per 100g",
        "tag": "<span class='badge badge-brown'>👑 Premium</span>",
        "desc": "The 'King of Dates'. Large, soft, and melt-in-your-mouth sweet.",
        "image_file": os.path.join(CURRENT_DIR, "medjool.jpg")
    },
    {
        "id": 4, "name": "Mazafati Dates", "price": 380, "unit": "500g box", "price_per": "₹76 per 100g",
        "tag": "<span class='badge badge-brown'>✨ Everyday Delight</span>",
        "desc": "Soft, dark, and naturally sweet with a melt-in-the-mouth texture.",
        "image_file": os.path.join(CURRENT_DIR, "MAZAFATi.jpg")
    },
    {
        "id": 5, "name": "Kimia Gold", "price": 420, "unit": "500g box", "price_per": "₹84 per 100g",
        "tag": "<span class='badge badge-gold'>🌟 Premium Quality</span>",
        "desc": "Premium melt-in-mouth dates, perfect for daily consumption.",
        "image_file": os.path.join(CURRENT_DIR, "KIMIA.jpg")
    }
]

# Dynamic Row Generation for unlimited products
for i in range(0, len(products), 3):
    cols = st.columns(3, gap="large")
    row_products = products[i:i+3]
    
    for j, product in enumerate(row_products):
        with cols[j]:
            with st.container(border=True):
                if os.path.exists(product["image_file"]):
                    st.image(product["image_file"], use_container_width=True)
                else:
                    st.markdown(
                        """<div style="background-color: #E8ECE9; height: 250px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
                            <span style="color: #1F3D2B; font-size: 0.9rem; font-weight: 600;">📸 Photo Placeholder</span>
                        </div>""", unsafe_allow_html=True
                    )
                
                st.markdown(product['tag'], unsafe_allow_html=True)
                st.markdown(f"<h3 style='font-size: 1.6rem; margin: 0;'>{product['name']}</h3>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style="margin-top: 4px; margin-bottom: 10px;">
                    <span style="color: #B8892B; font-size: 0.9rem;">★★★★★</span>
                    <span style="color: #2B2B2B; font-size: 0.75rem; margin-left: 5px; opacity: 0.8;">(Fresh batch packed this week)</span>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"<p style='height: 45px; font-size: 0.95rem; line-height: 1.4;'>{product['desc']}</p>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 15px 0; border: none; border-top: 1px solid rgba(31,61,43,0.1);'>", unsafe_allow_html=True)
                
                bottom_col1, bottom_col2 = st.columns([1, 1.2])
                with bottom_col1:
                    st.markdown(f"""
                    <div style="line-height: 1.2;">
                        <span style='font-family: "Playfair Display", serif; font-weight: 900; font-size: 1.5rem;'>₹{product['price']}</span><br>
                        <span style='font-size: 0.75rem; font-weight: 600; opacity: 0.8;'>{product['unit']}</span><br>
                        <span style='font-size: 0.7rem; color: #888;'>{product['price_per']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with bottom_col2:
                    if st.button("Add to Cart", key=f"add_{product['id']}", use_container_width=True):
                        pid = product['id']
                        st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
                        st.toast(f"✅ Added to cart! Scroll down to checkout.")

# --- 4. COMPARISON GUIDE ---
st.markdown("<hr style='margin: 4rem 0 3rem 0; border: none;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 1rem;' class='animate-fade'>Which Date is Right For You?</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="animate-fade table-responsive">
<table class="compare-table">
    <tr>
        <th>Feature</th>
        <th>The Marathon Date</th>
        <th>Premium Ajwa</th>
        <th>Medjool Caramel</th>
        <th>Mazafati</th>
        <th>Kimia Gold</th>
    </tr>
    <tr>
        <td><strong>Best For</strong></td>
        <td>Pre-workout fuel</td>
        <td>Heart health & daily immunity</td>
        <td>Gifting & sweet cravings</td>
        <td>Daily snacking</td>
        <td>Smoothies & desserts</td>
    </tr>
    <tr>
        <td><strong>Taste & Texture</strong></td>
        <td>Sweet & salty, firm chew</td>
        <td>Rich, dark, slightly dry</td>
        <td>Caramel-like, ultra soft</td>
        <td>Soft, dark, juicy</td>
        <td>Melt-in-mouth sweet</td>
    </tr>
    <tr>
        <td><strong>Size</strong></td>
        <td>Medium</td>
        <td>Small to Medium</td>
        <td>Large (Jumbo)</td>
        <td>Medium</td>
        <td>Medium</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)


# --- 5. SMART CHECKOUT (SLOTS, COUPONS & QR CODE) ---
st.markdown("<hr style='margin: 4rem 0 2rem 0; border: none;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 2.2rem;'>🛒 Your Cart</h2>", unsafe_allow_html=True)

if not st.session_state.cart:
    st.markdown("<p style='text-align: center; font-size: 1.1rem; opacity: 0.8;'>Your cart is currently empty.</p>", unsafe_allow_html=True)
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
                        if st.session_state.cart[pid] == 0: del st.session_state.cart[pid]
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
        
        # Coupon Logic
        coupon = st.text_input("Gift Card or Discount Code", placeholder="e.g. FIRST50")
        discount = 0
        if coupon.strip().upper() == "FIRST50":
            discount = 50
            st.success("✅ ₹50 Welcome Discount Applied!")
        elif coupon:
            st.error("Invalid code.")
            
        final_total = total_price - discount

        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px; padding-top: 15px; border-top: 2px solid #1F3D2B;">
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.5rem;">Final Amount</span>
                <span style="font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.8rem; color: #B8892B;">₹{final_total}</span>
            </div>
            <div style="text-align: center; margin-top: 10px; font-size: 0.85rem; font-weight: 600; opacity: 0.8;">
                🛡️ Payment Accepted: UPI, Cards, Cash on Delivery
            </div>
        """, unsafe_allow_html=True)
        
        # --- DYNAMIC UPI QR CODE SECTION ---
        merchant_upi_id = "9210191930@pthdfc" # Wired to the exact ID from your image
        merchant_name = "Khajoorwala"
        
        upi_link = f"upi://pay?pa={merchant_upi_id}&pn={urllib.parse.quote(merchant_name)}&am={final_total}&cu=INR"
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(upi_link)}"
        
        st.markdown(f"""
        <div style="background: rgba(31,61,43,0.03); padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0; border: 1px dashed rgba(31,61,43,0.2);">
            <p style="font-weight: 700; font-size: 1.1rem; color: #1F3D2B; margin-bottom: 15px;">Pay Instantly via UPI</p>
            <img src="{qr_api_url}" style="width: 180px; height: 180px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <p style="font-size: 0.85rem; color: #666; margin-top: 15px; font-weight: 600;">Scan with GPay, PhonePe, or Paytm</p>
            <p style="font-size: 0.75rem; color: #888; margin-top: 5px;">Amount: <strong>₹{final_total}</strong> will be auto-filled</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Delivery Slot Picker
        st.markdown("<p style='color: #1F3D2B; font-weight: 700; margin-bottom: 5px;'>🕒 Select Delivery Slot</p>", unsafe_allow_html=True)
        delivery_slot = st.selectbox("Preferred Time", ["Morning (9 AM - 12 PM)", "Afternoon (12 PM - 4 PM)", "Evening (4 PM - 8 PM)"], label_visibility="collapsed")
        
        # Close the white card box
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        seller_phone = "919210191930" 
        receipt_lines = [f"▪️ {qty}x {next(p['name'] for p in products if p['id'] == pid)} (₹{next(p['price'] for p in products if p['id'] == pid) * qty})" for pid, qty in st.session_state.cart.items()]
        order_details = "\n".join(receipt_lines)
        
        message = f"🌴 *New Order for Khajoorwala*\n\n{order_details}\n\n*Subtotal:* ₹{total_price}\n*Discount:* -₹{discount}\n*Total:* ₹{final_total}\n\n*Preferred Slot:* {delivery_slot}\n*Payment Status:* Scanned QR Code / Pay on Delivery\n\nPlease confirm my order! (If paid via QR, I will share the screenshot here)."
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
            <p style="text-align: center; margin-top: 15px; font-size: 0.85rem; color: #888;">Tap to send your order details directly to our team.</p>
            """, unsafe_allow_html=True
        )

# --- 6. WHY DATES & BRAND STORY ---
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
    st.markdown("<h2>Our Story</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.05rem; line-height: 1.7; opacity: 0.9;">
    What started as a search for pure, unrefined energy for our own morning runs turned into a passion for sourcing the finest dates in the world. <br><br>
    At Khajoorwala, we hand-pack every box right here in South Delhi. Whether you are breaking your fast, gifting a loved one, or fueling a marathon, you are getting nature's absolute best.
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

# --- 7. FAQ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 1.5rem;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)
with st.expander("How long do the dates stay fresh?"):
    st.write("Our dates are packed fresh weekly. When stored in a cool, dry place in their airtight container, they will easily stay fresh for 3 to 6 months. For longer storage, you can keep them in the refrigerator.")
with st.expander("What are the payment options?"):
    st.write("For ultimate trust and convenience, we accept UPI payments and Cash on Delivery (COD). You can easily scan the QR code at checkout to pay instantly.")
with st.expander("How long does delivery take?"):
    st.write("Orders placed before 2 PM are typically delivered the same day in Malviya Nagar. Surrounding South Delhi areas are delivered within 24 hours.")

# --- 8. 4-COLUMN FUNCTIONAL FOOTER (FIXED COLORS) ---
whatsapp_base = "https://wa.me/919210191930"

st.markdown(f"""
<div class="premium-footer">
    <div style="display: flex; flex-wrap: wrap; justify-content: space-around; max-width: 1200px; margin: 0 auto; gap: 30px;">
        <div style="flex: 1; min-width: 250px;">
            <h4 style="color: #B8892B !important; font-family: 'Inter', sans-serif !important; letter-spacing: 1px; text-transform: uppercase; font-size: 1.2rem; margin-bottom: 15px;">Khajoorwala</h4>
            <p>Premium, hand-selected dates sourced globally and packed fresh locally. Your ultimate source for natural energy.</p>
            <p>📍 Malviya Nagar, New Delhi, 110017</p>
        </div>
        <div style="flex: 1; min-width: 150px;">
            <h4 style="color: #B8892B !important; font-family: 'Inter', sans-serif !important; letter-spacing: 1px; text-transform: uppercase; font-size: 1.2rem; margin-bottom: 15px;">Shop</h4>
            <p style="margin-bottom: 8px;">The Marathon Date</p>
            <p style="margin-bottom: 8px;">Premium Ajwa</p>
            <p style="margin-bottom: 8px;">Medjool Caramel</p>
            <p><a href="{whatsapp_base}?text=Hi!%20I%20would%20like%20to%20inquire%20about%20Corporate%20Gifting%20and%20Custom%20Hampers." target="_blank">Corporate Gifting</a></p>
        </div>
        <div style="flex: 1; min-width: 150px;">
            <h4 style="color: #B8892B !important; font-family: 'Inter', sans-serif !important; letter-spacing: 1px; text-transform: uppercase; font-size: 1.2rem; margin-bottom: 15px;">Help</h4>
            <p><a href="{whatsapp_base}?text=Hi!%20I%20would%20like%20to%20track%20my%20recent%20order." target="_blank">Track Order</a></p>
            <p><a href="{whatsapp_base}?text=Hi!%20Could%20you%20share%20your%20shipping%20and%20delivery%20policy?" target="_blank">Shipping Policy</a></p>
            <p><a href="{whatsapp_base}?text=Hi!%20I%20have%20a%20question%20about%20refunds/returns." target="_blank">Refunds & Returns</a></p>
            <p><a href="{whatsapp_base}?text=Hi!%20I%20need%20dates%20in%20bulk.%20Can%20we%20discuss%20pricing?" target="_blank">Bulk Orders</a></p>
        </div>
        <div style="flex: 1; min-width: 200px;">
            <h4 style="color: #B8892B !important; font-family: 'Inter', sans-serif !important; letter-spacing: 1px; text-transform: uppercase; font-size: 1.2rem; margin-bottom: 15px;">Contact</h4>
            <p><a href="{whatsapp_base}" target="_blank">📱 WhatsApp: +91 92101 91930</a></p>
            <p><a href="mailto:hello@khajoorwala.in">✉️ hello@khajoorwala.in</a></p>
            <p style="margin-top: 15px;">🕒 Mon-Sat, 9 AM - 8 PM</p>
            <p style="margin-top: 5px; font-size: 0.8rem; color: #888 !important;">FSSAI Lic No: [Add License Here]</p>
        </div>
    </div>
    <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.8rem; color: #888 !important;">
        &copy; 2026 Khajoorwala. All rights reserved. 
    </div>
</div>
""", unsafe_allow_html=True)
