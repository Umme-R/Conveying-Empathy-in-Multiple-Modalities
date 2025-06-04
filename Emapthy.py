import parselmouth as pm
import os
from parselmouth.praat import call
import pandas as pd

path = os.path.join(".", "Downloads", "4GZhL7OjNFM.wav")
# print(path)

sound = pm.Sound(path)


output_df = pd.DataFrame(columns=["Speech File", 
                                    "Min Pitch", "Max Pitch", "Mean Pitch", "Sd Pitch", 
                                    "Min Intensity", "Max Intensity", "Mean Intensity", "Sd Intensity", 
                                    "Jitter", "Shimmer", "HNR"])

# PITCH
pitch = call(sound, "To Pitch", 0.0, 75.0, 600.0)
min_pitch = call(pitch, "Get minimum", 0.0, 0.0, "Hertz", "Parabolic")
#print("minimum pitch: ", min_pitch)
max_pitch = call(pitch, "Get maximum", 0.0, 0.0, "Hertz", "Parabolic")
#print("maximum pitch: ", max_pitch)
mean_pitch = call(pitch, "Get mean", 0.0, 0.0, "Hertz")
#print("mean pitch: ", mean_pitch)
sd_pitch = call(pitch, "Get standard deviation", 0.0, 0.0, "Hertz")
#print("pitch standard deviation: ", sd_pitch)

# INTENSITY
intensity = call(sound, "To Intensity", 100.0, 0.0)
min_intensity = call(intensity, "Get minimum", 0.0, 0.0, "Parabolic")
#print("minimum intensity: ", min_intensity)
max_intensity = call(intensity, "Get maximum", 0.0, 0.0, "Parabolic")
#print("maximum intensity", max_intensity)
mean_intensity = call(intensity, "Get mean", 0.0, 0.0, "energy")
#print("mean intensity: ", mean_intensity)
sd_intensity = call(intensity, "Get standard deviation", 0.0, 0.0)
#print("intensity standard deviation: ", sd_intensity)

# JITTER, SHIMMER
point_process = call(sound, "To PointProcess (periodic, cc)", 75.0, 600.0)
jitter = call(point_process, "Get jitter (local)", 0.0, 0.0, 0.0001, 0.02, 1.3)
#print("jitter: ", jitter)
shimmer = call([sound, point_process], "Get shimmer (local)", 0.0, 0.0, 0.0001, 0.02, 1.3, 1.6)
#print("shimmer: ", shimmer)

# HNR
harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
hnr = call(harmonicity, "Get mean", 0.0, 0.0)
#print("hnr: ", hnr)

output_df = output_df.append(pd.Series([min_pitch, max_pitch, mean_pitch, sd_pitch,
                                                    min_intensity, max_intensity, mean_intensity, sd_intensity,
                                                    jitter, shimmer, hnr],
                                                    index=output_df.columns), ignore_index=True)

print(output_df)