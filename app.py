import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------- STREAMLIT PAGE CONFIG -----------------

st.set_page_config(
    page_title="Clothing Product Recommender",
    layout="wide"
)

DATA_PATH = "fashion_products.csv"  


# ----------------- HELPER FUNCTIONS -----------------

def bucket_price(price):
    """Convert numeric price into a simple bucket label."""
    try:
        p = float(price)
    except Exception:
        return "price_unknown"

    if p < 500:
        return "price_low"
    elif p < 1500:
        return "price_medium"
    else:
        return "price_high"


@st.cache_data
def load_and_prepare_data(file_path: str):
    """
    Load Fashion Clothing Products Dataset and create combined_features.
    This is customized for columns:
    ProductID, ProductName, ProductBrand, Gender, Price (INR), NumImages, Description, PrimaryColor
    """
    df = pd.read_csv(file_path)

    # Normalize column names to lower case
    df.columns = [c.strip().lower() for c in df.columns]
    # Now should be:
    # productid, productname, productbrand, gender,
    # price (inr), numimages, description, primarycolor

    # Map your columns explicitly
    name_col = "productname"
    brand_col = "productbrand"
    price_col = "price (inr)"
    desc_col = "description"
    gender_col = "gender"
    color_col = "primarycolor"

    # Fill missing values
    used_cols = [name_col, brand_col, price_col, desc_col, gender_col, color_col]
    for c in used_cols:
        if c not in df.columns:
            raise ValueError(f"Expected column '{c}' not found in dataset.")
    df[used_cols] = df[used_cols].fillna("")

    # Create price bucket
    df["price_bucket"] = df[price_col].apply(bucket_price)

    # Create a single combined text feature for similarity
    df["combined_features"] = (
        df[name_col].astype(str) + " " +
        df[brand_col].astype(str) + " " +
        df[gender_col].astype(str) + " " +
        df["price_bucket"].astype(str) + " " +
        df[color_col].astype(str) + " " +
        df[desc_col].astype(str)
    )

    # For display purposes, treat Gender as a kind of "category"
    df["category"] = df[gender_col]

    # Standardize key column names for later use
    df.rename(
        columns={
            name_col: "product_name",
            brand_col: "brand",
            price_col: "price"
        },
        inplace=True,
    )

    return df


@st.cache_data
def build_similarity_matrix(text_series: pd.Series):
    """Build TF-IDF vectors & cosine similarity matrix from combined_features."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(text_series)
    similarity = cosine_similarity(tfidf_matrix)
    return similarity


def get_recommendations(product_name: str,
                        df: pd.DataFrame,
                        similarity_matrix,
                        top_n: int = 5) -> pd.DataFrame:
    """Given a product name, return top_n most similar products."""
    # Find index of the selected product
    matches = df[df["product_name"].str.lower() == product_name.lower()]
    if matches.empty:
        return pd.DataFrame()

    idx = matches.index[0]

    # Similarity scores for this product
    sim_scores = list(enumerate(similarity_matrix[idx]))
    # Sort by similarity score (highest first)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip first (itself), take next top_n
    sim_indices = [i for i, _ in sim_scores[1 : top_n + 1]]

    # Return selected columns
    return df.loc[
        sim_indices,
        ["product_name", "category", "brand", "price", "description", "primarycolor"]
    ]


# ----------------- MAIN APP -----------------

st.title("🛍️ Online Clothing Product Recommendation System")
st.write(
    "This app recommends similar clothing products based on brand, gender, color, "
    "price range and description using TF-IDF + cosine similarity."
)

with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("**Dataset file:** `fashion_products.csv`")
    st.write(
        "Required columns in the CSV:\n"
        "- ProductID\n"
        "- ProductName\n"
        "- ProductBrand\n"
        "- Gender\n"
        "- Price (INR)\n"
        "- NumImages\n"
        "- Description\n"
        "- PrimaryColor\n"
    )
    top_n = st.slider("Number of recommendations", min_value=3, max_value=15, value=5, step=1)

# Load dataset
try:
    df = load_and_prepare_data(DATA_PATH)
    st.sidebar.success(f"✅ Loaded {len(df)} products")
except Exception as e:
    st.error(f"❌ Could not load dataset: {e}")
    st.stop()

# Build similarity matrix once
similarity_matrix = build_similarity_matrix(df["combined_features"])

# Product selection
product_names = sorted(df["product_name"].unique())
selected_product = st.selectbox("Choose a product", product_names)

if st.button("🔍 Show Similar Products"):
    with st.spinner("Finding similar products..."):
        recommendations = get_recommendations(
            selected_product, df, similarity_matrix, top_n=top_n
        )

    if recommendations.empty:
        st.warning("No similar products found.")
    else:
        st.subheader(f"Products similar to: **{selected_product}**")
        st.dataframe(recommendations.reset_index(drop=True), use_container_width=True)
