import streamlit as st
from openai import OpenAI

# Configure unified system browser layouts
st.set_page_config(
    page_title="LocalSEO AI Engine",
    page_icon="📍",
    layout="wide"
)

# Custom High-End Dark Enterprise Styling Matrix
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(46,160,67,0.3);
    }
    </style>
""", unsafe_allowed_html=True)

# Main Structural Sidebar Configurator
st.sidebar.title("⚙️ System Control Panel")
st.sidebar.markdown("---")
api_key_input = st.sidebar.text_input("Enter OpenAI API Key", type="password", help="Powers the underlying natural language model layers.")
selected_model = st.sidebar.selectbox("AI Processing Brain", ["gpt-4o-mini", "gpt-4o"])

st.sidebar.markdown("""
### 💰 Commercial Valuation Profile:
- **Resell Ready**: Ready to be white-labeled under independent corporate branding.
- **Zero Fixed Overhead**: Operating architecture scales free via local API token mapping.
- **Deployment Status**: Production-stable script structure.
""")

# Interface Header Framework
st.title("📍 LocalSEO AI & Review Responder Suite")
st.markdown("Automate local business authority optimization. Instantly draft strategic customer crisis responses and generate hyper-local geographic content pipelines.")

# Tabular Interface Separation
tab1, tab2 = st.tabs(["💬 Reputation Management Engine", "✍️ Geo-Targeted Blog Factory"])

with tab1:
    st.markdown('<div class="card">', unsafe_allowed_html=True)
    st.subheader("💡 Automated Reputation Success Manager")
    
    col1, col2 = st.columns(2)
    with col1:
        biz_name = st.text_input("Business / Client Name", placeholder="e.g., Main Street Automotive")
        biz_type = st.text_input("Business Operational Niche", placeholder="e.g., Independent Auto Repair Shop")
    with col2:
        star_rating = st.selectbox("Observed Review Star Rating", ["⭐️ (1 Star - Critical Customer Grievance)", "⭐️⭐️⭐️⭐️⭐️ (5 Star - Positive Review)"])
        
    customer_review = st.text_area("Raw Review Feedback Copy", placeholder="Paste the feedback text retrieved from Google Maps or Yelp platforms here...")
    
    submit_review = st.button("Execute Strategic Response Generation")
    st.markdown('</div>', unsafe_allowed_html=True)
    
    if submit_review:
        if not api_key_input:
            st.error("⚠️ System Incomplete: An OpenAI API key must be inserted into the sidebar to authenticate server calls.")
        elif not customer_review or not biz_name:
            st.error("⚠️ Missing Context: Please ensure all business parameter entry forms are populated.")
        else:
            with st.spinner("Processing deep contextual language response loops..."):
                try:
                    client = OpenAI(api_key=api_key_input)
                    system_prompt = (
                        "You are an elite Public Relations Director specializing in brand management "
                        "and local enterprise customer satisfaction pipelines."
                    )
                    user_prompt = f"Draft a context-aware strategic public response for this local business review framework:\nBusiness Profile: {biz_name} ({biz_type})\nRating Scale: {star_rating}\nFeedback Context: {customer_review}\n\nOperational Protocols:\nIf review context matches a low score (1 star): Be deeply professional and empathetic. Apologize for the inconvenience caused without legally assuming liability. Provide a generic offline resolution pathway (e.g., support@business.com) to neutralize the visibility of the problem.\nIf review context matches a high score (5 stars): Be exceptionally appreciative. Enthusiastically thank the patron by name if available, and seamlessly embed one of the core service offerings back into the copy to boost local map-pack keyword density."
                    
                    response = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=0.7
                    )
                    
                    output_text = response.choices.message.content
                    st.success("✅ Reputation Mitigation Strategy Complete!")
                    st.info(output_text)
                    st.download_button("Download Response Script (.txt)", output_text, file_name="local_review_response.txt")
                except Exception as e:
                    st.error(f"Processing Deficit Encountered: {str(e)}")

with tab2:
    st.markdown('<div class="card">', unsafe_allowed_html=True)
    st.subheader("🚀 Hyper-Local Search Engine Optimization Factory")
    
    col3, col4 = st.columns(2)
    with col3:
        target_city = st.text_input("Target Geographic City / Municipality", placeholder="e.g., Ellesmere Port, UK")
    with col4:
        target_keyword = st.text_input("Core High-Value Commercial Intent Keyword", placeholder="e.g., Emergency Brake Replacement")
        
    submit_seo = st.button("Synthesize Location-Optimized Article Architecture")
    st.markdown('</div>', unsafe_allowed_html=True)
    
    if submit_seo:
        if not api_key_input:
            st.error("⚠️ System Incomplete: An OpenAI API key must be inserted into the sidebar to authenticate server calls.")
        elif not target_city or not target_keyword:
            st.error("⚠️ Information Gap: Map-pack tracking generation requires definite location inputs.")
        else:
            with st.spinner("Assembling keyword density models..."):
                try:
                    client = OpenAI(api_key=api_key_input)
                    seo_system_prompt = "You are a master local search engine optimization strategist specializing in geo-targeted visibility patterns."
                    seo_user_prompt = f"Generate a fully structured local landing page copy layout built to convert localized query traffic.\nTarget Location: {target_city}\nTarget Commercial Keyword: {target_keyword}\n\nStructural Architecture Constraints:\n- Formulate an unmissable H1 Headline naturally containing both the exact keyword and city target.\n- Develop an engaging opening narrative focusing directly on localized consumer problems.\n- Build a structured 3-point value analysis demonstrating explicit mechanical or operational superiority.\n- Ensure natural geographic keyword density without triggers that flag search engine crawlers.\n- Provide a highly direct transactional Call to Action (CTA) block."
                    
                    response = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": "system", "content": seo_system_prompt},
                            {"role": "user", "content": seo_user_prompt}
                        ],
                        temperature=0.6
                    )
                    
                    seo_output = response.choices.message.content
                    st.success("✅ Local SEO Strategy Framework Generated!")
                    st.markdown(seo_output)
                    st.download_button("Export Deployment Markdown Asset (.md)", seo_output, file_name="local_seo_article.md")
                except Exception as e:
                    st.error(f"Processing Deficit Encountered: {str(e)}")
