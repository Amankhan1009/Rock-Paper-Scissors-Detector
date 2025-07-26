
import streamlit as st
from PIL import Image
from ultralytics import YOLO

# App title
st.title("Rock-Paper-Scissors Detector ✌️✊✋")

st.warning("⚠️ **Note:** The model is trained on real hand images and may not perform accurately on drawings, animations, or cartoon-style inputs. For best results, please use actual hand gesture photographs.")

# Load YOLOv8 detection model
# model_path = r'C:\Users\amank\Desktop\Data Science\Deep Learning\Rock Paper Scissor\best_model\runs\detect\train\weights\best.pt'  # replace with your actual trained model path

# Use relative path
model_path = "best_model/runs/detect/train/weights/best.pt"
model = YOLO(model_path)


# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display image preview
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Add Predict button
    if st.button("🔍 Predict"):
        # Run detection
        results = model(image)

        # Display detection result
        annotated_image = results[0].plot()
        st.image(annotated_image, caption="Detection Result", use_container_width=True)

        # Extract and display class info
        boxes = results[0].boxes
        if boxes:
            st.subheader("📋 Detected Classes")
            for box in boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                st.write(f"🧠 Class ID: {class_id}, 🔍 Confidence: {confidence:.2f}")
        else:
            st.warning("No objects detected.")
