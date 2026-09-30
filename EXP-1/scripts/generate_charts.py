from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUT = Path("images/charts")
OUT.mkdir(parents=True, exist_ok=True)

COLORS = {
    "bg": (248, 250, 252),
    "ink": (15, 23, 42),
    "muted": (71, 85, 105),
    "grid": (203, 213, 225),
    "proxmox": (245, 101, 39),
    "vmware": (37, 99, 235),
    "good": (22, 163, 74),
    "panel": (255, 255, 255),
}

DATA = {
    "Proxmox VE (Type-1)": {
        "eps": 1749.16,
        "events": 17494,
        "total_time": 10.0005,
        "min_latency": 0.57,
        "avg_latency": 0.57,
        "p95_latency": 0.58,
        "max_latency": 2.43,
        "color": COLORS["proxmox"],
    },
    "VMware Workstation (Type-2)": {
        "eps": 1119.03,
        "events": 11194,
        "total_time": 10.0006,
        "min_latency": 0.61,
        "avg_latency": 0.89,
        "p95_latency": 1.50,
        "max_latency": 22.38,
        "color": COLORS["vmware"],
    },
}


def font(size, bold=False):
    names = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded_panel(draw, box, radius=22):
    draw.rounded_rectangle(box, radius=radius, fill=COLORS["panel"], outline=(226, 232, 240), width=2)


def label(draw, xy, text, size=26, fill=None, bold=False, anchor=None):
    draw.text(xy, text, font=font(size, bold), fill=fill or COLORS["ink"], anchor=anchor)


def bar_chart(path, title, metric, suffix="", lower_is_better=False):
    img = Image.new("RGB", (1400, 820), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    label(draw, (70, 55), title, 42, bold=True)
    label(draw, (70, 110), "Measured from the submitted Part-A and Part-B screenshots.", 24, COLORS["muted"])
    rounded_panel(draw, (70, 170, 1330, 735))

    values = [(name, cfg[metric], cfg["color"]) for name, cfg in DATA.items()]
    max_value = max(v for _, v, _ in values) * 1.12
    x0, y0 = 190, 630
    chart_w, chart_h = 980, 350

    for i in range(5):
        y = y0 - (chart_h * i / 4)
        draw.line((x0, y, x0 + chart_w, y), fill=COLORS["grid"], width=1)
        label(draw, (120, y - 13), f"{max_value * i / 4:.0f}", 18, COLORS["muted"])

    bar_w = 260
    gap = 170
    for idx, (name, value, color) in enumerate(values):
        x = x0 + 170 + idx * (bar_w + gap)
        bar_h = int(chart_h * value / max_value)
        draw.rounded_rectangle((x, y0 - bar_h, x + bar_w, y0), radius=18, fill=color)
        label(draw, (x + bar_w / 2, y0 - bar_h - 42), f"{value:,.2f}{suffix}", 30, bold=True, anchor="mm")
        short = "Proxmox VE" if "Proxmox" in name else "VMware"
        label(draw, (x + bar_w / 2, y0 + 38), short, 24, COLORS["ink"], bold=True, anchor="mm")
        label(draw, (x + bar_w / 2, y0 + 74), "Type-1" if "Proxmox" in name else "Type-2", 20, COLORS["muted"], anchor="mm")

    prox = DATA["Proxmox VE (Type-1)"][metric]
    vmw = DATA["VMware Workstation (Type-2)"][metric]
    if lower_is_better:
        delta = (vmw - prox) / vmw * 100
        callout = f"Proxmox lowers this metric by {delta:.2f}%"
    else:
        delta = (prox - vmw) / vmw * 100
        callout = f"Proxmox leads by {delta:.2f}%"
    label(draw, (700, 705), callout, 28, COLORS["good"], bold=True, anchor="mm")
    img.save(OUT / path)


def latency_chart():
    metrics = [
        ("Min", "min_latency"),
        ("Avg", "avg_latency"),
        ("95th", "p95_latency"),
        ("Max", "max_latency"),
    ]
    img = Image.new("RGB", (1500, 900), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    label(draw, (70, 55), "Latency Profile", 42, bold=True)
    label(draw, (70, 110), "Lower values are better. The Type-2 run shows a much larger maximum latency spike.", 24, COLORS["muted"])
    rounded_panel(draw, (70, 170, 1430, 805))

    max_value = 24
    x0, y0 = 175, 700
    chart_w, chart_h = 1120, 430
    for i in range(7):
        y = y0 - (chart_h * i / 6)
        draw.line((x0, y, x0 + chart_w, y), fill=COLORS["grid"], width=1)
        label(draw, (110, y - 13), f"{max_value * i / 6:.0f} ms", 18, COLORS["muted"])

    group_w = chart_w / len(metrics)
    bar_w = 78
    for idx, (label_name, key) in enumerate(metrics):
        center = x0 + group_w * idx + group_w / 2
        for offset, repo in [(-48, "Proxmox VE (Type-1)"), (48, "VMware Workstation (Type-2)")]:
            value = DATA[repo][key]
            color = DATA[repo]["color"]
            h = int(chart_h * value / max_value)
            x = center + offset - bar_w / 2
            draw.rounded_rectangle((x, y0 - h, x + bar_w, y0), radius=14, fill=color)
            label(draw, (x + bar_w / 2, y0 - h - 24), f"{value:.2f}", 18, COLORS["ink"], bold=True, anchor="mm")
        label(draw, (center, y0 + 42), label_name, 23, COLORS["ink"], bold=True, anchor="mm")

    label(draw, (1040, 225), "Proxmox VE", 24, DATA["Proxmox VE (Type-1)"]["color"], bold=True)
    label(draw, (1040, 265), "VMware Workstation", 24, DATA["VMware Workstation (Type-2)"]["color"], bold=True)
    img.save(OUT / "latency-profile.png")


def dashboard():
    img = Image.new("RGB", (1600, 950), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    label(draw, (80, 62), "Cloud Computing Lab Performance Dashboard", 44, bold=True)
    label(draw, (80, 118), "Part-A: Type-1 Proxmox VE vs Part-B: Type-2 VMware Workstation", 25, COLORS["muted"])

    cards = [
        ("Throughput", "1749.16 eps", "+56.31% vs VMware", COLORS["proxmox"]),
        ("Events Processed", "17,494", "+6,300 events", COLORS["good"]),
        ("Average Latency", "0.57 ms", "35.96% lower", COLORS["proxmox"]),
        ("Max Latency Spike", "2.43 ms", "VMware reached 22.38 ms", COLORS["vmware"]),
    ]
    x, y = 80, 190
    for i, (title, value, note, accent) in enumerate(cards):
        cx = x + (i % 2) * 730
        cy = y + (i // 2) * 230
        rounded_panel(draw, (cx, cy, cx + 660, cy + 175), 24)
        draw.rounded_rectangle((cx + 28, cy + 32, cx + 44, cy + 143), radius=8, fill=accent)
        label(draw, (cx + 75, cy + 34), title, 26, COLORS["muted"], bold=True)
        label(draw, (cx + 75, cy + 78), value, 42, COLORS["ink"], bold=True)
        label(draw, (cx + 75, cy + 132), note, 23, accent, bold=True)

    rounded_panel(draw, (80, 690, 1520, 850), 24)
    label(draw, (120, 728), "Conclusion", 30, bold=True)
    label(
        draw,
        (120, 775),
        "The Type-1 hypervisor delivered higher CPU throughput and steadier latency because it runs closer to the physical hardware.",
        25,
        COLORS["muted"],
    )
    label(draw, (120, 815), "For production-style cloud workloads, Type-1 virtualization is the stronger architecture.", 25, COLORS["muted"])
    img.save(OUT / "performance-dashboard.png")


if __name__ == "__main__":
    bar_chart("throughput-comparison.png", "CPU Throughput Comparison", "eps", " eps")
    bar_chart("events-comparison.png", "Total Events Processed in 10 Seconds", "events")
    latency_chart()
    dashboard()
    print(f"Generated charts in {OUT.resolve()}")
