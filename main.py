from itertools import count
from grab_dou import DouGrabber
from grab_upwork import UpworkGrabber
from stats.stats_counter import StatsCounter

if __name__ == '__main__':
    delimeter = "\n------------------------"
    grabber = UpworkGrabber("seeding/seed-android-upwork.html", "results/results-upwork-android.txt", delimeter)
    grabber.process()

    counter = StatsCounter("results/results-upwork-android.txt", delimeter, "stats/stats-android-upwork.txt")
    counter.check()
    counter.write_results()