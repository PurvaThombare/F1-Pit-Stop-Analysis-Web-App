import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_pit_stop_comparison(df, year):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))

    df["label"] = df["team_name"] + " - " + df["surname"]
    df = df.sort_values(["team_name", "surname"])
    unique_labels = df["label"].unique()

    palette = {}
    color_list = []

    for i in range(0, len(unique_labels), 2):
        label1 = unique_labels[i]
        label2 = unique_labels[i + 1] if i + 1 < len(unique_labels) else None
        palette[label1] = "black"
        color_list.append((label1, "black"))
        if label2:
            palette[label2] = "red"
            color_list.append((label2, "red"))

    sns.barplot(
        data=df,
        x="team_name",
        y="duration",
        hue="label",
        palette=palette
    )

    plt.title(f"Average Pit Stop Duration ({year}) – Team vs Teammate")
    plt.xlabel("Team")
    plt.ylabel("Average Pit Stop Duration (seconds)")
    plt.xticks(rotation=45)
    plt.legend([], [], frameon=False)  # Hide legend
    plt.tight_layout()

    plot_path = f"plots/pitstop_{year}.png"
    plt.savefig(plot_path)
    plt.close()
    return f"/plot/pitstop_{year}.png", color_list