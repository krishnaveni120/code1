
import calendar
import matplotlib.pyplot as plt

year = 2027
calendar.setfirstweekday(calendar.SUNDAY)

fig, axes = plt.subplots(4, 3, figsize=(15, 16))
fig.patch.set_facecolor("#fff0f6")

for month, ax in enumerate(axes.flat, start=1):
    ax.set_facecolor("#fff8fb")

    ax.set_title(
        calendar.month_name[month],
        fontsize=18,
        fontweight="bold",
        color="#8e4580"
    )

    month_data = calendar.monthcalendar(year, month)

    table_data = [
        [str(day) if day else "" for day in week]
        for week in month_data
    ]

    table = ax.table(
        cellText=table_data,
        colLabels=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.65)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#e6b7d4")

        if row == 0:
            cell.set_facecolor("#d9b4e5")
            cell.get_text().set_color("#4d285e")
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor("#fff8fb")
            cell.get_text().set_color("#5a4655")

    ax.axis("off")

fig.suptitle(
    f"{year} CALENDAR",
    fontsize=30,
    fontweight="bold",
    color="#853f78"
)

plt.tight_layout(rect=[0, 0, 1, 0.96], h_pad=2.3, w_pad=1.5)

# Save calendar as an image
plt.savefig(
    f"calendar_{year}.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()
