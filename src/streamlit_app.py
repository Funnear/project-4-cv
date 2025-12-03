import os
import numpy as np
from PIL import Image

import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# -----------------------------
# Paths & constants
# -----------------------------
DATASET_ROOT = "../data/images"  # assuming app is in project root
MODEL_PATH = "../notebooks/best_mobilenetv2.h5"
IMG_SIZE = (224, 224)

# -----------------------------
# Class names (same order as training)
# -----------------------------
def load_class_names(dataset_root: str):
    classes = [
        d for d in sorted(os.listdir(dataset_root))
        if os.path.isdir(os.path.join(dataset_root, d)) and not d.startswith(".")
    ]
    return classes

CLASS_NAMES = load_class_names(DATASET_ROOT)


# -----------------------------
# Recycling advice per class
# -----------------------------
RECYCLING_INFO = {
    "aerosol_cans": ("Metal", "Often recyclable if empty and non-hazardous. Check local rules."),
    "aluminum_food_cans": ("Metal", "Typically recyclable after rinsing."),
    "aluminum_soda_cans": ("Metal", "Widely recyclable; one of the easiest streams."),
    "cardboard_boxes": ("Paper/Cardboard", "Usually recyclable if clean and flattened."),
    "cardboard_packaging": ("Paper/Cardboard", "Recyclable when free from food contamination."),
    "clothing": ("Textiles", "Textile recycling or donation is preferred; not regular bin."),
    "coffee_grounds": ("Organic", "Best suited for organic/compost waste."),
    "disposable_plastic_cutlery": ("Plastic", "Often not recyclable in household streams."),
    "eggshells": ("Organic", "Compost/organic bin where available."),
    "food_waste": ("Organic", "Belongs to organic/biowaste, not recyclables."),
    "glass_beverage_bottles": ("Glass", "Typically recyclable in glass containers."),
    "glass_cosmetic_containers": ("Glass", "Rinse and follow local glass recycling rules."),
    "glass_food_jars": ("Glass", "Recyclable after rinsing and removing lids."),
    "magazines": ("Paper", "Often recyclable; remove plastic wrap."),
    "newspaper": ("Paper", "Highly recyclable paper stream."),
    "office_paper": ("Paper", "Standard recyclable office paper."),
    "paper_cups": ("Paper/Composite", "Can be restricted; many places treat as general waste."),
    "plastic_cup_lids": ("Plastic", "Sometimes recyclable; check local plastic rules."),
    "plastic_detergent_bottles": ("Plastic", "Commonly recyclable when empty and rinsed."),
    "plastic_food_containers": ("Plastic", "Often recyclable if clean and labelled."),
    "plastic_shopping_bags": ("Plastic film", "Return-to-store collection preferred."),
    "plastic_soda_bottles": ("Plastic (PET)", "Widely recyclable; high-value stream."),
    "plastic_straws": ("Plastic", "Usually not recyclable; general waste."),
    "plastic_trash_bags": ("Plastic", "Not recyclable once used; general waste."),
    "plastic_water_bottles": ("Plastic (PET)", "Widely recyclable; empty and cap on."),
    "shoes": ("Textiles/Composite", "Best sent to textile or reuse collections."),
    "steel_food_cans": ("Metal", "Recyclable after rinsing."),
    "styrofoam_cups": ("Foam/Styrofoam", "Rarely recyclable; general waste."),
    "styrofoam_food_containers": ("Foam/Styrofoam", "Usually general waste due to contamination."),
    "tea_bags": ("Organic/Composite", "Often suitable for organic waste; staples may need removal."),
}


def get_recycling_advice(class_name: str) -> str:
    material, note = RECYCLING_INFO.get(
        class_name,
        ("Unknown", "No specific guidance available; follow local recycling instructions."),
    )
    return f"Material: {material}. {note}"


# -----------------------------
# Load model (cached)
# -----------------------------
@st.cache_resource
def load_model(path: str):
    model = tf.keras.models.load_model(path)
    return model


model = load_model(MODEL_PATH)


# -----------------------------
# Preprocess image for model
# -----------------------------
def preprocess_image(image: Image.Image):
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)
    arr = np.array(image).astype("float32")
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)
    return arr


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Waste Classification Demo", layout="centered")

st.title("Waste Image Classifier — MobileNetV2 Demo")
st.write(
    "Upload an image of a waste item and the model will predict the most likely category "
    "and provide a short recycling-oriented interpretation."
)

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)

    if st.button("Classify image"):
        with st.spinner("Analyzing image..."):
            x = preprocess_image(image)
            preds = model.predict(x)[0]

        # Top-3 predictions
        top_indices = preds.argsort()[-3:][::-1]
        st.subheader("Top predictions")
        for rank, idx in enumerate(top_indices, start=1):
            class_name = CLASS_NAMES[idx]
            prob = float(preds[idx])
            st.write(f"{rank}. **{class_name}** — {prob:0.2%}")

        # Domain-specific interpretation for top class
        best_idx = top_indices[0]
        best_class = CLASS_NAMES[best_idx]
        st.markdown("---")
        st.subheader("Recycling context for top prediction")
        st.write(f"Predicted class: **{best_class}**")
        st.write(get_recycling_advice(best_class))
else:
    st.info("Upload a PNG or JPEG file to get a prediction.")