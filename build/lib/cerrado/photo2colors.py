from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.colors import rgb_to_hsv
import webcolors




def rgb_to_color_name(rgb_tuple):
    try:
        closest_color = webcolors.rgb_to_name(rgb_tuple)
        return closest_color
    except ValueError:
        return "Unknown"

def get_dominant_colors(image_path, num_colors=6):
    img = Image.open(image_path)
    
    img = img.convert("RGB")
    
    # Resize the image for faster processing (optional)
#     img = img.resize((100, 100))
    
    img_array = np.array(img)
    
    pixels = img_array.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=num_colors, random_state=0).fit(pixels)
    
    dominant_colors = kmeans.cluster_centers_
    
    # Convert dominant colors to integer values
    dominant_colors = dominant_colors.astype(int)
    
    # Count occurrences of each dominant color
    color_counts = Counter(tuple(color) for color in dominant_colors)
    
    # Sort the colors by frequency
    sorted_colors = sorted(color_counts, key=lambda x: color_counts[x], reverse=True)
    
    return sorted_colors



def rgb_to_hex(rgb_tuple):
    return "#{:02x}{:02x}{:02x}".format(*rgb_tuple)

