# Where's Waldo? 🔍

**Where's Waldo?** is a cutting-edge deep learning project aimed at simplifying the search for Waldo in the widely beloved children's book series. By leveraging Convolutional Neural Networks (CNNs) and YOLO (You Only Look Once), our model achieves efficient and precise detection of Waldo's location in various scenes.

## Demo Video

Watch our project in action and see the precision of our Waldo detection model:

[![Where's Waldo Demo](https://img.youtube.com/vi/7cTAlfzxZlw/0.jpg)](https://www.youtube.com/watch?v=7cTAlfzxZlw)

Additionally, experience our project firsthand through the interactive user interface:

- **User Interface App**: [https://wheres-waldo.streamlit.app/](https://wheres-waldo.streamlit.app/)

## Project Overview

The project starts with leveraging the **Hey-Waldo repository**, containing over 7,000 images classified into "Waldo" and "Not Waldo" categories. Through the integration of OpenCV and the YOLO object detection framework with CNNs, we have trained a neural network that surpasses mere image recognition. Our model is finely tuned to identify and locate Waldo with unmatched accuracy.

### Data Sources

- **Hey-Waldo GitHub Repository**: The backbone of our dataset, consisting of a comprehensive collection of images for model training and evaluation.

### Key Features

- **Object Detection with YOLO & CNNs**: Combining YOLO's efficiency with CNNs' powerful feature extraction for top-tier object detection.
- **TensorFlow Object Detection API**: Using TensorFlow to create a model that not only identifies but also precisely localizes Waldo within the image.

## Getting Started

Embark on your own **Where's Waldo?** journey by following these steps:

1. Clone the repository:
    #### git clone https://github.com/fabianbacher/wheres-waldo.git
    #### git clone https://github.com/fabianbacher/wheres-waldo-frontend
2. Install required dependencies:
    #### pip install -r requirements.txt

3. Review the documentation for detailed setup instructions and dataset preparation.

## Usage

With the setup complete, begin training the model with your dataset as outlined in our documentation. The project includes scripts for training and inference, allowing you to assess the model's detection capabilities on new images.

## Contributions

We welcome contributions! For improvements or bug fixes, please fork the repository and submit a pull request.

## Links & References

- [How to Find Wally with a Neural Network](https://towardsdatascience.com/how-to-find-wally-neural-network-eddbb20b0b90)
- [How To Label Where’s Wally/Waldo images using OpenCV and Deep Learning (YOLO v2)](https://fortes-arthur.medium.com/how-to-label-wheres-wally-waldo-images-using-opencv-and-deep-learning-yolo-v2-abba7150999f)
- [Where’s Waldo: Terminator Edition](https://hackernoon.com/wheres-waldo-terminator-edition-8b3bd0805741)
- [Here's Waldo: Computing the optimal search strategy for finding Waldo](https://randalolson.com/2015/02/03/heres-waldo-computing-the-optimal-search-strategy-for-finding-waldo/)

## Acknowledgments

A heartfelt thanks to everyone who has contributed to and supported the **Where's Waldo?** project. Your enthusiasm and contributions have been invaluable.

