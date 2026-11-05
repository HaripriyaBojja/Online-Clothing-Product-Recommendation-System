# Online Clothing Product Recommendation System

## 1. Introduction

### Why Do We Need This Project?

Online shopping platforms offer thousands of clothing products from different brands, categories, colours, and price ranges. With so many choices available, customers may find it difficult and time-consuming to identify products that match their preferences.

A product recommendation system helps solve this problem by suggesting similar products based on the characteristics of a product selected by the user.

This project, **Online Clothing Product Recommendation System**, is designed to simplify the product discovery process by recommending clothing items that are similar to the selected product. It analyzes product information such as brand, gender, price range, colour, and description to identify relevant recommendations.

The system uses Natural Language Processing (NLP) techniques, particularly TF-IDF Vectorization and Cosine Similarity, to calculate the similarity between products.

## 2. Advantages of the Project

- **Personalized Product Discovery:** Helps users discover products similar to their selected clothing item.
- **Saves Time:** Reduces the effort required to search through a large collection of clothing products.
- **Content-Based Recommendations:** Recommends products based on their attributes rather than depending on other users' purchasing history.
- **Multiple Product Attributes:** Considers brand, gender, price range, colour, and product description when identifying similar products.
- **Adjustable Recommendations:** Allows users to select the number of similar products they want to see.
- **Simple User Interface:** Provides an interactive interface through Streamlit without requiring complex navigation.
- **Efficient Similarity Calculation:** Uses TF-IDF and Cosine Similarity to identify products with similar characteristics.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Dataset loading and data preprocessing |
| Scikit-learn | TF-IDF Vectorization and Cosine Similarity |
| TF-IDF | Converts product text information into numerical vectors |
| Cosine Similarity | Measures similarity between product vectors |

## 4. How the System Works

The recommendation system follows these steps:

1. **Dataset Loading:** Loads clothing product information from `fashion_products.csv` using Pandas.
2. **Data Preprocessing:** Normalizes column names and handles missing values in the required product attributes.
3. **Price Categorization:** Groups products into three price ranges:
   - Low: Below ₹500
   - Medium: ₹500 to below ₹1,500
   - High: ₹1,500 and above
4. **Feature Combination:** Combines product name, brand, gender, price category, primary colour, and description into a single text feature.
5. **TF-IDF Vectorization:** Converts the combined textual information into numerical vectors using `TfidfVectorizer`.
6. **Similarity Calculation:** Applies Cosine Similarity to calculate similarity scores between products.
7. **Product Selection:** Allows users to select a clothing product from the available product list.
8. **Recommendation Generation:** Identifies and displays the most similar products based on their similarity scores.

## 5. Project Structure

```text
Online-Clothing-Product-Recommendation/
│
├── app.py
├── fashion_products.csv
├── requirements.txt
└── README.md
```

**File descriptions:**

- `app.py` – Contains the main application, data preprocessing, recommendation logic, and Streamlit interface.
- `fashion_products.csv` – Dataset containing clothing product information.
- `requirements.txt` – Contains the Python dependencies required to run the project.
- `README.md` – Provides project documentation and execution instructions.

## 6. Dataset Requirements

The application expects a CSV dataset named:

```text
fashion_products.csv
```

The dataset should be placed in the same directory as `app.py`.

The CSV file must contain the following columns:

| Column | Description |
|---|---|
| ProductID | Unique product identifier |
| ProductName | Name of the clothing product |
| ProductBrand | Brand of the product |
| Gender | Target gender category |
| Price (INR) | Product price in Indian Rupees |
| NumImages | Number of product images |
| Description | Product description |
| PrimaryColor | Main colour of the product |

The application uses product name, brand, gender, price, description, and primary colour for its recommendation calculations.

## 7. Installation and Execution

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.9 or above
- pip (Python package manager)
- Visual Studio Code or any Python-supported IDE

### Step 1: Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Navigate to the project directory:

```bash
cd Online-Clothing-Product-Recommendation
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

**For Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**For Git Bash:**

```bash
source .venv/Scripts/activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

### Step 6: Access the Application

Once the application starts, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your web browser to access the Online Clothing Product Recommendation System.

## 8. How to Use the Application

1. Launch the application using Streamlit.
2. Select a clothing product from the dropdown list.
3. Choose the number of recommendations using the slider in the sidebar (3–15 products).
4. Click the **Show Similar Products** button.
5. View the recommended products along with their category, brand, price, description, and primary colour.

## 9. Recommendation Algorithm

This project uses a content-based filtering approach.

### TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF converts textual product information into numerical representations. It assigns importance to words based on their frequency within a product description and their occurrence across the dataset.

### Cosine Similarity

Cosine Similarity measures the similarity between two numerical vectors.

The similarity score ranges from 0 to 1 for the non-negative TF-IDF vectors used in this project. A higher score indicates greater similarity between two products.

The system ranks products based on their similarity scores and displays the highest-ranking products as recommendations.

## 10. Future Enhancements

- Display product images alongside recommendations.
- Introduce filters for brand, colour, gender, and price range.
- Improve recommendations using user preferences and interaction history.
- Integrate real-time product information from e-commerce platforms.
- Develop a more personalized recommendation experience.

---

**Note:** This project uses content-based filtering. Recommendations are generated from product attributes and descriptions, not from individual user purchase histories.