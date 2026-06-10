from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project = Path("Penguin Research Project")
data_folder = project / "data"
output_folder = project / "outputs"

#read the input file
input_csv = output_folder / "penguin_size_clean.csv"

#convert to dataframe
penguins_df = pd.read_csv(input_csv)

# species_df = penguins_df["species"].value_counts()


# #plt.figure
# #plt.hist(penguins_df["body_mass_g"], bins=5, color="pink", edgecolor="black")
# plt.title("Count for each penguin species: ")

# plt.xlabel("flipper length") # using for all js for lables
# # # plt.ylabel("# of penguin species")

# plt.ylabel("body mass") # this one too
# # plt.xticks(rotation=0)  # rotate all lables
# # plt.tight_layout()  # makes graph realize how much space it needs 
# # plt.savefig(output_folder / "hist_species_mass.png", dpi=300)  #

# # species_body_mass = penguins_df.groupby("species")["body_mass_g"].mean()
# # plt.show()

# #scatter plot
# # plt.scatter(Body, Flipper)

# plt.show()

# plt.scatter(penguins_df["flipper_length_mm"],penguins_df["body_mass_g"])
# plt.title("Flipper length vs. Body mass: ")
# plt.xticks(rotation=0)
# plt.grid(True, alpha=0.2)
# plt.tight_layout() 
# plt.savefig(output_folder / "scatter_flipper_mass.png", dpi=300)

#box plot
penguins_df.boxplot(column="body_mass_g", by="species")
plt.grid(False)
plt.show()

plt.title("Box plot for body mass organized by species: ")
plt.xlabel("Species")
plt.ylabel("body mass")
plt.xticks(rotation=0)
plt.grid(True, alpha=0.2)
plt.tight_layout() 
plt.savefig(output_folder / "box_species_body_mass", dpi=300)

#multi label graphs
# x - species
# y - both the length, depth of the penguins

#have a data frame for species and culme length

# cul_df = penguins_df["culmen_length_mm"]
# cul_depth_df = penguins_df["culmen_depth_mm"]
# spec_df = penguins_df["species"]
# cul_df.plot(kind="bar")
# plt.show()
stu = ["a", "b", "c", "d"]
x = [1, 2, 3, 4]
y = [4, 6, 8, 10]

plt.figure()
plt.bar(stu, x, label="First Exam scores", color="red")
plt.bar(stu, y, label="Second Exam Scores")
plt.xlables("Students")
plt.ylabel("Scores for both exams")
plt.legend()
plt.show()






