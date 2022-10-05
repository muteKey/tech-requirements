from itertools import count
from grab_dou import DouGrabber
from grab_upwork import UpworkGrabber
from stats.stats_counter import StatsCounter

if __name__ == '__main__':
    delimeter = "\n------------------------"
    # grabber = UpworkGrabber("seeding/seed-android-upwork.html", "results/results-upwork-android.txt", delimeter)
    # grabber.process()

    grabber = DouGrabber('seeding/seed-ba.html', 'results/results-dou-ba.txt', delimeter)
    grabber.process()

    counter = StatsCounter("results/results-dou-ba.txt", 'stats/BA_Skills.csv', delimeter, "stats/stats-ba-dou.txt")
    counter.check()
    counter.write_results()
