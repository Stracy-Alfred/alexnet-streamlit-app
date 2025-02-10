import streamlit as st

# Title of the web app
st.title("🚀 AlexNet: The Game-Changer in Deep Learning")

# Introduction
st.header("🌟 What is AlexNet?")
st.write("""
AlexNet is a **convolutional neural network (CNN)** that revolutionized the field of computer vision. 
It was designed by **Alex Krizhevsky**, **Ilya Sutskever**, and **Geoffrey Hinton** and won the **ImageNet Large Scale Visual Recognition Challenge (ILSVRC)** in 2012.
AlexNet's success marked the beginning of the **deep learning boom** and inspired many modern AI models.
""")

# Add an image of AlexNet
st.image("https://miro.medium.com/v2/resize:fit:1400/1*qyc21qM0oxWEuRaj-XJKcw.png", caption="AlexNet Architecture", use_column_width=True)

# Why AlexNet is Important
st.header("💡 Why is AlexNet Important?")
st.write("""
- **Won the ImageNet Challenge**: AlexNet reduced the error rate by a huge margin compared to traditional methods.
- **Popularized Deep Learning**: It showed the world the power of deep neural networks.
- **Introduced Key Techniques**: AlexNet used **ReLU activation**, **dropout**, and **data augmentation**, which are now standard in deep learning.
""")

# Architecture Explained Simply
st.header("🧠 AlexNet Architecture: Simplified")
st.write("""
AlexNet has **8 layers** in total: **5 convolutional layers** and **3 fully connected layers**. Here's a simple breakdown:
""")

# Display the architecture in a user-friendly way
st.subheader("1. Input Layer")
st.write("""
- Takes an image of size **227x227 pixels** (RGB color).
""")

st.subheader("2. Convolutional Layers")
st.write("""
- **Conv1**: Extracts basic features like edges and textures using 96 filters.
- **Conv2**: Extracts more complex patterns using 256 filters.
- **Conv3**, **Conv4**, **Conv5**: Extract high-level features like shapes and objects.
""")

st.subheader("3. Pooling Layers")
st.write("""
- Reduces the size of the image while keeping the important features.
- Uses **max pooling** with a 3x3 window.
""")

st.subheader("4. Fully Connected Layers")
st.write("""
- **FC6 & FC7**: Combine all the features to understand the image.
- **FC8**: Outputs the final prediction (e.g., "cat" or "dog").
""")

# Interactive Section
st.header("🎯 Fun Fact!")
st.write("""
Did you know? AlexNet was trained on **1.2 million images** from the ImageNet dataset! That's like looking at a photo every second for **14 days straight**! 😲
""")

# Add a checkbox to show more details
if st.checkbox("🤓 Show Technical Details"):
    st.write("""
    - **ReLU Activation**: Makes training faster by avoiding vanishing gradients.
    - **Dropout**: Prevents overfitting by randomly turning off neurons during training.
    - **Local Response Normalization (LRN)**: Helps improve generalization.
    """)

# Impact and Legacy
st.header("🌍 Impact and Legacy")
st.write("""
AlexNet's success in 2012 sparked a **deep learning revolution**. It inspired researchers to build even better models like **VGG**, **ResNet**, and **EfficientNet**.
Today, AlexNet is considered a **landmark in AI history** and is still studied by students and researchers worldwide.
""")

# Conclusion
st.header("🎉 Conclusion")
st.write("""
AlexNet is more than just a neural network—it's a **pioneer** that changed the way we think about AI. 
Whether you're a beginner or an expert, understanding AlexNet is a great way to dive into the world of deep learning!
""")

# Footer
st.write("""
**References**:
- [AlexNet Paper](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
- [ImageNet Challenge](https://www.image-net.org/)
""")
