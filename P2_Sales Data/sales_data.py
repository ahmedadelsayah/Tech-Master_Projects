import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np
import pandas as pd


def load_data(path="sales_data.csv"):
    df = pd.read_csv(path, encoding="latin1")
    df.dropna(subset=["Sales", "Order Date"], inplace=True)
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    return df


df = load_data()

fig = plt.figure(figsize=(16, 9))
fig.patch.set_facecolor("beige")
fig.suptitle(
    "Ledger — Superstore Sales Dashboard",
    fontsize=18,
    fontweight="bold",
    color="steelblue",
    y=0.97,
)

gs = fig.add_gridspec(
    3,
    4,
    left=0.20,
    right=0.98,
    top=0.80,
    bottom=0.05,
    hspace=0.45,
    wspace=0.35,
)

ax_trend = fig.add_subplot(gs[0, 0:2])
ax_region = fig.add_subplot(gs[0, 2])
ax_ship = fig.add_subplot(gs[0, 3])

ax_cat = fig.add_subplot(gs[1, 0])
ax_seg = fig.add_subplot(gs[1, 1])
ax_subcat = fig.add_subplot(gs[1:3, 2:])

ax_states = fig.add_subplot(gs[2, 0:2])

all_axes = [
    ax_trend,
    ax_region,
    ax_ship,
    ax_cat,
    ax_seg,
    ax_subcat,
    ax_states,
]

years = ["All"] + [str(y) for y in np.sort(df["Year"].dropna().unique())]
regions = ["All"] + list(np.sort(df["Region"].unique()))
categories = ["All"] + list(np.sort(df["Category"].unique()))

ax_radio_year = fig.add_axes([0.02, 0.65, 0.12, 0.22], facecolor="white")
ax_radio_reg = fig.add_axes([0.02, 0.35, 0.12, 0.25], facecolor="white")
ax_radio_cat = fig.add_axes([0.02, 0.10, 0.12, 0.20], facecolor="white")

fig.text(0.02, 0.88, "YEAR", fontweight="bold", color="gray", fontsize=9)
fig.text(0.02, 0.61, "REGION", fontweight="bold", color="gray", fontsize=9)
fig.text(0.02, 0.31, "CATEGORY", fontweight="bold", color="gray", fontsize=9)

radio_year = RadioButtons(ax_radio_year, years, active=0)
radio_reg = RadioButtons(ax_radio_reg, regions, active=0)
radio_cat = RadioButtons(ax_radio_cat, categories, active=0)


def update(val=None):
    filtered_df = df.copy()

    sel_y = radio_year.value_selected
    sel_r = radio_reg.value_selected
    sel_c = radio_cat.value_selected

    mask = np.ones(len(filtered_df), dtype=bool)
    if sel_y != "All":
        mask &= filtered_df["Year"].values == int(sel_y)
    if sel_r != "All":
        mask &= filtered_df["Region"].values == sel_r
    if sel_c != "All":
        mask &= filtered_df["Category"].values == sel_c

    filtered_df = filtered_df[mask]

    for ax in all_axes:
        ax.clear()

    sales_arr = filtered_df["Sales"].values if not filtered_df.empty else np.array([0])
    profit_arr = (
        filtered_df["Profit"].values
        if "Profit" in filtered_df.columns and not filtered_df.empty
        else np.array([0])
    )
    quantity_arr = (
        filtered_df["Quantity"].values
        if "Quantity" in filtered_df.columns and not filtered_df.empty
        else np.array([0])
    )

    sales = np.sum(sales_arr)
    profit = np.sum(profit_arr)
    margin = np.where(sales > 0, (profit / sales) * 100, 0.0).item()
    orders = (
        filtered_df["Order ID"].nunique()
        if "Order ID" in filtered_df.columns
        else len(filtered_df)
    )
    avg_order = np.where(orders > 0, sales / orders, 0.0).item()
    units = np.sum(quantity_arr)

    kpis_text = f"SALES: ${sales:,.0f}   |   PROFIT: ${profit:,.0f}   |   MARGIN: {margin:.1f}%   |   ORDERS: {orders:,}   |   AVG ORDER: ${avg_order:,.1f}   |   UNITS: {units:,}"

    if hasattr(fig, "_kpi_text_obj"):
        fig._kpi_text_obj.remove()
    fig._kpi_text_obj = fig.text(
        0.58,
        0.88,
        kpis_text,
        ha="center",
        fontsize=10.5,
        fontweight="bold",
        color="darkslategrey",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="tan"),
    )

    if filtered_df.empty:
        ax_trend.text(
            0.5,
            0.5,
            "NO DATA FOUND",
            ha="center",
            va="center",
            fontweight="bold",
            color="red",
        )
        fig.canvas.draw_idle()
        return

    trend = filtered_df.groupby(["Month", "Year"])["Sales"].sum().unstack()
    trend.plot(ax=ax_trend, marker="o", lw=1.8, legend=False)
    ax_trend.set_title(
        "Sales Trend", fontsize=10, fontweight="bold", color="steelblue", loc="left"
    )
    ax_trend.set_xticks(range(1, 13))
    ax_trend.set_xticklabels(
        ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"], fontsize=8
    )

    reg_s = filtered_df.groupby("Region")["Sales"].sum()
    ax_region.pie(
        reg_s, labels=reg_s.index, autopct="%1.0f%%", textprops={"fontsize": 8}
    )
    ax_region.set_title(
        "By Region", fontsize=10, fontweight="bold", color="steelblue", loc="left"
    )

    ship_s = filtered_df.groupby("Ship Mode")["Sales"].sum()
    ax_ship.pie(
        ship_s, labels=ship_s.index, autopct="%1.0f%%", textprops={"fontsize": 8}
    )
    ax_ship.set_title(
        "Ship Mode", fontsize=10, fontweight="bold", color="steelblue", loc="left"
    )

    cat_s = filtered_df.groupby("Category")["Sales"].sum()
    ax_cat.bar(cat_s.index, cat_s.values, color="indianred", width=0.5)
    ax_cat.set_title(
        "By Category", fontsize=10, fontweight="bold", color="steelblue", loc="left"
    )
    ax_cat.tick_params(axis="x", rotation=15, labelsize=8)

    seg_s = filtered_df.groupby("Segment")["Sales"].sum()
    ax_seg.pie(
        seg_s, labels=seg_s.index, autopct="%1.0f%%", textprops={"fontsize": 8}
    )
    ax_seg.set_title(
        "By Segment", fontsize=10, fontweight="bold", color="steelblue", loc="left"
    )

    sub_s = filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values()
    ax_subcat.barh(sub_s.index, sub_s.values, color="darkgoldenrod", height=0.6)
    ax_subcat.set_title(
        "Top Sub-Categories",
        fontsize=10,
        fontweight="bold",
        color="steelblue",
        loc="left",
    )
    ax_subcat.tick_params(axis="y", labelsize=8)

    top_st = (
        filtered_df.groupby("State")["Sales"].sum().nlargest(10).sort_values()
    )
    ax_states.barh(top_st.index, top_st.values, color="teal", height=0.6)
    ax_states.set_title(
        "Top 10 States",
        fontsize=10,
        fontweight="bold",
        color="steelblue",
        loc="left",
    )
    ax_states.tick_params(axis="y", labelsize=8)

    for ax in [ax_trend, ax_cat, ax_subcat, ax_states]:
        ax.grid(True, linestyle="--", alpha=0.3)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.canvas.draw_idle()


radio_year.on_clicked(update)
radio_reg.on_clicked(update)
radio_cat.on_clicked(update)

update()

plt.show()