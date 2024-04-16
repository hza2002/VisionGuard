import os

import cv2
import matplotlib.pyplot as plt


# 统计每分钟的数据数量和认证状态
def plot_chart(data, interval_group):
    time_data = {}
    for item in data:
        timestamp = data[item]["time"]
        info = data[item]["verified"]

        if interval_group == "min":
            interval = timestamp.split()[1][:-3]  # 按分钟分组
        elif interval_group == "hour":
            interval = timestamp.split()[1].split(":")[0]  # 按小时分组
        elif interval_group == "day":
            interval = timestamp.split()[0]  # 按天分组
        else:
            raise ValueError(
                "Invalid interval value. Must be one of 'min', 'hour', or 'day'."
            )

        if interval not in time_data:
            time_data[interval] = {"total": 0, "verified": 0, "unverified": 0}
        time_data[interval]["total"] += 1
        if info:
            time_data[interval]["verified"] += 1
        else:
            time_data[interval]["unverified"] += 1

    # 提取统计结果
    intervals = sorted(time_data.keys())
    total_values = [time_data[interval]["total"] for interval in intervals]
    verified_values = [time_data[interval]["verified"] for interval in intervals]
    unverified_values = [time_data[interval]["unverified"] for interval in intervals]

    # 设置柱状图的宽度
    bar_width = 0.25

    # 计算每个柱子的位置
    bar_positions_total = range(len(intervals))
    bar_positions_authenticated = [pos + bar_width for pos in bar_positions_total]
    bar_positions_unauthenticated = [pos + 2 * bar_width for pos in bar_positions_total]

    # 创建figure对象
    fig = plt.figure()
    # 绘制柱状图
    plt.bar(bar_positions_total, total_values, width=bar_width, label="Total")
    plt.bar(
        bar_positions_authenticated,
        verified_values,
        width=bar_width,
        label="Verified",
    )
    plt.bar(
        bar_positions_unauthenticated,
        unverified_values,
        width=bar_width,
        label="Unverified",
    )

    plt.xlabel("Interval")
    plt.ylabel("Count")
    plt.xticks(bar_positions_total, intervals, rotation=90)  # 以避免重叠

    plt.legend()  # 根据当前绘图的标签自动创建图例
    plt.tight_layout()  # 自动调整子图之间的间距

    img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/report_chart.png"
    )
    plt.savefig(img_path)
    # plt.savefig(img_path, bbox_inches="tight")
    plt.close(fig)  # 关闭图形对象
    return img_path


if __name__ == "__main__":
    data = {
        "2024-04-15 11:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 11:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 11:00:00": {"time": "2024-04-15 11:00:00", "verified": True},
        "2024-04-15 11:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 11:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 11:01:00": {"time": "2024-04-15 11:01:00", "verified": False},
        "2024-04-15 11:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 11:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 11:02:00": {"time": "2024-04-15 11:02:00", "verified": True},
        "2024-04-15 11:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 11:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 12:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 12:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 12:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 12:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-15 12:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 12:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 12:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 12:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 12:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-15 12:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 12:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 12:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 12:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-15 12:02:00": {"time": "2024-04-15 12:02:00", "verified": True},
        "2024-04-16 11:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-16 11:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-16 11:00:00": {"time": "2024-04-15 12:00:00", "verified": True},
        "2024-04-16 11:01:00": {"time": "2024-04-15 12:01:00", "verified": False},
        "2024-04-16 11:01:00": {"time": "2024-04-16 11:01:00", "verified": False},
        "2024-04-16 11:01:00": {"time": "2024-04-16 11:01:00", "verified": False},
        "2024-04-16 11:01:00": {"time": "2024-04-16 11:01:00", "verified": False},
        "2024-04-16 11:02:00": {"time": "2024-04-16 11:02:00", "verified": True},
        "2024-04-16 11:02:00": {"time": "2024-04-16 11:02:00", "verified": True},
        "2024-04-16 11:02:00": {"time": "2024-04-16 11:02:00", "verified": True},
        "2024-04-16 11:02:00": {"time": "2024-04-16 11:02:00", "verified": True},
        "2024-04-16 12:00:00": {"time": "2024-04-16 12:00:00", "verified": True},
        "2024-04-16 12:00:00": {"time": "2024-04-16 12:00:00", "verified": True},
        "2024-04-16 12:00:00": {"time": "2024-04-16 12:00:00", "verified": True},
        "2024-04-16 12:00:00": {"time": "2024-04-16 12:00:00", "verified": True},
        "2024-04-16 12:01:00": {"time": "2024-04-16 12:01:00", "verified": False},
        "2024-04-16 12:01:00": {"time": "2024-04-16 12:01:00", "verified": False},
        "2024-04-16 12:01:00": {"time": "2024-04-16 12:01:00", "verified": False},
        "2024-04-16 12:01:00": {"time": "2024-04-16 12:01:00", "verified": False},
        "2024-04-16 12:01:00": {"time": "2024-04-16 12:01:00", "verified": False},
        "2024-04-16 12:02:00": {"time": "2024-04-16 12:02:00", "verified": True},
        "2024-04-16 12:02:00": {"time": "2024-04-16 12:02:00", "verified": True},
        "2024-04-16 12:02:00": {"time": "2024-04-16 12:02:00", "verified": True},
        "2024-04-16 12:02:00": {"time": "2024-04-16 12:02:00", "verified": True},
        "2024-04-16 12:02:00": {"time": "2024-04-16 12:02:00", "verified": True},
    }
    img_path = plot_chart(data, "hour")
    image = cv2.imread(img_path)
    cv2.imshow("Report Chart", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
