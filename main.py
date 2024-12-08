from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# List of your 50 friends' names
friends_names = [
               "Asif", "Masum", "Darda", "Taslima", "Ayshi",
            "Maruf", "Rakib", "Hasan", "Robi", "Nafiz",
            "Disha", "Luna", "Sani", "Dulal", "Shuvo",
            "Sadia", "Mimtanna", "Galib", "Priya", "Arshi",
            "Aronna", "Saad", "Sayem", "Onthy", "Basher", "Anik"

]

# Combine names into a single string
text = " ".join(friends_names)

# Load the shape image of "ABIR"
mask = np.array(Image.open("ABIR.png"))

# Create the word cloud
wordcloud = WordCloud(
    background_color="black",  # Background color
    mask=mask,
    contour_width=2,
    contour_color="white",
    colormap="plasma"  # Gradient color map
).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Save the word cloud as an image
wordcloud.to_file("abir_wordcloud.png")
