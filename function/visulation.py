import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

LABEL_MAP = {
    8: "Command Injection",
    9: "SQL Injection",
    5: "XSS",
    0: "Normal",
    -1: "Undefined"
}


def create_bar_graph(df):
    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)

    df = df.copy()
    df["label_name"] = df["predicted_label"].map(LABEL_MAP)
    order = df["label_name"].value_counts().index

    sns.countplot(
        data=df,
        x="label_name",
        hue="label_name", 
        order=order,
        palette="viridis",
        legend=False,
        ax=ax
    )

    ax.set_title("Frequency of Security Events")
    ax.set_xlabel("Attack Type")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=30)

    return fig


def create_pie_chart(df):
    fig = Figure(figsize=(6, 5))
    ax = fig.add_subplot(111)

    df = df.copy()
    df["label_name"] = df["predicted_label"].map(LABEL_MAP)
    counts = df["label_name"].value_counts()

    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140
    )

    ax.set_title("Attack Distribution")
    return fig


def create_heatmap(df):
    fig = Figure(figsize=(8, 5))
    ax = fig.add_subplot(111)

    numeric_df = df.select_dtypes(include=["int64", "float64"])
    corr = numeric_df.corr()

    sns.heatmap(
        corr,
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Correlation Heatmap")
    return fig
